import streamlit as st
from datetime import date
import smtplib
from email.mime.text import MIMEText

st.set_page_config(page_title="영원파파 결혼식 서비스", layout="centered")

# ================================================================================================
#                                       🎨  HTML + CSS 풀디자인
# ================================================================================================

HTML_HEADER = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Gmarket+Sans:wght@700&family=Pretendard:wght@400;600;700&display=swap');

html, body, .stApp {
    background:#f6f2ea;
    margin:0;
    padding:0;
    font-family:Pretendard;
    overflow-x:hidden;
}

.weddingbook-wrapper {
    width:100%;
    padding:40px 0 30px 0;
    background:linear-gradient(135deg,#f9f6f0,#f4eee6,#faf7f3);
    box-shadow:inset 0 0 50px rgba(160,130,90,0.15);
}

.card {
    width:850px;
    max-width:92%;
    padding:45px 55px 40px 55px;
    margin:0px auto 40px auto;
    background:rgba(255,255,255,0.90);
    border-radius:32px;
    backdrop-filter:blur(5px);
    box-shadow:0 0 40px rgba(200,170,110,0.25), inset 0 0 12px rgba(255,240,210,0.35);
}

.header-frame {
    padding:35px 20px;
    border-radius:40px;
    border:7px solid;
    border-image:linear-gradient(135deg,#bf9f63,#f6e9c8,#d6b67a,#f3e6c8,#b99151) 1;
    background:rgba(255,255,255,0.65);
    box-shadow:
        0 0 20px rgba(250,225,160,0.45),
        inset 0 0 18px rgba(245,220,180,0.40);
}

.header-floral {
    width:100%;
    height:100px;
    background-image:url('https://cdn.pixabay.com/photo/2016/11/29/08/09/flower-1867614_1280.png');
    background-repeat:no-repeat;
    background-position:center;
    background-size:240px;
    opacity:0.18;
    margin-bottom:15px;
}

.title-main-kr {
    font-family:"Gmarket Sans";
    font-size:1.45rem;
    text-align:center;
    font-weight:900;
    background:linear-gradient(90deg,#d1b06a,#f6e6c8,#c19b59,#f6e6c8,#d1b06a);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.title-main-en {
    text-align:center;
    font-size:2.2rem;
    font-weight:800;
    background:linear-gradient(90deg,#c8a266,#f0e4c2,#b78c4e,#f0e4c2,#c8a266);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.gold-line {
    width:60%;
    margin:20px auto;
    height:2px;
    background:linear-gradient(90deg,transparent,#cbaa72,transparent);
}

.title-sub {
    text-align:center;
    font-family:"Gowun Batang";
    font-size:1.15rem;
    color:#907b68;
}

/* 아이콘 */
.icon-section {
    text-align:center;
    margin-top:40px;
}
.icon-section svg {
    width:40px;
    margin:0 22px;
    filter:drop-shadow(0 0 6px rgba(185,150,95,0.45));
}

/* 구분선 */
.gold-divider {
    width:70%;
    height:4px;
    margin:35px auto;
    background:linear-gradient(90deg,transparent,#d2b67e,#f4e6c4,#d2b67e,transparent);
    border-radius:3px;
}

/* 추천곡 박스 */
.recommend-box {
    width:85%;
    margin:0 auto 40px auto;
    padding:28px 35px;
    background:rgba(255,255,255,0.90);
    border-radius:22px;
    border:4px solid;
    border-image:linear-gradient(135deg,#c9a564,#f3e6c5,#b89152) 1;
}
.recommend-title {
    text-align:center;
    font-family:"Gmarket Sans";
    font-size:1.55rem;
    margin-bottom:18px;
    background:linear-gradient(90deg,#d1b27a,#f3e4c3,#b89457);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}
.song-item {
    padding:10px 0;
    font-size:1.05rem;
    border-bottom:1px solid #e8dcc7;
}
.song-item:last-child {border-bottom:none;}
.song-item:hover {
    color:#b48b4f;
    transform:translateX(6px);
    transition:0.25s;
}

/* 모바일 */
@media(max-width:600px) {
    .card {padding:35px 20px;}
    .title-main-en {font-size:1.65rem;}
    .recommend-box {padding:22px;}
}
</style>

<div class="weddingbook-wrapper">
    <div class="card">

        <div class="header-floral"></div>

        <div class="header-frame">
            <div class="title-main-kr">영원파파</div>
            <div class="title-main-en">Wedding Ceremony with You</div>
            <div class="gold-line"></div>
            <p class="title-sub">Singing & Hosting Professional Service</p>
        </div>

        <div class="icon-section">
            <svg fill="#c9a667" viewBox="0 0 24 24">
                <path d="M12 2l3 3-3 3-3-3 3-3zm0 6a7 7 0 110 14 7 7 0 010-14zm0 2a5 5 0 100 10 5 5 0 000-10z"/>
            </svg>
            <svg fill="#c9a667" viewBox="0 0 24 24">
                <path d="M12 21s-7-4.3-7-10a5 5 0 019-3 5 5 0 019 3c0 5.7-7 10-7 10z"/>
            </svg>
            <svg fill="#c9a667" viewBox="0 0 24 24">
                <path d="M12 14a3 3 0 003-3V5a3 3 0 00-6 0v6a3 3 0 003 3zm5-3a5 5 0 01-10 0H5a7 7 0 0014 0h-2z"/>
            </svg>
        </div>

        <div class="gold-divider"></div>

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
"""

st.markdown(HTML_HEADER, unsafe_allow_html=True)

# ============================================================================================================
#                                    🎤 서비스 입력 섹션 (기능 파트)
# ============================================================================================================

st.markdown("## 🎤 의뢰 서비스 선택")
service = st.multiselect("선택", ["축가", "사회"])

st.markdown("## 👰🤵 기본 정보")
role = st.radio("결혼식 주인공", ["신랑", "신부"])
name = st.text_input("이름")
age = st.number_input("만 나이", min_value=18, max_value=80)
wedding_date = st.date_input("예식일", value=date.today())

st.markdown("## 🏩 예식 정보")
venue = st.selectbox("예식 장소", ["호텔", "하우스 웨딩", "야외", "컨벤션", "기타"])
venue_address = st.text_input("예식장 주소")
mood = st.radio("예식 분위기", ["낭만적 💞", "유쾌하게 😄", "격식 있게 🎩"])

host_style = None
if "사회" in service:
    host_style = st.radio("사회 스타일", ["담백·심플 (정석)", "센스 있고 위트 있게"])

song_pref = None
custom_song = None

song_recommend_list = [
    "임영웅 - 이제 나만 믿어요",
    "유해준 - 나에게 그대만이 (탑현 ver.)",
    "윤종신 - 오르막길",
    "이석훈 - 그대를 사랑하는 10가지 이유",
    "이준호 - 넌",
    "허각 - 언제나",
    "허각 - 물론",
    "정승환 - 사뿐",
    "유리상자 - 신부에게",
    "김범수 - 사랑의 시작은 고백에서부터 (전상근 ver.)",
    "김범수 - 오직 너만",
    "한동근 - 그대라는 사치",
    "윤종신 - 그대 없이는 못살아 (늦가을 ver.)"
]

if "축가" in service:
    st.markdown("## 🎵 축가 정보")
    song_pref = st.radio("원하는 곡이 있나요?", ["네, 있어요", "추천해주세요!"])
    if song_pref == "네, 있어요":
        custom_song = st.text_input("곡명 입력")
    else:
        custom_song = st.selectbox("추천곡 선택", song_recommend_list)

# 연락처
st.markdown("## ✍️ 연락처 & 요청사항")
user_email = st.text_input("📧 이메일")
user_phone = st.text_input("📱 핸드폰 번호")
special_request = st.text_area("특이사항 / 기타 요청사항", height=100)

# ============================================================================================================
#                                          ✉ 이메일 전송
# ============================================================================================================

def send_email(to, subject, body):
    try:
        sender = st.secrets["email"]["address"]
        pw = st.secrets["email"]["password"]

        msg = MIMEText(body, _charset="utf-8")
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = to

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, pw)
            smtp.send_message(msg)
        return True

    except Exception as e:
        st.error("❌ 이메일 전송 실패: " + str(e))
        return False


if st.button("💌 신청서 제출하기"):
    st.success("의뢰 신청이 완료되었습니다! 💐")

    form_data = {
        "주인공": role,
        "이름": name,
        "만 나이": age,
        "예식일": wedding_date,
        "예식 장소": venue,
        "주소": venue_address or "미입력",
        "분위기": mood,
        "서비스": ", ".join(service),
        "사회 스타일": host_style or "해당 없음",
        "축가 방식": song_pref or "해당 없음",
        "축가 곡명": custom_song or "미입력",
        "기타": special_request or "없음",
        "이메일": user_email or "미입력",
        "전화번호": user_phone or "미입력",
    }

    email_body = "💒 영원파파 결혼식 의뢰 신청 내역\n\n"
    for k, v in form_data.items():
        email_body += f"▪ {k}: {v}\n"

    send_email("hd261818@gmail.com", "[새 의뢰] 영원파파 신청서", email_body)

    if user_email:
        send_email(user_email, "[영원파파] 의뢰 접수 완료",
                   "신청이 정상 접수되었습니다 💐\n3일 이내 순차 회신 드립니다!")


