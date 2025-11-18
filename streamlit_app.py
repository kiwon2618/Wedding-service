import streamlit as st
from datetime import date
import smtplib
from email.mime.text import MIMEText


# ============================================================================================
#                                   🌸 페이지 기본 설정
# ============================================================================================
st.set_page_config(page_title="영원파파 결혼식 축가·사회 의뢰", page_icon="💐", layout="centered")

# ============================================================================================
#                     🌸 고급 + 은은한 웨딩 스타일 (흰 꽃 + 깃털 + 웨딩 텍스처)
# ============================================================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Pretendard:wght@600;700;800&family=Gmarket+Sans:wght@700&display=swap');

body, .stApp {
    background:
        linear-gradient(rgba(255,255,255,0.94), rgba(255,255,255,0.92)),
        url('https://www.transparenttextures.com/patterns/white-feather.png'),
        url('https://www.transparenttextures.com/patterns/white-floral.png'),
        url('https://images.unsplash.com/photo-1508973376-37031c9f9a43?w=1600&q=80') center/cover fixed;
    background-blend-mode: normal, screen, overlay, multiply;
}

/* 메인 카드 */
.block-container {
    background: rgba(255, 255, 255, 0.80) !important;
    padding: 40px 30px !important;
    border-radius: 25px !important;
    box-shadow: 0 10px 35px rgba(180,160,150,0.28) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(230,210,210,0.45) !important;
}

/* 타이틀 */
.title-main {
    font-family: "Gmarket Sans", "Pretendard", sans-serif;
    font-size: 3.6rem;
    font-weight: 800;
    color: #d37288;
    letter-spacing: 1px;
    text-shadow: 0 0 6px rgba(255, 200, 210, 0.6);
    margin-bottom: 5px;
}

.title-sub {
    font-family: "Pretendard", sans-serif;
    font-size: 1.2rem;
    color: #8d6f62;
    font-weight: 600;
}

/* 금색 라인 */
.gold-line {
    width: 55%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #d8bba0, transparent);
    margin: 15px auto 20px auto;
}

/* 고급 꽃 아이콘 */
.white-flowers {
    width: 95px;
    filter: drop-shadow(0px 3px 5px rgba(200, 180, 180, 0.4));
}

/* 입력창 */
.stTextInput input, .stTextArea textarea,
.stSelectbox div[data-baseweb="select"],
.stNumberInput input, .stDateInput input {
    background: rgba(255,255,255,0.92) !important;
    border: 2px solid #e7d6cf !important;
    border-radius: 12px !important;
    padding: 10px 15px !important;
}

/* 버튼 */
.stButton button {
    background: linear-gradient(135deg, #d8b9ad, #e7d6cf, #f5ece9) !important;
    color: #5b4a45 !important;
    font-family: "Pretendard", sans-serif !important;
    font-weight: 700 !important;
    font-size: 1.15rem !important;
    padding: 14px 38px !important;
    border-radius: 30px !important;
    box-shadow: 0 6px 18px rgba(180,150,130,0.28) !important;
    border: none !important;
    transition: 0.3s !important;
}
.stButton button:hover {
    transform: translateY(-4px) !important;
    box-shadow: 0 12px 28px rgba(180,150,130,0.38) !important;
}

/* 인스타 버튼 */
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
#                                   🌸 헤더
# ============================================================================================
st.markdown("""
<div style="text-align:center; padding:40px 0 25px 0;">

    <img class="white-flowers"
         src="https://cdn-icons-png.flaticon.com/512/7665/7665330.png">

    <div class="title-main">영원파파</div>

    <img class="white-flowers"
         src="https://cdn-icons-png.flaticon.com/512/7665/7665330.png">

    <div class="gold-line"></div>

    <p class="title-sub">Wedding Singer & Host Service</p>

    <p style="font-family:'Gowun Batang';
              color:#a18478; font-size:0.92rem; margin-top:3px;">
        당신의 가장 특별한 순간을 더욱 아름답게 만들어드립니다
    </p>

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
#                                   🌸 이메일 전송 함수
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
        st.code(body)
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

    # 관리자 메일
    send_email("hd261818@gmail.com", "[새 의뢰] 결혼식 축가·사회 신청", email_body)

    # 사용자 확인 메일
    if user_email:
        confirm = f"""
안녕하세요, 영원파파입니다 💒

의뢰 신청이 정상 접수되었습니다!
영원파파를 선택해주셔서 다시 한번 감사드리며,
📌 **3일 이내에 순차적으로 회신드리겠습니다.**

--- 신청 내용 ---
{email_body}

문의사항은 인스타그램 @0one.papa 로 언제든 편하게 문의해주세요 💕
"""
        send_email(user_email, "[영원파파] 의뢰 접수 완료", confirm)


# ============================================================================================
#                           🌸 인스타그램 버튼 (강조형)
# ============================================================================================
st.markdown("""
<div style="text-align:center; margin-top:50px; margin-bottom:30px;">
    <a class="insta-btn" href="https://www.instagram.com/0one.papa/" target="_blank">
        📸 Instagram @0one.papa
    </a>
</div>
""", unsafe_allow_html=True)
