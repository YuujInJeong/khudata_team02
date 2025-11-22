"""
부동산 전월세 실거래 데이터 전처리 파이프라인

이 모듈은 국토교통부에서 제공하는 전월세 실거래 데이터를 전처리하여
분석 가능한 형태로 변환하는 전체 파이프라인을 제공합니다.

주요 기능:
1. 여러 CSV 파일 병합
2. 지역 필터링 및 캠퍼스 존 분류
3. 월주거비 통일 계산 (전세/월세 통합)
4. 금리 및 CPI 반영
5. 실질 월주거비 계산
"""

import pandas as pd
import numpy as np
import glob
import os
from typing import List, Tuple, Optional


def merge_csv_files(base_dir: str, output_file: str = None) -> pd.DataFrame:
    """
    여러 CSV 파일을 하나의 DataFrame으로 병합
    
    Args:
        base_dir: CSV 파일들이 있는 디렉토리 경로
        output_file: 저장할 파일 경로 (None이면 저장하지 않음)
    
    Returns:
        병합된 DataFrame
    
    Input:
        - 여러 개의 CSV 파일 (연립다세대, 단독다가구, 오피스텔 전월세 실거래 데이터)
        - 인코딩: cp949, euc-kr, utf-8 중 하나
    
    Output:
        - 병합된 DataFrame (부동산유형, 원본파일명 컬럼 추가)
    """
    csv_files = glob.glob(os.path.join(base_dir, "*.csv"))
    
    print(f"발견된 CSV 파일 수: {len(csv_files)}")
    print("\n파일 목록:")
    for i, file in enumerate(csv_files, 1):
        print(f"{i}. {os.path.basename(file)}")
    
    dataframes = []
    
    for file in csv_files:
        print(f"\n처리 중: {os.path.basename(file)}")
        
        # 헤더 라인 찾기 (보통 "NO"로 시작하는 줄이 헤더)
        header_line = None
        encodings = ["cp949", "euc-kr", "utf-8"]
        
        for encoding in encodings:
            try:
                with open(file, "r", encoding=encoding) as f:
                    for i, line in enumerate(f, 1):
                        if '"NO"' in line or 'NO' in line.split(',')[0]:
                            header_line = i - 1  # 0-based index
                            break
                if header_line is not None:
                    break
            except:
                continue
        
        if header_line is None:
            header_line = 15  # 기본값
        
        # 파일 읽기
        df = None
        for encoding in encodings:
            try:
                df = pd.read_csv(file, encoding=encoding, skiprows=header_line, header=0)
                print(f"  ✓ {encoding} 인코딩으로 성공적으로 읽음 (헤더 라인: {header_line+1}, 행 수: {len(df)})")
                break
            except Exception as e:
                continue
        
        if df is None:
            print(f"  ✗ 읽기 실패: 모든 인코딩 시도 실패")
            continue
        
        # 파일명에서 부동산 유형 추출
        filename = os.path.basename(file)
        if "연립다세대" in filename:
            df["부동산유형"] = "연립다세대"
        elif "단독다가구" in filename:
            df["부동산유형"] = "단독다가구"
        elif "오피스텔" in filename:
            df["부동산유형"] = "오피스텔"
        else:
            df["부동산유형"] = "기타"
        
        df["원본파일명"] = filename
        dataframes.append(df)
        print(f"  컬럼 수: {len(df.columns)}")
        print(f"  컬럼명: {list(df.columns)[:5]}...")
    
    if dataframes:
        print("\n" + "="*50)
        print("모든 파일을 하나의 DataFrame으로 합치는 중...")
        df_merged = pd.concat(dataframes, ignore_index=True)
        
        print(f"\n✓ 합치기 완료!")
        print(f"  총 행 수: {len(df_merged)}")
        print(f"  총 컬럼 수: {len(df_merged.columns)}")
        print(f"\n부동산 유형별 행 수:")
        print(df_merged["부동산유형"].value_counts())
        
        if output_file:
            df_merged.to_csv(output_file, index=False, encoding="utf-8-sig")
            print(f"\n✓ 합쳐진 데이터가 저장되었습니다: {output_file}")
        
        return df_merged
    else:
        print("\n✗ 읽을 수 있는 파일이 없습니다.")
        return pd.DataFrame()


def create_campus_zone(df: pd.DataFrame, output_file: str = None) -> pd.DataFrame:
    """
    경희대 국제캠퍼스 기준으로 코어/확장 생활권 분류
    
    Args:
        df: 병합된 원본 데이터프레임
        output_file: 저장할 파일 경로 (None이면 저장하지 않음)
    
    Returns:
        campus_zone 컬럼이 추가된 DataFrame
    
    Input:
        - merged_all_data.csv (병합된 전월세 데이터)
        - 시군구 컬럼 필요
    
    Output:
        - campus_zone 컬럼 추가 ('core' 또는 'extended')
        - 코어 존: 국캠 도보/버스 생활권 (서천동, 영덕동, 구갈동, 중동, 이의동, 원천동, 영통동)
        - 확장 존: 그 외 지역
    """
    # 수원시 영통구 + 용인시 기흥구만 필터
    mask_gu = (
        df["시군구"].str.contains("수원시 영통구") |
        df["시군구"].str.contains("용인시 기흥구")
    )
    df_area = df[mask_gu].copy()
    
    print("필터 후 shape:", df_area.shape)
    print("\n동별 빈도 상위 20개:")
    print(df_area["시군구"].value_counts().head(20))
    
    # 국캠 기준 '코어 생활권' 동 리스트 정의
    core_dongs = [
        "경기도 용인시 기흥구 서천동",
        "경기도 용인시 기흥구 영덕동",
        "경기도 용인시 기흥구 구갈동",
        "경기도 용인시 기흥구 중동",
        "경기도 수원시 영통구 이의동",
        "경기도 수원시 영통구 원천동",
        "경기도 수원시 영통구 영통동",
    ]
    
    # 코어/확장 라벨링
    def label_campus_zone(sigungu_str: str) -> str:
        if sigungu_str in core_dongs:
            return "core"      # 국캠 도보/버스 생활권
        else:
            return "extended"  # 그래도 근처지만 조금 더 바깥
    
    df_area["campus_zone"] = df_area["시군구"].apply(label_campus_zone)
    
    print("\n캠퍼스 존 분포:")
    print(df_area["campus_zone"].value_counts())
    
    if output_file:
        df_area.to_csv(output_file, index=False, encoding="utf-8-sig")
        print(f"\n✓ 결과가 저장되었습니다: {output_file}")
    
    return df_area


def calculate_monthly_cost(df: pd.DataFrame, annual_rate: float = 0.04, 
                           output_file: str = None) -> pd.DataFrame:
    """
    전세/월세를 하나의 월주거비로 통일 계산
    
    Args:
        df: campus_zone이 추가된 데이터프레임
        annual_rate: 연이자율 (기본값 0.04 = 4%)
        output_file: 저장할 파일 경로 (None이면 저장하지 않음)
    
    Returns:
        converted_monthly_cost, cost_per_m2 컬럼이 추가된 DataFrame
    
    Input:
        - merged_all_data_with_zone.csv
        - 보증금(만원), 월세금(만원), 전용면적(㎡), 계약년월 컬럼 필요
    
    Output:
        - contract_year, contract_month: 계약 연도/월
        - converted_monthly_cost: 월세 + (보증금 * 연이자율 / 12)
        - cost_per_m2: converted_monthly_cost / 전용면적(㎡)
    
    공식:
        converted_monthly_cost = 월세금 + (보증금 × 연이자율 / 12)
    """
    print("원본 shape:", df.shape)
    
    # 계약년월/계약일 숫자로 정리
    df["계약년월"] = pd.to_numeric(df["계약년월"], errors="coerce")
    df["계약일"] = pd.to_numeric(df["계약일"], errors="coerce")
    
    # 연, 월 컬럼 만들기
    df["contract_year"] = (df["계약년월"] // 100).astype("Int64")
    df["contract_month"] = (df["계약년월"] % 100).astype("Int64")
    
    # 금액/면적 숫자형으로 변환
    for col in ["보증금(만원)", "월세금(만원)", "전용면적(㎡)"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    
    # 연이자율 설정
    df["annual_rate"] = annual_rate
    
    # 월 기준 환산 주거비 계산
    df["converted_monthly_cost"] = (
        df["월세금(만원)"].fillna(0)
        + df["보증금(만원)"].fillna(0) * (df["annual_rate"] / 12)
    )
    
    # 전용면적당 월주거비 (m2당)
    df["cost_per_m2"] = df["converted_monthly_cost"] / df["전용면적(㎡)"]
    
    print("\nconverted_monthly_cost 기초 통계:")
    print(df["converted_monthly_cost"].describe())
    
    print("\ncost_per_m2 기초 통계:")
    print(df["cost_per_m2"].describe())
    
    print("\ncampus_zone별 평균 월주거비 / m2당 월주거비:")
    print(df.groupby("campus_zone")[["converted_monthly_cost", "cost_per_m2"]].mean())
    
    # 모든 컬럼 유지 (나중에 좌표/환경 데이터 추가를 위해)
    print("\ndf_model shape:", df.shape)
    
    if output_file:
        df.to_csv(output_file, index=False, encoding="utf-8-sig")
        print(f"\n✓ 모델용 데이터가 저장되었습니다: {output_file}")
    
    return df


def create_interest_cpi_template(df: pd.DataFrame, output_file: str = None) -> pd.DataFrame:
    """
    월별 금리 및 CPI 템플릿 생성
    
    Args:
        df: contract_year, contract_month 컬럼이 있는 데이터프레임
        output_file: 저장할 파일 경로 (None이면 저장하지 않음)
    
    Returns:
        월별 금리/CPI 템플릿 DataFrame
    
    Input:
        - merged_data_with_costs.csv
        - contract_year, contract_month 컬럼 필요
    
    Output:
        - year_month: 연-월 문자열 (예: "2023-11")
        - annual_rate: 연 주택담보대출 금리 (초기값 NaN, 나중에 채워야 함)
        - cpi_index: 소비자물가지수 (초기값 NaN, 나중에 채워야 함)
    """
    # (연, 월) 유니크 조합 뽑기
    month_keys = (
        df[["contract_year", "contract_month"]]
        .dropna()
        .drop_duplicates()
        .sort_values(["contract_year", "contract_month"])
        .reset_index(drop=True)
    )
    
    # year_month 문자열 컬럼 만들기
    month_keys["year_month"] = month_keys.apply(
        lambda row: f"{int(row['contract_year']):04d}-{int(row['contract_month']):02d}",
        axis=1
    )
    
    # 금리 / CPI 컬럼은 일단 NaN 채워두기
    month_keys["annual_rate"] = pd.NA
    month_keys["cpi_index"] = pd.NA
    
    print(f"\n전체 기간: {month_keys['year_month'].min()} ~ {month_keys['year_month'].max()}")
    print(f"총 월 수: {len(month_keys)}개")
    
    if output_file:
        month_keys.to_csv(output_file, index=False, encoding="utf-8-sig")
        print(f"\n✓ 템플릿 CSV 저장 완료: {output_file}")
    
    return month_keys


def fill_annual_rate(df_template: pd.DataFrame, method: str = "linear", 
                    output_file: str = None) -> pd.DataFrame:
    """
    템플릿의 annual_rate를 추정값으로 채우기
    
    Args:
        df_template: interest_cpi_template.csv
        method: "linear" (선형 감소) 또는 "yearly" (연도별 고정)
        output_file: 저장할 파일 경로 (None이면 저장하지 않음)
    
    Returns:
        annual_rate가 채워진 템플릿 DataFrame
    
    Input:
        - interest_cpi_template.csv
        - contract_year, contract_month 컬럼 필요
    
    Output:
        - annual_rate: 추정 주택담보대출 금리 (3.5% ~ 4.0% 범위)
        - 참고: 실제 데이터는 한국은행 ECOS에서 받아야 함
    """
    if method == "linear":
        # 2023년 11월부터 2025년 10월까지 선형 감소 가정 (4.0% -> 3.5%)
        start_rate = 0.040
        end_rate = 0.035
        n_months = len(df_template)
        rates_linear = np.linspace(start_rate, end_rate, n_months)
        df_template['annual_rate'] = rates_linear
    elif method == "yearly":
        # 연도별 평균값 사용
        estimated_rates = {
            2023: 0.040,  # 4.0%
            2024: 0.038,  # 3.8%
            2025: 0.037,  # 3.7%
        }
        for year in estimated_rates.keys():
            mask = df_template['contract_year'] == year
            df_template.loc[mask, 'annual_rate'] = estimated_rates[year]
    
    print("\nannual_rate 통계:")
    print(df_template['annual_rate'].describe())
    
    if output_file:
        df_template.to_csv(output_file, index=False, encoding="utf-8-sig")
        print(f"\n✓ 업데이트된 템플릿 저장 완료: {output_file}")
    
    return df_template


def merge_and_recalculate_costs(df_model: pd.DataFrame, df_template: pd.DataFrame,
                                output_file: str = None) -> pd.DataFrame:
    """
    금리/CPI 템플릿과 병합하여 실제 금리로 월주거비 재계산 및 실질 월주거비 생성
    
    Args:
        df_model: merged_data_with_costs.csv
        df_template: interest_cpi_template.csv (annual_rate, cpi_index 포함)
        output_file: 저장할 파일 경로 (None이면 저장하지 않음)
    
    Returns:
        real_monthly_cost, real_cost_per_m2 컬럼이 추가된 최종 DataFrame
    
    Input:
        - merged_data_with_costs.csv (명목 월주거비 포함)
        - interest_cpi_template.csv (annual_rate, cpi_index 포함)
    
    Output:
        - converted_monthly_cost: 실제 금리로 재계산된 명목 월주거비
        - cost_per_m2: 실제 금리로 재계산된 명목 m2당 월주거비
        - real_monthly_cost: CPI로 조정된 실질 월주거비
        - real_cost_per_m2: CPI로 조정된 실질 m2당 월주거비
    
    공식:
        converted_monthly_cost = 월세 + (보증금 × 실제_연이자율 / 12)
        real_monthly_cost = converted_monthly_cost / (현재_CPI / 기준_CPI)
    """
    print("df_model shape:", df_model.shape)
    print("템플릿 shape:", df_template.shape)
    
    # 템플릿과 merge
    df_merged = df_model.merge(
        df_template[["contract_year", "contract_month", "annual_rate", "cpi_index"]],
        on=["contract_year", "contract_month"],
        how="left"
    )
    
    print(f"merge 후 shape: {df_merged.shape}")
    print(f"\nannual_rate 결측치: {df_merged['annual_rate'].isna().sum()}개")
    print(f"cpi_index 결측치: {df_merged['cpi_index'].isna().sum()}개")
    
    # 실제 금리로 월주거비 재계산
    df_merged["보증금(만원)"] = pd.to_numeric(df_merged["보증금(만원)"], errors="coerce")
    df_merged["월세금(만원)"] = pd.to_numeric(df_merged["월세금(만원)"], errors="coerce")
    df_merged["annual_rate"] = pd.to_numeric(df_merged["annual_rate"], errors="coerce")
    
    df_merged["converted_monthly_cost"] = (
        df_merged["월세금(만원)"].fillna(0)
        + df_merged["보증금(만원)"].fillna(0) * (df_merged["annual_rate"] / 12)
    )
    
    df_merged["cost_per_m2"] = df_merged["converted_monthly_cost"] / df_merged["전용면적(㎡)"]
    
    # CPI로 실질 월주거비 계산
    base_cpi = df_merged["cpi_index"].dropna().iloc[0] if not df_merged["cpi_index"].dropna().empty else 100.0
    print(f"\nCPI 기준점 (base_cpi): {base_cpi}")
    
    df_merged["real_monthly_cost"] = df_merged["converted_monthly_cost"] / (df_merged["cpi_index"] / base_cpi)
    df_merged["real_cost_per_m2"] = df_merged["real_monthly_cost"] / df_merged["전용면적(㎡)"]
    
    print("\n실질 월주거비(real_monthly_cost) 통계:")
    print(df_merged["real_monthly_cost"].describe())
    
    print("\n명목 월주거비 (campus_zone별):")
    print(df_merged.groupby("campus_zone")[["converted_monthly_cost", "cost_per_m2"]].mean())
    
    print("\n실질 월주거비 (campus_zone별):")
    print(df_merged.groupby("campus_zone")[["real_monthly_cost", "real_cost_per_m2"]].mean())
    
    # 모든 컬럼 유지 (좌표/환경 데이터 추가를 위해)
    df_final = df_merged.copy()
    
    if output_file:
        df_final.to_csv(output_file, index=False, encoding="utf-8-sig")
        print(f"\n✓ 최종 데이터 저장 완료: {output_file}")
    
    return df_final


def restore_missing_columns(df_final: pd.DataFrame, df_original: pd.DataFrame, 
                            output_file: str = None) -> pd.DataFrame:
    """
    최종 데이터에 누락된 원본 컬럼 복원
    
    Args:
        df_final: 최종 데이터프레임 (일부 컬럼만 포함)
        df_original: 원본 데이터프레임 (모든 컬럼 포함)
        output_file: 저장할 파일 경로 (None이면 저장하지 않음)
    
    Returns:
        누락된 컬럼이 복원된 DataFrame
    
    Input:
        - final_data_with_real_costs.csv (최종 데이터)
        - merged_all_data_with_zone.csv (원본 데이터)
    
    Output:
        - NO, 번지, 본번, 부번, 건물명, 계약일, 층, 건축년도, 도로명 등
        - 모든 원본 컬럼 복원
    """
    required_columns = [
        "NO", "번지", "본번", "부번", "건물명", "계약일", 
        "층", "건축년도", "도로명", "계약기간", "계약구분",
        "갱신요구권 사용", "종전계약 보증금(만원)", "종전계약 월세(만원)",
        "원본파일명", "단지명", "도로조건", "계약면적(㎡)"
    ]
    
    # 원본에 있지만 최종에 없는 컬럼 찾기
    missing_columns = []
    for col in required_columns:
        if col in df_original.columns and col not in df_final.columns:
            missing_columns.append(col)
    
    if not missing_columns:
        print("누락된 컬럼이 없습니다.")
        return df_final
    
    print(f"누락된 컬럼 {len(missing_columns)}개 복원 중...")
    
    # 행 수가 같으면 인덱스 기준으로 추가
    if len(df_original) == len(df_final):
        df_original_reset = df_original.reset_index(drop=True)
        df_final_reset = df_final.reset_index(drop=True)
        
        for col in missing_columns:
            if col in df_original_reset.columns:
                df_final_reset[col] = df_original_reset[col]
                print(f"  ✓ {col} 추가됨")
        
        df_restored = df_final_reset
    else:
        # 키 기반 merge
        merge_keys = ["시군구", "계약년월", "보증금(만원)", "월세금(만원)", "전용면적(㎡)"]
        df_original_subset = df_original[merge_keys + missing_columns].copy()
        
        df_restored = df_final.merge(
            df_original_subset,
            on=merge_keys,
            how="left",
            suffixes=("", "_original")
        )
        
        for col in missing_columns:
            if f"{col}_original" in df_restored.columns:
                df_restored[col] = df_restored[f"{col}_original"]
                df_restored = df_restored.drop(columns=[f"{col}_original"])
    
    print(f"\n복원 후 shape: {df_restored.shape}")
    
    if output_file:
        df_restored.to_csv(output_file, index=False, encoding="utf-8-sig")
        print(f"✓ 복원된 데이터 저장 완료: {output_file}")
    
    return df_restored


def analyze_data(df: pd.DataFrame) -> None:
    """
    데이터 기본 통계 분석
    
    Args:
        df: 분석할 데이터프레임
    
    Output:
        - 전체 shape
        - 부동산유형별 건수
        - 시군구 예시 및 빈도
    """
    print("전체 shape:", df.shape)
    print("\n부동산유형별 건수:")
    print(df["부동산유형"].value_counts())
    print("\n시군구 예시 10개:")
    print(df["시군구"].head(10).tolist())
    print("\n시군구 상위 30개 빈도:")
    print(df["시군구"].value_counts().head(30))


# 메인 파이프라인 실행 함수
def run_full_pipeline(base_dir: str, output_dir: str = "real_estate/preprogressed") -> pd.DataFrame:
    """
    전체 전처리 파이프라인 실행
    
    Args:
        base_dir: 원본 CSV 파일들이 있는 디렉토리
        output_dir: 출력 파일들을 저장할 디렉토리
    
    Returns:
        최종 전처리된 DataFrame
    """
    # Step 1: CSV 파일 병합
    df_merged = merge_csv_files(
        base_dir, 
        output_file=os.path.join(output_dir, "merged_all_data.csv")
    )
    
    # Step 2: 캠퍼스 존 분류
    df_zone = create_campus_zone(
        df_merged,
        output_file=os.path.join(output_dir, "merged_all_data_with_zone.csv")
    )
    
    # Step 3: 월주거비 계산 (임시 금리 4%)
    df_costs = calculate_monthly_cost(
        df_zone,
        annual_rate=0.04,
        output_file=os.path.join(output_dir, "merged_data_with_costs.csv")
    )
    
    # Step 4: 금리/CPI 템플릿 생성
    df_template = create_interest_cpi_template(
        df_costs,
        output_file=os.path.join(output_dir, "interest_cpi_template.csv")
    )
    
    # Step 5: 템플릿에 추정 금리 채우기
    df_template = fill_annual_rate(
        df_template,
        method="linear",
        output_file=os.path.join(output_dir, "interest_cpi_template.csv")
    )
    
    # Step 6: 실제 금리로 재계산 및 실질 월주거비 생성
    df_final = merge_and_recalculate_costs(
        df_costs,
        df_template,
        output_file=os.path.join(output_dir, "final_data_with_real_costs.csv")
    )
    
    # Step 7: 누락된 컬럼 복원
    df_final = restore_missing_columns(
        df_final,
        df_zone,
        output_file=os.path.join(output_dir, "final_data_with_real_costs.csv")
    )
    
    return df_final


if __name__ == "__main__":
    # 예시 실행
    base_dir = "/Users/jeong-yujin/Downloads/khudata"
    df_final = run_full_pipeline(base_dir)
    print("\n전처리 파이프라인 완료!")

