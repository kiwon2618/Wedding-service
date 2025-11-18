import streamlit as st
from datetime import date
import smtplib
from email.mime.text import MIMEText

st.set_page_config(page_title="영원파파 결혼식 축가·사회 의뢰", page_icon="💐", layout="centered")

# =========================================================
# CSS (들여쓰기 절대 금지)
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Gmarket+Sans:wght@700&family=Pretendard:wght@400;600;700&display=swap');

html, body, .stApp {
    background:#f8f4ed;
    font-family:Pretendard;
    overflow-x:hidden;
}

/* 메인 카드 */
.card {
    width:830px;
    background:rgba(255,255,255,0.93);
    border-radius:28px;
    padding:48px 55px 70px 55px;
    margin:0 auto;
    margin-top:40px;
    box-shadow:0 0 40px rgba(0,0,0,0.05);
    position:relative;
}

/* 배경 금가루 */
@keyframes goldDust {
  0%{opacity:.07; transform:translateY(0) scale(1);}
  50%{opacity:.16; transform:translateY(-18px) scale(1.15);}
  100%{opacity:.07; transform:translateY(0) scale(1);}
}
.gold-dust {
    position:absolute;
    top:-45px; left:0;
    width:100%; height:180px;
    background-image:url('https://cdn.pixabay.com/photo/2015/01/08/18/25/gold-593119_1280.jpg');
    background-repeat:repeat-x;
    background-size:cover;
    opacity:0.08;
    animation:goldDust 5s infinite ease-in-out;
}

/* 꽃 패턴 */
.header-floral {
    width:100%; height:120px;
    background-image:url('https://cdn.pixabay.com/photo/2016/11/29/08/09/flower-1867614_1280.png');
    background-repeat:no-repeat;
    background-size:contain;
    background-position:center;
    opacity:0.25;
}

/* 금박 프레임 */
.header-frame {
    padding:35px 30px 30px 30px;
    border-radius:42px;
    border:6px solid;
    border-image:linear-gradient(135deg,#c4a46a,#ebdebe,#d6b680,#f7eed3,#c4a46a) 1;
    background:rgba(255,255,255,0.58);
    box-shadow:0 0 18px rgba(210,180,120,0.35), inset 0 0 22px rgba(250,230,200,0.4);
}

/* 웨딩 이미지 */
.wedding-img {
    width:120px; opacity:.6; display:block; margin:auto;
}

/* 타이틀 */
.title-main-kr {
    font-family:"Gmarket Sans";
    text-align:center;
    font-weight:900;
    font-size:1.7rem;   
    color:#d36c87;
}
.title-main-en {
    text-align:center;
    margin-top:4px;
    color:#8a6b6b;
    font-size:1.65rem;
    font-weight:600;
}

.gold-line {
    width:55%; height:2px;
    background:linear-gradient(90deg,transparent,#d6b680,transparent);
    margin:18px auto;
}

.title-sub {
    font-family:"Gowun Batang";
    text-align:center;
    font-size:1.0rem;
    color:#9c8372;
}

/* 인스타 버튼 */
.insta-btn {
    font-size:1.3rem;
    font-family:Pretendard;
    font-weight:700;
    padding:18px 50px;
    background:linear-gradient(45deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888);
    color:white; border-radius:40px;
    text-decoration:none;
    box-shadow:0 6px 20px rgba(255,90,130,0.45);
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

<img src="https://cdn.pixabay.com/photo/2016/06/05/19/02/just-married-1436861_1280.png" class="wedding-img">

<div class="title-main-kr">영원파파</div>
<div class="title-main-en">Wedding Ceremony with You</div>

<div class="gold-line"></div>

<div style="text-align:center; margin-top:4px;">
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
# FORM AREA
# =========================================================
st.markdown("### 🎤 의뢰 서비스 선택")
service = st.multiselect("", ["축가", "사회"], label_visibility="collapsed")


st.markdown("### 👰🤵 기본 정보")
role = st.radio("결혼식 주인공", ["신랑", "신부"])
name = st.text_input("이름")
age = st.number_input("만 나이", 18, 80)
wedding_date = st.date_input("예식일", date.today())


st.markdown("### 🏩 예식 정보")
venue = st.selectbox("예식 장소", ["호텔","하우스 웨딩","야외","컨벤션","기타"])
venue_address = st.text_input("예식장 주소")
mood = st.radio("예식 분위기", ["낭만적 💞","유쾌하게 😄","격식 있게 🎩"])


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
    st.success("의뢰 신청이 완료되었습니다! 💐")



# =========================================================
# END CARD CLOSE
# =========================================================
st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# INSTAGRAM BUTTON
# =========================================================
st.markdown("""
<div style='text-align:center; margin-top:45px;'>
    <a class="insta-btn" href="https://www.instagram.com/0one.papa/" target="_blank">
        📸 Instagram @0one.papa
    </a>
</div>
""", unsafe_allow_html=True)
