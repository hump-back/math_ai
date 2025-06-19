import streamlit as st
import numpy as np
import pandas as pd

st.title("조건부 확률과 주변 확률 분포 (Conditional & Marginal Probability Distributions) 📊")

st.markdown("""
## 📝 시험 문제 풀이 가이드

### 1️⃣ 문제 해결 단계

1. **주변확률 구하기**
   - p(x): 각 행의 합 (→ 방향)
   - p(y): 각 열의 합 (↓ 방향)
   - 합계를 표 옆/아래에 바로 메모하기

2. **조건부확률 계산**
   - 공식: P(A|B) = P(A,B) / P(B)
   - 조건이 되는 행/열만 선택하여 계산
   - 계산 결과는 반드시 합이 1이 되어야 함

3. **검산하기**
   - 모든 확률은 0~1 사이
   - 각 분포의 합은 1
   - 분수 형태와 소수점 형태 모두 기록
""")

# 예제 데이터
st.markdown("""
### 2️⃣ 예제 문제
다음 결합확률분포표를 이용하여 주변확률과 조건부확률을 구해보세요.
""")

# 초기 결합 확률 분포표
default_joint_prob = np.array([
    [0.01, 0.05, 0.10],
    [0.02, 0.10, 0.05],
    [0.03, 0.05, 0.03],
    [0.10, 0.07, 0.05],
    [0.10, 0.20, 0.04]
])

# 데이터프레임 생성 - Index 객체 사용
df = pd.DataFrame(
    default_joint_prob,
    index=pd.Index(['x₁', 'x₂', 'x₃', 'x₄', 'x₅']),
    columns=pd.Index(['y₁', 'y₂', 'y₃'])
)
st.dataframe(df.style.format("{:.3f}"))

# 주변 확률 분포 계산
st.subheader("📈 Step 2: 주변 확률 분포 계산")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    #### p(x) 계산 방법
    1. 각 행의 값을 **오른쪽 방향**으로 더하기
    2. 계산 과정을 표 옆에 메모
    """)
    px = df.sum(axis=1)
    px_df = pd.DataFrame(px, columns=pd.Index(['확률']))
    st.dataframe(px_df.style.format("{:.3f}"))
    
    st.markdown("""
    **✍️ 계산 예시:**
    ```
    p(x₁) = 0.01 + 0.05 + 0.10 = 0.16
    p(x₂) = 0.02 + 0.10 + 0.05 = 0.17
    p(x₃) = 0.03 + 0.05 + 0.03 = 0.11
    p(x₄) = 0.10 + 0.07 + 0.05 = 0.22
    p(x₅) = 0.10 + 0.20 + 0.04 = 0.34
    ```
    ✅ 합계 = 1.00 (검산 완료)
    """)

with col2:
    st.markdown("""
    #### p(y) 계산 방법
    1. 각 열의 값을 **아래 방향**으로 더하기
    2. 계산 과정을 표 아래에 메모
    """)
    py = df.sum(axis=0)
    py_df = pd.DataFrame(py, columns=pd.Index(['확률']))
    st.dataframe(py_df.style.format("{:.3f}"))
    
    st.markdown("""
    **✍️ 계산 예시:**
    ```
    p(y₁) = 0.01 + 0.02 + 0.03 + 0.10 + 0.10 = 0.26
    p(y₂) = 0.05 + 0.10 + 0.05 + 0.07 + 0.20 = 0.47
    p(y₃) = 0.10 + 0.05 + 0.03 + 0.05 + 0.04 = 0.27
    ```
    ✅ 합계 = 1.00 (검산 완료)
    """)

# 조건부 확률 분포 계산
st.subheader("📊 Step 3: 조건부 확률 분포 계산")

# Y=y₁일 때 X의 조건부 확률
st.markdown("""
#### 3-1. p(x|Y=y₁) 계산
1. y₁열의 값들만 선택
2. 각 값을 p(y₁)로 나누기
3. 분수 형태로 먼저 쓰고, 소수점으로 변환
""")
px_given_y1 = df['y₁'] / py['y₁']
px_given_y1_df = pd.DataFrame(px_given_y1, columns=pd.Index(['확률']))
st.dataframe(px_given_y1_df.style.format("{:.3f}"))

st.markdown("""
**✍️ 상세 계산:**
```
p(x₁|Y=y₁) = 0.01/0.26 = 0.038
p(x₂|Y=y₁) = 0.02/0.26 = 0.077
p(x₃|Y=y₁) = 0.03/0.26 = 0.115
p(x₄|Y=y₁) = 0.10/0.26 = 0.385
p(x₅|Y=y₁) = 0.10/0.26 = 0.385
```
✅ 합계 = 1.00 (검산 완료)
""")

# X=x₃일 때 Y의 조건부 확률
st.markdown("""
#### 3-2. p(y|X=x₃) 계산
1. x₃행의 값들만 선택
2. 각 값을 p(x₃)로 나누기
3. 분수 형태로 먼저 쓰고, 소수점으로 변환
""")
py_given_x3 = df.loc['x₃'] / px['x₃']
py_given_x3_df = pd.DataFrame(py_given_x3, columns=pd.Index(['확률']))
st.dataframe(py_given_x3_df.style.format("{:.3f}"))

st.markdown("""
**✍️ 상세 계산:**
```
p(y₁|X=x₃) = 0.03/0.11 = 0.273
p(y₂|X=x₃) = 0.05/0.11 = 0.455
p(y₃|X=x₃) = 0.03/0.11 = 0.273
```
✅ 합계 = 1.00 (검산 완료)
""")

# 시험 팁
st.subheader("💡 시험 꿀팁")
st.markdown("""
1. **계산 순서**
   - 주변확률 → 조건부확률 순서로 풀기
   - 주변확률은 표에 직접 합계 메모하기
   - 조건부확률은 분수 형태 먼저 쓰기

2. **실수 방지**
   - 모든 확률의 합이 1인지 검산
   - 확률값이 0~1 사이인지 확인
   - 분모가 주변확률이 맞는지 재확인

3. **시간 절약**
   - 계산기 사용 시 분수 계산 먼저하기
   - 주변확률 계산 시 표에 바로 메모
   - 조건부확률은 필요한 행/열만 보기

4. **답안 작성**
   - 분수 형태와 소수점 형태 모두 기록
   - 각 단계의 계산 과정 명확히 표시
   - 최종 답안 박스 처리 또는 밑줄
""")

# 연습문제 제안
st.markdown("""
### 🎯 연습하기 좋은 문제 유형
1. 3x3 또는 4x3 크기의 결합확률분포표
2. 조건부확률 구하기 (특정 조건 하에서의 확률)
3. 주변확률을 이용한 독립성 검정
4. 베이즈 정리 활용 문제
""") 