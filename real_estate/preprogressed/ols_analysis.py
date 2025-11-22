"""
real_cost_per_m2를 타겟으로 하는 OLS 회귀분석
- 교차항 포함
- 이상치 탐지
- 시각화
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
import warnings
warnings.filterwarnings('ignore')

# 한글 폰트 설정
plt.rcParams['font.family'] = 'AppleGothic'  # macOS
plt.rcParams['axes.unicode_minus'] = False

print("="*60)
print("Step 1: 데이터 로드 및 전처리")
print("="*60)

# 데이터 로드
df = pd.read_csv("real_estate/preprogressed/final_data_with_real_costs.csv", 
                 encoding="utf-8-sig", low_memory=False)

print(f"원본 데이터 shape: {df.shape}")
print(f"\n컬럼 목록: {df.columns.tolist()}")

# 타겟 변수 확인
print(f"\nreal_cost_per_m2 통계:")
print(df["real_cost_per_m2"].describe())
print(f"\nreal_cost_per_m2 결측치: {df['real_cost_per_m2'].isna().sum()}개")

# 분석용 데이터 준비 (결측치 제거)
df_clean = df.dropna(subset=["real_cost_per_m2"]).copy()
print(f"\n결측치 제거 후 shape: {df_clean.shape}")

# 0 또는 음수 값 제거 (의미 없는 값)
df_clean = df_clean[df_clean["real_cost_per_m2"] > 0].copy()
print(f"양수 값만 남긴 후 shape: {df_clean.shape}")

print("\n" + "="*60)
print("Step 2: 독립변수 준비")
print("="*60)

# 숫자형 변수 준비
numeric_vars = {
    "전용면적(㎡)": "area",
    "보증금(만원)": "deposit",
    "월세금(만원)": "monthly_rent",
    "층": "floor",
    "건축년도": "build_year",
    "contract_year": "contract_year",
    "contract_month": "contract_month",
    "annual_rate": "annual_rate",
    "cpi_index": "cpi_index"
}

# 변수 생성
for col, name in numeric_vars.items():
    if col in df_clean.columns:
        df_clean[name] = pd.to_numeric(df_clean[col], errors="coerce")

# 건축년도로부터 건물 연령 계산
if "build_year" in df_clean.columns:
    df_clean["building_age"] = df_clean["contract_year"] - df_clean["build_year"]
    df_clean["building_age"] = df_clean["building_age"].fillna(df_clean["building_age"].median())

# 범주형 변수 더미화
categorical_vars = {
    "부동산유형": "property_type",
    "전월세구분": "rent_type",
    "campus_zone": "campus_zone"
}

dummy_cols_list = []
for col, name in categorical_vars.items():
    if col in df_clean.columns:
        dummies = pd.get_dummies(df_clean[col], prefix=name, drop_first=True)
        df_clean = pd.concat([df_clean, dummies], axis=1)
        dummy_cols_list.extend(dummies.columns.tolist())

print("\n생성된 변수들:")
print([col for col in df_clean.columns if col in ["area", "deposit", "monthly_rent", 
                                                   "floor", "building_age", "contract_year",
                                                   "annual_rate", "cpi_index"]])

print("\n더미 변수들:")
dummy_cols = dummy_cols_list
print(dummy_cols)

print("\n" + "="*60)
print("Step 3: 독립변수 선택 및 교차항 생성")
print("="*60)

# 기본 독립변수
base_vars = ["area", "deposit", "monthly_rent", "floor", "building_age"]

# 교차항 생성
interaction_terms = []
if all(col in df_clean.columns for col in ["area", "deposit"]):
    df_clean["area_x_deposit"] = df_clean["area"] * df_clean["deposit"]
    interaction_terms.append("area_x_deposit")

if all(col in df_clean.columns for col in ["area", "monthly_rent"]):
    df_clean["area_x_monthly_rent"] = df_clean["area"] * df_clean["monthly_rent"]
    interaction_terms.append("area_x_monthly_rent")

if all(col in df_clean.columns for col in ["area", "building_age"]):
    df_clean["area_x_age"] = df_clean["area"] * df_clean["building_age"]
    interaction_terms.append("area_x_age")

if all(col in df_clean.columns for col in ["deposit", "monthly_rent"]):
    df_clean["deposit_x_rent"] = df_clean["deposit"] * df_clean["monthly_rent"]
    interaction_terms.append("deposit_x_rent")

if all(col in df_clean.columns for col in ["campus_zone_core", "area"]):
    df_clean["core_x_area"] = df_clean.get("campus_zone_core", 0) * df_clean["area"]
    interaction_terms.append("core_x_area")

print(f"생성된 교차항: {interaction_terms}")

# 최종 독립변수 리스트
feature_vars = base_vars + interaction_terms + dummy_cols

# 결측치가 있는 변수 제거
available_vars = [v for v in feature_vars if v in df_clean.columns and df_clean[v].notna().sum() > 0]

print(f"\n사용 가능한 독립변수 수: {len(available_vars)}")

# 분석용 데이터프레임 생성
analysis_vars = ["real_cost_per_m2"] + available_vars
df_analysis = df_clean[analysis_vars].dropna().copy()

# 모든 변수를 숫자형으로 변환
for col in available_vars:
    if col in df_analysis.columns:
        df_analysis[col] = pd.to_numeric(df_analysis[col], errors='coerce')

# 다시 결측치 제거
df_analysis = df_analysis.dropna()

print(f"\n최종 분석 데이터 shape: {df_analysis.shape}")
print(f"타겟 변수 통계:")
print(df_analysis["real_cost_per_m2"].describe())

print("\n" + "="*60)
print("Step 4: OLS 회귀분석")
print("="*60)

# 독립변수와 종속변수 분리
X = df_analysis[available_vars].copy()
y = df_analysis["real_cost_per_m2"].copy()

# 모든 변수를 float64로 변환
X = X.astype(float)
y = y.astype(float)

# 상수항 추가
X_with_const = sm.add_constant(X)

# OLS 모델 적합
model = sm.OLS(y, X_with_const).fit()

print("\n회귀분석 결과:")
print(model.summary())

# VIF (다중공선성) 확인
print("\n" + "="*60)
print("Step 5: 다중공선성 확인 (VIF)")
print("="*60)

vif_data = pd.DataFrame()
vif_data["Variable"] = X_with_const.columns
vif_data["VIF"] = [variance_inflation_factor(X_with_const.values, i) 
                   for i in range(X_with_const.shape[1])]

print("\nVIF 값 (10 이상이면 다중공선성 문제):")
print(vif_data.sort_values("VIF", ascending=False).head(20))

print("\n" + "="*60)
print("Step 6: 이상치 탐지")
print("="*60)

# 잔차 계산
y_pred = model.predict(X_with_const)
residuals = y - y_pred
standardized_residuals = residuals / residuals.std()

# 이상치 기준 (표준화 잔차의 절댓값이 3 이상)
outlier_threshold = 3
outliers = np.abs(standardized_residuals) > outlier_threshold

print(f"\n이상치 개수 (|표준화 잔차| > {outlier_threshold}): {outliers.sum()}개")
print(f"이상치 비율: {outliers.sum() / len(outliers) * 100:.2f}%")

# Cook's Distance 계산
influence = model.get_influence()
cooks_d = influence.cooks_distance[0]
cooks_threshold = 4 / len(y)  # 일반적인 기준

high_influence = cooks_d > cooks_threshold
print(f"\n높은 영향력 관측치 (Cook's D > {cooks_threshold:.4f}): {high_influence.sum()}개")

print("\n" + "="*60)
print("Step 7: 시각화")
print("="*60)

# 그래프 생성
fig = plt.figure(figsize=(20, 15))

# 1. 잔차 플롯
ax1 = plt.subplot(3, 3, 1)
ax1.scatter(y_pred, residuals, alpha=0.5, s=10)
ax1.axhline(y=0, color='r', linestyle='--')
ax1.set_xlabel('예측값')
ax1.set_ylabel('잔차')
ax1.set_title('잔차 플롯 (Residual Plot)')
ax1.grid(True, alpha=0.3)

# 2. 표준화 잔차 플롯
ax2 = plt.subplot(3, 3, 2)
ax2.scatter(y_pred, standardized_residuals, alpha=0.5, s=10)
ax2.axhline(y=0, color='r', linestyle='--')
ax2.axhline(y=outlier_threshold, color='orange', linestyle='--', label=f'이상치 기준 ({outlier_threshold})')
ax2.axhline(y=-outlier_threshold, color='orange', linestyle='--')
ax2.set_xlabel('예측값')
ax2.set_ylabel('표준화 잔차')
ax2.set_title('표준화 잔차 플롯')
ax2.legend()
ax2.grid(True, alpha=0.3)

# 3. Q-Q 플롯
ax3 = plt.subplot(3, 3, 3)
sm.qqplot(residuals, line='s', ax=ax3)
ax3.set_title('Q-Q 플롯 (정규성 검정)')
ax3.grid(True, alpha=0.3)

# 4. Cook's Distance
ax4 = plt.subplot(3, 3, 4)
ax4.scatter(range(len(cooks_d)), cooks_d, alpha=0.5, s=10)
ax4.axhline(y=cooks_threshold, color='r', linestyle='--', label=f'기준 ({cooks_threshold:.4f})')
ax4.set_xlabel('관측치 번호')
ax4.set_ylabel("Cook's Distance")
ax4.set_title("Cook's Distance")
ax4.legend()
ax4.grid(True, alpha=0.3)

# 5. 실제값 vs 예측값
ax5 = plt.subplot(3, 3, 5)
ax5.scatter(y, y_pred, alpha=0.5, s=10)
ax5.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
ax5.set_xlabel('실제값')
ax5.set_ylabel('예측값')
ax5.set_title(f'실제값 vs 예측값 (R² = {model.rsquared:.3f})')
ax5.grid(True, alpha=0.3)

# 6. 타겟 변수 분포
ax6 = plt.subplot(3, 3, 6)
ax6.hist(y, bins=50, edgecolor='black', alpha=0.7)
ax6.set_xlabel('real_cost_per_m2')
ax6.set_ylabel('빈도')
ax6.set_title('타겟 변수 분포')
ax6.grid(True, alpha=0.3)

# 7. 잔차 분포
ax7 = plt.subplot(3, 3, 7)
ax7.hist(residuals, bins=50, edgecolor='black', alpha=0.7)
ax7.set_xlabel('잔차')
ax7.set_ylabel('빈도')
ax7.set_title('잔차 분포')
ax7.grid(True, alpha=0.3)

# 8. 주요 변수별 영향력 (상위 10개)
coef_df = pd.DataFrame({
    '변수': model.params.index[1:],  # 상수항 제외
    '계수': model.params.values[1:],
    'p-value': model.pvalues.values[1:]
})
coef_df = coef_df.sort_values('계수', key=abs, ascending=False).head(10)

ax8 = plt.subplot(3, 3, 8)
colors = ['red' if p < 0.05 else 'gray' for p in coef_df['p-value']]
ax8.barh(range(len(coef_df)), coef_df['계수'], color=colors)
ax8.set_yticks(range(len(coef_df)))
ax8.set_yticklabels(coef_df['변수'], fontsize=8)
ax8.set_xlabel('계수')
ax8.set_title('주요 변수 계수 (상위 10개)\n빨강: p<0.05, 회색: p≥0.05')
ax8.grid(True, alpha=0.3, axis='x')

# 9. 이상치 표시
ax9 = plt.subplot(3, 3, 9)
ax9.scatter(y[~outliers], y_pred[~outliers], alpha=0.5, s=10, label='정상')
ax9.scatter(y[outliers], y_pred[outliers], alpha=0.7, s=20, color='red', label='이상치')
ax9.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
ax9.set_xlabel('실제값')
ax9.set_ylabel('예측값')
ax9.set_title(f'이상치 시각화 ({outliers.sum()}개)')
ax9.legend()
ax9.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('real_estate/preprogressed/ols_analysis_results.png', dpi=300, bbox_inches='tight')
print("\n✓ 그래프 저장 완료: real_estate/preprogressed/ols_analysis_results.png")

# 주요 변수 요약
print("\n" + "="*60)
print("Step 8: 주요 변수 요약")
print("="*60)

print("\n유의한 변수 (p < 0.05):")
significant_vars = coef_df[coef_df['p-value'] < 0.05].sort_values('계수', key=abs, ascending=False)
print(significant_vars)

print("\n모델 성능:")
print(f"  R²: {model.rsquared:.4f}")
print(f"  조정 R²: {model.rsquared_adj:.4f}")
print(f"  RMSE: {np.sqrt(mean_squared_error(y, y_pred)):.4f}")

# 이상치 상세 정보
print("\n이상치 상세 정보 (상위 10개):")
outlier_df = df_analysis[outliers].copy()
outlier_df['residual'] = residuals[outliers]
outlier_df['standardized_residual'] = standardized_residuals[outliers]
outlier_df = outlier_df.sort_values('standardized_residual', key=abs, ascending=False).head(10)
print(outlier_df[['real_cost_per_m2', 'area', 'deposit', 'monthly_rent', 
                  'residual', 'standardized_residual']].to_string())

plt.show()

