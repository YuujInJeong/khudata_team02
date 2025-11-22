"""
경희대 국제캠퍼스까지 거리 시각화

지도 위에 부동산 위치와 거리를 표시하고,
거리 분포 및 거리-가격 관계를 시각화합니다.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap, MarkerCluster
import os

# 한글 폰트 설정
plt.rcParams['font.family'] = 'AppleGothic'  # macOS
plt.rcParams['axes.unicode_minus'] = False

def visualize_campus_distance(input_file: str, output_dir: str = "real_estate/preprogressed"):
    """
    경희대 국제캠퍼스까지 거리를 다양한 방식으로 시각화합니다.
    """
    print("="*60)
    print("경희대 국제캠퍼스 거리 시각화")
    print("="*60)
    
    # 데이터 로드
    print(f"\n데이터 로드 중: {input_file}")
    df = pd.read_csv(input_file, encoding="utf-8-sig", low_memory=False)
    
    # 좌표가 있는 데이터만 필터링
    df_coords = df[df["latitude"].notna() & df["longitude"].notna() & df["dist_to_campus_m"].notna()].copy()
    print(f"시각화할 데이터: {len(df_coords):,}개")
    
    # 경희대 국제캠퍼스 좌표
    KHU_ICAMPUS = (37.2430, 127.0801)  # (lat, lon)
    
    # ============================================================
    # 1. 지도 위에 점으로 표시 (Folium)
    # ============================================================
    print("\n1. 인터랙티브 지도 생성 중...")
    
    # 지도 중심을 경희대 국제캠퍼스로 설정
    m = folium.Map(
        location=KHU_ICAMPUS,
        zoom_start=13,
        tiles='OpenStreetMap'
    )
    
    # 경희대 국제캠퍼스 마커 추가
    folium.Marker(
        KHU_ICAMPUS,
        popup='경희대 국제캠퍼스',
        tooltip='경희대 국제캠퍼스',
        icon=folium.Icon(color='red', icon='university', prefix='fa')
    ).add_to(m)
    
    # 거리 구간별 색상 설정
    def get_color(dist):
        if dist < 1000:
            return 'green'
        elif dist < 2000:
            return 'blue'
        elif dist < 3000:
            return 'orange'
        elif dist < 5000:
            return 'purple'
        else:
            return 'red'
    
    # 샘플링 (너무 많으면 느려질 수 있으므로)
    sample_size = min(1000, len(df_coords))
    df_sample = df_coords.sample(n=sample_size, random_state=42) if len(df_coords) > 1000 else df_coords
    
    # 각 부동산 위치에 마커 추가
    for idx, row in df_sample.iterrows():
        dist = row["dist_to_campus_m"]
        color = get_color(dist)
        
        popup_text = f"""
        <b>주소:</b> {row.get('full_address', 'N/A')}<br>
        <b>거리:</b> {dist:.0f}m ({dist/1000:.2f}km)<br>
        <b>실질 월주거비:</b> {row.get('real_monthly_cost', 0):.0f}만원<br>
        <b>캠퍼스 존:</b> {row.get('campus_zone', 'N/A')}
        """
        
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=5,
            popup=folium.Popup(popup_text, max_width=300),
            color=color,
            fill=True,
            fillColor=color,
            fillOpacity=0.6
        ).add_to(m)
    
    # 히트맵 추가
    heat_data = [[row["latitude"], row["longitude"]] for idx, row in df_coords.iterrows()]
    HeatMap(heat_data, radius=15, blur=10, max_zoom=1).add_to(m)
    
    map_file = os.path.join(output_dir, "campus_distance_map.html")
    m.save(map_file)
    print(f"✓ 인터랙티브 지도 저장: {map_file}")
    
    # ============================================================
    # 2. 통계 그래프들
    # ============================================================
    print("\n2. 통계 그래프 생성 중...")
    
    fig = plt.figure(figsize=(20, 12))
    
    # 2-1. 거리 분포 히스토그램
    ax1 = plt.subplot(2, 3, 1)
    ax1.hist(df_coords["dist_to_campus_m"] / 1000, bins=50, edgecolor='black', alpha=0.7, color='skyblue')
    ax1.axvline(df_coords["dist_to_campus_m"].median() / 1000, color='red', linestyle='--', linewidth=2, label=f'중앙값: {df_coords["dist_to_campus_m"].median()/1000:.2f}km')
    ax1.axvline(df_coords["dist_to_campus_m"].mean() / 1000, color='orange', linestyle='--', linewidth=2, label=f'평균: {df_coords["dist_to_campus_m"].mean()/1000:.2f}km')
    ax1.set_xlabel('경희대까지 거리 (km)', fontsize=12)
    ax1.set_ylabel('빈도', fontsize=12)
    ax1.set_title('경희대 국제캠퍼스까지 거리 분포', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2-2. 거리 구간별 분포 (막대 그래프)
    ax2 = plt.subplot(2, 3, 2)
    bins = [0, 500, 1000, 2000, 3000, 5000, 10000]
    labels = ['0-0.5km', '0.5-1km', '1-2km', '2-3km', '3-5km', '5-10km']
    df_coords['dist_category'] = pd.cut(df_coords["dist_to_campus_m"], bins=bins, labels=labels, right=False)
    dist_counts = df_coords['dist_category'].value_counts().sort_index()
    bars = ax2.bar(range(len(dist_counts)), dist_counts.values, color='coral', edgecolor='black', alpha=0.7)
    ax2.set_xticks(range(len(dist_counts)))
    ax2.set_xticklabels(dist_counts.index, rotation=45, ha='right')
    ax2.set_ylabel('건수', fontsize=12)
    ax2.set_title('거리 구간별 부동산 수', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')
    
    # 막대 위에 숫자 표시
    for i, (idx, val) in enumerate(dist_counts.items()):
        ax2.text(i, val, f'{val:,}', ha='center', va='bottom', fontsize=10)
    
    # 2-3. 거리 vs 실질 월주거비 산점도
    ax3 = plt.subplot(2, 3, 3)
    # 실질 월주거비가 0이 아닌 데이터만
    df_valid_cost = df_coords[df_coords["real_monthly_cost"] > 0].copy()
    if len(df_valid_cost) > 0:
        scatter = ax3.scatter(
            df_valid_cost["dist_to_campus_m"] / 1000,
            df_valid_cost["real_monthly_cost"],
            c=df_valid_cost["dist_to_campus_m"] / 1000,
            cmap='viridis',
            alpha=0.5,
            s=20
        )
        ax3.set_xlabel('경희대까지 거리 (km)', fontsize=12)
        ax3.set_ylabel('실질 월주거비 (만원)', fontsize=12)
        ax3.set_title('거리 vs 실질 월주거비', fontsize=14, fontweight='bold')
        plt.colorbar(scatter, ax=ax3, label='거리 (km)')
        ax3.grid(True, alpha=0.3)
    else:
        ax3.text(0.5, 0.5, '데이터 없음', ha='center', va='center', transform=ax3.transAxes)
        ax3.set_title('거리 vs 실질 월주거비 (데이터 없음)', fontsize=14)
    
    # 2-4. 캠퍼스 존별 거리 분포 (박스플롯)
    ax4 = plt.subplot(2, 3, 4)
    if 'campus_zone' in df_coords.columns:
        df_coords_box = df_coords[df_coords['campus_zone'].notna()].copy()
        if len(df_coords_box) > 0:
            zones = df_coords_box['campus_zone'].unique()
            data_to_plot = [df_coords_box[df_coords_box['campus_zone'] == zone]["dist_to_campus_m"] / 1000 for zone in zones]
            bp = ax4.boxplot(data_to_plot, labels=zones, patch_artist=True)
            for patch in bp['boxes']:
                patch.set_facecolor('lightblue')
                patch.set_alpha(0.7)
            ax4.set_ylabel('거리 (km)', fontsize=12)
            ax4.set_title('캠퍼스 존별 거리 분포', fontsize=14, fontweight='bold')
            ax4.grid(True, alpha=0.3, axis='y')
    else:
        ax4.text(0.5, 0.5, 'campus_zone 컬럼 없음', ha='center', va='center', transform=ax4.transAxes)
        ax4.set_title('캠퍼스 존별 거리 분포', fontsize=14)
    
    # 2-5. 거리 vs m²당 실질 월주거비
    ax5 = plt.subplot(2, 3, 5)
    df_valid_m2 = df_coords[df_coords["real_cost_per_m2"] > 0].copy()
    if len(df_valid_m2) > 0:
        scatter2 = ax5.scatter(
            df_valid_m2["dist_to_campus_m"] / 1000,
            df_valid_m2["real_cost_per_m2"],
            c=df_valid_m2["dist_to_campus_m"] / 1000,
            cmap='plasma',
            alpha=0.5,
            s=20
        )
        ax5.set_xlabel('경희대까지 거리 (km)', fontsize=12)
        ax5.set_ylabel('m²당 실질 월주거비 (만원/㎡)', fontsize=12)
        ax5.set_title('거리 vs m²당 실질 월주거비', fontsize=14, fontweight='bold')
        plt.colorbar(scatter2, ax=ax5, label='거리 (km)')
        ax5.grid(True, alpha=0.3)
    else:
        ax5.text(0.5, 0.5, '데이터 없음', ha='center', va='center', transform=ax5.transAxes)
        ax5.set_title('거리 vs m²당 실질 월주거비 (데이터 없음)', fontsize=14)
    
    # 2-6. 거리 구간별 평균 실질 월주거비
    ax6 = plt.subplot(2, 3, 6)
    if len(df_valid_cost) > 0:
        df_valid_cost['dist_category'] = pd.cut(df_valid_cost["dist_to_campus_m"], bins=bins, labels=labels, right=False)
        avg_cost_by_dist = df_valid_cost.groupby('dist_category')['real_monthly_cost'].mean()
        bars2 = ax6.bar(range(len(avg_cost_by_dist)), avg_cost_by_dist.values, color='lightgreen', edgecolor='black', alpha=0.7)
        ax6.set_xticks(range(len(avg_cost_by_dist)))
        ax6.set_xticklabels(avg_cost_by_dist.index, rotation=45, ha='right')
        ax6.set_ylabel('평균 실질 월주거비 (만원)', fontsize=12)
        ax6.set_title('거리 구간별 평균 실질 월주거비', fontsize=14, fontweight='bold')
        ax6.grid(True, alpha=0.3, axis='y')
        
        # 막대 위에 숫자 표시
        for i, (idx, val) in enumerate(avg_cost_by_dist.items()):
            ax6.text(i, val, f'{val:.0f}', ha='center', va='bottom', fontsize=10)
    else:
        ax6.text(0.5, 0.5, '데이터 없음', ha='center', va='center', transform=ax6.transAxes)
        ax6.set_title('거리 구간별 평균 실질 월주거비 (데이터 없음)', fontsize=14)
    
    plt.tight_layout()
    
    graph_file = os.path.join(output_dir, "campus_distance_visualization.png")
    plt.savefig(graph_file, dpi=300, bbox_inches='tight')
    print(f"✓ 통계 그래프 저장: {graph_file}")
    plt.close()
    
    # ============================================================
    # 3. 요약 통계 출력
    # ============================================================
    print("\n" + "="*60)
    print("시각화 요약 통계")
    print("="*60)
    print(f"총 시각화된 데이터: {len(df_coords):,}개")
    print(f"거리 범위: {df_coords['dist_to_campus_m'].min():.0f}m ~ {df_coords['dist_to_campus_m'].max():.0f}m")
    print(f"평균 거리: {df_coords['dist_to_campus_m'].mean():.1f}m ({df_coords['dist_to_campus_m'].mean()/1000:.2f}km)")
    print(f"중앙값 거리: {df_coords['dist_to_campus_m'].median():.1f}m ({df_coords['dist_to_campus_m'].median()/1000:.2f}km)")
    
    if len(df_valid_cost) > 0:
        print(f"\n거리와 가격 상관관계:")
        correlation = df_valid_cost[['dist_to_campus_m', 'real_monthly_cost']].corr().iloc[0, 1]
        print(f"  거리-실질월주거비 상관계수: {correlation:.3f}")
    
    print("\n" + "="*60)
    print("시각화 완료!")
    print("="*60)
    print(f"\n생성된 파일:")
    print(f"  1. {map_file} (인터랙티브 지도)")
    print(f"  2. {graph_file} (통계 그래프)")

if __name__ == "__main__":
    input_path = "real_estate/preprogressed/final_data_with_real_costs.csv"
    visualize_campus_distance(input_path)

