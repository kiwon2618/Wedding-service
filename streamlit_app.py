import streamlit as st
from datetime import date
import smtplib
from email.mime.text import MIMEText

# ============================================================================================
#                                   🌸 페이지 설정
# ============================================================================================
st.set_page_config(
    page_title="영원파파 결혼식 축가·사회 의뢰",
    page_icon="💐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================================================
#                         🌸 A4 청첩장 레이아웃 + 배경 애니메이션 CSS
# ============================================================================================
st.markdown("""
<style>
/* 기본 폰트 */
@import url("https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Pretendard:wght@600;700&family=Gmarket+Sans:wght@700&display=swap");

/* ========================================
   📄 A4 청첩장 비율 중앙 레이아웃
======================================== */
html, body {
    background: #f9f5ef !important;
    font-family: "Pretendard", sans-serif;
}

.stApp {
    background: #f9f5ef !important;
    padding: 20px 0 !important;
    display: flex !important;
    justify-content: center !important;
    align-items: flex-start !important;
}

/* Streamlit 메인 컨테이너 */
.main .block-container {
    padding: 0 !important;
    max-width: 100% !important;
    margin: 0 !important;
}

/* A4 카드 래퍼 */
.a4-card-wrapper {
    width: 780px;
    margin: 20px auto;
    padding: 0;
    position: relative;
}

/* A4 비율 박스 */
.a4-card {
    width: 100%;
    min-height: 1100px;
    padding: 40px 50px 80px 50px;
    margin: 0;
    border-radius: 22px;
    background: rgba(255, 255, 255, 0.87);
    box-shadow:
        0 0 40px rgba(0,0,0,0.05),
        0 0 80px rgba(0,0,0,0.04);
    position: relative;
    overflow: visible;
    display: block;
    box-sizing: border-box;
}

/* A4 카드 안의 모든 Streamlit 요소 */
.a4-card-wrapper .element-container,
.a4-card-wrapper [data-testid],
.a4-card-wrapper .stMarkdown {
    width: 100% !important;
    max-width: 100% !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    padding: 0 !important;
}

/* Streamlit 기본 블록 스타일 제거 및 통일 */
.a4-card-wrapper > div {
    width: 100% !important;
    max-width: 100% !important;
}

/* Streamlit 섹션 간격 조정 */
.a4-card-wrapper .element-container {
    margin-bottom: 1rem !important;
}

/* ========================================
   ✨ 배경 금가루 애니메이션
======================================== */
@keyframes goldDust {
  0%   { opacity: 0.05; transform: translateY(0px) scale(1); }
  50%  { opacity: 0.18; transform: translateY(-14px) scale(1.2); }
  100% { opacity: 0.05; transform: translateY(0px) scale(1); }
}

.gold-dust {
    position: absolute;
    top: -60px;
    left: 0;
    width: 100%;
    height: 260px;
    background-image: url('https://cdn.pixabay.com/photo/2015/01/08/18/25/gold-593119_1280.jpg');
    background-size: cover;
    background-repeat: repeat-x;
    opacity: 0.07;
    animation: goldDust 5s ease-in-out infinite;
    pointer-events: none;
    z-index: 1;
}

/* ========================================
   🌸 헤더 꽃 패턴 텍스처 (Soft Floral)
======================================== */
.header-floral {
    width: 100%;
    height: 160px;
    background-image: url('https://cdn.pixabay.com/photo/2016/11/29/08/09/flower-1867614_1280.png');
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center top;
    opacity: 0.26;
    margin-top: -20px;
    position: relative;
    z-index: 2;
}

/* ========================================
   🎀 상단 금박 곡선 프레임
======================================== */
.header-frame {
    width: 100%;
    margin: 35px auto 20px auto;
    padding: 45px 28px 35px 28px;
    border-radius: 48px / 38px;
    background: rgba(255,255,255,0.55);
    backdrop-filter: blur(6px);
    border: 6px solid #d6b680;
    box-shadow:
       0 0 15px rgba(210,180,120,0.35),
       inset 0 0 22px rgba(250,230,200,0.35);
    position: relative;
    z-index: 10;
}

/* 금박 리본 */
.ribbon-box { 
    text-align: center; 
    margin-top: 12px; 
    opacity: 0.9; 
}

.wedding-img {
    width: 280px;
    max-width: 100%;
    height: auto;
    opacity: 0.62;
    margin: auto;
    display: block;
}

/* ========================================
   📝 텍스트 스타일
======================================== */
.title-main-kr {
    font-family: "Gmarket Sans", sans-serif;
    font-size: 2.95rem;
    font-weight: 900;
    text-align: center;
    color: #d36c87;
    margin: 15px 0;
}

.title-main-en {
    font-family: "Pretendard", sans-serif;
    font-size: 1.2rem;
    text-align: center;
    margin-top: -10px;
    color: #8a6b6b;
}

.title-sub {
    font-family: "Gowun Batang", serif;
    font-size: 1.08rem;
    text-align: center;
    margin-top: 10px;
    color: #9f8576;
}

.gold-line {
    width: 55%;
    height: 2px;
    margin: 15px auto;
    background: linear-gradient(90deg, transparent, #d6b680, transparent);
}

/* Streamlit 기본 요소 스타일 조정 */
.a4-card .stSelectbox, 
.a4-card .stTextInput, 
.a4-card .stNumberInput, 
.a4-card .stDateInput, 
.a4-card .stRadio, 
.a4-card .stMultiselect, 
.a4-card .stTextArea {
    margin-bottom: 1rem;
    width: 100%;
}

.a4-card .stButton>button {
    width: 100%;
    font-size: 1.1rem;
    padding: 0.75rem;
    border-radius: 10px;
    background: linear-gradient(135deg, #d36c87, #e6683c);
    color: white;
    border: none;
    font-weight: 700;
}

.a4-card .stButton>button:hover {
    background: linear-gradient(135deg, #c55a7a, #d5572f);
    transform: scale(1.02);
    transition: all 0.3s;
}

/* Streamlit 요소가 카드 밖으로 나가지 않도록 */
.a4-card .element-container {
    max-width: 100% !important;
    padding: 0 !important;
}

.a4-card h3 {
    margin-top: 1.5rem;
    margin-bottom: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# ============================================================================================
#                          🌸 A4 카드 컨테이너 시작
# ============================================================================================
# Streamlit 컨테이너 사용
with st.container():
    # A4 카드 래퍼 시작
    st.markdown('<div class="a4-card-wrapper">', unsafe_allow_html=True)
    
    # 금가루 배경과 꽃 무늬를 포함한 전체 카드 시작
    st.markdown("""
    <div class="a4-card">
        <div class="gold-dust"></div>
        <div class="header-floral"></div>
    """, unsafe_allow_html=True)

    # ============================================================================================
    #                           🌸 헤더 금박 영역
    # ============================================================================================
    header_html = """
    <div class="header-frame">
        <img src="https://cdn.pixabay.com/photo/2016/06/05/19/02/just-married-1436861_1280.png"
             class="wedding-img"
             alt="Wedding Illustration">
        
        <div class="title-main-kr">영원파파</div>
        <div class="title-main-en">Wedding Ceremony with You</div>
        
        <div class="gold-line"></div>
        
        <div class="ribbon-box">
            <svg width="200" height="28" viewBox="0 0 300 60">
                <path d="M10 30 Q80 5 150 30 T290 30" 
                      stroke="url(#gold)" 
                      stroke-width="6" 
                      fill="none" />
                <defs>
                    <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" stop-color="#c9a667"/>
                        <stop offset="25%" stop-color="#f3e6c0"/>
                        <stop offset="50%" stop-color="#d8b98b"/>
                        <stop offset="75%" stop-color="#f3e6c0"/>
                        <stop offset="100%" stop-color="#c9a667"/>
                    </linearGradient>
                </defs>
            </svg>
        </div>
        
        <p class="title-sub">Singing & Hosting Professional Service</p>
    </div>
    """
    
    st.markdown(header_html, unsafe_allow_html=True)
    
    # ============================================================================================
    #                                   🌸 아래부터 기존 폼
    # ============================================================================================
    st.markdown("### 🎤 의뢰 서비스 선택")
    service = st.multiselect("", ["축가", "사회"], label_visibility="collapsed")
    
    st.markdown("### 👰🤵 기본 정보")
    role = st.radio("결혼식 주인공", ["신랑", "신부"])
    name = st.text_input("이름")
    age = st.number_input("만 나이", min_value=18, max_value=80)
    wedding_date = st.date_input("예식일", value=date.today())
    
    st.markdown("### 🏩 예식 정보")
    venue = st.selectbox("예식 장소", ["호텔", "하우스 웨딩", "야외", "컨벤션", "기타"])
    venue_address = st.text_input("예식장 주소")
    mood = st.radio("예식 분위기", ["낭만적 💞", "유쾌하게 😄", "격식 있게 🎩"])
    
    # 사회 선택 시 추가
    host_style = None
    if "사회" in service:
        st.markdown("### 🎙️ 사회 스타일")
        host_style = st.radio("진행 스타일", ["담백·심플 (정석)", "센스 있고 위트 있게"])
    
    # 축가 선택 시 추가
    song_pref = None
    custom_song = None
    if "축가" in service:
        st.markdown("### 🎵 축가 정보")
        song_pref = st.radio("원하는 곡이 있나요?", ["네, 있어요", "추천해주세요!"])
        
        if song_pref == "네, 있어요":
            custom_song = st.text_input("축가 곡명 입력")
        else:
            song_recommend_list = [
                '임영웅 - 이제 나만 믿어요',
                '유해준 - 나에게 그대만이 (탑현 ver. 가능)',
                '윤종신 - 오르막길',
                '이석훈 - 그대를 사랑하는 10가지 이유',
                '이준호 - 넌',
                '허각 - 언제나',
                '허각 - 물론',
                '정승환 - 사뿐',
                '유리상자 - 신부에게',
                '김범수 - 사랑의 시작은 고백에서부터 (전상근 ver. 가능)',
                '김범수 - 오직 너만',
                '한동근 - 그대라는 사치',
                '윤종신 - 그대 없이는 못살아 (늦가을 ver.)'
            ]
            custom_song = st.selectbox("추천 곡 선택", song_recommend_list)
    
    st.markdown("### ✍️ 연락처 & 기타 요청사항")
    col1, col2 = st.columns(2)
    user_email = col1.text_input("📧 이메일")
    user_phone = col2.text_input("📱 핸드폰 번호")
    
    special_request = st.text_area("특이사항 / 기타 요청사항", height=120)
    
    # ============================================================================================
    #                                   🌸 제출 버튼
    # ============================================================================================
    if st.button("💌 신청서 제출하기"):
        # 유효성 검사
        if not service:
            st.error("⚠️ 의뢰 서비스를 선택해주세요.")
        elif not name:
            st.error("⚠️ 이름을 입력해주세요.")
        elif not user_email and not user_phone:
            st.error("⚠️ 연락처를 최소 하나는 입력해주세요.")
        else:
            st.success("✅ 의뢰 신청이 완료되었습니다! 💐")
            st.info(f"""
            📋 신청 내용 요약:
            - 서비스: {', '.join(service)}
            - 주인공: {role} {name} ({age}세)
            - 예식일: {wedding_date.strftime('%Y년 %m월 %d일')}
            - 장소: {venue} ({venue_address if venue_address else '미입력'})
            - 분위기: {mood}
            """)
            
            if host_style:
                st.info(f"🎙️ 사회 스타일: {host_style}")
            
            if custom_song:
                st.info(f"🎵 선택한 곡: {custom_song}")
    
    # ============================================================================================
    #                                   🌸 인스타 버튼
    # ============================================================================================
    st.markdown("""
    <div style="text-align:center; margin-top:40px; padding-bottom: 20px;">
        <a href="https://www.instagram.com/0one.papa/" 
           target="_blank"
           style="
                font-size:1.3rem;
                font-family:'Pretendard', sans-serif;
                font-weight:700;
                padding:18px 50px;
                background:linear-gradient(45deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888);
                color:white;
                border-radius:40px;
                text-decoration:none;
                box-shadow:0 6px 20px rgba(255,90,130,0.45);
                display:inline-block;
                transition: transform 0.3s;
            ">
            📸 Instagram @0one.papa
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # A4 카드 닫기
    st.markdown("""
        </div>
    </div>
    </div>
    """, unsafe_allow_html=True)
