import streamlit as st
from datetime import date
import smtplib
from email.mime.text import MIMEText

# ============================================================================================
#                                   🌸 페이지 설정
# ============================================================================================
st.set_page_config(page_title="영원파파 결혼식 축가·사회 의뢰", page_icon="💐", layout="centered")


# ============================================================================================
#                        🌸 웨딩 로고 이미지 (안정 URL)
# ============================================================================================
wedding_image = "https://cdn.pixabay.com/photo/2016/06/05/19/02/just-married-1436861_1280.png"

# 금박 리본 base64 SVG (고급 청첩장 느낌)
gold_ribbon = """
<svg width="200" height="28" viewBox="0 0 300 60" xmlns="http://www.w3.org/2000/svg">
<path d="M10 30 Q80 5 150 30 T290 30" stroke="url(#gold)" stroke-width="6" fill="none" />
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
"""


# ============================================================================================
#                          🌸 CSS – 청첩장급 프리미엄 금박 프레임
# ============================================================================================
st.markdown("""
<style>
@import url("https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Pretendard:wght@600;700&family=Gmarket+Sans:wght@700&display=swap");

body, .stApp {
    background-color: #f9f6f2;
    background-image:
        url('https://cdn.pixabay.com/photo/2017/03/30/12/40/background-2181508_1280.png'),
        url('https://cdn.pixabay.com/photo/2016/11/29/05/34/beige-1867744_1280.jpg');
    background-size: cover;
    background-repeat: repeat;
    background-blend-mode: lighten;
}

/* ------------------------------------------------------------------
   🔥 물결형 + 둥근 청첩장 금박 프레임
-------------------------------------------------------------------*/
.header-frame {
    width: 90%;
    margin: 40px auto 20px auto;
    padding: 45px 28px 35px 28px;

    border-radius: 48px / 38px;
    background: rgba(255,255,255,0.55);
    backdrop-filter: blur(6px);

    position: relative;

    /* Gold gradient border */
    border: 6px solid;
    border-image: linear-gradient(135deg,
                #c4a46a,
                #ebdebe,
                #d6b680,
                #f7eed3,
                #c4a46a) 1;

    /* 금박 노이즈 느낌 */
    box-shadow:
        0 0 15px rgba(210,180,120,0.35),
        inset 0 0 22px rgba(250,230,200,0.4);
}

/* 물결형 효과 */
.header-frame::before {
    content: "";
    position: absolute;
    inset: 0;
    border-radius: 48px / 38px;
    padding: 4px;
    background: repeating-linear-gradient(
        45deg,
        rgba(255,255,255,0.15),
        rgba(255,255,255,0.15) 3px,
        rgba(0,0,0,0) 3px,
        rgba(0,0,0,0) 6px
    );
    mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
}

/* 상단 장식 골드 아이콘 */
.header-frame:after,
.header-frame:before {
    pointer-events:none;
}

/* ------------------------------------------------------------------
   로고
-------------------------------------------------------------------*/
.wedding-img {
    width: 300px;
    opacity: 0.62;
    display: block;
    margin: auto;
}

/* ------------------------------------------------------------------
   텍스트
-------------------------------------------------------------------*/
.title-main-kr {
    font-family: "Gmarket Sans";
    font-size: 3.0rem;
    color: #d36c87;
    font-weight: 900;
    text-align: center;
}

.title-main-en {
    font-family: "Pretendard";
    font-size: 1.15rem;
    text-align: center;
    margin-top: -8px;
    color: #8a6b6b;
}

.title-sub {
    font-family: "Gowun Batang";
    font-size: 1.05rem;
    text-align: center;
    color: #9f8576;
    margin-top: 10px;
}

.gold-line {
    width: 55%;
    height: 2px;
    margin: 15px auto;
    background: linear-gradient(90deg, transparent, #d6b680, transparent);
}
</style>
""", unsafe_allow_html=True)



# ============================================================================================
#                                   🌸 상단 헤더 UI
# ============================================================================================
st.markdown(f"""
<div class="header-frame">
    <img src="{wedding_image}" class="wedding-img" />

    <div class="title-main-kr">영원파파</div>

    <div class="title-main-en">Wedding Ceremony with You</div>

    <div class="gold-line"></div>

    <!-- 금박 리본 삽입 -->
    <div style="text-align:center; margin-top:12px; opacity:0.9;">
        {gold_ribbon}
    </div>

    <p class="title-sub">Singing & Hosting Professional Service</p>
</div>
""", unsafe_allow_html=True)



# ============================================================================================
#                                   🌸 입력 폼
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


# 사회 선택 시
host_style = None
if "사회" in service:
    st.markdown("### 🎙️ 사회 스타일")
    host_style = st.radio("진행 스타일", ["담백·심플 (정석)", "센스 있고 위트 있게"])


# 축가 선택 시
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
            '유해준 - 나에게 그대만이 (탑현 ver.)',
            '윤종신 - 오르막길',
            '이석훈 - 그대를 사랑하는 10가지 이유',
            '김범수 - 오직 너만',
        ]
        custom_song = st.selectbox("추천 곡 선택", song_recommend_list)



# ============================================================================================
#                                   🌸 연락처
# ============================================================================================
st.markdown("### ✍️ 연락처 & 기타 요청사항")
col1, col2 = st.columns(2)
user_email = col1.text_input("📧 이메일")
user_phone = col2.text_input("📱 핸드폰 번호")

special_request = st.text_area("특이사항 / 기타 요청사항", height=120)


# ============================================================================================
#                                   🌸 제출
# ============================================================================================
if st.button("💌 신청서 제출하기"):
    st.success("의뢰 신청이 완료되었습니다! 💐")


# ============================================================================================
#                                   🌸 인스타 버튼
# ============================================================================================
st.markdown("""
<div style="text-align:center; margin-top:40px; margin-bottom:20px;">
    <a href="https://www.instagram.com/0one.papa/" target="_blank"
       style="
            font-size:1.3rem;
            font-family:Pretendard;
            font-weight:700;
            padding:18px 50px;
            background:linear-gradient(45deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888);
            color:white;
            border-radius:40px;
            text-decoration:none;
            box-shadow:0 6px 20px rgba(255,90,130,0.45);
        ">
        📸 Instagram @0one.papa
    </a>
</div>
""", unsafe_allow_html=True)
