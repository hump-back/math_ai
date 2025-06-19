import streamlit as st
import numpy as np

st.title("베이즈 정리 (Bayes' Theorem) - 의료 검진 예제 🏥")

st.markdown("""
## 1. 베이즈 정리 기본 개념

베이즈 정리는 조건부 확률을 계산하는 방법으로, 특히 새로운 증거가 주어졌을 때 
가설의 확률이 어떻게 업데이트되는지를 계산하는 데 사용됩니다.

### 기본 공식
$$P(X|Y) = \\frac{P(Y|X) \\cdot P(X)}{P(Y)}$$

여기서:
- P(X|Y): 사건 Y가 일어났을 때, 사건 X가 일어날 조건부 확률
- P(Y|X): 사건 X가 일어났을 때, 사건 Y가 일어날 조건부 확률
- P(X): 사건 X의 사전 확률
- P(Y): 사건 Y의 확률

### 확장된 공식
분모 P(Y)는 다음과 같이 전체 확률의 법칙으로 표현할 수 있습니다:
$$P(Y) = P(Y|X) \\cdot P(X) + P(Y|X^C) \\cdot P(X^C)$$

따라서 베이즈 정리의 완전한 형태는:
$$P(X|Y) = \\frac{P(Y|X) \\cdot P(X)}{P(Y|X) \\cdot P(X) + P(Y|X^C) \\cdot P(X^C)}$$

## 2. 시험 문제 예시

### 문제 1
양성판정 정확도 90%, 양성인 사람의 비율 1%, 음성판정 정확도 90%일 때,
어떤 사람이 양성판정을 받았을 때 실제로 병에 걸릴 확률을 계산하시오.

여기서:
- X: 병에 걸리는 사건
- Y: 양성판정되는 사건
- P(X|Y): 양성판정인데 실제 병에 걸린 사람

### 풀이 과정
1) 문제에서 주어진 확률:
   - P(Y|X) = 90% = 0.90 (양성판정 정확도)
   - P(X) = 1% = 0.01 (사전 병에 걸린 확률)
   - P(Y|X^C) = 10% = 0.10 (위양성률 = 1 - 음성판정 정확도)
   - P(X^C) = 99% = 0.99 (병에 걸리지 않은 확률)

2) 분모 P(Y) 계산:
   $$P(Y) = P(Y|X) \\cdot P(X) + P(Y|X^C) \\cdot P(X^C)$$
   $$P(Y) = 0.90 \\times 0.01 + 0.10 \\times 0.99 = 0.108$$

3) 베이즈 정리 적용:
   $$P(X|Y) = \\frac{P(Y|X) \\cdot P(X)}{P(Y)} = \\frac{0.90 \\times 0.01}{0.108} = 0.0833$$

따라서, 양성판정을 받은 사람이 실제로 병에 걸렸을 확률은 약 8.33% (또는 83.33%)입니다.

### 시험 준비 팁 📝
1. 베이즈 정리 문제를 풀 때는 다음 순서를 따르세요:
   - 주어진 확률들을 명확히 정리하기 (P(Y|X), P(X) 등)
   - 구하고자 하는 조건부 확률 파악하기 (보통 P(X|Y))
   - 분모의 전체 확률 계산하기 (P(Y))
   - 베이즈 정리 공식에 대입하기

2. 자주 나오는 문제 유형:
   - 의료 검진 관련 문제
   - 품질 검사 문제
   - 시험/테스트 결과 해석 문제

3. 주의할 점:
   - 확률값의 보수 관계 활용 (P(X^C) = 1 - P(X))
   - 조건부 확률의 방향성 주의 (P(X|Y)와 P(Y|X)는 다름)
   - 분모 계산시 전체 확률의 법칙 적용 잊지 않기

## 3. 의료 검진 예제
""")

# 입력값 설정
st.subheader("📊 검사 정확도 설정")
col1, col2, col3 = st.columns(3)

with col1:
    sensitivity = st.slider("민감도 (양성판정 정확도)", 0.0, 100.0, 90.0, 0.1, format="%g%%") / 100
    st.markdown("실제 병이 있는 사람 중 양성 판정 비율")

with col2:
    specificity = st.slider("특이도 (음성판정 정확도)", 0.0, 100.0, 90.0, 0.1, format="%g%%") / 100
    st.markdown("실제 병이 없는 사람 중 음성 판정 비율")

with col3:
    prevalence = st.slider("유병률", 0.0, 100.0, 1.0, 0.1, format="%g%%") / 100
    st.markdown("전체 인구 중 실제 병이 있는 비율")

# 계산
false_positive_rate = 1 - specificity
p_positive = sensitivity * prevalence + false_positive_rate * (1 - prevalence)
p_disease_given_positive = (sensitivity * prevalence) / p_positive

# 결과 표시
st.subheader("🧮 계산 결과")
st.markdown(f"""
양성 판정을 받은 사람이 실제로 병에 걸렸을 확률은 **{p_disease_given_positive:.1%}** 입니다.
""")

# 계산 과정 설명
st.subheader("📝 상세 계산 과정")
st.markdown(f"""
### 주어진 확률값
- P(양성|병) = 민감도 = {sensitivity:.1%}
- P(음성|비병) = 특이도 = {specificity:.1%}
- P(병) = 유병률 = {prevalence:.1%}
- P(비병) = 1 - 유병률 = {1-prevalence:.1%}
- P(양성|비병) = 위양성률 = {false_positive_rate:.1%}

### 베이즈 정리 적용
$$P(병|양성) = \\frac{{P(양성|병) \\cdot P(병)}}{{P(양성)}}$$

여기서 P(양성)은:
$$P(양성) = P(양성|병) \\cdot P(병) + P(양성|비병) \\cdot P(비병)$$
$$P(양성) = {sensitivity:.3f} \\times {prevalence:.3f} + {false_positive_rate:.3f} \\times {1-prevalence:.3f} = {p_positive:.3f}$$

따라서:
$$P(병|양성) = \\frac{{{sensitivity:.3f} \\times {prevalence:.3f}}}{{{p_positive:.3f}}} = {p_disease_given_positive:.3f}$$
""")

# 직관적인 설명
st.subheader("💡 직관적인 이해")
population = 1000
diseased = int(prevalence * population)
healthy = population - diseased

true_positives = int(diseased * sensitivity)
false_positives = int(healthy * false_positive_rate)
total_positives = true_positives + false_positives

st.markdown(f"""
1000명을 검사했다고 가정해보면:
- 실제 병이 있는 사람: {diseased}명
- 실제 병이 없는 사람: {healthy}명

이 중에서:
- 병이 있는 사람 중 양성 판정: {true_positives}명
- 병이 없는 사람 중 양성 판정: {false_positives}명
- 전체 양성 판정: {total_positives}명

따라서, 양성 판정을 받은 {total_positives}명 중 실제로 병이 있는 사람은 {true_positives}명으로,
이는 전체 양성 판정의 {p_disease_given_positive:.1%}에 해당합니다.
""") 