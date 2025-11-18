import streamlit as st
from datetime import date
import pandas as pd
import smtplib
from email.mime.text import MIMEText


# ============================================================================================
#                                   🌸 페이지 기본 설정
# ============================================================================================
st.set_page_config(page_title="영원파파 결혼식 축가·사회 의뢰", page_icon="💐", layout="centered")


# ============================================================================================
#                               🌸 고급스러운 웨딩 스타일 적용
# ============================================================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Playfair+Display:wght@400;600;700&display=swap');

    body {
        background:
            linear-gradient(rgba(255,255,255,0.95), rgba(255,255,255,0.9)),
            url('https://images.unsplash.com/photo-1529634806980-cd96697e63d7?w=1600&q=80') center/cover fixed !important;
        font-family: 'Gowun Batang', serif !important;
    }

    .stApp {
        background:
            linear-gradient(rgba(255,255,255,0.95), rgba(255,255,255,0.9)),
            url('https://images.unsplash.com/photo-1529634806980-cd96697e63d7?w=1600&q=80') center/cover fixed !important;
    }

    .block-container {
        background: rgba(255, 255, 255, 0.85) !important;
        padding: 40px 30px !important;
        border-radius: 25px !important;
        backdrop-filter: blur(12px) !important;
        box-shadow: 0 10px 30px rgba(210, 180, 170, 0.25) !important;
        border: 1px solid rgba(220,200,200,0.4) !important;
    }

    h1 {
        font-family: 'Playfair Display', serif !important;
        color: #c79a8b !important;
        font-size: 2.7rem !important;
        text-align: center !important;
        font-weight: 700 !important;
    }

    h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: #b48679 !important;
        font-weight: 600 !important;
    }

    label {
        color: #8d6f62 !important;
        font-family: 'Gowun Batang', serif !important;
        font-weight: 700 !important;
    }

    .stTextInput input, .stTextArea textarea,
    .stSelectbox div[data-baseweb="select"],
    .stNumberInput input, .stDateInput input {
        background: rgba(255,255,255,0.9) !important;
        border: 2px solid #e7d6cf !important;
        border-radius: 12px !important;
        padding: 10px 15px !important;
    }

    .stButton button {
        background: linear-gradient(135deg, #d8b9ad, #e7d6cf, #f5ece9) !important;
        color: #5b4a45 !important;
        font-family: 'Playfair Display', serif !important;
        font-weight: 700 !important;
        font-size: 1.15rem !important;
        padding: 15px 40px !important;
        border-radius: 30px !important;
        border: none !important;
        box-shadow: 0 6px 18px rgba(180,150,130,0.3) !important;
        transition: 0.3s !important;
    }

    .stButton button:hover {
        transform: translateY(-4px) !important;
        box-shadow: 0 10px 25px rgba(180,150,130,0.4) !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================================================
#                                       🌸 상단 헤더
# ============================================================================================
st.markdown(
    """
    <div style="text-align:center; padding:30px 20px; background:rgba(255,255,255,0.75);
         border-radius:25px; border:1px solid rgba(220,200,200,0.4);
         box-shadow:0 6px 20px rgba(200,180,170,0.25); margin-bottom:25px;">
        <h1>영원파파</h1>
        <p style="font-family:'Playfair Display', serif; color:#b48679; font-size:1.3rem;">
            Wedding Singer & Host Request
        </p>
        <p style="color:#9b7a70; font-size:0.95rem;">특별한 날을 더욱 우아하게 만들어드립니다</p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================================================
#                                   🌸 서비스 선택
# ============================================================================================
st.markdown("### 🎤 의뢰 서비스 선택")
service = st.multiselect("", ["축가", "사회"], label_visibility="collapsed")


# ============================================================================================
#                                   🌸 기본 정보 입력
# ============================================================================================
st.markdown("### 👰🤵 기본 정보 입력")

role = st.radio("결혼식의 주인공을 선택해주세요", ["신랑", "신부"])
name = st.text_input("이름을 입력해주세요")
age = st.number_input("만 나이를 입력해주세요", min_value=18, max_value=80, step=1)
wedding_date = st.date_input("예식일을 선택해주세요", value=date.today())


# ============================================================================================
#                                   🌸 예식 정보 입력
# ============================================================================================
st.markdown("### 🏩 예식 관련 정보")

venue = st.selectbox("예식 장소", ["호텔", "하우스 웨딩", "야외", "컨벤션", "기타"])
venue_address = st.text_input("예식장 상세 주소")
mood = st.radio("예식 분위기", ["낭만적 💞", "유쾌하고 즐겁게 😄", "격식 있고 포멀하게 🎩"])


# ============================================================================================
#                                   🌸 사회 선택 시
# ============================================================================================
host_style = None
if "사회" in service:
    st.markdown("### 🎙️ 사회 스타일 선택")
    host_style = st.radio(
        "진행 스타일을 선택해주세요",
        ["담백하고 심플하게 (정석 스타일)", "센스 있고 위트 있게"]
    )


# ============================================================================================
#                                   🌸 축가 선택 시
# ============================================================================================
song_pref, custom_song = None, None
song_info = ""

if "축가" in service:
    st.markdown("### 🎵 축가 관련 정보")
    song_pref = st.radio("원하는 노래가 있으신가요?", ["네, 있어요", "추천해주세요!"])

    if song_pref == "네, 있어요":
        custom_song = st.text_input("축가 곡명을 입력해주세요")
        song_info = f"▪ 축가 곡: {custom_song if custom_song else '미입력'}"
    else:
        song_info = "▪ 축가: 추천 요청"


# ============================================================================================
#                               🌸 연락처 & 추가 요청
# ============================================================================================
st.markdown("### ✍️ 연락처 & 요청사항")

col1, col2 = st.columns(2)
with col1:
    user_email = st.text_input("📧 이메일")
with col2:
    user_phone = st.text_input("📱 핸드폰 번호")

special_request = st.text_area("특이사항 / 기타 요청사항", height=120)


# ============================================================================================
#                               🌸 이메일 전송 함수
# ============================================================================================
def send_email(to_email, subject, body):
    try:
        if "email" not in st.secrets:
            st.warning("⚠️ 이메일 설정이 필요합니다.")
            st.code(body)
            return False

        sender = st.secrets["email"]["address"]
        pw = st.secrets["email"]["password"]

        msg = MIMEText(body, _charset="utf-8")
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = to_email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, pw)
            smtp.send_message(msg)

        return True
    except Exception as e:
        st.error(f"❌ 이메일 전송 실패: {e}")
        st.code(body)
        return False


# ============================================================================================
#                                   🌸 제출 버튼
# ============================================================================================
if st.button("💌 신청서 제출하기 💌"):

    st.success("의뢰 신청이 완료되었습니다! 💐")

    # 이메일 본문 (모든 항목 누락 없이 포함)
    email_body = f"""
💒 결혼식 축가·사회 의뢰 신청 정보 💒

▪ 주인공: {role}
▪ 이름: {name if name else "미입력"}
▪ 만나이: {age}
▪ 예식일: {wedding_date}
▪ 예식 장소: {venue}
▪ 예식장 주소: {venue_address if venue_address else "미입력"}
▪ 예식 분위기: {mood}
▪ 서비스 선택: {", ".join(service) if service else "미선택"}

{"▪ 사회 스타일: " + host_style if host_style else ""}
{song_info}

▪ 기타 요청사항:
{special_request if special_request else "없음"}

--- 연락처 ---
▪ 이메일: {user_email if user_email else "미입력"}
▪ 핸드폰: {user_phone if user_phone else "미입력"}

감사합니다 💐
"""

    # 관리자 이메일 전송
    admin_email = "hd261818@gmail.com"
    send_email(admin_email, "[새 의뢰] 결혼식 축가·사회 신청서", email_body)

    # 사용자 확인 메일 전송
    if user_email:
        confirm_mail = f"""
안녕하세요, 영원파파입니다. 💒

의뢰 신청이 정상적으로 접수되었습니다.
영원파파를 선택해주셔서 다시 한번 감사드리며,
📌 **3일 이내에 순차적으로 회신드릴 예정입니다.**

--- 신청 내용 ---
{email_body}

문의사항은 인스타그램 @0one.papa 혹은 이메일로 연락주세요.
감사합니다. 💐
"""
        send_email(user_email, "[영원파파] 의뢰 신청 접수 완료", confirm_mail)


# ============================================================================================
#                                   🌸 인스타그램 링크
# ============================================================================================
st.markdown(
    """
    <div style="text-align:center; padding:30px; margin-top:40px;">
        <a href="https://www.instagram.com/0one.papa/" target="_blank"
           style="font-size:1.1rem; color:#8d6f62; text-decoration:none;">
            📸 Instagram @0one.papa
        </a>
    </div>
    """,
    unsafe_allow_html=True
)




