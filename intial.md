실거래 예측가와 환경 리스크를 기반으로 AI가 '괜찮은 옵션'을 제공하는 서비스 모델링을 위해, 타겟 변수, 리스크 변수, 통제 변수의 선정 조건 및 잔차 추출 시 지역 단위 설정에 대한 보고서를 제공합니다.

### 타겟 변수, 리스크 변수, 통제 변인의 선정 조건

#### 타겟 변수 (Target Variable)
타겟 변수는 예측 모델에서 목표로 하는 값으로, 실거래가 예측 모델에서는 주로 주택의 거래 금액과 관련된 변수들을 활용합니다.

*   **정의 및 조건**:
    *   **실거래 가격**: 아파트의 실거래가를 타겟 변수로 사용하는 연구가 많습니다. 주택 가격 예측 모형 연구에서 서울시 주택 매매 실거래가를 중심으로 분석을 진행하기도 합니다. 부동산 전월세 매물 예측 모델 개발을 위해 진주시 14개 동의 아파트 및 오피스텔 실거래가 데이터가 사용된 사례도 있습니다. 특히 아파트 단지 단위에서 실거래가를 분석하여 머신러닝 기법의 예측력을 검증하기도 했습니다.
    *   **단위면적당 실거래가**: '단위면적당 실거래가'를 Target 변수로 설정하고 독립변수와의 상관계수를 도출하는 연구도 있습니다. 아파트 실거래가에 영향을 미치는 변인들의 시공간적 이질성을 탐색하는 데 아파트 실거래가가 활용되기도 합니다. 주택 가격 변동률 분포의 특성 분석을 위해 개별 주택가격에 대한 패널데이터를 구축하여 가격지수가 아닌 변화율의 분포를 통해 주택 시장의 변동성을 분석하기도 합니다.
    *   **거래금액 (단위: 만원)**: 서울시 아파트 실거래가 매매 데이터를 기반으로 아파트 가격을 예측하는 대회에서는 각 시점에서의 거래금액(단위: 만원)을 예측하는 것을 목표로 설정하기도 했습니다.

#### 리스크 변수 (Risk Variable)
리스크 변수는 예측 결과의 불확실성이나 위험도를 나타내는 요소로 사용됩니다.

*   **정의 및 조건**:
    *   **부동산 특성 요인의 영향**: 특정 요인들이 실거래가 예측 잔차에 미치는 영향을 분석하는 데 활용됩니다. 부동산 특성(예: 비정형성)이 모델 잔차에 미치는 영향을 검증하여 부동산 시장 분석을 지원할 수 있습니다.
    *   **시장 리스크**: 주택 가격 변동의 시장 리스크를 반영하여 조정된 민감도를 나타내는 변수를 사용할 수 있습니다. 전국 단위의 아파트 가격 지수를 시장 포트폴리오의 대리변수로 활용할 수 있습니다.
    *   **부동산 프로젝트 파이낸싱(PF) 사업 리스크**: 부동산 PF 사업의 안정적 추진을 위해 사업단계별 리스크 요인(사업 안전성, 수익 계획, 사업 계획, 시장 환경, 사업비 증가, 자금 조달, 인허가, 사업 지연, 현금 흐름, 공기 연장, 공사 중단 리스크 등)을 도출하고 이들 요인 간의 영향 관계를 분석할 수 있습니다. 이 중 사업비 증가, 현금 흐름, 사업 안전성, 자금 조달, 인허가 리스크가 PF 사업 안정성에 큰 영향을 미치는 것으로 나타났습니다.
    *   **주택 시장 참여 법인의 거래량**: 법인이 매수한 부동산 거래량을 종속변수로 하여 주택 시장 및 거시경제 변수(서울시 아파트 가격지수, 시군구 주민등록세대수 증가율, 이자율, 코스피지수 등)를 독립변수로 설정하고 리스크 요인을 분석할 수도 있습니다.

#### 통제 변수 (Control Variable)
통제 변수는 예측 모델의 정확도를 높이기 위해, 타겟 변수에 영향을 미칠 수 있는 외부 요인들을 제어하는 데 사용됩니다.

*   **정의 및 조건**:
    *   **아파트 정보 및 경제지표**: 미래 아파트 매매 실거래가격을 예측하는 모델에서는 다양한 아파트 정보와 경제지표 등 가능한 많은 변수를 수집하여 다중 공선성 문제를 해결하며 사용합니다.
    *   **지역적 특성**: 부동산은 공간적 의존성과 이질성 문제가 발생할 수 있어, 공간적 자기상관성을 고려한 분석 방법이 요구됩니다. 부산시의 공동주택을 대상으로 지역별 주택 가격을 형성하는 공간회귀모형을 구축하여 지역별 가격 결정 요인의 다양성을 분석한 사례가 있습니다.
    *   **주택 특성**: 주택 가격에 영향을 미치는 다양한 특성을 설명하기 위해 헤도닉 가격 모형이 활용됩니다. 주택 가격 추정에 있어 전통적인 OLS 모형과 공간계량모형의 적합도를 평가하여 우수한 모형을 선정하기도 합니다.
    *   **거시경제 변수**: 주택 가격에 큰 영향을 미치는 거시경제 변수로는 CD금리(91일물), 총통화평잔증가율(M2), 코스피지수, 주거용지가 변동률 등을 선정할 수 있습니다. 주택가격지수 예측 모형에서는 외부 충격 요인(개입 효과)이 주택가격지수에 미치는 영향을 파악하는 것이 중요합니다. 또한, 부동산 안정화 정책이 시장 가격 안정에 도움이 되지만, 부동산 소비 심리에 영향을 주는 요인이 될 수 있음을 인지하는 것이 정책의 적시성과 효과에 유리합니다.
    *   **전월세 특성**: 전세 특성을 고려한 예측 모형은 전세 특성을 고려하지 않은 경우보다 예측 정확도가 상승하여, 전세 특성이 가격 예측에 중요한 요인으로 작용함이 입증되었습니다.
    *   **실거래가 자료**: 상업용 부동산 실거래가 결정 시 영향을 미치는 요인(생활권, 금액, 변수, 특성별)을 구분하여 분석하기도 합니다.
    *   **정책 변수**: 부동산 수요 조절 정책이 주택 가격에 미치는 영향을 분석할 때, 금융 및 세금 규제와 같은 정책 변수를 고려할 수 있습니다.

### 잔차 추출 시 지역 단위 설정

잔차를 추출할 때 지역 단위는 분석의 목적과 활용 가능한 데이터의 세분화 정도에 따라 달라질 수 있습니다.

*   **행정 구역 단위**:
    *   **동 단위**: 서울시 아파트 실거래가 변화 패턴을 분석하기 위해 아파트별 및 동별 평균 실거래가 자료를 활용하여 GIS 데이터로 구축한 사례가 있습니다.
    *   **구 단위**: 서울시 아파트 실거래가의 공간적 불균형을 분석할 때 구 단위의 자료를 활용하기도 합니다. 특정 연구에서는 서울의 강남구, 서초구 등 8개 구를 투기 지역으로 지정하여 분석하기도 했습니다. 서울시 오피스 시장의 실거래 가격을 바탕으로 도심 지역과 강남 지역의 특성을 분석하는 연구도 있습니다. 또한 서울시의 25개 자치구를 대상으로 주택가격, 인구, 지역내총생산의 인과성을 분석하기도 했습니다.
    *   **시·도 단위**: 우리나라 16개 시·도 지역의 주택 가격 변화를 공간 패널 모형을 활용하여 분석한 연구가 있습니다. 공동주택 실거래 가격의 지역별 상관성 분석에서는 서울과 경기 지역의 아파트 매매 가격이 가장 높게 나타났으며, 특히 서울의 동남권 및 도시 지역이 가장 높은 것으로 나타났습니다.
*   **미시적 단위**:
    *   **개별 아파트 단지 단위**: 아파트 실거래가를 이용하여 단기적이고 국지적인 시장 분석이 용이하다는 연구 결과가 있습니다. 미시적 단위의 시공간 빅데이터를 활용하여 실거래가와 공시 가격 차이의 공간적 분포를 분석하기도 합니다.
    *   **하위 시장**: 서울시 주택 시장은 여러 이질적인 주택 하위 시장으로 구성되어 있으며, 주택 특성의 가격 효과가 국지적으로 다름을 확인할 수 있습니다. 이를 통해 미시적인 주택 하위 시장 분석 및 부동산 정책 수립에 활용할 수 있습니다.
*   **유의 사항**:
    *   **데이터의 가용성**: 국토교통부에서 제공하는 부동산 실거래가 공개 시스템을 통해 주택, 오피스텔 등 매매 실거래 정보가 공개되고 있습니다.
    *   **지역별 이질성**: 아파트 실거래가와 같은 공간 데이터에 영향을 미치는 외부 환경도 지역별 이질성이 크기 때문에 공간적 편차가 나타납니다. 따라서 지역별 상이한 특성과 환경을 고려하는 것이 중요합니다.
    *   **잔차의 공간적 상관관계**: 잔차의 상관관계를 측정하여 분석할 수 있으며, 공간적 자기상관 관계를 반영한 모델이 전통적인 모델보다 설명력이 높은 경우가 있습니다.

출처: 
[1] Hypothesis testing in hedonic price estimation – On the selection of independent variables, https://link.springer.com/article/10.1007/s001689900010
[2] Hedonic Regression Analysis in Real Estate Markets: A Primer, https://www.semanticscholar.org/paper/711bfe50493450f567496c130cc3e691409fb071
[3] Econometric Identification of the Impact of Real Estate Characteristics Based on Predictive and Studentized Residuals, https://www.semanticscholar.org/paper/54e9002b3fd9d8d419fc979ff65c281e7a348244
[4] 딥러닝 기법과 잔차 크리깅을 이용한 지가 예측, https://www.kdiss.org/journal/download_pdf.php?doi=10.7465/jkdi.2021.32.3.475
[5] (PDF) Empirical Analysis of XGBoost-based Real Estate ..., https://www.researchgate.net/publication/394553972_Empirical_Analysis_of_XGBoost-based_Real_Estate_Automated_Valuation_Model
[6] 딥러닝과 머신러닝을 이용한 아파트 실거래가 예측, https://ktsde.kips.or.kr/journals/ktsde/digital-library/manuscript/file/38415/01-22M-05-009-%EC%98%A4%ED%95%98%EC%98%81_59-76.pdf
[7] 기계학습을 이용한 부동산 전월세 매물 예측 연구: 경상남도 진주 지역을 사례로, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE11652057
[8] 기계 학습을 이용한 공동주택 가격 추정: 서울 강남구를 사례로*, http://www.kreaa.or.kr/data/vol24-1/24_01_05.pdf
[9] Upstage AI LAB 대회 회고 : [ML] House Price Prediction, https://refine-thinking.tistory.com/58
[10] 국토정책 Brief, https://www.krihs.re.kr/boardDownload.es?bid=0008&list_no=397975&seq=3
[11] 서울시 아파트가격의 동학적 특성에 관한 연구, http://kreaa.or.kr/data/vol19-4/08--%EB%B0%95%ED%97%8C%EC%88%98.pdf
[12] 51-2대지01Shawn Shen.indd, https://www.kgeography.or.kr/media/11/fixture/data/bbs/publishing/journal/51/02/51-2-all.pdf
[13] 인공지능(AI)의 MLP모델을 이용한 주택 가격 정보 예측 기법, https://koreascience.kr/article/JAKO202521154004490.page;
[14] 빅데이터를 활용한 주택시장 분석 및 예측 모형 개발 ..., https://www.codil.or.kr/filebank/original/RK/OTKCRK220247/OTKCRK220247.pdf?stream=T
[15] Modelling real property transactions: an overview, https://www.semanticscholar.org/paper/daf323fc0202fb8ca2c36c3331232baee4ea7089
[16] 심리변수에 따른 아파트 매매가격지수 예측력 비교 분석, https://www.kpaj.or.kr/xml/36621/36621.pdf
[17] 비영리 - S-Space - 서울대학교, https://s-space.snu.ac.kr/bitstream/10371/120377/1/000000053288.pdf
[18] 뉴스 빅데이터를 이용한 전세 가격 예측, http://www.reacademy.org/rboard/data/krea2_new/69_4.pdf
[19] 공공데이터 분석을 통한 변동성 요인 분석과 예측 모델 생성에 대한 연구, https://www.kais99.org/jkais/journal/Vol24No12/vol24no12p086.pdf
[20] 서울시의 지역주거환경특성이 주택가격에 미치는 영향 ..., http://www.kreaa.or.kr/data/vol19-4/15--%EC%9C%A4%ED%9A%A8%EB%AC%B5.pdf
[21] 주택가격의 공간적 영향력 검증 - - 서울과 부산의 아파트 ..., https://www.codil.or.kr/filebank/original/RK/OTKARK950359//OTKARK950359.pdf
[22] 머신러닝과 패널고정효과를 활용한 아파트 실거래가 예측 비교: Predicting Actual Transaction apartment Price Using Machine Learning Methods and Fixed Effects …, https://www.dbpia.co.kr/journal/detail?nodeId=T15741884
[23] 머신 러닝 방법과 시계열 분석 모형을 이용한 부동산 가격 ..., https://kahps.org/data/hshd/pdf_75_5
[24] 딥러닝(Deep Learning)을 이용한 주택가격 예측모형 연구 ..., http://sam.riss.kr/findThesisAnalysis.do?controlNo=000014659291&docType=T
[25] 머신러닝을 활용한 부동산 실거래가 요인 분석, https://ksc21.net/plugin/file_down.php?sys_filename=156_h_sfile.pdf&down_filename=14_%EC%A7%80%EC%A0%8139%EA%B6%8C3%ED%98%B8_%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D%EC%9D%84_%ED%99%9C%EC%9A%A9%ED%95%9C(199-210)_%EB%B0%95%EC%84%9C%ED%98%84.%EA%B9%80%EB%8F%84%ED%98%95.pdf&down_dir=hak
[26] 단독주택가격 추정을 위한 기계학습 모형의 응용, https://www.kgeography.or.kr/media/11/fixture/data/bbs/publishing/journal/51/02/03.pdf
[27] XGBoost 기반 부동산 자동가치산정모형 (Automated ..., https://www.ejrea.org/archive/view_article?pid=jrea-11-2-21
[28] 라쏘 방법을 이용한 수도권 주택 매매가 및 전세가 예측 변인 ..., https://econeng.sogang.ac.kr/Download?pathStr=NTQjIzU0IyM1NyMjNTEjIzEyNCMjMTA0IyMxMTYjIzk3IyM4MCMjMTAxIyMxMDgjIzEwNSMjMTAyIyMzNSMjMzMjIzM1IyM0OSMjMTI0IyMxMjAjIzEwMSMjMTAwIyMxMTAjIzEwNSMjMzUjIzMzIyMzNSMjNTQjIzU3IyM1MiMjNTYjIzU2IyM1NiMjMTI0IyMxMDAjIzEwNSMjMTA3IyMxMTI=&fileName=JOME_V51_3_1.pdf&gubun=board
[29] 구조방정식을 이용한 서울시 권역별 주상복합아파트 실거래가 영향요인 및 인과구조 분석, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE01998998
[30] 머신러닝을 활용한 아파트 매도 호가와 매물량이 실거래가에 ..., https://ki-it.com/xml/38205/38205.pdf
[31] 인공지능을 이용한 주택가격 변동성 예측 모델 연구: 전통통계모형과 인공지능학습모형 융합을 중심으로: Design of Real Estate Prediction Model based on Bigdata with …, https://www.dbpia.co.kr/journal/detail?nodeId=T16674817
[32] 부동산 정책에 따른 서울시 아파트 가격지수 변화방향에 대한 ..., https://koreascience.kr/article/CFKO201125752340480.pdf
[33] 공간통계기법을 이용한 서울시 아파트 실거래가 변인의 ..., https://koreascience.kr/article/JAKO201610235352362.pdf
[34] 머신러닝과 패널고정효과를 활용한 아파트 실거래가 예측, https://kahps.org/data/hshd/pdf_91_2
[35] Real Estate Price Modeling and Empirical Analysis, https://link.springer.com/article/10.1007/BF03405736
[36] 주택구매소비자의 의사결정구조를 반영한 ..., https://kremap.krihs.re.kr/File/%EB%B0%95%EC%B2%9C%EA%B7%9C,%20%EA%B9%80%EC%A7%80%ED%98%9C,%20%ED%99%A9%EA%B4%80%EC%84%9D,%20%EC%98%A4%EB%AF%BC%EC%A4%80,%20%EC%B5%9C%EC%A7%84,%20%EA%B6%8C%EA%B1%B4%EC%9A%B0,%20%EC%98%A4%EC%95%84%EC%97%B0,%20%ED%99%A9%EC%9D%B8%EC%98%81.%202020.%20%EC%A3%BC%ED%83%9D%EA%B5%AC%EB%A7%A4%EC%86%8C%EB%B9%84%EC%9E%90%EC%9D%98%20%EC%9D%98%EC%82%AC%EA%B2%B0%EC%A0%95%EA%B5%AC%EC%A1%B0%EB%A5%BC%20%EB%B0%98%EC%98%81%ED%95%9C%20%EC%A3%BC%ED%83%9D%EC%8B%9C%EC%9E%A5%20%EB%B6%84%EC%84%9D%20%EC%B2%B4%EA%B3%84%20%EA%B5%AC%EC%B6%95.%20%EC%84%B8%EC%A2%85%20%EA%B5%AD%ED%86%A0%EC%97%B0%EA%B5%AC%EC%9B%90.pdf.pdf
[37] 상업용 토지 가격의 베이지안 추정: 주관적 사전지식과 크리깅 기법의 활용을 중심으로, https://www.kgeography.or.kr/media/11/fixture/data/bbs/publishing/journal/49/05/09.pdf
[38] 제 40 권 제 4 호, https://repository.krei.re.kr/bitstream/2018.oak/22367/1/%EB%86%8D%EC%B4%8C%EA%B2%BD%EC%A0%9C%20%EC%A0%9C40%EA%B6%8C%20%EC%A0%9C4%ED%98%B8.pdf
[39] 서원석, https://kpaj.or.kr/_common/do.php?a=full&bidx=1763&aidx=21769
[40] 머신러닝을 활용한 아파트 매도 호가와 매물량이 실거래가에 미치는 영향 연구, https://www.ki-it.com/xml/38205/38205.pdf
[41] 딥러닝 모형을 활용한 서울 주택가격지수 예측에 관한 연구: 다변량 시계열 자료를 중심으로: 다변량 시계열 자료를 중심으로, https://www.dbpia.co.kr/pdf/pdfView?nodeId=NODE07530536
[42] 제주특별자치도 토지 실거래가격 결정요인에 관한 연구, http://www.reacademy.org/rboard/data/krea2_new/61_12.pdf
[43] 주택시장 경기변동과 주거특성들의 아파트가격에 대한 ..., http://www.reacademy.org/rboard/data/krea2_new/58_16.pdf
[44] 개별공시지가와 주택실거래가의 공간적 불일치에 관한 연구, https://www.kgeography.or.kr/media/11/fixture/data/bbs/publishing/journal/48/06/05.pdf
[45] A Study on the Forecasting Model of Real Estate Market : The Case of Korea, https://www.semanticscholar.org/paper/2bd8ce40d7a3375e65c059fbb73b9f562d3f025c
[46] 부동산 시장 효율성에 관한 연구, https://s-space.snu.ac.kr/handle/10371/215971
[47] 머신러닝 기반의 부동산경매 낙찰가 예측 모델에 관한 연구, https://grad.cuk.edu/CMSPublic/FUload/b05293b5-a897-4ac9-a5f2-0c415a3d20f2.pdf
[48] 서울시 아파트 가격 행태 예측 모델에 관한 연구, https://koreascience.kr/article/JAKO201313660603619.pdf
[49] 주택 자본자산가격결정모형(Capital Asset ..., https://pdfs.semanticscholar.org/f67c/b2d7ba3a7df46f66eb02266e88005ef0fa78.pdf
[50] 서울시 아파트 실거래가와 공시가격의 차이에 불형평성이 존재하는가? 부동산 빅데이터를 활용한 실증연구, https://scholarworks.bwise.kr/cau/handle/2019.sw.cau/63311
[51] 전세특성을 고려한 부동산 가격 급상승기 공동주택 가격추정에 관한 연구-회귀모형과 기계학습 기법 비교를 중심으로, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE11615705
[52] 의사결정트리 (Decision Tree) 를 활용한 글로벌 부동산 가격 분석, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE11082180
[53] [논문]통계 모형을 이용한 서울시 아파트 매매가 예측 분석, https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=DIKO0013976052
[54] 지역 하위시장의 아파트 가격 특성 분석, https://www.e-hfr.org/archive/view_article?pid=hfr-5-2-61
[55] 개별 경제지표에 의한 부동산 경기전망에 관한 연구: 건물유형별 및 토지거래건수를 중심으로: 건물유형별 및 토지거래건수를 중심으로, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE01170718
[56] 공간회귀모형을 이용한 토지시세가격 추정, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE11400094
[57] 비모수 통계검정을 이용한 토지 실거래가 이상치 탐색에 관한 실증분석 연구, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE10818694
[58] [논문]주택가격지수 예측모형에 관한 비교연구, https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO201405981330811
[59] 아파트가격의 지역 간 연관성 분석, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE07547756
[60] 잔차 신호 부호화 및 복호화 장치와 그 방법, https://www.semanticscholar.org/paper/da97af3fb14e7d523da7f7e454297357832121bc
[61] [논문]CNN 모형을 이용한 서울 아파트 가격 예측과 그 요인, https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO202033564390568
[62] 서울시 오피스시장의 지역특성과 가격결정요인에 관한 연구-오피스빌딩 실거래가격을 중심으로, https://s-space.snu.ac.kr/handle/10371/134076
[63] 부동산 감성지수의 주택가격 예측 유용성: 뉴스기사와 방송뉴스 빅데이터 활용 사례, https://kpaj.or.kr/_PR/view/?aidx=30321&bidx=2679
[64] Residuals – Reality and Models Compared, https://www.semanticscholar.org/paper/07e0624bd86fd1b7fd02c9f36fa73a3ad2fa76a6
[65] 상업용부동산 실거래가에 영향을 미치는 요인에 관한 연구: A Study on Factors Affecting the Real Transaction Price of Commercial Real Estate, https://www.dbpia.co.kr/journal/detail?nodeId=T16093619
[66] 멀티-뷰 또는 3 차원 비디오 코딩에서의 인터-뷰 잔차 예측, https://www.semanticscholar.org/paper/1ef1132f14717f870965f083a996c863048287e0
[67] 주택 가격의 지역간 상관 관계 분석 연구: 수도권의 아파트 ..., https://cerik.re.kr/uploads/report/%EC%A3%BC%ED%83%9D%20%EA%B0%80%EA%B2%A9%EC%9D%98%20%EC%A7%80%EC%97%AD%EA%B0%84%20%EC%83%81%EA%B4%80%20%EA%B4%80%EA%B3%84%20%EB%B6%84%EC%84%9D%20%EC%97%B0%EA%B5%AC.pdf
[68] 우리나라 주요 지역 주택가격의 요인분석: 공통요인의 식별을 중심으로, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE02372222
[69] 부동산 실거래가를 보고 부동산 적정가격 산정하는 방법, https://blog.naver.com/eunj704/222268385367?viewType=pc
[70] Risk and Return in the Ulsan Housing Market, https://www.semanticscholar.org/paper/f187b4e2e400ef3a6a341ad398e53f9f57d91a7f
[71] 경관 차폐거리가 주택가격에 미치는 영향에 관한 연구, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE10895864
[72] Risk and return in residential spatial markets: An empiric and theoretic model, https://www.semanticscholar.org/paper/81cb71f24032cf7b7eb4c83d5b8c4e9ae24ac182
[73] 트리 기반 앙상블 방법을 활용한 자동 평가 모형 개발 및 평가, https://www.kdiss.org/journal/download_pdf.php?doi=10.7465/jkdi.2020.31.2.375
[74] 단독주택 실거래가격 토지･건물 배분비율 분석, http://journal.cartography.or.kr/articles/pdf/RvmO/kca-2020-020-02-5.pdf
[75] 아파트 매매가격과 부동산 온라인 뉴스의 교차상관관계와 ..., https://kpaj.or.kr/_PR/view/?aidx=18557&bidx=1622
[76] 토지 실거래가격 결정요인에 관한 연구, https://www.semanticscholar.org/paper/1f8aafad9a110d4bcdc07c17e8849865736df3fc
[77] 서울특별시 아파트의 순환변동에 관한 비교 분석* - HP filter ..., http://www.kreaa.or.kr/data/vol24-1/24_01_02.pdf
[78] 서울시 아파트 실거래가의 변화패턴 분석, https://www.semanticscholar.org/paper/b86fefc44042850a9ec2c87d84696b9b50d21d17
[79] 기본재산 공제제도 개편방안 연구, https://www.semanticscholar.org/paper/43ff0d0366ca051e6348d420007224dfd3b09bf6
[80] 부동산 정책의 효과에 관한 연구, https://s-space.snu.ac.kr/bitstream/10371/130387/1/000000009021.pdf
[81] 공간통계기법을 이용한 서울시 아파트 실거래가 변인의 시공간적 이질성 분석, https://www.semanticscholar.org/paper/7a6e553dacac0551c1ba02808b2d001af2b5b3b8
[82] 아파트 가격에 대한 APC(age-period-cohort) 효과 분석, https://kpa1959.or.kr/file/F110.pdf
[83] 주택정책을 위한 헤도닉 모형 평가에 관한 연구, https://www.semanticscholar.org/paper/e3878c6ee5bcb7fe069b3fb5c164f5ac59269b23
[84] The Analysis on Estimation and Determinants of Regional Housing Risk Premium using Fixed Effect Model, https://www.semanticscholar.org/paper/49904ba0d1890b6d8299ca9760efcbba02c2b307
[85] [논문]수도권 주택가격 결정요인 변화 연구, https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO201308438433204
[86] 주식, 채권, 부동산시장의 변동성 전이에 관한 연구, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE07426696
[87] 자산가격 결정모형을 이용한 우리나라 주택가격 분석, https://www.semanticscholar.org/paper/d7c0d3d9eee3c76f9d8466420abce064d7b9a4bd
[88] Why residuals can be useful in real estate valuation, https://www.semanticscholar.org/paper/e555f7fbffdb01561e36fd891f03efceb41b7770
[89] 실거래가 신고후 지가변동률에 관한 연구, https://www.semanticscholar.org/paper/41635bdc7a914567efccb4c14114bc5ce94bc25e
[90] 친환경적 기피시설이 아파트 가격에 미치는 영향, https://koreashe.org/wp-content/uploads/2025/10/%ED%8F%AC%EC%8A%A4%ED%84%B0_5_%ED%99%98%EA%B2%BD%EC%A0%95%EC%B1%85_%ED%95%9C%EC%84%B1%EC%9A%B0.pdf
[91] 국내외 주택가격모형의 특성에 관한 연구: 메타회귀분석을 ..., https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001815540
[92] Spatial Econometric Analysis of Regional Housing Markets, https://www.semanticscholar.org/paper/298372b1970f6a1f242d492ca76094586e7bfdce
[93] The residual method of valuation, http://link.springer.com/10.1007/978-1-137-01728-4_7
[94] 아파트 실거래가와 거래량이 시세에 미치는 영향, https://www.semanticscholar.org/paper/3bcf17f55e040beccb99cdba807cc900eaef1e1e
[95] A Study on the Theoretical and Empirical Analysis of Housing Pricing - Focused on the Seoul Apartment Market-, https://www.semanticscholar.org/paper/155bb8f2b80ed663dfda397e234d33ec261c121c
[96] 소비자의 주택가격전망이 아파트 거래량에 미치는 영향 연구, https://www.ejhuf.org/archive/view_article?pid=jhuf-1-2-5
[97] 규제정책이 서울시 지가변화에 미치는 영향력 분석, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE02000710
[98] 논문 : 부동산 실거래가격 확보방안에 관한 연구, https://www.semanticscholar.org/paper/83fb0c9c77401cf6af679fbc317eb6034a613e83
[99] 서울시 주택가격, 인구, 지역내총생산의 인과분석, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE07260656
[100] 물류부동산 거래가격에 영향을 미치는 요인에 대한 연구, https://s-space.snu.ac.kr/bitstream/10371/183180/1/000000170891.pdf
[101] 구조 변화를 감안한 우리나라 주택시장 분석, https://www.semanticscholar.org/paper/3436b143a1f60ce0f451091bef9f1aeb80ce2fba
[102] 주택가격 변동의 지역간 파급효과 분석, https://www.e-hfr.org/archive/view_article?pid=hfr-8-2-71
[103] 패널 자료를 이용한 지역별 주택매매가격 분석, https://www.semanticscholar.org/paper/7b2aaddf915b06e828fa24ae5dc9e8278c4e991b
[104] 논문(論文) : 공간패널모형을 활용한 우리나라 주택가격의 동학적 특성분석, https://www.semanticscholar.org/paper/f513fcf92bbf617a868927d1469ac35a9d68872e
[105] GWR 접근법을 활용한 부동산 감정평가 모형 연구: 서울시 아파트를 사례로, https://www.semanticscholar.org/paper/a4eeb54d6e8e830a75615b0d3922dce8c65496ac
[106] 직거래 정보가 아파트 매매가격 및 거래량의 변동에 미치는 영향, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE11468494
[107] 주택 거래 간 시공간 의존성을 고려한 헤도닉 가격 추정, https://www.semanticscholar.org/paper/d73dbe1e5ffe298de451d0d0fcc447635629a10b
[108] Residual Statistics, https://www.taylorfrancis.com/books/9781003213758/chapters/10.4324/9781003213758-3
[109] 위험프리미엄이 임대수익률에 미친 영향, https://s-space.snu.ac.kr/handle/10371/151706
[110] 시간적 상관도를 활용한 변환 영역 잔차 신호 Wyner-Ziv 부호화, https://www.semanticscholar.org/paper/c70184d0b7275e7b7a9bbd5f54a961b411a62235
[111] 통화정책과 부동산정책이 주택시장에 미치는 영향 연구: 지방광역시 고가아파트 중심으로: Research on the impact of monetary policy and real estate policy on the …, https://www.dbpia.co.kr/journal/detail?nodeId=T16857243
[112] 공간계량모형을 활용한 아파트가격 영향요인 분석 연구, https://journal.khousing.or.kr/articles/pdf/NGwa/khousing-2020-031-01-8.pdf
[113] 연구논문(硏究論文) : 지리가중회귀모델을 이용한 주택가격 결정요인의 지역별 특성에 관한 연구 -부산광역시를 중심으로-, https://www.semanticscholar.org/paper/22b6b2d04d593a12622acad7a858815fc48eb5be
[114] "같은 구인데 집값 30배 차이?" 서울 부동산 시장 양극화 심화, https://v.daum.net/v/fT70YJ0Hln
[115] 서울지역 아파트의 경매낙찰가율에 영향을 미치는 요인에 관한 연구 - 시점수정 낙찰가율과 법원경매 낙찰가율에 미치는 영향요인에 대한 비교연구 -, https://www.semanticscholar.org/paper/03c02b4cd29f8e933449e2b9498f1c9ca0929bb8
[116] 부동산 비기초가격과 부동산 신문담론의 관계에 대한 시계열 분석, https://s-space.snu.ac.kr/bitstream/10371/197489/1/000000178523.pdf
[117] 지리가중회귀모형을 활용한 서울시 주택하위시장 도출에, https://www.kpaj.or.kr/xml/22367/22367.pdf
[118] An Empirical Study on the Resale Regulation and Housing Price in Korea - Focused on the 11.3 Real Estate Measures -, https://www.semanticscholar.org/paper/c36be7e0eac382d2f7137b7a89cd9e8d2900cb1d
[119] A Study on the Relation between Price Change and Trading Volume intra Zoning of Real Estate Market: Focused on the Daegu Region, https://www.semanticscholar.org/paper/18a7a9097fd0e14d6e6b58e6d97b65e6fe212903
[120] 잔차 오차 최소에 의한 HEMT의 외인성 파라미터 추출, https://www.semanticscholar.org/paper/d78b06839b5fa994c231bf93444ad4f056582a0d
[121] CR-DPCM을 이용한 HEVC 무손실 인트라 예측 방법, https://www.semanticscholar.org/paper/8b5a77c5f93d8f7783cad9a25b88efc7ca5aa04f
[122] Housing Price Estimation using Spatial Econometrics Models : Focused on the Real Transaction Housing Price in the Busan, https://www.semanticscholar.org/paper/b63e11a930bda6346adac374d189af5807770f8d
[123] 수도권 불안정주택시장에서 주택가격 변동에 영향을 미치는 요인 분석, https://www.semanticscholar.org/paper/b23b7aa0a006be0214c2b95efcc0d3334fcfb79b
[124] 아파트 실거래가 지수를 이용한 부동산 시장 평가, https://www.semanticscholar.org/paper/e4f463a3b51c34a6699c6b3c05d30be8fe1e820f
[125] 공동주택 실거래가격의 지역별 상관성 분석에 관한 기초연구, https://www.semanticscholar.org/paper/729d9e4d9570f093706c39e050e80c4339cc7a7f
[126] 부동산가격에 있어 장기균형과 충격반응분석: 강남구, 성남시, 안양시, 용인시를 중심으로: 강남구, 성남시, 안양시, 용인시를 중심으로, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE01085751
[127] 특성가격함수를 이용한 주택가격지수 개발에 관한 연구 -시간변동계수모형에 의한 연쇄지수, https://www.semanticscholar.org/paper/65c9218e3a9f3a753c1043bbc3cc204bfe9e0244
[128] 개별 주택가격 데이터를 이용한 주택가격 변동률 분포의 특성 ..., https://www.ejhuf.org/archive/view_article?pid=jhuf-7-1-27
[129] 아파트 매매가격지수 변동률에 의한 전국 주택시장 유형화 및 유형별 가격변동 영향요인 분석, https://www.semanticscholar.org/paper/501c2fadf21eed9b90d90d4f7a3f3e44b40c1fab
[130] 부동산정책에 따른 투자심리와 주택가격 변화에 관한 연구, https://s-space.snu.ac.kr/handle/10371/193038
[131] 공간적탐색기법을 이용한 부산 주택시장 다이나믹스 분석, https://www.semanticscholar.org/paper/464e3634488a910cb9b94773b0b3080e2b54c438
[132] 토지특성 요인에 입각한 개별공시지가의 실거래가 반영률 차이분석, https://www.semanticscholar.org/paper/075e52ef8cd1a99c36223b2afc161a028b98d1b4
[133] 제 2차 잔차 변환을 이용한 HEVC 무손실 인트라 코딩, https://www.semanticscholar.org/paper/e160d2eca630731c8f834941bbd7096a015bb0ec
[134] 인루프 필터링을 적용한 예측 방법을 이용한 영상 부호화/복호화 방법 및 장치, https://www.semanticscholar.org/paper/4a987389051d2f1edba4e66bf4892a10f68504de
[135] 주식시장 지수와 부동산시장 지수의 시계열 특성비교와 관계에 관한 실증적 연구, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE01671916
[136] 부동산 수요 조절 정책이 서울시 아파트 매매가격에 미치는 효과: 2019 년과 2020 년 주택시장 안정화 방안 사례, http://kreaa.or.kr/data/vol28-3/28_03_04.pdf
[137] 코로나 19와 부동산 감정평가, https://www.semanticscholar.org/paper/f69f693b8ab926d3fec8dafbb8a00a2c85284975
[138] 유동성의 변동이 주택가격 변동성에 미치는 영향, https://www.semanticscholar.org/paper/5563eac55c921389b9f6736b22970b1fcbb74ffc
[139] 부동산 PF사업 사업단계별 리스크 요인 영향관계 분석, https://www.semanticscholar.org/paper/7ebacaf9f10bb23e241cf729d85c52d67e5e2e44
[140] 고도차에 따른 GBAS 대류층 잔차 불확실성 모델 분석, https://www.semanticscholar.org/paper/8cf26f235e1b442fc1cbff4db10395d216746263
[141] 주거환경의 지역 간 불균형에 따른 주택가격 영향분석, https://gdi.re.kr/datafile/dgpaper_down/paper_12_2_7.pdf
[142] 住宅建設과 住宅賣買價格 및 여타 住宅關聯 變數들의 因果關係分析, https://www.semanticscholar.org/paper/88cd1a1075d22d26b3a03263c2db340d9b3c3308
[143] 도시지역의 녹지공간이 공동주택가격에 미치는 영향-서울시 근린공원을 중심으로, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE09872034
[144] 실질주택매매가격 변동성에 영향을 주는 요인 고찰, https://www.semanticscholar.org/paper/5b6d9f235afcfa479fd2c1d8091c5226f50c5668
[145] 부동산 시가표준액의 합리적 결정방안, https://www.kilf.re.kr/cmm/fms/PDF.do;jsessionid=943D88DC2D7E52CCE9FA22C151901DC3?atchFileId=FILE_000000000004990&fileSn=0
[146] 은퇴계층의 부동산 자산 배분 결정요인 분석, https://s-space.snu.ac.kr/handle/10371/129831
[147] Determinants of Price Gap between Asking Price and Real Transaction Price of Apartment in Seoul Metropolitan Area, https://www.semanticscholar.org/paper/9281b1f143ed93c12d3b049f72008c154fff96b0
[148] 지역단위 사회서비스 기초통계 개발 및 관리방안 연구, https://www.semanticscholar.org/paper/85f60422e7fee3c2f034c4f642a87b84fadc8a2b
[149] 주택 매매 및 전세시장의 변화와 은행의 건전성, https://www.semanticscholar.org/paper/8405e6843831a02c1625f17bc98cef0012ecbb1e
[150] 부동산규제가 법인의 주택시장 참여에 미친 영향, https://s-space.snu.ac.kr/handle/10371/176278
[151] 부동산 거래정보(콘텐츠)에 관한 법적규제의 쟁점, https://www.semanticscholar.org/paper/ec78ef1ad3e24e210b1e4e5c9b24cc3089bde0a7
[152] 주택 정책의 지역별 시장 파급효과 분석을 위한 시뮬레이션 모델 개발, https://www.semanticscholar.org/paper/7ae586e930f336f7ada345549409769a4e984b72
[153] 지역 차원의 소득과 자산 간 결합분포: 수도권과 비수도권의 비교, https://www.semanticscholar.org/paper/c4bcf5f95550a9ffd1a0172fe3908579db6016d7
[154] 공간사용 규제가 택지가격에 미치는 영향에 대한 공간가중 ..., http://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002390312
[155] 투자자별 부동산 선호요인이 재투자 의사에 미치는 영향 분석, https://www.semanticscholar.org/paper/a58fa6532e41ad07851c2d427b8dc308c6796fec
실거래 예측가와 환경 리스크를 기반으로 AI가 '괜찮은 옵션'을 제공하는 서비스 모델링을 위해, 타겟 변수, 리스크 변수, 통제 변수의 선정 조건 및 잔차 추출 시 지역 단위 설정에 대한 보고서를 제공합니다.

### 타겟 변수, 리스크 변수, 통제 변인의 선정 조건

#### 타겟 변수 (Target Variable)
타겟 변수는 예측 모델에서 목표로 하는 값으로, 실거래가 예측 모델에서는 주로 주택의 거래 금액과 관련된 변수들을 활용합니다.

*   **정의 및 조건**:
    *   **실거래 가격**: 아파트의 실거래가를 타겟 변수로 사용하는 연구가 많습니다. 주택 가격 예측 모형 연구에서 서울시 주택 매매 실거래가를 중심으로 분석을 진행하기도 합니다. 부동산 전월세 매물 예측 모델 개발을 위해 진주시 14개 동의 아파트 및 오피스텔 실거래가 데이터가 사용된 사례도 있습니다. 특히 아파트 단지 단위에서 실거래가를 분석하여 머신러닝 기법의 예측력을 검증하기도 했습니다.
    *   **단위면적당 실거래가**: '단위면적당 실거래가'를 Target 변수로 설정하고 독립변수와의 상관계수를 도출하는 연구도 있습니다. 아파트 실거래가에 영향을 미치는 변인들의 시공간적 이질성을 탐색하는 데 아파트 실거래가가 활용되기도 합니다. 주택 가격 변동률 분포의 특성 분석을 위해 개별 주택가격에 대한 패널데이터를 구축하여 가격지수가 아닌 변화율의 분포를 통해 주택 시장의 변동성을 분석하기도 합니다.
    *   **거래금액 (단위: 만원)**: 서울시 아파트 실거래가 매매 데이터를 기반으로 아파트 가격을 예측하는 대회에서는 각 시점에서의 거래금액(단위: 만원)을 예측하는 것을 목표로 설정하기도 했습니다.

#### 리스크 변수 (Risk Variable)
리스크 변수는 예측 결과의 불확실성이나 위험도를 나타내는 요소로 사용됩니다.

*   **정의 및 조건**:
    *   **부동산 특성 요인의 영향**: 특정 요인들이 실거래가 예측 잔차에 미치는 영향을 분석하는 데 활용됩니다. 부동산 특성(예: 비정형성)이 모델 잔차에 미치는 영향을 검증하여 부동산 시장 분석을 지원할 수 있습니다.
    *   **시장 리스크**: 주택 가격 변동의 시장 리스크를 반영하여 조정된 민감도를 나타내는 변수를 사용할 수 있습니다. 전국 단위의 아파트 가격 지수를 시장 포트폴리오의 대리변수로 활용할 수 있습니다.
    *   **부동산 프로젝트 파이낸싱(PF) 사업 리스크**: 부동산 PF 사업의 안정적 추진을 위해 사업단계별 리스크 요인(사업 안전성, 수익 계획, 사업 계획, 시장 환경, 사업비 증가, 자금 조달, 인허가, 사업 지연, 현금 흐름, 공기 연장, 공사 중단 리스크 등)을 도출하고 이들 요인 간의 영향 관계를 분석할 수 있습니다. 이 중 사업비 증가, 현금 흐름, 사업 안전성, 자금 조달, 인허가 리스크가 PF 사업 안정성에 큰 영향을 미치는 것으로 나타났습니다.
    *   **주택 시장 참여 법인의 거래량**: 법인이 매수한 부동산 거래량을 종속변수로 하여 주택 시장 및 거시경제 변수(서울시 아파트 가격지수, 시군구 주민등록세대수 증가율, 이자율, 코스피지수 등)를 독립변수로 설정하고 리스크 요인을 분석할 수도 있습니다.

#### 통제 변수 (Control Variable)
통제 변수는 예측 모델의 정확도를 높이기 위해, 타겟 변수에 영향을 미칠 수 있는 외부 요인들을 제어하는 데 사용됩니다.

*   **정의 및 조건**:
    *   **아파트 정보 및 경제지표**: 미래 아파트 매매 실거래가격을 예측하는 모델에서는 다양한 아파트 정보와 경제지표 등 가능한 많은 변수를 수집하여 다중 공선성 문제를 해결하며 사용합니다.
    *   **지역적 특성**: 부동산은 공간적 의존성과 이질성 문제가 발생할 수 있어, 공간적 자기상관성을 고려한 분석 방법이 요구됩니다. 부산시의 공동주택을 대상으로 지역별 주택 가격을 형성하는 공간회귀모형을 구축하여 지역별 가격 결정 요인의 다양성을 분석한 사례가 있습니다.
    *   **주택 특성**: 주택 가격에 영향을 미치는 다양한 특성을 설명하기 위해 헤도닉 가격 모형이 활용됩니다. 주택 가격 추정에 있어 전통적인 OLS 모형과 공간계량모형의 적합도를 평가하여 우수한 모형을 선정하기도 합니다.
    *   **거시경제 변수**: 주택 가격에 큰 영향을 미치는 거시경제 변수로는 CD금리(91일물), 총통화평잔증가율(M2), 코스피지수, 주거용지가 변동률 등을 선정할 수 있습니다. 주택가격지수 예측 모형에서는 외부 충격 요인(개입 효과)이 주택가격지수에 미치는 영향을 파악하는 것이 중요합니다. 또한, 부동산 안정화 정책이 시장 가격 안정에 도움이 되지만, 부동산 소비 심리에 영향을 주는 요인이 될 수 있음을 인지하는 것이 정책의 적시성과 효과에 유리합니다.
    *   **전월세 특성**: 전세 특성을 고려한 예측 모형은 전세 특성을 고려하지 않은 경우보다 예측 정확도가 상승하여, 전세 특성이 가격 예측에 중요한 요인으로 작용함이 입증되었습니다.
    *   **실거래가 자료**: 상업용 부동산 실거래가 결정 시 영향을 미치는 요인(생활권, 금액, 변수, 특성별)을 구분하여 분석하기도 합니다.
    *   **정책 변수**: 부동산 수요 조절 정책이 주택 가격에 미치는 영향을 분석할 때, 금융 및 세금 규제와 같은 정책 변수를 고려할 수 있습니다.

### 잔차 추출 시 지역 단위 설정

잔차를 추출할 때 지역 단위는 분석의 목적과 활용 가능한 데이터의 세분화 정도에 따라 달라질 수 있습니다.

*   **행정 구역 단위**:
    *   **동 단위**: 서울시 아파트 실거래가 변화 패턴을 분석하기 위해 아파트별 및 동별 평균 실거래가 자료를 활용하여 GIS 데이터로 구축한 사례가 있습니다.
    *   **구 단위**: 서울시 아파트 실거래가의 공간적 불균형을 분석할 때 구 단위의 자료를 활용하기도 합니다. 특정 연구에서는 서울의 강남구, 서초구 등 8개 구를 투기 지역으로 지정하여 분석하기도 했습니다. 서울시 오피스 시장의 실거래 가격을 바탕으로 도심 지역과 강남 지역의 특성을 분석하는 연구도 있습니다. 또한 서울시의 25개 자치구를 대상으로 주택가격, 인구, 지역내총생산의 인과성을 분석하기도 했습니다.
    *   **시·도 단위**: 우리나라 16개 시·도 지역의 주택 가격 변화를 공간 패널 모형을 활용하여 분석한 연구가 있습니다. 공동주택 실거래 가격의 지역별 상관성 분석에서는 서울과 경기 지역의 아파트 매매 가격이 가장 높게 나타났으며, 특히 서울의 동남권 및 도시 지역이 가장 높은 것으로 나타났습니다.
*   **미시적 단위**:
    *   **개별 아파트 단지 단위**: 아파트 실거래가를 이용하여 단기적이고 국지적인 시장 분석이 용이하다는 연구 결과가 있습니다. 미시적 단위의 시공간 빅데이터를 활용하여 실거래가와 공시 가격 차이의 공간적 분포를 분석하기도 합니다.
    *   **하위 시장**: 서울시 주택 시장은 여러 이질적인 주택 하위 시장으로 구성되어 있으며, 주택 특성의 가격 효과가 국지적으로 다름을 확인할 수 있습니다. 이를 통해 미시적인 주택 하위 시장 분석 및 부동산 정책 수립에 활용할 수 있습니다.
*   **유의 사항**:
    *   **데이터의 가용성**: 국토교통부에서 제공하는 부동산 실거래가 공개 시스템을 통해 주택, 오피스텔 등 매매 실거래 정보가 공개되고 있습니다.
    *   **지역별 이질성**: 아파트 실거래가와 같은 공간 데이터에 영향을 미치는 외부 환경도 지역별 이질성이 크기 때문에 공간적 편차가 나타납니다. 따라서 지역별 상이한 특성과 환경을 고려하는 것이 중요합니다.
    *   **잔차의 공간적 상관관계**: 잔차의 상관관계를 측정하여 분석할 수 있으며, 공간적 자기상관 관계를 반영한 모델이 전통적인 모델보다 설명력이 높은 경우가 있습니다.

출처: 
[1] Hypothesis testing in hedonic price estimation – On the selection of independent variables, https://link.springer.com/article/10.1007/s001689900010
[2] Hedonic Regression Analysis in Real Estate Markets: A Primer, https://www.semanticscholar.org/paper/711bfe50493450f567496c130cc3e691409fb071
[3] Econometric Identification of the Impact of Real Estate Characteristics Based on Predictive and Studentized Residuals, https://www.semanticscholar.org/paper/54e9002b3fd9d8d419fc979ff65c281e7a348244
[4] 딥러닝 기법과 잔차 크리깅을 이용한 지가 예측, https://www.kdiss.org/journal/download_pdf.php?doi=10.7465/jkdi.2021.32.3.475
[5] (PDF) Empirical Analysis of XGBoost-based Real Estate ..., https://www.researchgate.net/publication/394553972_Empirical_Analysis_of_XGBoost-based_Real_Estate_Automated_Valuation_Model
[6] 딥러닝과 머신러닝을 이용한 아파트 실거래가 예측, https://ktsde.kips.or.kr/journals/ktsde/digital-library/manuscript/file/38415/01-22M-05-009-%EC%98%A4%ED%95%98%EC%98%81_59-76.pdf
[7] 기계학습을 이용한 부동산 전월세 매물 예측 연구: 경상남도 진주 지역을 사례로, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE11652057
[8] 기계 학습을 이용한 공동주택 가격 추정: 서울 강남구를 사례로*, http://www.kreaa.or.kr/data/vol24-1/24_01_05.pdf
[9] Upstage AI LAB 대회 회고 : [ML] House Price Prediction, https://refine-thinking.tistory.com/58
[10] 국토정책 Brief, https://www.krihs.re.kr/boardDownload.es?bid=0008&list_no=397975&seq=3
[11] 서울시 아파트가격의 동학적 특성에 관한 연구, http://kreaa.or.kr/data/vol19-4/08--%EB%B0%95%ED%97%8C%EC%88%98.pdf
[12] 51-2대지01Shawn Shen.indd, https://www.kgeography.or.kr/media/11/fixture/data/bbs/publishing/journal/51/02/51-2-all.pdf
[13] 인공지능(AI)의 MLP모델을 이용한 주택 가격 정보 예측 기법, https://koreascience.kr/article/JAKO202521154004490.page;
[14] 빅데이터를 활용한 주택시장 분석 및 예측 모형 개발 ..., https://www.codil.or.kr/filebank/original/RK/OTKCRK220247/OTKCRK220247.pdf?stream=T
[15] Modelling real property transactions: an overview, https://www.semanticscholar.org/paper/daf323fc0202fb8ca2c36c3331232baee4ea7089
[16] 심리변수에 따른 아파트 매매가격지수 예측력 비교 분석, https://www.kpaj.or.kr/xml/36621/36621.pdf
[17] 비영리 - S-Space - 서울대학교, https://s-space.snu.ac.kr/bitstream/10371/120377/1/000000053288.pdf
[18] 뉴스 빅데이터를 이용한 전세 가격 예측, http://www.reacademy.org/rboard/data/krea2_new/69_4.pdf
[19] 공공데이터 분석을 통한 변동성 요인 분석과 예측 모델 생성에 대한 연구, https://www.kais99.org/jkais/journal/Vol24No12/vol24no12p086.pdf
[20] 서울시의 지역주거환경특성이 주택가격에 미치는 영향 ..., http://www.kreaa.or.kr/data/vol19-4/15--%EC%9C%A4%ED%9A%A8%EB%AC%B5.pdf
[21] 주택가격의 공간적 영향력 검증 - - 서울과 부산의 아파트 ..., https://www.codil.or.kr/filebank/original/RK/OTKARK950359//OTKARK950359.pdf
[22] 머신러닝과 패널고정효과를 활용한 아파트 실거래가 예측 비교: Predicting Actual Transaction apartment Price Using Machine Learning Methods and Fixed Effects …, https://www.dbpia.co.kr/journal/detail?nodeId=T15741884
[23] 머신 러닝 방법과 시계열 분석 모형을 이용한 부동산 가격 ..., https://kahps.org/data/hshd/pdf_75_5
[24] 딥러닝(Deep Learning)을 이용한 주택가격 예측모형 연구 ..., http://sam.riss.kr/findThesisAnalysis.do?controlNo=000014659291&docType=T
[25] 머신러닝을 활용한 부동산 실거래가 요인 분석, https://ksc21.net/plugin/file_down.php?sys_filename=156_h_sfile.pdf&down_filename=14_%EC%A7%80%EC%A0%8139%EA%B6%8C3%ED%98%B8_%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D%EC%9D%84_%ED%99%9C%EC%9A%A9%ED%95%9C(199-210)_%EB%B0%95%EC%84%9C%ED%98%84.%EA%B9%80%EB%8F%84%ED%98%95.pdf&down_dir=hak
[26] 단독주택가격 추정을 위한 기계학습 모형의 응용, https://www.kgeography.or.kr/media/11/fixture/data/bbs/publishing/journal/51/02/03.pdf
[27] XGBoost 기반 부동산 자동가치산정모형 (Automated ..., https://www.ejrea.org/archive/view_article?pid=jrea-11-2-21
[28] 라쏘 방법을 이용한 수도권 주택 매매가 및 전세가 예측 변인 ..., https://econeng.sogang.ac.kr/Download?pathStr=NTQjIzU0IyM1NyMjNTEjIzEyNCMjMTA0IyMxMTYjIzk3IyM4MCMjMTAxIyMxMDgjIzEwNSMjMTAyIyMzNSMjMzMjIzM1IyM0OSMjMTI0IyMxMjAjIzEwMSMjMTAwIyMxMTAjIzEwNSMjMzUjIzMzIyMzNSMjNTQjIzU3IyM1MiMjNTYjIzU2IyM1NiMjMTI0IyMxMDAjIzEwNSMjMTA3IyMxMTI=&fileName=JOME_V51_3_1.pdf&gubun=board
[29] 구조방정식을 이용한 서울시 권역별 주상복합아파트 실거래가 영향요인 및 인과구조 분석, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE01998998
[30] 머신러닝을 활용한 아파트 매도 호가와 매물량이 실거래가에 ..., https://ki-it.com/xml/38205/38205.pdf
[31] 인공지능을 이용한 주택가격 변동성 예측 모델 연구: 전통통계모형과 인공지능학습모형 융합을 중심으로: Design of Real Estate Prediction Model based on Bigdata with …, https://www.dbpia.co.kr/journal/detail?nodeId=T16674817
[32] 부동산 정책에 따른 서울시 아파트 가격지수 변화방향에 대한 ..., https://koreascience.kr/article/CFKO201125752340480.pdf
[33] 공간통계기법을 이용한 서울시 아파트 실거래가 변인의 ..., https://koreascience.kr/article/JAKO201610235352362.pdf
[34] 머신러닝과 패널고정효과를 활용한 아파트 실거래가 예측, https://kahps.org/data/hshd/pdf_91_2
[35] Real Estate Price Modeling and Empirical Analysis, https://link.springer.com/article/10.1007/BF03405736
[36] 주택구매소비자의 의사결정구조를 반영한 ..., https://kremap.krihs.re.kr/File/%EB%B0%95%EC%B2%9C%EA%B7%9C,%20%EA%B9%80%EC%A7%80%ED%98%9C,%20%ED%99%A9%EA%B4%80%EC%84%9D,%20%EC%98%A4%EB%AF%BC%EC%A4%80,%20%EC%B5%9C%EC%A7%84,%20%EA%B6%8C%EA%B1%B4%EC%9A%B0,%20%EC%98%A4%EC%95%84%EC%97%B0,%20%ED%99%A9%EC%9D%B8%EC%98%81.%202020.%20%EC%A3%BC%ED%83%9D%EA%B5%AC%EB%A7%A4%EC%86%8C%EB%B9%84%EC%9E%90%EC%9D%98%20%EC%9D%98%EC%82%AC%EA%B2%B0%EC%A0%95%EA%B5%AC%EC%A1%B0%EB%A5%BC%20%EB%B0%98%EC%98%81%ED%95%9C%20%EC%A3%BC%ED%83%9D%EC%8B%9C%EC%9E%A5%20%EB%B6%84%EC%84%9D%20%EC%B2%B4%EA%B3%84%20%EA%B5%AC%EC%B6%95.%20%EC%84%B8%EC%A2%85%20%EA%B5%AD%ED%86%A0%EC%97%B0%EA%B5%AC%EC%9B%90.pdf.pdf
[37] 상업용 토지 가격의 베이지안 추정: 주관적 사전지식과 크리깅 기법의 활용을 중심으로, https://www.kgeography.or.kr/media/11/fixture/data/bbs/publishing/journal/49/05/09.pdf
[38] 제 40 권 제 4 호, https://repository.krei.re.kr/bitstream/2018.oak/22367/1/%EB%86%8D%EC%B4%8C%EA%B2%BD%EC%A0%9C%20%EC%A0%9C40%EA%B6%8C%20%EC%A0%9C4%ED%98%B8.pdf
[39] 서원석, https://kpaj.or.kr/_common/do.php?a=full&bidx=1763&aidx=21769
[40] 머신러닝을 활용한 아파트 매도 호가와 매물량이 실거래가에 미치는 영향 연구, https://www.ki-it.com/xml/38205/38205.pdf
[41] 딥러닝 모형을 활용한 서울 주택가격지수 예측에 관한 연구: 다변량 시계열 자료를 중심으로: 다변량 시계열 자료를 중심으로, https://www.dbpia.co.kr/pdf/pdfView?nodeId=NODE07530536
[42] 제주특별자치도 토지 실거래가격 결정요인에 관한 연구, http://www.reacademy.org/rboard/data/krea2_new/61_12.pdf
[43] 주택시장 경기변동과 주거특성들의 아파트가격에 대한 ..., http://www.reacademy.org/rboard/data/krea2_new/58_16.pdf
[44] 개별공시지가와 주택실거래가의 공간적 불일치에 관한 연구, https://www.kgeography.or.kr/media/11/fixture/data/bbs/publishing/journal/48/06/05.pdf
[45] A Study on the Forecasting Model of Real Estate Market : The Case of Korea, https://www.semanticscholar.org/paper/2bd8ce40d7a3375e65c059fbb73b9f562d3f025c
[46] 부동산 시장 효율성에 관한 연구, https://s-space.snu.ac.kr/handle/10371/215971
[47] 머신러닝 기반의 부동산경매 낙찰가 예측 모델에 관한 연구, https://grad.cuk.edu/CMSPublic/FUload/b05293b5-a897-4ac9-a5f2-0c415a3d20f2.pdf
[48] 서울시 아파트 가격 행태 예측 모델에 관한 연구, https://koreascience.kr/article/JAKO201313660603619.pdf
[49] 주택 자본자산가격결정모형(Capital Asset ..., https://pdfs.semanticscholar.org/f67c/b2d7ba3a7df46f66eb02266e88005ef0fa78.pdf
[50] 서울시 아파트 실거래가와 공시가격의 차이에 불형평성이 존재하는가? 부동산 빅데이터를 활용한 실증연구, https://scholarworks.bwise.kr/cau/handle/2019.sw.cau/63311
[51] 전세특성을 고려한 부동산 가격 급상승기 공동주택 가격추정에 관한 연구-회귀모형과 기계학습 기법 비교를 중심으로, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE11615705
[52] 의사결정트리 (Decision Tree) 를 활용한 글로벌 부동산 가격 분석, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE11082180
[53] [논문]통계 모형을 이용한 서울시 아파트 매매가 예측 분석, https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=DIKO0013976052
[54] 지역 하위시장의 아파트 가격 특성 분석, https://www.e-hfr.org/archive/view_article?pid=hfr-5-2-61
[55] 개별 경제지표에 의한 부동산 경기전망에 관한 연구: 건물유형별 및 토지거래건수를 중심으로: 건물유형별 및 토지거래건수를 중심으로, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE01170718
[56] 공간회귀모형을 이용한 토지시세가격 추정, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE11400094
[57] 비모수 통계검정을 이용한 토지 실거래가 이상치 탐색에 관한 실증분석 연구, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE10818694
[58] [논문]주택가격지수 예측모형에 관한 비교연구, https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO201405981330811
[59] 아파트가격의 지역 간 연관성 분석, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE07547756
[60] 잔차 신호 부호화 및 복호화 장치와 그 방법, https://www.semanticscholar.org/paper/da97af3fb14e7d523da7f7e454297357832121bc
[61] [논문]CNN 모형을 이용한 서울 아파트 가격 예측과 그 요인, https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO202033564390568
[62] 서울시 오피스시장의 지역특성과 가격결정요인에 관한 연구-오피스빌딩 실거래가격을 중심으로, https://s-space.snu.ac.kr/handle/10371/134076
[63] 부동산 감성지수의 주택가격 예측 유용성: 뉴스기사와 방송뉴스 빅데이터 활용 사례, https://kpaj.or.kr/_PR/view/?aidx=30321&bidx=2679
[64] Residuals – Reality and Models Compared, https://www.semanticscholar.org/paper/07e0624bd86fd1b7fd02c9f36fa73a3ad2fa76a6
[65] 상업용부동산 실거래가에 영향을 미치는 요인에 관한 연구: A Study on Factors Affecting the Real Transaction Price of Commercial Real Estate, https://www.dbpia.co.kr/journal/detail?nodeId=T16093619
[66] 멀티-뷰 또는 3 차원 비디오 코딩에서의 인터-뷰 잔차 예측, https://www.semanticscholar.org/paper/1ef1132f14717f870965f083a996c863048287e0
[67] 주택 가격의 지역간 상관 관계 분석 연구: 수도권의 아파트 ..., https://cerik.re.kr/uploads/report/%EC%A3%BC%ED%83%9D%20%EA%B0%80%EA%B2%A9%EC%9D%98%20%EC%A7%80%EC%97%AD%EA%B0%84%20%EC%83%81%EA%B4%80%20%EA%B4%80%EA%B3%84%20%EB%B6%84%EC%84%9D%20%EC%97%B0%EA%B5%AC.pdf
[68] 우리나라 주요 지역 주택가격의 요인분석: 공통요인의 식별을 중심으로, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE02372222
[69] 부동산 실거래가를 보고 부동산 적정가격 산정하는 방법, https://blog.naver.com/eunj704/222268385367?viewType=pc
[70] Risk and Return in the Ulsan Housing Market, https://www.semanticscholar.org/paper/f187b4e2e400ef3a6a341ad398e53f9f57d91a7f
[71] 경관 차폐거리가 주택가격에 미치는 영향에 관한 연구, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE10895864
[72] Risk and return in residential spatial markets: An empiric and theoretic model, https://www.semanticscholar.org/paper/81cb71f24032cf7b7eb4c83d5b8c4e9ae24ac182
[73] 트리 기반 앙상블 방법을 활용한 자동 평가 모형 개발 및 평가, https://www.kdiss.org/journal/download_pdf.php?doi=10.7465/jkdi.2020.31.2.375
[74] 단독주택 실거래가격 토지･건물 배분비율 분석, http://journal.cartography.or.kr/articles/pdf/RvmO/kca-2020-020-02-5.pdf
[75] 아파트 매매가격과 부동산 온라인 뉴스의 교차상관관계와 ..., https://kpaj.or.kr/_PR/view/?aidx=18557&bidx=1622
[76] 토지 실거래가격 결정요인에 관한 연구, https://www.semanticscholar.org/paper/1f8aafad9a110d4bcdc07c17e8849865736df3fc
[77] 서울특별시 아파트의 순환변동에 관한 비교 분석* - HP filter ..., http://www.kreaa.or.kr/data/vol24-1/24_01_02.pdf
[78] 서울시 아파트 실거래가의 변화패턴 분석, https://www.semanticscholar.org/paper/b86fefc44042850a9ec2c87d84696b9b50d21d17
[79] 기본재산 공제제도 개편방안 연구, https://www.semanticscholar.org/paper/43ff0d0366ca051e6348d420007224dfd3b09bf6
[80] 부동산 정책의 효과에 관한 연구, https://s-space.snu.ac.kr/bitstream/10371/130387/1/000000009021.pdf
[81] 공간통계기법을 이용한 서울시 아파트 실거래가 변인의 시공간적 이질성 분석, https://www.semanticscholar.org/paper/7a6e553dacac0551c1ba02808b2d001af2b5b3b8
[82] 아파트 가격에 대한 APC(age-period-cohort) 효과 분석, https://kpa1959.or.kr/file/F110.pdf
[83] 주택정책을 위한 헤도닉 모형 평가에 관한 연구, https://www.semanticscholar.org/paper/e3878c6ee5bcb7fe069b3fb5c164f5ac59269b23
[84] The Analysis on Estimation and Determinants of Regional Housing Risk Premium using Fixed Effect Model, https://www.semanticscholar.org/paper/49904ba0d1890b6d8299ca9760efcbba02c2b307
[85] [논문]수도권 주택가격 결정요인 변화 연구, https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO201308438433204
[86] 주식, 채권, 부동산시장의 변동성 전이에 관한 연구, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE07426696
[87] 자산가격 결정모형을 이용한 우리나라 주택가격 분석, https://www.semanticscholar.org/paper/d7c0d3d9eee3c76f9d8466420abce064d7b9a4bd
[88] Why residuals can be useful in real estate valuation, https://www.semanticscholar.org/paper/e555f7fbffdb01561e36fd891f03efceb41b7770
[89] 실거래가 신고후 지가변동률에 관한 연구, https://www.semanticscholar.org/paper/41635bdc7a914567efccb4c14114bc5ce94bc25e
[90] 친환경적 기피시설이 아파트 가격에 미치는 영향, https://koreashe.org/wp-content/uploads/2025/10/%ED%8F%AC%EC%8A%A4%ED%84%B0_5_%ED%99%98%EA%B2%BD%EC%A0%95%EC%B1%85_%ED%95%9C%EC%84%B1%EC%9A%B0.pdf
[91] 국내외 주택가격모형의 특성에 관한 연구: 메타회귀분석을 ..., https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001815540
[92] Spatial Econometric Analysis of Regional Housing Markets, https://www.semanticscholar.org/paper/298372b1970f6a1f242d492ca76094586e7bfdce
[93] The residual method of valuation, http://link.springer.com/10.1007/978-1-137-01728-4_7
[94] 아파트 실거래가와 거래량이 시세에 미치는 영향, https://www.semanticscholar.org/paper/3bcf17f55e040beccb99cdba807cc900eaef1e1e
[95] A Study on the Theoretical and Empirical Analysis of Housing Pricing - Focused on the Seoul Apartment Market-, https://www.semanticscholar.org/paper/155bb8f2b80ed663dfda397e234d33ec261c121c
[96] 소비자의 주택가격전망이 아파트 거래량에 미치는 영향 연구, https://www.ejhuf.org/archive/view_article?pid=jhuf-1-2-5
[97] 규제정책이 서울시 지가변화에 미치는 영향력 분석, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE02000710
[98] 논문 : 부동산 실거래가격 확보방안에 관한 연구, https://www.semanticscholar.org/paper/83fb0c9c77401cf6af679fbc317eb6034a613e83
[99] 서울시 주택가격, 인구, 지역내총생산의 인과분석, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE07260656
[100] 물류부동산 거래가격에 영향을 미치는 요인에 대한 연구, https://s-space.snu.ac.kr/bitstream/10371/183180/1/000000170891.pdf
[101] 구조 변화를 감안한 우리나라 주택시장 분석, https://www.semanticscholar.org/paper/3436b143a1f60ce0f451091bef9f1aeb80ce2fba
[102] 주택가격 변동의 지역간 파급효과 분석, https://www.e-hfr.org/archive/view_article?pid=hfr-8-2-71
[103] 패널 자료를 이용한 지역별 주택매매가격 분석, https://www.semanticscholar.org/paper/7b2aaddf915b06e828fa24ae5dc9e8278c4e991b
[104] 논문(論文) : 공간패널모형을 활용한 우리나라 주택가격의 동학적 특성분석, https://www.semanticscholar.org/paper/f513fcf92bbf617a868927d1469ac35a9d68872e
[105] GWR 접근법을 활용한 부동산 감정평가 모형 연구: 서울시 아파트를 사례로, https://www.semanticscholar.org/paper/a4eeb54d6e8e830a75615b0d3922dce8c65496ac
[106] 직거래 정보가 아파트 매매가격 및 거래량의 변동에 미치는 영향, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE11468494
[107] 주택 거래 간 시공간 의존성을 고려한 헤도닉 가격 추정, https://www.semanticscholar.org/paper/d73dbe1e5ffe298de451d0d0fcc447635629a10b
[108] Residual Statistics, https://www.taylorfrancis.com/books/9781003213758/chapters/10.4324/9781003213758-3
[109] 위험프리미엄이 임대수익률에 미친 영향, https://s-space.snu.ac.kr/handle/10371/151706
[110] 시간적 상관도를 활용한 변환 영역 잔차 신호 Wyner-Ziv 부호화, https://www.semanticscholar.org/paper/c70184d0b7275e7b7a9bbd5f54a961b411a62235
[111] 통화정책과 부동산정책이 주택시장에 미치는 영향 연구: 지방광역시 고가아파트 중심으로: Research on the impact of monetary policy and real estate policy on the …, https://www.dbpia.co.kr/journal/detail?nodeId=T16857243
[112] 공간계량모형을 활용한 아파트가격 영향요인 분석 연구, https://journal.khousing.or.kr/articles/pdf/NGwa/khousing-2020-031-01-8.pdf
[113] 연구논문(硏究論文) : 지리가중회귀모델을 이용한 주택가격 결정요인의 지역별 특성에 관한 연구 -부산광역시를 중심으로-, https://www.semanticscholar.org/paper/22b6b2d04d593a12622acad7a858815fc48eb5be
[114] "같은 구인데 집값 30배 차이?" 서울 부동산 시장 양극화 심화, https://v.daum.net/v/fT70YJ0Hln
[115] 서울지역 아파트의 경매낙찰가율에 영향을 미치는 요인에 관한 연구 - 시점수정 낙찰가율과 법원경매 낙찰가율에 미치는 영향요인에 대한 비교연구 -, https://www.semanticscholar.org/paper/03c02b4cd29f8e933449e2b9498f1c9ca0929bb8
[116] 부동산 비기초가격과 부동산 신문담론의 관계에 대한 시계열 분석, https://s-space.snu.ac.kr/bitstream/10371/197489/1/000000178523.pdf
[117] 지리가중회귀모형을 활용한 서울시 주택하위시장 도출에, https://www.kpaj.or.kr/xml/22367/22367.pdf
[118] An Empirical Study on the Resale Regulation and Housing Price in Korea - Focused on the 11.3 Real Estate Measures -, https://www.semanticscholar.org/paper/c36be7e0eac382d2f7137b7a89cd9e8d2900cb1d
[119] A Study on the Relation between Price Change and Trading Volume intra Zoning of Real Estate Market: Focused on the Daegu Region, https://www.semanticscholar.org/paper/18a7a9097fd0e14d6e6b58e6d97b65e6fe212903
[120] 잔차 오차 최소에 의한 HEMT의 외인성 파라미터 추출, https://www.semanticscholar.org/paper/d78b06839b5fa994c231bf93444ad4f056582a0d
[121] CR-DPCM을 이용한 HEVC 무손실 인트라 예측 방법, https://www.semanticscholar.org/paper/8b5a77c5f93d8f7783cad9a25b88efc7ca5aa04f
[122] Housing Price Estimation using Spatial Econometrics Models : Focused on the Real Transaction Housing Price in the Busan, https://www.semanticscholar.org/paper/b63e11a930bda6346adac374d189af5807770f8d
[123] 수도권 불안정주택시장에서 주택가격 변동에 영향을 미치는 요인 분석, https://www.semanticscholar.org/paper/b23b7aa0a006be0214c2b95efcc0d3334fcfb79b
[124] 아파트 실거래가 지수를 이용한 부동산 시장 평가, https://www.semanticscholar.org/paper/e4f463a3b51c34a6699c6b3c05d30be8fe1e820f
[125] 공동주택 실거래가격의 지역별 상관성 분석에 관한 기초연구, https://www.semanticscholar.org/paper/729d9e4d9570f093706c39e050e80c4339cc7a7f
[126] 부동산가격에 있어 장기균형과 충격반응분석: 강남구, 성남시, 안양시, 용인시를 중심으로: 강남구, 성남시, 안양시, 용인시를 중심으로, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE01085751
[127] 특성가격함수를 이용한 주택가격지수 개발에 관한 연구 -시간변동계수모형에 의한 연쇄지수, https://www.semanticscholar.org/paper/65c9218e3a9f3a753c1043bbc3cc204bfe9e0244
[128] 개별 주택가격 데이터를 이용한 주택가격 변동률 분포의 특성 ..., https://www.ejhuf.org/archive/view_article?pid=jhuf-7-1-27
[129] 아파트 매매가격지수 변동률에 의한 전국 주택시장 유형화 및 유형별 가격변동 영향요인 분석, https://www.semanticscholar.org/paper/501c2fadf21eed9b90d90d4f7a3f3e44b40c1fab
[130] 부동산정책에 따른 투자심리와 주택가격 변화에 관한 연구, https://s-space.snu.ac.kr/handle/10371/193038
[131] 공간적탐색기법을 이용한 부산 주택시장 다이나믹스 분석, https://www.semanticscholar.org/paper/464e3634488a910cb9b94773b0b3080e2b54c438
[132] 토지특성 요인에 입각한 개별공시지가의 실거래가 반영률 차이분석, https://www.semanticscholar.org/paper/075e52ef8cd1a99c36223b2afc161a028b98d1b4
[133] 제 2차 잔차 변환을 이용한 HEVC 무손실 인트라 코딩, https://www.semanticscholar.org/paper/e160d2eca630731c8f834941bbd7096a015bb0ec
[134] 인루프 필터링을 적용한 예측 방법을 이용한 영상 부호화/복호화 방법 및 장치, https://www.semanticscholar.org/paper/4a987389051d2f1edba4e66bf4892a10f68504de
[135] 주식시장 지수와 부동산시장 지수의 시계열 특성비교와 관계에 관한 실증적 연구, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE01671916
[136] 부동산 수요 조절 정책이 서울시 아파트 매매가격에 미치는 효과: 2019 년과 2020 년 주택시장 안정화 방안 사례, http://kreaa.or.kr/data/vol28-3/28_03_04.pdf
[137] 코로나 19와 부동산 감정평가, https://www.semanticscholar.org/paper/f69f693b8ab926d3fec8dafbb8a00a2c85284975
[138] 유동성의 변동이 주택가격 변동성에 미치는 영향, https://www.semanticscholar.org/paper/5563eac55c921389b9f6736b22970b1fcbb74ffc
[139] 부동산 PF사업 사업단계별 리스크 요인 영향관계 분석, https://www.semanticscholar.org/paper/7ebacaf9f10bb23e241cf729d85c52d67e5e2e44
[140] 고도차에 따른 GBAS 대류층 잔차 불확실성 모델 분석, https://www.semanticscholar.org/paper/8cf26f235e1b442fc1cbff4db10395d216746263
[141] 주거환경의 지역 간 불균형에 따른 주택가격 영향분석, https://gdi.re.kr/datafile/dgpaper_down/paper_12_2_7.pdf
[142] 住宅建設과 住宅賣買價格 및 여타 住宅關聯 變數들의 因果關係分析, https://www.semanticscholar.org/paper/88cd1a1075d22d26b3a03263c2db340d9b3c3308
[143] 도시지역의 녹지공간이 공동주택가격에 미치는 영향-서울시 근린공원을 중심으로, https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE09872034
[144] 실질주택매매가격 변동성에 영향을 주는 요인 고찰, https://www.semanticscholar.org/paper/5b6d9f235afcfa479fd2c1d8091c5226f50c5668
[145] 부동산 시가표준액의 합리적 결정방안, https://www.kilf.re.kr/cmm/fms/PDF.do;jsessionid=943D88DC2D7E52CCE9FA22C151901DC3?atchFileId=FILE_000000000004990&fileSn=0
[146] 은퇴계층의 부동산 자산 배분 결정요인 분석, https://s-space.snu.ac.kr/handle/10371/129831
[147] Determinants of Price Gap between Asking Price and Real Transaction Price of Apartment in Seoul Metropolitan Area, https://www.semanticscholar.org/paper/9281b1f143ed93c12d3b049f72008c154fff96b0
[148] 지역단위 사회서비스 기초통계 개발 및 관리방안 연구, https://www.semanticscholar.org/paper/85f60422e7fee3c2f034c4f642a87b84fadc8a2b
[149] 주택 매매 및 전세시장의 변화와 은행의 건전성, https://www.semanticscholar.org/paper/8405e6843831a02c1625f17bc98cef0012ecbb1e
[150] 부동산규제가 법인의 주택시장 참여에 미친 영향, https://s-space.snu.ac.kr/handle/10371/176278
[151] 부동산 거래정보(콘텐츠)에 관한 법적규제의 쟁점, https://www.semanticscholar.org/paper/ec78ef1ad3e24e210b1e4e5c9b24cc3089bde0a7
[152] 주택 정책의 지역별 시장 파급효과 분석을 위한 시뮬레이션 모델 개발, https://www.semanticscholar.org/paper/7ae586e930f336f7ada345549409769a4e984b72
[153] 지역 차원의 소득과 자산 간 결합분포: 수도권과 비수도권의 비교, https://www.semanticscholar.org/paper/c4bcf5f95550a9ffd1a0172fe3908579db6016d7
[154] 공간사용 규제가 택지가격에 미치는 영향에 대한 공간가중 ..., http://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002390312
[155] 투자자별 부동산 선호요인이 재투자 의사에 미치는 영향 분석, https://www.semanticscholar.org/paper/a58fa6532e41ad07851c2d427b8dc308c6796fec

---

## 데이터 전처리 및 분석 방법론

### 데이터 소스 및 입력

**원본 데이터:**
- 국토교통부 전월세 실거래 데이터 (data.go.kr)
- 지역: 경기도 수원시 영통구, 용인시 기흥구
- 기간: 2023년 11월 ~ 2025년 11월
- 부동산 유형: 연립다세대, 단독다가구, 오피스텔
- 총 12개 CSV 파일 (각 유형별 4개 파일)

**주요 입력 변수:**
- 시군구, 번지, 본번, 부번, 건물명, 도로명
- 전월세구분, 보증금(만원), 월세금(만원)
- 전용면적(㎡), 층, 건축년도
- 계약년월, 계약일, 계약기간
- 주택유형, 부동산유형

### 데이터 전처리 파이프라인

**구현 파일:** `real_estate/preprogressed/data_preprocessing.py`

#### 1. CSV 파일 병합 (`merge_csv_files`)
- **Input:** 12개 CSV 파일 (cp949/euc-kr 인코딩)
- **Process:**
  - 헤더 라인 자동 탐지 (NO 컬럼 기준)
  - 인코딩 자동 감지 및 변환
  - 파일명에서 부동산유형 추출
  - 원본파일명 컬럼 추가
- **Output:** `merged_all_data.csv` (38,023행, 26개 컬럼)

#### 2. 캠퍼스 존 분류 (`create_campus_zone`)
- **Input:** `merged_all_data.csv`
- **Process:**
  - 수원시 영통구 + 용인시 기흥구 필터링
  - 경희대 국제캠퍼스 기준 코어/확장 생활권 분류
    - 코어 존: 서천동, 영덕동, 구갈동, 중동, 이의동, 원천동, 영통동
    - 확장 존: 그 외 지역
- **Output:** `merged_all_data_with_zone.csv` (campus_zone 컬럼 추가)

#### 3. 월주거비 통일 계산 (`calculate_monthly_cost`)
- **Input:** `merged_all_data_with_zone.csv`
- **Process:**
  - 계약년월 → contract_year, contract_month 분리
  - 전세/월세를 하나의 월주거비로 통일
  - 공식: `converted_monthly_cost = 월세금 + (보증금 × 연이자율 / 12)`
  - 전용면적당 월주거비: `cost_per_m2 = converted_monthly_cost / 전용면적`
- **Output:** `merged_data_with_costs.csv`
- **초기 연이자율:** 4% (임시값, 나중에 실제 금리로 교체)

#### 4. 금리/CPI 템플릿 생성 (`create_interest_cpi_template`)
- **Input:** `merged_data_with_costs.csv`
- **Process:**
  - 계약년월별 유니크 조합 추출
  - year_month 문자열 생성 (예: "2023-11")
  - annual_rate, cpi_index 컬럼 생성 (초기값 NaN)
- **Output:** `interest_cpi_template.csv` (24개월)

#### 5. 금리 추정값 채우기 (`fill_annual_rate`)
- **Input:** `interest_cpi_template.csv`
- **Process:**
  - 주택담보대출 금리 추정 (선형 감소 가정)
  - 2023년 11월: 4.0% → 2025년 10월: 3.5%
  - 참고: 실제 데이터는 한국은행 ECOS에서 받아야 함
- **Output:** `interest_cpi_template.csv` (annual_rate 채워짐)

#### 6. 실질 월주거비 계산 (`merge_and_recalculate_costs`)
- **Input:** 
  - `merged_data_with_costs.csv`
  - `interest_cpi_template.csv` (annual_rate, cpi_index 포함)
- **Process:**
  - 실제 금리로 월주거비 재계산
  - CPI로 실질 월주거비 계산
  - 공식: `real_monthly_cost = converted_monthly_cost / (현재_CPI / 기준_CPI)`
- **Output:** `final_data_with_real_costs.csv`
- **생성 변수:**
  - `converted_monthly_cost`: 실제 금리로 계산된 명목 월주거비
  - `cost_per_m2`: 명목 m²당 월주거비
  - `real_monthly_cost`: CPI로 조정된 실질 월주거비
  - `real_cost_per_m2`: 실질 m²당 월주거비

#### 7. 누락 컬럼 복원 (`restore_missing_columns`)
- **Input:**
  - `final_data_with_real_costs.csv` (일부 컬럼만 포함)
  - `merged_all_data_with_zone.csv` (모든 컬럼 포함)
- **Process:**
  - 원본 데이터에서 누락된 컬럼 복원
  - 복원 컬럼: NO, 번지, 본번, 부번, 건물명, 계약일, 층, 건축년도, 도로명, 계약기간, 계약구분, 갱신요구권 사용, 종전계약 보증금/월세, 원본파일명, 단지명, 도로조건, 계약면적
- **Output:** `final_data_with_real_costs.csv` (35개 컬럼)

#### 8. 주소 분리 (`split_address`)
- **Input:** `final_data_with_real_costs.csv`
- **Process:**
  - 시군구 컬럼을 시도/시/구군/동읍면으로 분리
  - 예: "경기도 수원시 영통구 원천동" → 시도: 경기도, 시: 수원시, 구군: 영통구, 동읍면: 원천동
- **Output:** `final_data_with_real_costs.csv` (39개 컬럼)
- **결과:**
  - 동읍면 고유 개수: 25개
  - 시도: 경기도 (100%)
  - 시: 수원시 (22,826건), 용인시 (15,197건)
  - 구군: 영통구 (22,826건), 기흥구 (15,197건)

#### 9. room_key 생성 (`create_room_key`)
- **Input:** `final_data_with_real_costs.csv`
- **Process:**
  - full_address 생성 (시군구 + 도로명 또는 번지)
  - room_key 생성: "주소|층|면적" 조합
  - 완전 중복 행 제거 (주요 컬럼 기준)
- **Output:** `final_data_with_real_costs.csv` (38개 컬럼)
- **결과:**
  - room_key 고유 개수: 6,662개
  - 방당 평균 거래 횟수: 5.71회
  - 중복 제거: 38,023행 → 31,653행

### OLS 회귀분석

**구현 파일:** `real_estate/preprogressed/ols_analysis.py`

**타겟 변수:** `real_cost_per_m2` (실질 m²당 월주거비)

**독립변수:**
- 기본 변수: area (전용면적), deposit (보증금), monthly_rent (월세), floor (층), building_age (건물연령)
- 교차항: area × deposit, area × monthly_rent, area × building_age, deposit × monthly_rent
- 범주형 더미: property_type (부동산유형), rent_type (전월세구분), campus_zone

**모델 성능:**
- R²: 0.8630 (86.3% 설명력)
- 조정 R²: 0.8625
- RMSE: 0.2770
- 관측치 수: 3,303개

**주요 유의한 변수 (p < 0.05):**
- building_age: -0.0415 (건물 연령이 높을수록 m²당 주거비 감소)
- area: -0.0362 (면적이 클수록 m²당 주거비 감소, 규모의 경제)
- monthly_rent: 0.0245 (월세가 높을수록 m²당 주거비 증가)
- floor: -0.0061 (층수가 높을수록 m²당 주거비 약간 감소)
- deposit: 0.0010 (보증금이 높을수록 m²당 주거비 증가)

**교차항 (Interaction Terms):**
- area × age: 0.0010 (면적이 클수록 연령 효과 증가)
- area × monthly_rent: -0.000091 (면적이 클수록 월세 효과 감소)
- area × deposit: -0.000063 (면적이 클수록 보증금 효과 감소)
- deposit × rent: 0.000019 (보증금과 월세의 상호작용)

**이상치 탐지:**
- 표준화 잔차 > 3: 37개 (1.12%)
- 높은 영향력 관측치 (Cook's D): 188개

**시각화:**
- 잔차 플롯, 표준화 잔차 플롯, Q-Q 플롯
- Cook's Distance, 실제값 vs 예측값
- 타겟 변수/잔차 분포, 주요 변수 계수, 이상치 시각화
- 저장 파일: `ols_analysis_results.png`

### 최종 데이터 구조

**파일:** `real_estate/preprogressed/final_data_with_real_costs.csv`

**데이터 크기:**
- 행 수: 31,653행 (중복 제거 후)
- 컬럼 수: 38개

**주요 컬럼:**
1. 기본 정보: 시군구, 부동산유형, 전월세구분, 주택유형
2. 주소 정보: 시도, 시, 구군, 동읍면, full_address, 번지, 도로명
3. 면적 정보: 전용면적(㎡), 계약면적(㎡)
4. 금액 정보: 보증금(만원), 월세금(만원)
5. 시간 정보: 계약년월, contract_year, contract_month, 계약일
6. 건물 정보: 층, 건축년도, 건물명, 단지명
7. 지역 분류: campus_zone (core/extended)
8. 금리/물가: annual_rate, cpi_index
9. 계산 변수: converted_monthly_cost, cost_per_m2, real_monthly_cost, real_cost_per_m2
10. 식별 키: room_key, NO, 원본파일명

### 함수 및 메서드

**주요 함수 (`data_preprocessing.py`):**
1. `merge_csv_files()`: 여러 CSV 파일 병합
2. `create_campus_zone()`: 캠퍼스 존 분류
3. `calculate_monthly_cost()`: 월주거비 계산
4. `create_interest_cpi_template()`: 금리/CPI 템플릿 생성
5. `fill_annual_rate()`: 금리 추정값 채우기
6. `merge_and_recalculate_costs()`: 실질 월주거비 계산
7. `restore_missing_columns()`: 누락 컬럼 복원
8. `analyze_data()`: 기본 통계 분석
9. `run_full_pipeline()`: 전체 파이프라인 실행

**분석 함수 (`ols_analysis.py`):**
- OLS 회귀분석, 다중공선성 확인 (VIF), 이상치 탐지, 시각화

**주소 처리 함수 (`split_address.py`, `create_room_key.py`):**
- 주소 분리, full_address 생성, room_key 생성

### 출력 파일

1. `final_data_with_real_costs.csv`: 최종 전처리 데이터 (38개 컬럼, 31,653행)
2. `interest_cpi_template.csv`: 월별 금리/CPI 템플릿 (24개월)
3. `ols_analysis_results.png`: OLS 회귀분석 시각화 결과

### 다음 단계

1. 지오코딩: 동별 중심 좌표 매핑 (카카오/네이버/VWorld API)
2. 환경 데이터 추가: 버스정류장, 상권, 공기질, 소음 데이터
3. 교통 데이터 추가: 대중교통 접근성, 교통량 등
4. 리스크 변수 추가: 환경 리스크, 교통 리스크 등
