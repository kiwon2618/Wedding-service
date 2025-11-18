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
#                           🌸 고급+귀여운 웨딩 텍스처 스타일
# ============================================================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Playfair+Display:wght@400;600;700&family=Pacifico&display=swap');

    body {
        background:
            linear-gradient(rgba(255,255,255,0.95), rgba(255,255,255,0.85)),
            url('https://www.transparenttextures.com/patterns/white-paper.png'),
            url('https://images.unsplash.com/photo-1529634806980-cd96697e63d7?w=1600&q=80') center/cover fixed !important;
        background-blend-mode: normal, soft-light, overlay;
        font-family: 'Gowun Batang', serif !important;
    }

    .stApp {
        background:
            linear-gradient(rgba(255,255,255,0.95), rgba(255,255,255,0.85)),
            url('https://www.transparenttextures.com/patterns/flowers.png'),
            url('https://images.unsplash.com/photo-1529634806980-cd96697e63d7?w=1600&q=80') center/cover fixed !important;
        background-blend-mode: normal, soft-light, overlay;
    }

    .block-container {
        background: rgba(255, 255, 255, 0.78) !important;
        padding: 40px 30px !important;
        border-radius: 25px !important;
        box-shadow: 0 10px 35px rgba(180,160,150,0.30) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(230,210,210,0.4) !important;
    }

    .wedding-title {
        font-family: 'Pacifico', cursive;
        font-size: 3rem;
        color: #d69ca3;
        text-shadow: 0px 0px 8px rgba(255, 220, 230, 0.7);
        letter-spacing: 2px;
    }

    .gold-line {
        width: 60%;
        height: 2px;
        margin: 15px auto 5px auto;
        background: linear-gradient(90deg, transparent, #d8bba0, transparent);
    }

    .insta-btn {
        font-size: 1.3rem;
        font-weight: 700;
        padding: 18px 45px;
        color: white !important;
        background: linear-gradient(45deg,
            #f09433 0%, #e6683c 25%, #dc2743 50%,
            #cc2366 75%, #bc1888 100%) !important;
        border-radius: 40px;
        text-decoration: none !important;
        display: inline-block;
        box-shadow: 0 6px 22px rgba(255,80,120,0.45);
        transition: 0.35s;
        border: 2px solid rgba(255,255,255,0.6);
    }

    .insta-btn:hover {
        transform: scale(1.07);
        box-shadow: 0 10px 30px rgba(255,90,130,0.6);
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================================================
#                                   🌸 상단 웨딩 헤더
# ============================================================================================
st.markdown(
    """
    <div style="text-align:center; padding:35px 10px;">
        <div class="wedding-title">💐 Yeongwon Papa 💐</div>
        <div class="gold-line"></div>
        <p style="font-family:'Playfair Display'; color:#a18478; font-size:1.15rem;">
            Wedding Singer & Host Request
        </p>
        <p style="font-family:'Gowun Batang'; color:#a18478; font-size:0.9rem;">
            특별한 날을 더욱 우아하고 사랑스럽게 만들어드립니다
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================================================
#                         🌸 입력 폼 (사용자가 입력하는 모든 값)
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

# 사회
host_style = None
if "사회" in service:
    st.markdown("### 🎙️ 사회 스타일")
    host_style = st.radio("진행 스타일", ["담백·심플 (정석)", "센스 있고 위트 있게"])

# 축가
song_pref = None
custom_song = None
if "축가" in service:
    st.markdown("### 🎵 축가 정보")
    song_pref = st.radio("원하는 곡이 있나요?", ["네, 있어요", "추천해주세요!"])
    if song_pref == "네, 있어요":
        custom_song = st.text_input("축가 곡명 입력 (정확한 곡명)")


# 연락처 & 기타 요청
st.markdown("### ✍️ 연락처 & 요청사항")

col1, col2 = st.columns(2)
with col1:
    user_email = st.text_input("📧 이메일")
with col2:
    user_phone = st.text_input("📱 핸드폰 번호")

special_request = st.text_area("특이사항 / 기타 요청사항", height=120)


# ============================================================================================
#                    🌸 이메일 전송: 모든 입력값을 빠짐없이 자동 정리
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
        st.error(f"❌ 이메일 전송 실패: {e}")
        st.code(body)
        return False


# ============================================================================================
#                               🌸 제출 버튼
# ============================================================================================
if st.button("💌 신청서 제출하기"):

    st.success("의뢰 신청이 완료되었습니다! 💐")

    # --------------- 모든 입력값을 dict 형태로 정리 (누락 방지) ------------------
    form_data = {
        "주인공": role or "미입력",
        "이름": name or "미입력",
        "만 나이": age,
        "예식일": wedding_date,
        "예식 장소": venue,
        "예식장 주소": venue_address or "미입력",
        "예식 분위기": mood,
        "선택한 서비스": ", ".join(service) if service else "미선택",

        # 사회 선택 여부
        "사회 스타일": host_style if host_style else "해당 없음",

        # 축가 선택 여부
        "축가 선택 방식": song_pref if song_pref else "해당 없음",
        "축가 곡명": custom_song if custom_song else ("추천 요청" if song_pref == "추천해주세요!" else "미입력"),

        "기타 요청사항": special_request if special_request else "없음",

        "이메일": user_email or "미입력",
        "핸드폰": user_phone or "미입력",
    }

    # ---------------- 이메일 본문 자동 생성 ----------------
    email_body = "💒 결혼식 축가·사회 의뢰 신청 내용 💒\n\n"
    for key, value in form_data.items():
        email_body += f"▪ {key}: {value}\n"

    email_body += "\n감사합니다 💐\n"

    # 관리자에게 전송
    admin_email = "hd261818@gmail.com"
    send_email(admin_email, "[새 의뢰] 결혼식 축가·사회 신청", email_body)

    # 사용자에게 확인 메일 전송
    if user_email:
        confirm_msg = f"""
안녕하세요, 영원파파입니다 💒

의뢰 신청이 정상 접수되었습니다!
영원파파를 선택해주셔서 다시 한번 감사드리며,
📌 **3일 이내에 순차적으로 회신드리겠습니다.**

--- 신청 내용 ---
{email_body}

문의 사항은 인스타그램 @0one.papa 로 언제든지 연락주세요 💕
"""
        send_email(user_email, "[영원파파] 의뢰 접수 완료", confirm_msg)


# ============================================================================================
#                        🌸 인스타그램 버튼 (눈에 확 띄도록)
# ============================================================================================
st.markdown(
    """
    <div style="text-align:center; margin-top:50px; margin-bottom:30px;">
        <a class="insta-btn" href="https://www.instagram.com/0one.papa/" target="_blank">
            📸 Instagram @0one.papa
        </a>
    </div>
    """,
    unsafe_allow_html=True
)


