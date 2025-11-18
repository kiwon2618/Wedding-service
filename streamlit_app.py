import streamlit as st
from datetime import date

st.set_page_config(page_title="영원파파 결혼식 축가·사회 의뢰", page_icon="💐", layout="centered")

# =========================================================
# CSS ONLY (HTML 없음)
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Gmarket+Sans:wght@700&family=Pretendard:wght@400;600;700&display=swap');

html, body, .stApp {
    background:#f9f5ef;
    font-family:Pretendard;
    display:flex;
    justify-content:center;
}

/* A4 카드 */
.a4-card {
    width:780px;
    min-height:1100px;
    background:rgba(255,255,255,0.94);
    border-radius:22px;
    padding:50px 55px 90px 55px;
    margin-top:40px;
    box-shadow:0 0 40px rgba(0,0,0,0.05);
    position:relative;
    overflow:hidden;
}

/* 금가루 에니메이션 */
@keyframes goldDust {
  0%{opacity:.07;transform:translateY(0) scale(1);}
  50%{opacity:.16;transform:translateY(-15px) scale(1.15);}
  100%{opacity:.07;transform:translateY(0) scale(1);}
}
.gold-dust {
    position:absolute;
    top:-60px; left:0;
    width:100%; height:260px;
    background-image:url('https://cdn.pixabay.com/photo/2015/01/08/18/25/gold-593119_1280.jpg');
    background-repeat:repeat-x;
    background-size:cover;
    opacity:0.08;
    animation:goldDust 5s infinite ease-in-out;
    pointer-events:none;
}

/* 꽃 패턴 */
.header-floral {
    width:100%; height:160px;
    background-image:url('https://cdn.pixabay.com/photo/2016/11/29/08/09/flower-1867614_1280.png');
    background-repeat:no-repeat;
    background-size:contain;
    background-position:center;
    opacity:0.25;
}

/* 금박 프레임 */
.header-frame {
    margin-top:20px;
    padding:45px 30px 35px 30px;
    border-radius:48px;
    backdrop-filter:blur(6px);
    border:6px solid;
    border-image:linear-gradient(135deg,#c4a46a,#ebdebe,#d6b680,#f7eed3,#c4a46a) 1;
    background:rgba(255,255,255,0.55);
    box-shadow:0 0 15px rgba(210,180,120,0.35), inset 0 0 22px rgba(250,230,200,0.35);
}

.wedding-img {
    width:260px; opacity:.62; display:block; margin:auto;
}

.title-main-kr {
    font-family:"Gmarket Sans";
    font-weight:900;
    font-size:2.9rem;
    text-align:center;
    color:#d36c87;
}
.title-main-en {
    text-align:center;
    margin-top:-10px;
    color:#8a6b6b;
    font-size:1.15rem;
}
.gold-line {
    width:55%; height:2px;
    background:linear-gradient(90deg,transparent,#d6b680,transparent);
    margin:18px auto;
}
.title-sub {
    font-family:"Gowun Batang";
    text-align:center;
    font-size:1.05rem;
    color:#9c8372;
    margin-top:12px;
}

.ribbon-box {text-align:center;margin-top:12px;opacity:0.9;}
</style>
""", unsafe_allow_html=True)



# =========================================================
# HTML HEADER (함수로 분리 → 공백 0)
# =========================================================
def render_header():
    st.markdown("""
<div class="header-frame">
    <img src="https://cdn.pixabay.com/photo/2016/06/05/19/02/just-married-1436861_1280.png" class="wedding-img">
    <div class="title-main-kr">영원파파</div>
    <div class="title-main-en">Wedding Ceremony with You</div>
    <div class="gold-line"></div>
    <div class="ribbon-box">
        <svg width="200" height="28" viewBox="0 0 300 60">
            <path d="M10 30 Q80 5 150 30 T290 30" stroke="url(#gold)" stroke-width="6" fill="none"/>
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
# A4 카드 시작 (→ 헤더/금가루 반드시 이 안에 넣어야 함)
# =========================================================
st.markdown('<div class="a4-card">', unsafe_allow_html=True)

st.markdown('<div class="gold-dust"></div>', unsafe_allow_html=True)
st.markdown('<div class="header-floral"></div>', unsafe_allow_html=True)

render_header()   # ← 이제 A4 카드 안에 표시됨 (핵심)



# =========================================================
# FORM
# =========================================================

st.markdown("### 🎤 의뢰 서비스 선택")
service = st.multiselect("", ["축가", "사회"], label_visibility="collapsed")

st.markdown("### 👰🤵 기본 정보")
role = st.radio("결혼식 주인공", ["신랑", "신부"])
name = st.text_input("이름")
age = st.number_input("만 나이", min_value=18, max_value=80)
wedding_date = st.date_input("예식일", value=date.today())

st.markdown("### 🏩 예식 정보")
venue = st.selectbox("예식 장소", ["호텔","하우스 웨딩","야외","컨벤션","기타"])
venue_address = st.text_input("예식장 주소")
mood = st.radio("예식 분위기", ["낭만적 💞","유쾌하게 😄","격식 있게 🎩"])

if "사회" in service:
    st.markdown("### 🎙️ 사회 스타일")
    host_style = st.radio("진행 스타일", ["담백·심플 (정석)", "센스 있고 위트 있게"])

if "축가" in service:
    st.markdown("### 🎵 축가 정보")
    song_pref = st.radio("원하는 곡이 있나요?", ["네, 있어요", "추천해주세요!"])
    if song_pref == "네, 있어요":
        custom_song = st.text_input("축가 곡명 입력")
    else:
        song_recommend = ['임영웅 - 이제 나만 믿어요','유해준 - 나에게 그대만이','윤종신 - 오르막길']
        custom_song = st.selectbox("추천 곡 선택", song_recommend)

st.markdown("### ✍️ 연락처 & 기타 요청사항")
col1, col2 = st.columns(2)
user_email = col1.text_input("📧 이메일")
user_phone = col2.text_input("📱 핸드폰 번호")

special_request = st.text_area("특이사항 / 기타 요청사항", height=120)

if st.button("💌 신청서 제출하기"):
    st.success("의뢰 신청이 완료되었습니다! 💐")

st.markdown("</div>", unsafe_allow_html=True)
