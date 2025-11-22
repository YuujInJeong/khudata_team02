"""
시군구 컬럼을 시/구/동으로 분리
"""

import pandas as pd

# 데이터 로드
path = "real_estate/preprogressed/final_data_with_real_costs.csv"
df = pd.read_csv(path, encoding="utf-8-sig", low_memory=False)

print(f"원본 데이터 shape: {df.shape}")
print(f"\n시군구 컬럼 예시:")
print(df["시군구"].head(10).tolist())

# 1) 시/구/동 분리 함수 정의
def split_addr(value):
    """
    '경기도 수원시 영통구 원천동' 같은 문자열을
    시도 / 시 / 구군 / 동읍면으로 쪼개서 반환
    """
    if pd.isna(value):
        return pd.Series({"시도": None, "시": None, "구군": None, "동읍면": None})
    
    parts = str(value).split()
    # 예: ['경기도', '수원시', '영통구', '원천동']
    
    if len(parts) >= 4:
        sido = parts[0]              # 경기도
        si   = parts[1]              # 수원시 / 용인시 등
        gugu = parts[2]              # 영통구 / 기흥구 등
        dong = " ".join(parts[3:])   # 원천동, 서천동, 망포동 등 (뒤에 더 붙어도 전부)
    elif len(parts) == 3:
        # 혹시 '경기도 수원시 영통구' 까지만 있는 경우 대비
        sido, si, gugu = parts
        dong = None
    else:
        # 이상한 케이스 대비
        sido = parts[0]
        si = parts[1] if len(parts) > 1 else None
        gugu = None
        dong = None
    
    return pd.Series({"시도": sido, "시": si, "구군": gugu, "동읍면": dong})

# 2) 시군구 컬럼에 적용
print("\n" + "="*60)
print("주소 분리 중...")
print("="*60)

addr_split = df["시군구"].apply(split_addr)

# 3) 원본 df에 붙이기
df = pd.concat([df, addr_split], axis=1)

print(f"\n분리 후 shape: {df.shape}")
print(f"\n추가된 컬럼: {addr_split.columns.tolist()}")

# 4) 동 단위 고유값 확인
print("\n" + "="*60)
print("동읍면 분석")
print("="*60)

print(f"동읍면(unique) 개수: {df['동읍면'].nunique()}")

print("\n동읍면 예시 10개:")
dong_examples = df["동읍면"].dropna().unique()[:10]
for i, dong in enumerate(dong_examples, 1):
    print(f"  {i}. {dong}")

# 전체 동 목록
print(f"\n전체 동 목록 ({df['동읍면'].nunique()}개):")
all_dongs = sorted(df["동읍면"].dropna().unique())
for i, dong in enumerate(all_dongs, 1):
    print(f"  {i}. {dong}")

# 시도/시/구군 분포 확인
print("\n" + "="*60)
print("시도/시/구군 분포")
print("="*60)

print("\n시도별 건수:")
print(df["시도"].value_counts())

print("\n시별 건수:")
print(df["시"].value_counts())

print("\n구군별 건수:")
print(df["구군"].value_counts())

# 이상한 케이스 확인
print("\n" + "="*60)
print("이상 케이스 확인")
print("="*60)

# 동이 없는 경우
no_dong = df[df["동읍면"].isna()]
if len(no_dong) > 0:
    print(f"\n동이 없는 행: {len(no_dong)}개")
    print(no_dong[["시군구", "시도", "시", "구군", "동읍면"]].head())

# 동이 아닌 다른 단위가 섞인 경우 (읍, 면 등)
dong_with_other = df[df["동읍면"].notna() & ~df["동읍면"].str.contains("동", na=False)]
if len(dong_with_other) > 0:
    print(f"\n'동'이 아닌 단위 포함: {len(dong_with_other)}개")
    print(dong_with_other[["시군구", "동읍면"]].head(10))

# 샘플 데이터 확인
print("\n" + "="*60)
print("샘플 데이터 (주소 분리 결과)")
print("="*60)
print(df[["시군구", "시도", "시", "구군", "동읍면"]].head(10))

# 저장
output_file = "real_estate/preprogressed/final_data_with_real_costs.csv"
df.to_csv(output_file, index=False, encoding="utf-8-sig")
print(f"\n✓ 주소 분리된 데이터 저장 완료: {output_file}")

