import streamlit as st
import numpy as np

st.title("Minibatch 크기의 장단점 💻")

st.markdown("""
## 1. 문제 이해하기

### 시험 문제 예시
* "Large minibatch와 small minibatch의 장단점을 모두 쓰시오"
* "Minibatch 크기가 학습에 미치는 영향을 설명하시오"
* "딥러닝에서 배치 크기 선택의 trade-off를 설명하시오"

## 2. 모범 답안 구조

### Large Minibatch의 장단점

#### 장점 ✅
1. **안정적인 Gradient 추정**
   * gradient의 분산이 감소
   * 더 안정적인 학습 과정

2. **병렬 처리의 효율성**
   * GPU 활용도 증가
   * 병렬 컴퓨팅 환경에서 유리

3. **적은 업데이트 횟수**
   * 전체 데이터셋 처리에 필요한 iteration 감소
   * 계산 효율성 향상

#### 단점 ❌
1. **높은 계산 비용**
   * 많은 메모리 요구
   * 높은 연산 자원 필요

2. **국소 최적 문제**
   * local minima에 빠지기 쉬움
   * 평균적 특성에 과도하게 민감

3. **느린 학습 속도**
   * 파라미터 업데이트 빈도 감소
   * 상대적으로 느린 수렴 속도

### Small Minibatch의 장단점

#### 장점 ✅
1. **빠른 업데이트**
   * 잦은 파라미터 업데이트
   * 빠른 학습 진행 가능

2. **향상된 일반화 성능**
   * 노이즈 효과로 인한 local minima 회피
   * 더 좋은 일반화 능력

3. **낮은 메모리 사용**
   * 적은 메모리 요구량
   * 대규모 모델 학습에 유리

#### 단점 ❌
1. **불안정한 학습**
   * gradient 추정의 높은 분산
   * 학습 과정의 불안정성

2. **비효율적인 계산**
   * 병렬 처리 효율 감소
   * 전체적인 계산 속도 저하

3. **불확실한 학습 방향**
   * gradient variance 증가
   * 최적화 방향의 불확실성

## 3. 시험 답안 작성법 📝

### 모범 답안 예시
```
Large minibatch와 small minibatch의 장단점은 다음과 같다:

1. Large minibatch
장점:
- 안정적인 gradient 추정으로 학습이 안정적
- GPU 등 병렬 처리 효율성 증가
- 전체 iteration 수 감소

단점:
- 높은 계산 비용과 메모리 요구량
- local minima에 빠지기 쉬움
- 상대적으로 느린 학습 속도

2. Small minibatch
장점:
- 빠른 파라미터 업데이트로 학습 속도 향상
- 노이즈 효과로 인한 일반화 성능 향상
- 적은 메모리 사용량

단점:
- 불안정한 gradient 추정
- 병렬 처리 효율성 감소
- 학습 방향의 불확실성 증가
```

## 4. 시험 대비 체크리스트 ✅

1. 기본 개념
   - [ ] Minibatch의 개념 이해
   - [ ] Batch size가 미치는 영향 파악
   - [ ] Trade-off 관계 이해

2. 장단점 암기
   - [ ] Large batch 장점 3가지
   - [ ] Large batch 단점 3가지
   - [ ] Small batch 장점 3가지
   - [ ] Small batch 단점 3가지

3. 실제 적용
   - [ ] 상황별 적절한 batch size 선택
   - [ ] 하드웨어 제약 고려
   - [ ] 학습 목표에 따른 선택

## 5. 자주 나오는 시험 문제 유형 📚

1. 개념 설명형
   * "Minibatch 크기가 학습에 미치는 영향을 설명하시오"
   * "Batch size 선택의 중요성을 설명하시오"

2. 장단점 비교형
   * "Large/Small minibatch의 장단점을 비교하시오"
   * "Batch size에 따른 trade-off를 설명하시오"

3. 응용형
   * "주어진 상황에서 적절한 batch size를 선택하고 이유를 설명하시오"
   * "모델 학습 시 batch size 조정 전략을 설명하시오"
""")

# 사이드바에 학습 가이드 추가
st.sidebar.markdown("""
## 📚 학습 순서 가이드

1. 개념 이해하기
   * Minibatch의 의미
   * Batch size의 영향
   * Trade-off 관계

2. 장단점 암기하기
   * Large batch 특징
   * Small batch 특징
   * 실제 적용 사례

3. 답안 작성 연습
   * 구조화된 답안
   * 키워드 중심
   * 예시 활용

## 🎯 시험 직전 체크리스트

- [ ] 장단점 각각 3가지씩 암기
- [ ] Trade-off 관계 이해
- [ ] 실제 적용 사례 준비
- [ ] 모범 답안 작성 연습
""") 