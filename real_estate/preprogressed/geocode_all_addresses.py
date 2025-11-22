"""
OSM Nominatim을 사용한 전체 주소 지오코딩
"""
import pandas as pd
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import numpy as np
from tqdm import tqdm

USER_AGENT = "khudata_geocoding/1.0"

def geocode_address(geolocator, address, max_retries=3, delay=1.0):
    if pd.isna(address) or str(address).strip() == "":
        return None, None
    
    for attempt in range(max_retries):
        try:
            location = geolocator.geocode(str(address), timeout=10, language='ko')
            if location:
                return location.latitude, location.longitude
            else:
                return None, None
        except (GeocoderTimedOut, GeocoderServiceError) as e:
            if attempt < max_retries - 1:
                time.sleep(delay * (attempt + 1))
                continue
            else:
                print(f"\n지오코딩 실패: {address[:50]}...")
                return None, None
        except Exception as e:
            print(f"\n오류: {address[:50]}... - {str(e)}")
            return None, None
    
    return None, None

def main():
    print("="*60)
    print("OSM Nominatim 지오코딩 시작")
    print("="*60)
    
    input_file = "real_estate/preprogressed/final_data_with_real_costs.csv"
    print(f"\n데이터 로드 중: {input_file}")
    df = pd.read_csv(input_file, encoding="utf-8-sig", low_memory=False)
    
    print(f"전체 행 수: {len(df):,}")
    
    if "full_address" not in df.columns:
        print("\n⚠️  full_address 컬럼 생성 중...")
        def create_full_address(row):
            sigungu = str(row.get("시군구", ""))
            if pd.notna(row.get("도로명")) and str(row.get("도로명", "")).strip():
                return f"{sigungu} {str(row.get('도로명', '')).strip()}"
            elif pd.notna(row.get("번지")) and str(row.get("번지", "")).strip():
                return f"{sigungu} {str(row.get('번지', '')).strip()}"
            return sigungu
        df["full_address"] = df.apply(create_full_address, axis=1)
    
    unique_addresses = df["full_address"].dropna().unique()
    print(f"고유 주소 개수: {len(unique_addresses):,}")
    
    if "latitude" in df.columns and "longitude" in df.columns:
        existing_geocoded = df[df["latitude"].notna() & df["longitude"].notna()]
        print(f"이미 지오코딩된 행 수: {len(existing_geocoded):,}")
        geocoded_addresses = set(existing_geocoded["full_address"].unique())
        addresses_to_geocode = [addr for addr in unique_addresses if addr not in geocoded_addresses]
        print(f"지오코딩 필요한 주소 수: {len(addresses_to_geocode):,}")
    else:
        addresses_to_geocode = list(unique_addresses)
        df["latitude"] = np.nan
        df["longitude"] = np.nan
    
    if len(addresses_to_geocode) == 0:
        print("\n✓ 모든 주소가 이미 지오코딩되어 있습니다!")
        return
    
    print("\nNominatim geocoder 초기화 중...")
    geolocator = Nominatim(user_agent=USER_AGENT)
    REQUEST_DELAY = 1.1
    
    geocode_results = {}
    print(f"\n지오코딩 시작 (예상 시간: 약 {len(addresses_to_geocode) * REQUEST_DELAY / 60:.1f}분)")
    print("="*60)
    
    for address in tqdm(addresses_to_geocode, desc="지오코딩 진행"):
        lat, lon = geocode_address(geolocator, address, max_retries=3, delay=1.0)
        geocode_results[address] = (lat, lon)
        time.sleep(REQUEST_DELAY)
    
    print("\n결과를 DataFrame에 반영 중...")
    for address, (lat, lon) in geocode_results.items():
        mask = df["full_address"] == address
        df.loc[mask, "latitude"] = lat
        df.loc[mask, "longitude"] = lon
    
    print("\n" + "="*60)
    print("지오코딩 결과 통계")
    print("="*60)
    
    total_rows = len(df)
    geocoded_rows = df["latitude"].notna().sum()
    failed_rows = total_rows - geocoded_rows
    
    print(f"전체 행 수: {total_rows:,}")
    print(f"성공한 행 수: {geocoded_rows:,} ({geocoded_rows/total_rows*100:.1f}%)")
    print(f"실패한 행 수: {failed_rows:,} ({failed_rows/total_rows*100:.1f}%)")
    
    unique_geocoded = df[df["latitude"].notna()]["full_address"].nunique()
    unique_total = df["full_address"].nunique()
    print(f"\n고유 주소 성공률: {unique_geocoded}/{unique_total} ({unique_geocoded/unique_total*100:.1f}%)")
    
    output_file = "real_estate/preprogressed/final_data_with_real_costs.csv"
    print(f"\n결과 저장 중: {output_file}")
    df.to_csv(output_file, index=False, encoding="utf-8-sig")
    print("✓ 저장 완료!")
    
    print("\n" + "="*60)
    print("지오코딩 완료!")
    print("="*60)

if __name__ == "__main__":
    main()
