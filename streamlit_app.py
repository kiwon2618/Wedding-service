import streamlit as st
from datetime import date
import smtplib
from email.mime.text import MIMEText

st.set_page_config(
    page_title="영원파파 결혼식 축가·사회 의뢰",
    page_icon="💐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CSS (들여쓰기 절대 금지)
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Gmarket+Sans:wght@700&family=Pretendard:wght@400;600;700&display=swap');

html, body, .stApp {
    background: #f8f4ed !important;
    font-family: "Pretendard", sans-serif !important;
    overflow-x: hidden !important;
}

/* Streamlit 기본 컨테이너 제거 */
.main .block-container {
    padding: 0 !important;
    max-width: 100% !important;
    margin: 0 !important;
}

/* 메인 카드 */
.card {
    width: 830px;
    max-width: 95%;
    background: rgba(255, 255, 255, 0.98);
    border-radius: 28px;
    padding: 48px 55px 70px 55px;
    margin: 0 auto;
    margin-top: 40px;
    margin-bottom: 40px;
    box-shadow: 
        0 0 50px rgba(0, 0, 0, 0.08),
        0 10px 60px rgba(0, 0, 0, 0.05),
        inset 0 1px 0 rgba(255, 255, 255, 0.9);
    position: relative;
    overflow: visible;
}

/* 카드 안의 모든 Streamlit 요소 - 흰색 배경 강제 적용 */
.card .element-container,
.card [data-testid],
.card .stMarkdown,
.card .stSelectbox,
.card .stTextInput,
.card .stNumberInput,
.card .stDateInput,
.card .stRadio,
.card .stMultiselect,
.card .stTextArea,
.card .stButton,
.card .stSuccess,
.card .stInfo,
.card .stError,
.card .stColumns {
    width: 100% !important;
    max-width: 100% !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
    background: transparent !important;
}

/* 모든 입력 필드와 선택 박스에 흰색 배경 적용 */
.card .stTextInput > div > div > input,
.card .stNumberInput > div > div > input,
.card .stTextArea > div > div > textarea,
.card .stSelectbox > div > div,
.card .stMultiselect > div > div {
    background: white !important;
}

/* 라디오 버튼과 체크박스 배경 */
.card .stRadio > div,
.card .stCheckbox > div {
    background: transparent !important;
}

/* 배경 금가루 */
@keyframes goldDust {
    0% { opacity: 0.07; transform: translateY(0) scale(1); }
    50% { opacity: 0.16; transform: translateY(-18px) scale(1.15); }
    100% { opacity: 0.07; transform: translateY(0) scale(1); }
}

.gold-dust {
    position: absolute;
    top: -45px;
    left: 0;
    width: 100%;
    height: 180px;
    background: linear-gradient(135deg, 
        rgba(214, 182, 128, 0.05),
        rgba(250, 230, 200, 0.08),
        rgba(214, 182, 128, 0.05));
    background-image: url('https://cdn.pixabay.com/photo/2015/01/08/18/25/gold-593119_1280.jpg');
    background-repeat: repeat-x;
    background-size: cover;
    opacity: 0.08;
    animation: goldDust 5s infinite ease-in-out;
    pointer-events: none;
    z-index: 1;
}

/* 꽃 패턴 */
.header-floral {
    width: 100%;
    height: 120px;
    background: radial-gradient(circle at 50% 50%, 
        rgba(214, 182, 128, 0.1) 0%,
        transparent 60%);
    background-image: url('https://cdn.pixabay.com/photo/2016/11/29/08/09/flower-1867614_1280.png');
    background-repeat: no-repeat;
    background-size: contain;
    background-position: center;
    opacity: 0.25;
    position: relative;
    z-index: 2;
    margin-top: -20px;
}

/* 금박 프레임 */
.header-frame {
    padding: 35px 30px 30px 30px;
    border-radius: 42px;
    border: 6px solid #d6b680;
    background: linear-gradient(135deg, 
        rgba(255, 255, 255, 0.65),
        rgba(250, 240, 230, 0.55),
        rgba(255, 255, 255, 0.65));
    box-shadow: 
        0 0 18px rgba(210, 180, 120, 0.35),
        inset 0 0 25px rgba(250, 240, 220, 0.45),
        inset 0 2px 10px rgba(255, 255, 255, 0.8);
    position: relative;
    z-index: 10;
    backdrop-filter: blur(8px);
}

/* 웨딩 이미지 */
.wedding-img {
    width: 140px;
    max-width: 100%;
    height: auto;
    opacity: 0.65;
    display: block;
    margin: 0 auto 15px auto;
    filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.1));
}

/* 타이틀 */
.title-main-kr {
    font-family: "Gmarket Sans", sans-serif;
    text-align: center;
    font-weight: 900;
    font-size: 2.1rem;
    color: #d36c87;
    margin: 10px 0 5px 0;
    text-shadow: 0 2px 4px rgba(211, 108, 135, 0.15);
    letter-spacing: -0.5px;
}

.title-main-en {
    text-align: center;
    margin-top: 4px;
    color: #8a6b6b;
    font-size: 1.15rem;
    font-weight: 600;
    font-family: "Pretendard", sans-serif;
    letter-spacing: 0.5px;
}

.gold-line {
    width: 55%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #d6b680, transparent);
    margin: 18px auto;
    box-shadow: 0 1px 3px rgba(214, 182, 128, 0.3);
}

.title-sub {
    font-family: "Gowun Batang", serif;
    text-align: center;
    font-size: 0.95rem;
    color: #9c8372;
    margin-top: 12px;
    letter-spacing: 0.3px;
}

/* Streamlit 요소 스타일링 */
.card h3 {
    font-family: "Pretendard", sans-serif;
    font-weight: 700;
    font-size: 1.2rem;
    color: #5a4a42;
    margin-top: 1.8rem;
    margin-bottom: 0.8rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid rgba(214, 182, 128, 0.2);
}

.card .stRadio > div > div > label,
.card .stCheckbox > label {
    font-family: "Pretendard", sans-serif;
    font-size: 1rem;
}

.card .stTextInput > div > div > input,
.card .stNumberInput > div > div > input,
.card .stTextArea > div > div > textarea {
    border: 2px solid rgba(214, 182, 128, 0.3) !important;
    border-radius: 8px !important;
    padding: 0.6rem !important;
    font-family: "Pretendard", sans-serif !important;
    transition: all 0.3s !important;
    background: white !important;
    background-color: white !important;
}

.card .stTextInput > div > div > input:focus,
.card .stNumberInput > div > div > input:focus,
.card .stTextArea > div > div > textarea:focus {
    border-color: #d6b680 !important;
    box-shadow: 0 0 0 3px rgba(214, 182, 128, 0.15) !important;
    outline: none !important;
    background: white !important;
    background-color: white !important;
}

.card .stButton > button {
    width: 100%;
    font-size: 1.15rem;
    padding: 0.85rem;
    border-radius: 12px;
    background: linear-gradient(135deg, #d36c87, #e6683c);
    color: white;
    border: none;
    font-weight: 700;
    font-family: "Pretendard", sans-serif;
    box-shadow: 
        0 4px 15px rgba(211, 108, 135, 0.4),
        0 2px 5px rgba(0, 0, 0, 0.1);
    transition: all 0.3s;
    margin-top: 1rem;
}

.card .stButton > button:hover {
    background: linear-gradient(135deg, #c55a7a, #d5572f);
    transform: translateY(-2px);
    box-shadow: 
        0 6px 20px rgba(211, 108, 135, 0.5),
        0 3px 8px rgba(0, 0, 0, 0.15);
}

.card .stSelectbox > div > div {
    border: 2px solid rgba(214, 182, 128, 0.3) !important;
    border-radius: 8px !important;
    transition: all 0.3s !important;
    background: white !important;
    background-color: white !important;
}

.card .stSelectbox > div > div:hover {
    border-color: #d6b680 !important;
    background: white !important;
    background-color: white !important;
}

.card .stMultiselect > div > div {
    border: 2px solid rgba(214, 182, 128, 0.3) !important;
    border-radius: 8px !important;
    background: white !important;
    background-color: white !important;
}

.card .stDateInput > div > div > input {
    background: white !important;
    background-color: white !important;
    border: 2px solid rgba(214, 182, 128, 0.3) !important;
    border-radius: 8px !important;
}

/* 인스타 버튼 */
.insta-btn {
    font-size: 1.3rem;
    font-family: "Pretendard", sans-serif;
    font-weight: 700;
    padding: 18px 50px;
    background: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);
    color: white;
    border-radius: 40px;
    text-decoration: none;
    box-shadow: 0 6px 20px rgba(255, 90, 130, 0.45);
    display: inline-block;
    transition: all 0.3s;
}

.insta-btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(255, 90, 130, 0.6);
    text-decoration: none;
    color: white;
}

/* 성공/에러 메시지 스타일 */
.card .stSuccess,
.card .stInfo,
.card .stError {
    border-radius: 10px;
    padding: 1rem;
    margin-top: 1rem;
    border-left: 4px solid;
}

.card .stSuccess {
    background: rgba(76, 175, 80, 0.1);
    border-color: #4caf50;
}

.card .stInfo {
    background: rgba(33, 150, 243, 0.1);
    border-color: #2196f3;
}

.card .stError {
    background: rgba(244, 67, 54, 0.1);
    border-color: #f44336;
}

/* 반응형 디자인 */
@media (max-width: 900px) {
    .card {
        width: 95%;
        padding: 35px 30px 50px 30px;
    }
    
    .title-main-kr {
        font-size: 1.7rem;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER (HTML 공백 없이 바로 시작)
# =========================================================
st.markdown("""
<div class="card">
    <div class="gold-dust"></div>
    <div class="header-floral"></div>
    <div class="header-frame">
        <img src="https://cdn.pixabay.com/photo/2016/06/05/19/02/just-married-1436861_1280.png" 
             class="wedding-img"
             alt="Wedding"
             onerror="this.onerror=null; this.src='data:image/svg+xml,%3Csvg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'140\\' height=\\'100\\' viewBox=\\'0 0 140 100\\'%3E%3Crect fill=\\'%23f0e6d2\\' width=\\'140\\' height=\\'100\\'/%3E%3Ctext x=\\'50%25\\' y=\\'50%25\\' font-family=\\'Arial\\' font-size=\\'14\\' fill=\\'%23d6b680\\' text-anchor=\\'middle\\' dominant-baseline=\\'middle\\'%3E💒%3C/text%3E%3C/svg%3E';">
        <div class="title-main-kr">영원파파</div>
        <div class="title-main-en">Wedding Ceremony with You</div>
        <div class="gold-line"></div>
        <div style="text-align:center; margin-top:8px;">
            <svg width="200" height="28" viewBox="0 0 300 60">
                <path d="M10 30 Q80 5 150 30 T290 30" 
                      stroke="url(#gold)" 
                      stroke-width="6" 
                      fill="none"
                      stroke-linecap="round"/>
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
""", unsafe_allow_html=True)

# =========================================================
# FORM AREA
# =========================================================
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

# 사회
host_style = None
if "사회" in service:
    st.markdown("### 🎙️ 사회 스타일")
    host_style = st.radio("진행 스타일", ["담백·정석", "센스 있고 위트 있게"])

# 축가
song_pref = None
custom_song = None
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

if "축가" in service:
    st.markdown("### 🎵 축가 정보")
    song_pref = st.radio("원하는 곡이 있나요?", ["네, 있어요", "추천해주세요!"])
    
    if song_pref == "네, 있어요":
        custom_song = st.text_input("축가 곡명 입력")
    else:
        custom_song = st.selectbox("추천 곡 선택", song_recommend_list)

# 연락처
st.markdown("### ✍️ 연락처 & 기타 요청사항")
col1, col2 = st.columns(2)
user_email = col1.text_input("📧 이메일")
user_phone = col2.text_input("📱 핸드폰 번호")

special_request = st.text_area("특이사항 / 기타 요청사항", height=120)

# =========================================================
# SUBMIT BUTTON
# =========================================================
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

# =========================================================
# END CARD CLOSE
# =========================================================
st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# INSTAGRAM BUTTON
# =========================================================
st.markdown("""
<div style='text-align:center; margin-top:45px; margin-bottom:30px;'>
    <a class="insta-btn" href="https://www.instagram.com/0one.papa/" target="_blank">
        📸 Instagram @0one.papa
    </a>
</div>
""", unsafe_allow_html=True)
