"""
경희대 국제캠퍼스까지의 거리 계산

각 부동산 거래 데이터의 좌표를 사용하여
경희대 국제캠퍼스까지의 직선 거리를 계산합니다.
"""

import pandas as pd
from geopy.distance import geodesic
import numpy as np

def calculate_campus_distance(input_file: str, output_file: str = None) -> pd.DataFrame:
    """
    경희대 국제캠퍼스까지의 거리를 계산하여 컬럼을 추가합니다.
    
    Args:
        input_file: 입력 CSV 파일 경로
        output_file: 출력 CSV 파일 경로 (None이면 입력 파일에 덮어쓰기)
    
    Returns:
        거리 컬럼이 추가된 DataFrame
    """
    print("="*60)
    print("경희대 국제캠퍼스까지 거리 계산")
    print("="*60)
    
    # 1) 데이터 로드
    print(f"\n데이터 로드 중: {input_file}")
    df = pd.read_csv(input_file, encoding="utf-8-sig", low_memory=False)
    
    print(f"전체 행 수: {len(df):,}")
    print(f"컬럼 수: {len(df.columns)}")
    
    # 2) 위도/경도 컬럼 확인
    COL_LON = "longitude"
    COL_LAT = "latitude"
    
    if COL_LON not in df.columns or COL_LAT not in df.columns:
        print(f"\n⚠️  경고: {COL_LON} 또는 {COL_LAT} 컬럼이 없습니다.")
        print("사용 가능한 컬럼:")
        print([col for col in df.columns if 'lon' in col.lower() or 'lat' in col.lower()])
        return df
    
    # 좌표가 있는 행 수 확인
    has_coords = df[COL_LAT].notna() & df[COL_LON].notna()
    print(f"\n좌표가 있는 행 수: {has_coords.sum():,} ({has_coords.sum()/len(df)*100:.1f}%)")
    
    # 3) 경희대 국제캠퍼스 좌표 (위도, 경도)
    # 경희대 국제캠퍼스: 경기도 용인시 기흥구 덕영대로 1732
    KHU_ICAMPUS = (37.2430, 127.0801)  # (lat, lon) 순서
    
    print(f"\n경희대 국제캠퍼스 좌표: {KHU_ICAMPUS}")
    
    # 4) 거리 계산 함수
    def calc_dist_to_campus(row):
        lon = row[COL_LON]
        lat = row[COL_LAT]
        
        # 좌표 없는 행은 NaN 유지
        if pd.isna(lon) or pd.isna(lat):
            return np.nan
        
        try:
            # geodesic은 (lat, lon) 순서
            distance_m = geodesic((lat, lon), KHU_ICAMPUS).meters
            return distance_m
        except Exception as e:
            print(f"거리 계산 오류: {row.get('full_address', 'N/A')} - {str(e)}")
            return np.nan
    
    # 5) 거리 컬럼 생성
    print("\n거리 계산 중...")
    df["dist_to_campus_m"] = df.apply(calc_dist_to_campus, axis=1)
    
    # 6) 요약 통계
    print("\n" + "="*60)
    print("경희대까지 거리 통계 (단위: m)")
    print("="*60)
    
    dist_stats = df["dist_to_campus_m"].describe()
    print(dist_stats)
    
    # 추가 통계
    valid_dist = df["dist_to_campus_m"].dropna()
    if len(valid_dist) > 0:
        print(f"\n거리 통계 상세:")
        print(f"  - 유효한 거리 값: {len(valid_dist):,}개")
        print(f"  - 최소 거리: {valid_dist.min():.1f}m")
        print(f"  - 최대 거리: {valid_dist.max():.1f}m")
        print(f"  - 평균 거리: {valid_dist.mean():.1f}m")
        print(f"  - 중앙값 거리: {valid_dist.median():.1f}m")
        print(f"  - 표준편차: {valid_dist.std():.1f}m")
        
        # 거리 구간별 분포
        print(f"\n거리 구간별 분포:")
        bins = [0, 500, 1000, 2000, 3000, 5000, 10000, float('inf')]
        labels = ['0-500m', '500m-1km', '1-2km', '2-3km', '3-5km', '5-10km', '10km+']
        dist_categories = pd.cut(valid_dist, bins=bins, labels=labels, right=False)
        print(dist_categories.value_counts().sort_index())
    
    # 7) 예시 출력
    print("\n" + "="*60)
    print("거리 계산 결과 샘플 (상위 10개)")
    print("="*60)
    sample_cols = ["full_address", COL_LAT, COL_LON, "dist_to_campus_m", "campus_zone"]
    if all(col in df.columns for col in sample_cols):
        print(df[sample_cols].head(10).to_string())
    else:
        print(df[["full_address", COL_LAT, COL_LON, "dist_to_campus_m"]].head(10).to_string())
    
    # 8) 결과 저장
    if output_file is None:
        output_file = input_file
    
    print(f"\n결과 저장 중: {output_file}")
    df.to_csv(output_file, index=False, encoding="utf-8-sig")
    print("✓ 저장 완료!")
    
    print("\n" + "="*60)
    print("거리 계산 완료!")
    print("="*60)
    
    return df

if __name__ == "__main__":
    input_path = "real_estate/preprogressed/final_data_with_real_costs.csv"
    output_path = "real_estate/preprogressed/final_data_with_real_costs.csv"  # 동일 파일에 업데이트
    
    df_result = calculate_campus_distance(input_path, output_path)

