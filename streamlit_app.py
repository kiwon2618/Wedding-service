import streamlit as st
from datetime import date
import smtplib
from email.mime.text import MIMEText

# ----------------------------------------------------------
# 기본 설정
# ----------------------------------------------------------
st.set_page_config(page_title="영원파파 결혼식 축가·사회 의뢰", page_icon="💐", layout="centered")

# ----------------------------------------------------------
# CSS 스타일
# ----------------------------------------------------------
st.markdown("""
<style>
@import url("https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Pretendard:wght@600;700&family=Gmarket+Sans:wght@700&display=swap");

body, .stApp {
    background: linear-gradient(rgba(255,255,255,0.96), rgba(255,255,255,0.94));
}
.white-flower {
    width: 130px;
    opacity: 0.97;
    margin: 0 25px;
    filter: drop-shadow(0 5px 10px rgba(180,160,160,0.35));
}
.title-main {
    font-family: "Gmarket Sans", sans-serif;
    font-size: 2.8rem;
    font-weight: 800;
    color: #d55f85;
    text-align: center;
}
.title-sub {
    font-family: "Pretendard", sans-serif;
    font-size: 1.25rem;
    text-align: center;
    color: #8d6f62;
    font-weight: 600;
}
.gold-line {
    width: 50%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #d6b99d, transparent);
    margin: 18px auto;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# Base64 이미지 (빈칸에 너의 이미지 붙여 넣기)
# ----------------------------------------------------------
LEFT_FLOWER = "data:image/png;base64,PASTE_YOUR_LEFT_BASE64_HERE"
RIGHT_FLOWER = "data:image/png;base64,PASTE_YOUR_RIGHT_BASE64_HERE"

# ----------------------------------------------------------
# 헤더
# ----------------------------------------------------------
st.markdown(f"""
<div style="text-align:center; padding:40px 0 20px 0;">
    <img class="white-flower" src="{LEFT_FLOWER}">
    <div class="title-main">영원파파와 함께하는 아름다운 웨딩 세리머니</div>
    <img class="white-flower" src="{RIGHT_FLOWER}">
    <div class="gold-line"></div>
    <p class="title-sub">축가 & 사회 전문 의뢰 서비스</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# 입력 폼
# ----------------------------------------------------------
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

# ----------------------------------------------------------
# 축가 정보
# ----------------------------------------------------------
recommended_songs = [
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

song_pref = None
custom_song = None

if "축가" in service:
    st.markdown("### 🎵 축가 정보")
    song_pref = st.radio("원하는 곡이 있나요?", ["네, 있어요", "추천해주세요!"])

    if song_pref == "네, 있어요":
        custom_song = st.text_input("축가 곡명 입력")

    if song_pref == "추천해주세요!":
        custom_song = st.selectbox("추천곡 리스트", recommended_songs)

# ----------------------------------------------------------
# 사회 정보
# ----------------------------------------------------------
host_style = None
if "사회" in service:
    st.markdown("### 🎙️ 사회 스타일")
    host_style = st.radio("진행 스타일", ["담백·심플 (정석)", "센스 있고 위트 있게"])

# ----------------------------------------------------------
# 연락처
# ----------------------------------------------------------
st.markdown("### ✍️ 연락처 & 기타 요청사항")
col1, col2 = st.columns(2)
with col1:
    user_email = st.text_input("📧 이메일")
with col2:
    user_phone = st.text_input("📱 핸드폰 번호")

special_request = st.text_area("특이사항 / 기타 요청사항", height=120)

# ----------------------------------------------------------
# 이메일 함수
# ----------------------------------------------------------
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

# ----------------------------------------------------------
# 제출
# ----------------------------------------------------------
if st.button("💌 신청서 제출하기"):
    st.success("의뢰 신청이 완료되었습니다! 💐")

    data = {
        "주인공": role,
        "이름": name,
        "만 나이": age,
        "예식일": wedding_date,
        "예식 장소": venue,
        "예식장 주소": venue_address or "미입력",
        "예식 분위기": mood,
        "선택 서비스": ", ".join(service) if service else "미선택",
        "사회 스타일": host_style or "해당 없음",
        "축가 방식": song_pref or "해당 없음",
        "축가 곡명": custom_song or "미입력",
        "기타 요청사항": special_request or "없음",
        "이메일": user_email or "미입력",
        "핸드폰": user_phone or "미입력",
    }

    body = "💒 결혼식 축가·사회 신청 내용 💒\n\n"
    for k, v in data.items():
        body += f"▪ {k}: {v}\n"

    send_email("hd261818@gmail.com", "[새 의뢰] 신규 의뢰 도착", body)

    if user_email:
        confirm = f"""
안녕하세요 영원파파입니다 💒

의뢰 신청이 정상 접수되었습니다!
소중한 날 함께할 기회를 주셔서 감사합니다.

📌 3일 이내 순차적으로 연락드리겠습니다.

--- 신청 내용 ---
{body}

Instagram @0one.papa 로 언제든 편하게 문의 주세요 💕
"""
        send_email(user_email, "[영원파파] 의뢰 접수 완료", confirm)
