import streamlit as st

def init_page():
    # 페이지 설정 (반드시 첫 번째 Streamlit 명령어여야 함)
    st.set_page_config(
        page_title="인공지능수학 기말고사 대비 학습 플랫폼",
        page_icon="📚",
        layout="wide"
    )
    page = st.Page("app.py", title="인공지능수학", icon="🏠")
    page1 = st.Page("pages/1_베이즈정리.py", title="베이즈정리", icon="🏠")
    page2 = st.Page("pages/2_조건부확률과_주변확률.py", title="조건부확률과 주변확률", icon="🏠")
    page3 = st.Page("pages/3_다변수함수_연쇄법칙.py", title="다변수함수 연쇄법칙", icon="🏠")
    page4 = st.Page("pages/4_정규분포_난수생성.py", title="정규분포 난수생성", icon="🏠")
    page5 = st.Page("pages/5_테일러급수_설명.py", title="테일러급수", icon="🏠")
    page6 = st.Page("pages/6_확률변수의_독립.py", title="확률변수의 독립", icon="🏠")
    page7 = st.Page("pages/7_공액성_Conjugacy.py", title="Conjugacy(공액성)", icon="🏠")
    page8 = st.Page("pages/8_충분통계량.py", title="충분통계량", icon="🏠")
    page9 = st.Page("pages/9_그래디언트_계산.py", title="그레이디언트 계산", icon="🏠")
    page10 = st.Page("pages/10_Minibatch_크기의_장단점.py", title="Minibatch_크기의_장단점", icon="🏠")


    pg = st.navigation([page1, page2, page3, page4, page5, page6, page7, page8, page9, page10])
    pg.run()
    st.sidebar.caption("Made with ❤️ for 이성민")
    main()

def main():
    st.title("수학 시험 대비 학습 플랫폼 🎓")
    
    st.markdown("""
    ## 👋 환영합니다!
    
    이 플랫폼은 수학 시험 준비를 위한 다양한 개념과 문제 풀이를 제공합니다.
    
    ### 📚 학습 가능한 주제들:
    
    1. **베이즈 정리와 조건부 확률**
       - 베이즈 정리 예제
       - 조건부확률과 주변확률
    
    2. **다변수 함수와 미적분**
       - 다변수함수 연쇄법칙
       - 테일러 급수
    
    3. **확률과 통계**
       - 정규분포와 난수생성
       - 충분통계량
       - 공액성
    
    4. **머신러닝 기초**
       - Minibatch 크기의 장단점
       - Gradient 계산
    
    ### 💡 사용 방법
    
    1. 왼쪽 사이드바의 페이지 목록에서 학습하고 싶은 주제를 선택하세요.
    2. 각 페이지에서 개념 설명, 예제, 시험 문제 풀이를 확인할 수 있습니다.
    3. 체크리스트를 활용하여 학습 진도를 관리하세요.
    
    ### ✨ 특징
    
    - 실제 시험에 나오는 문제 유형 제공
    - 상세한 개념 설명과 풀이 과정
    - 시험 대비 체크리스트
    - 효율적인 학습 가이드
    """)

if __name__ == "__main__":
    init_page()