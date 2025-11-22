"""
room_key 생성: 같은 방을 식별하기 위한 키 생성
"""

import pandas as pd

path = "real_estate/preprogressed/final_data_with_real_costs.csv"
df = pd.read_csv(path, encoding="utf-8-sig", low_memory=False)

print("="*60)
print("Step 1: full_address 생성")
print("="*60)

# full_address 생성 (시군구 + 번지 조합)
# 도로명이 있으면 도로명 사용, 없으면 번지 사용
def create_full_address(row):
    """주소 문자열 생성"""
    sigungu = str(row.get("시군구", ""))
    
    # 도로명이 있으면 도로명 사용
    if pd.notna(row.get("도로명")) and str(row.get("도로명", "")).strip():
        road = str(row.get("도로명", "")).strip()
        return f"{sigungu} {road}"
    
    # 도로명이 없으면 번지 사용
    elif pd.notna(row.get("번지")) and str(row.get("번지", "")).strip():
        bunji = str(row.get("번지", "")).strip()
        return f"{sigungu} {bunji}"
    
    # 둘 다 없으면 시군구만
    else:
        return sigungu

df["full_address"] = df.apply(create_full_address, axis=1)

print(f"full_address 생성 완료")
print(f"\nfull_address 예시 5개:")
print(df["full_address"].head().tolist())

print("\n" + "="*60)
print("Step 2: room_key 생성")
print("="*60)

# --- 1) 방 구분에 쓸 컬럼 이름 설정 ---
COL_ADDR  = "full_address"   # 우리가 만든 컬럼
COL_FLOOR = "층"             # 층
COL_AREA  = "전용면적(㎡)"   # 전용면적

# 전용면적이 소수점이면, 너무 세세하면 같은 방도 다른 값처럼 보일 수 있어서 적당히 반올림
df["area_rounded"] = df[COL_AREA].round(1)

# --- 2) room_key 생성: "주소|층|면적" 조합 ---
df["room_key"] = (
    df[COL_ADDR].astype(str) + "|" +
    df[COL_FLOOR].astype(str) + "|" +
    df["area_rounded"].astype(str)
)

print(f"전체 행 수: {len(df)}")
print(f"room_key 고유 개수: {df['room_key'].nunique()}")
print(f"방당 평균 거래 횟수: {len(df) / df['room_key'].nunique():.2f}")

# --- 3) 같은 room_key인데 거래가 여러 번 있었던 방 몇 개 예시로 보기 ---
room_key_counts = df["room_key"].value_counts()
dup_rooms = pd.DataFrame({
    "room_key": room_key_counts.index,
    "cnt": room_key_counts.values
})

print("\n거래 횟수별 room_key 분포:")
print(dup_rooms["cnt"].value_counts().sort_index().head(10))

print("\n거래가 3번 이상 있었던 room_key 상위 10개:")
dup_3plus = dup_rooms[dup_rooms["cnt"] >= 3].head(10)
print(dup_3plus)

# 실제로 어떤 식으로 중복되는지 한 방(room_key 하나)만 살펴보기
if len(dup_3plus) > 0:
    example_key = dup_3plus["room_key"].iloc[0]
    print(f"\n예시 room_key: {example_key}")
    print(f"이 방의 거래 횟수: {dup_3plus[dup_3plus['room_key'] == example_key]['cnt'].values[0]}")
    
    example_data = df[df["room_key"] == example_key][
        [COL_ADDR, COL_FLOOR, COL_AREA, "계약년월", "contract_year", "contract_month",
         "보증금(만원)", "월세금(만원)", "converted_monthly_cost", "real_monthly_cost", "real_cost_per_m2"]
    ].sort_values(["contract_year", "contract_month"])
    
    print("\n이 방의 거래 이력:")
    print(example_data.to_string())

print("\n" + "="*60)
print("Step 3: 완전 중복 행 체크")
print("="*60)

# 완전한 중복 행 체크 (모든 컬럼 동일)
# room_key와 계약년월 같은 주요 컬럼만 체크
check_cols = ["room_key", "계약년월", "보증금(만원)", "월세금(만원)", "전용면적(㎡)"]
dup_full = df.duplicated(subset=check_cols, keep=False)

print(f"완전 중복 행 수 (주요 컬럼 기준): {dup_full.sum()}")

if dup_full.sum() > 0:
    print("\n중복 행 예시:")
    dup_example = df[dup_full].head(10)
    print(dup_example[["room_key", "계약년월", "보증금(만원)", "월세금(만원)"]].to_string())
    
    # 중복 제거 (첫 번째만 유지)
    print(f"\n중복 제거 전: {len(df)}행")
    df = df.drop_duplicates(subset=check_cols, keep='first')
    print(f"중복 제거 후: {len(df)}행")
else:
    print("완전 중복 행이 없습니다.")

print("\n" + "="*60)
print("Step 4: room_key 통계 요약")
print("="*60)

# 거래 횟수별 분포
transaction_counts = df["room_key"].value_counts()
print("\n거래 횟수별 방 개수:")
for i in range(1, 11):
    count = (transaction_counts == i).sum()
    if count > 0:
        print(f"  {i}회 거래: {count}개 방")

print(f"\n10회 이상 거래: {(transaction_counts >= 10).sum()}개 방")
print(f"최대 거래 횟수: {transaction_counts.max()}회")

# 저장
output_file = "real_estate/preprogressed/final_data_with_real_costs.csv"
df.to_csv(output_file, index=False, encoding="utf-8-sig")
print(f"\n✓ room_key가 추가된 데이터 저장 완료: {output_file}")
print(f"  추가된 컬럼: full_address, area_rounded, room_key")

