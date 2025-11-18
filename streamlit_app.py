import streamlit as st
from datetime import date

st.set_page_config(page_title="영원파파 결혼식 축가·사회 의뢰", page_icon="💐", layout="centered")

# =========================================================
# CSS + HEADER (절대 공백 넣지 마세요)
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Gmarket+Sans:wght@700&family=Pretendard:wght@400;600;700&display=swap');

html, body, .stApp {
    background:#f6f2ea;
    font-family:Pretendard;
    overflow-x:hidden;
}

/* --- 웨딩북 커버 효과 --- */
.weddingbook-wrapper {
    width:100%;
    padding:55px 0 80px 0;
    background:linear-gradient(135deg,#f8f5ef,#f3ede4,#faf7f0);
    box-shadow:inset 0 0 60px rgba(160,130,90,0.15);
}

/* 중앙 페이지 카드 */
.card {
    width:850px;
    max-width:92%;
    background:rgba(255,255,255,0.88);
    border-radius:34px;
    padding:55px 60px 80px 60px;
    margin:40px auto;
    box-shadow:
        0 0 40px rgba(200,170,110,0.28),
        inset 0 0 12px rgba(255,240,210,0.4);
    backdrop-filter:blur(5px);
}

/* 금박 테두리 */
.header-frame {
    padding:40px 25px;
    border-radius:45px;
    border:7px solid;
    border-image:linear-gradient(135deg,#bfa163,#f6e7c6,#d3b277,#f8efdc,#b99855) 1;
    background:rgba(255,255,255,0.65);
    box-shadow:
        0 0 20px rgba(250,225,160,0.55),
        0 0 40px rgba(255,230,180,0.4),
        inset 0 0 18px rgba(250,230,200,0.45);
}

/* 플로럴 */
.header-floral {
    width:100%; height:110px;
    background-image:url('https://cdn.pixabay.com/photo/2016/11/29/08/09/flower-1867614_1280.png');
    background-repeat:no-repeat;
    background-position:center;
    background-size:260px;
    opacity:0.22;
    margin-bottom:18px;
}

/* 금박 텍스트 */
.title-main-kr {
    font-family:"Gmarket Sans";
    font-size:1.4rem;
    text-align:center;
    font-weight:900;
    background:linear-gradient(90deg,#d7b77f,#f6e9ca,#c6a566,#f6e9ca,#e0c48c);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    text-shadow:
        0px 0px 6px rgba(240,210,150,0.8),
        1px 1px 2px rgba(160,120,70,0.3);
}

.title-main-en {
    margin-top:6px;
    text-align:center;
    font-size:2.2rem;
    font-weight:800;
    background:linear-gradient(90deg,#c8a46a,#f0e3c4,#b89457,#f0e3c4);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    text-shadow:
        0px 0px 8px rgba(255,230,180,0.7),
        1px 1px 3px rgba(150,120,80,0.35);
}

/* 금박 리본 */
.gold-line {width:60%; height:2px; background:linear-gradient(90deg,transparent,#caa86e,transparent); margin:22px auto;}
.ribbon-box svg {filter:drop-shadow(0px 0px 6px rgba(210,180,120,0.55));}

.title-sub {
    text-align:center;
    font-family:"Gowun Batang";
    font-size:1.1rem;
    color:#937d6b;
    margin-top:8px;
}

/* --- 금박 구분선 + 아이콘 --- */
.icon-section {
    text-align:center;
    margin-top:55px;
    margin-bottom:15px;
}
.icon-section svg {
    width:42px;
    margin:0 25px;
    filter:drop-shadow(0 0 6px rgba(180,150,90,0.6));
}

/* 금박 구분선 */
.gold-divider {
    width:70%;
    height:4px;
    margin:20px auto 45px auto;
    background:linear-gradient(90deg,transparent,#d3b780,#f4e6c3,#d3b780,transparent);
    border-radius:3px;
}


/* --- 추천곡 금박 스타일 --- */
.recommend-box {
    width:85%;
    margin:0 auto 40px auto;
    padding:30px 35px;
    background:rgba(255,255,255,0.85);
    border-radius:22px;
    border:4px solid;
    border-image:linear-gradient(135deg,#c9a467,#f5e7c8,#b99656) 1;
    box-shadow:0 0 25px rgba(200,170,110,0.25), inset 0 0 12px rgba(255,240,210,0.4);
}
.recommend-title {
    text-align:center;
    font-family:"Gmarket Sans";
    font-size:1.6rem;
    margin-bottom:15px;
    background:linear-gradient(90deg,#d1b27a,#f3e4c3,#b89457);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}
.song-item {
    padding:10px 0;
    font-size:1.1rem;
    border-bottom:1px solid #e8dcc7;
}
.song-item:last-child {border-bottom:none;}
.song-item:hover {
    color:#b38a4c;
    transform:translateX(6px);
    transition:0.25s;
}

/* 모바일 */
@media(max-width:600px) {
    .card {padding:35px 22px;}
    .title-main-en {font-size:1.65rem;}
    .icon-section svg {width:34px; margin:0 16px;}
    .recommend-box {padding:22px;}
    .song-item {font-size:0.95rem;}
}
</style>



<div class="weddingbook-wrapper">

    <div class="card">

        <div class="header-floral"></div>

        <div class="header-frame">
            <div class="title-main-kr">영원파파</div>
            <div class="title-main-en">Wedding Ceremony with You</div>
            <div class="gold-line"></div>

            <div class="ribbon-box" style="text-align:center;">
                <svg width="200" height="28" viewBox="0 0 300 60">
                    <path d="M10 30 Q80 5 150 30 T290 30"
                          stroke="url(#gold)" stroke-width="6" fill="none"/>
                    <defs>
                        <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="0%">
                            <stop offset="0%" stop-color="#c9a667"/>
                            <stop offset="25%" stop-color="#f5dfb3"/>
                            <stop offset="50%" stop-color="#d3b17f"/>
                            <stop offset="75%" stop-color="#f5dfb3"/>
                            <stop offset="100%" stop-color="#c9a667"/>
                        </linearGradient>
                    </defs>
                </svg>
            </div>

            <p class="title-sub">
                Singing & Hosting Professional Service
            </p>
        </div>

        <!-- 금박 아이콘 + 구분선 -->
        <div class="icon-section">
            <!-- 반지 -->
            <svg fill="url(#gold)" viewBox="0 0 24 24">
                <path d="M12 2l3 3-3 3-3-3 3-3zm0 6a7 7 0 110 14 7 7 0 010-14zm0 2a5 5 0 100 10 5 5 0 000-10z"/>
            </svg>

            <!-- 하트 -->
            <svg fill="url(#gold)" viewBox="0 0 24 24">
                <path d="M12 21s-7-4.3-7-10a5 5 0 019-3 5 5 0 019 3c0 5.7-7 10-7 10z"/>
            </svg>

            <!-- 마이크 -->
            <svg fill="url(#gold)" viewBox="0 0 24 24">
                <path d="M12 14a3 3 0 003-3V5a3 3 0 00-6 0v6a3 3 0 003 3zm5-3a5 5 0 01-10 0H5a7 7 0 0014 0h-2z"/>
            </svg>
        </div>

        <div class="gold-divider"></div>

        <!-- 추천곡 -->
        <div class="recommend-box">
            <div class="recommend-title">✨ 축가 추천곡 리스트</div>

            <div class="song-item">임영웅 – 이제 나만 믿어요</div>
            <div class="song-item">유해준 – 나에게 그대만이 (탑현 ver.)</div>
            <div class="song-item">윤종신 – 오르막길</div>
            <div class="song-item">이석훈 – 그대를 사랑하는 10가지 이유</div>
            <div class="song-item">이준호 – 넌</div>
            <div class="song-item">허각 – 언제나</div>
            <div class="song-item">허각 – 물론</div>
            <div class="song-item">정승환 – 사뿐</div>
            <div class="song-item">유리상자 – 신부에게</div>
            <div class="song-item">김범수 – 사랑의 시작은 고백에서부터 (전상근 ver.)</div>
            <div class="song-item">김범수 – 오직 너만</div>
            <div class="song-item">한동근 – 그대라는 사치</div>
            <div class="song-item">윤종신 – 그대 없이는 못살아 (늦가을 ver.)</div>
        </div>

    </div>
</div>
""", unsafe_allow_html=True)



# =========================================================
# FORM 영역
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

host_style = None
if "사회" in service:
    st.markdown("### 🎙️ 사회 스타일")
    host_style = st.radio("진행 스타일", ["담백·정석","센스 있고 위트 있게"])

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

st.markdown("### ✍️ 연락처 & 기타 요청사항")
col1, col2 = st.columns(2)
user_email = col1.text_input("📧 이메일")
user_phone = col2.text_input("📱 핸드폰 번호")
special_request = st.text_area("특이사항 / 기타 요청사항", height=120)

# =========================================================
# END CARD
# =========================================================
st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# INSTAGRAM
# =========================================================
st.markdown("""
<div style='text-align:center; margin-top:45px;'>
<a class="insta-btn" href="https://www.instagram.com/0one.papa/" target="_blank">
📸 Instagram @0one.papa
</a>
</div>
""", unsafe_allow_html=True)
