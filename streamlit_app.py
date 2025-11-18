import streamlit as st
from datetime import date
import smtplib
from email.mime.text import MIMEText

# ============================================================================================
#                                   🌸 페이지 설정
# ============================================================================================
st.set_page_config(page_title="영원파파 결혼식 축가·사회 의뢰", page_icon="💐", layout="centered")

# ============================================================================================
#                        🌸 스타일: 웨딩 배경 + 투명 화이트 플라워 + 서체
# ============================================================================================
st.markdown("""
<style>
@import url("https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Pretendard:wght@500;600;700&family=Gmarket+Sans:wght@700&display=swap");

body, .stApp {
    background:
        linear-gradient(rgba(255,255,255,0.95), rgba(255,255,255,0.93)),
        url("https://www.transparenttextures.com/patterns/white-linen.png");
}

.white-flower {
    width: 140px;
    opacity: 0.95;
    filter: drop-shadow(0 4px 10px rgba(190,170,170,0.5));
    margin: 0 30px;
}

.title-main {
    font-family: "Gmarket Sans", sans-serif;
    font-size: 3.6rem;
    font-weight: 800;
    color: #d55f85;
    text-align: center;
    text-shadow: 0 0 8px rgba(255,180,190,0.5);
}

.title-sub {
    font-family: "Pretendard", sans-serif;
    font-size: 1.22rem;
    font-weight: 600;
    text-align: center;
    color: #8d6f62;
}

.gold-line {
    width: 58%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #d6b99d, transparent);
    margin: 22px auto;
}

.insta-btn {
    font-size: 1.35rem;
    font-weight: 800;
    padding: 20px 50px;
    color: white !important;
    background: linear-gradient(45deg,
        #f09433 0%, #e6683c 25%, #dc2743 50%,
        #cc2366 75%, #bc1888 100%) !important;
    border-radius: 45px;
    text-decoration: none !important;
    display: inline-block;
    box-shadow: 0 6px 25px rgba(255,90,130,0.45);
    transition: 0.35s;
    border: 2px solid rgba(255,255,255,0.65);
}
.insta-btn:hover {
    transform: scale(1.08);
    box-shadow: 0 12px 35px rgba(255,90,130,0.65);
}
</style>
""", unsafe_allow_html=True)

# ============================================================================================
#                                   🌸 헤더 (웨딩 플라워 + 타이틀)
# ============================================================================================
st.markdown("""
<div style="text-align:center; padding:60px 0 35px 0;">

<img class="white-flower"
     src="https://raw.githubusercontent.com/morethanmin/WeddingAssets/main/flowers/white_flower_left.png">

<div class="title-main">축가 & 사회 전문 의뢰 서비스</div>

<img class="white-flower"
     src="https://raw.githubusercontent.com/morethanmin/WeddingAssets/main/flowers/white_flower_right.png">

<div class="gold-line"></div>

<p class="title-sub">영원파파와 함께하는 아름다운 웨딩 세리머니</p>

<p style="font-family:'Gowun Batang'; color:#a18478; font-size:0.96rem; margin-top:5px;">
당신의 가장 특별한 순간을 더욱 따뜻하게 만들어드립니다
</p>

</div>
""", unsafe_allow_html=True)

# ============================================================================================
#                                   🌸 입력폼
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

host_style = None
if "사회" in service:
    st.markdown("### 🎙️ 사회 스타일")
    host_style = st.radio("진행 스타일", ["담백·심플 (정석)", "센스 있고 위트 있게"])

song_pref = None
custom_song = None
if "축가" in service:
    st.markdown("### 🎵 축가 정보")
    song_pref = st.radio("원하는 곡이 있나요?", ["네, 있어요", "추천해주세요!"])
    if song_pref == "네, 있어요":
        custom_song = st.text_input("축가 곡명 입력")

st.markdown("### ✍️ 연락처 & 기타 요청사항")
col1, col2 = st.columns(2)
with col1:
    user_email = st.text_input("📧 이메일")
with col2:
    user_phone = st.text_input("📱 핸드폰 번호")

special_request = st.text_area("특이사항 / 기타 요청사항", height=120)

# ============================================================================================
#                        🌸 이메일 전송 함수
# ============================================================================================
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

# ============================================================================================
#                                   🌸 제출 버튼
# ============================================================================================
if st.button("💌 신청서 제출하기"):
    st.success("의뢰 신청이 완료되었습니다! 💐")

    form_data = {
        "주인공": role,
        "이름": name,
        "만 나이": age,
        "예식일": wedding_date,
        "예식 장소": venue,
        "예식장 주소": venue_address or "미입력",
        "예식 분위기": mood,
        "선택 서비스": ", ".join(service) if service else "미선택",
        "사회 스타일": host_style if host_style else "해당 없음",
        "축가 방식": song_pref if song_pref else "해당 없음",
        "축가 곡명": custom_song if custom_song else (
            "추천 요청" if song_pref == "추천해주세요!" else "미입력"
        ),
        "기타 요청사항": special_request if special_request else "없음",
        "이메일": user_email or "미입력",
        "핸드폰": user_phone or "미입력",
    }

    email_body = "💒 결혼식 축가·사회 의뢰 신청 내용 💒\n\n"
    for k, v in form_data.items():
        email_body += f"▪ {k}: {v}\n"
    email_body += "\n감사합니다 💐\n"

    send_email("hd261818@gmail.com", "[새 의뢰] 결혼식 축가·사회 신청", email_body)

    if user_email:
        confirm = f"""
안녕하세요, 영원파파입니다 💒

의뢰 신청이 정상 접수되었습니다!
영원파파를 선택해주셔서 다시 한번 감사드립니다.
📌 **3일 이내에 순차적으로 회신드리겠습니다.**

--- 신청 내용 ---
{email_body}

궁금하신 사항은 인스타그램 @0one.papa 로 편하게 문의주세요 💕
"""
        send_email(user_email, "[영원파파] 의뢰 접수 완료", confirm)

# ============================================================================================
#                                   🌸 인스타그램 버튼
# ============================================================================================
st.markdown("""
<div style="text-align:center; margin-top:55px; margin-bottom:35px;">
    <a class="insta-btn" href="https://www.instagram.com/0one.papa/" target="_blank">
        📸 Instagram @0one.papa
    </a>
</div>
""", unsafe_allow_html=True)
