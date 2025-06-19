import streamlit as st

st.title("다변수 함수의 연쇄법칙 (Chain Rule for Multivariable Functions) 📐")

st.markdown("""
## 📝 개념 정리

### 연쇄법칙(Chain Rule)이란?
합성함수의 미분법으로, 여러 변수가 서로 의존관계에 있을 때 사용하는 미분 방법입니다.

### 기본 공식
다변수 함수 $f(x_1, x_2)$에서 $x_1, x_2$가 $t$의 함수일 때:

$$
\\frac{df}{dt} = \\frac{\\partial f}{\\partial x_1} \\frac{dx_1}{dt} + \\frac{\\partial f}{\\partial x_2} \\frac{dx_2}{dt}
$$
""")

st.markdown("""
## 💡 예제 문제

### 문제
다음 함수의 $\\frac{df}{dt}$를 구하시오.

* $f(x_1, x_2) = (x_1 + 2x_2^3)^2$
* $x_1 = \\sin t$
* $x_2 = \\cos t$
""")

st.markdown("""
## 📌 단계별 풀이 방법

### Step 1: 편미분 계산 $\\frac{\\partial f}{\\partial x_1}, \\frac{\\partial f}{\\partial x_2}$

먼저 $u = x_1 + 2x_2^3$ 로 치환하면 $f = u^2$ 입니다.

#### (a) $\\frac{\\partial f}{\\partial x_1}$ 계산
```
∂f/∂x₁ = 2u · ∂u/∂x₁
       = 2(x₁ + 2x₂³) · 1
       = 2(x₁ + 2x₂³)
```

#### (b) $\\frac{\\partial f}{\\partial x_2}$ 계산
```
∂f/∂x₂ = 2u · ∂u/∂x₂
       = 2(x₁ + 2x₂³) · 6x₂²
       = 12x₂²(x₁ + 2x₂³)
```
""")

st.markdown("""
### Step 2: 변수 미분 $\\frac{dx_1}{dt}, \\frac{dx_2}{dt}$

* $\\frac{dx_1}{dt} = \\frac{d}{dt}(\\sin t) = \\cos t$
* $\\frac{dx_2}{dt} = \\frac{d}{dt}(\\cos t) = -\\sin t$
""")

st.markdown("""
### Step 3: 연쇄법칙 적용

$$
\\begin{align*}
\\frac{df}{dt} &= \\frac{\\partial f}{\\partial x_1} \\frac{dx_1}{dt} + \\frac{\\partial f}{\\partial x_2} \\frac{dx_2}{dt} \\\\
&= 2(x_1 + 2x_2^3)\\cos t + 12x_2^2(x_1 + 2x_2^3)(-\\sin t) \\\\
&= 2(x_1 + 2x_2^3)\\cos t - 12x_2^2(x_1 + 2x_2^3)\\sin t \\\\
&= 2(x_1 + 2x_2^3)[\\cos t - 6x_2^2\\sin t]
\\end{align*}
$$

### Step 4: 최종 정리
$x_2 = \\cos t$ 를 대입하면:

$$
\\frac{df}{dt} = 2(x_1 + 2x_2^3)(\\cos t - 6\\sin t \\cos^2 t)
$$
""")

st.markdown("""
## 🎯 시험 대비 체크리스트

1. **연쇄법칙 공식 암기**
   - $\\frac{df}{dt} = \\frac{\\partial f}{\\partial x_1} \\frac{dx_1}{dt} + \\frac{\\partial f}{\\partial x_2} \\frac{dx_2}{dt}$

2. **풀이 순서**
   - 함수와 변수 관계 정리
   - 연쇄법칙 공식 적용
   - 각 편미분 계산
   - 변수 미분 계산
   - 모든 항 곱하고 더하기
   - 주어진 값 대입하여 정리

3. **실수 방지 포인트**
   - 편미분 시 다른 변수는 상수 취급
   - 부호 실수 주의 (특히 삼각함수 미분)
   - 괄호 처리 주의
   - 최종 답 검산
""")

st.markdown("""
## 🔍 연습문제 유형

1. **기본형**
   - 다항식 + 삼각함수
   - 지수함수 + 로그함수
   - 분수함수

2. **응용형**
   - 매개변수 곡선의 접선
   - 음함수의 미분
   - 열역학/물리 문제

3. **고난도**
   - 3변수 이상의 연쇄법칙
   - 2차 이상의 고차 미분
   - 편미분 방정식
""")

st.markdown("""
## 💪 연습 방법

1. **기본 연습**
   - 연쇄법칙 공식 암기
   - 간단한 다항식부터 시작
   - 삼각함수 미분 연습

2. **실전 연습**
   - 시간 재고 풀어보기
   - 답 없이 풀어보고 검산
   - 다양한 유형 반복 연습

3. **오답 노트**
   - 실수한 부분 표시
   - 헷갈리는 공식 정리
   - 유형별 풀이법 요약
""")

# 시험 꿀팁
st.sidebar.markdown("""
## 📌 시험 꿀팁

1. **시간 배분**
   - 공식 확인: 30초
   - 편미분 계산: 2분
   - 정리 및 검산: 1분

2. **실수 방지**
   - 부호 실수 주의
   - 괄호 확인
   - 검산 필수

3. **답안 작성**
   - 단계별로 구분
   - 중간 과정 표시
   - 최종 답 박스 처리
""") 