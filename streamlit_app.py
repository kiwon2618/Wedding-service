import streamlit as st
from datetime import date
import smtplib
from email.mime.text import MIMEText

# ============================================================================================
#                                   🌸 페이지 설정
# ============================================================================================
st.set_page_config(page_title="영원파파 결혼식 축가·사회 의뢰", page_icon="💐", layout="centered")

# ============================================================================================
#                          🌸 스타일 (웨딩톤 + Base64 이미지 안정)
# ============================================================================================
st.markdown("""
<style>
@import url("https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Pretendard:wght@500;600;700&family:Gmarket+Sans:wght@700&display=swap");

body, .stApp {
    background: linear-gradient(rgba(255,255,255,0.96), rgba(255,255,255,0.94));
}

.white-flower {
    width: 130px;
    opacity: 0.97;
    filter: drop-shadow(0 4px 8px rgba(160,140,140,0.35));
    margin: 0 25px;
}

.title-main {
    font-family: "Gmarket Sans", sans-serif;
    font-size: 3.2rem;
    font-weight: 800;
    color: #d55f85;
    text-align: center;
}

.title-sub {
    font-family: "Pretendard", sans-serif;
    font-size: 1.28rem;
    text-align: center;
    color: #8d6f62;
    font-weight: 600;
}

.gold-line {
    width: 55%;
    height: 2px;
    margin: 22px auto;
    background: linear-gradient(90deg, transparent, #d6b99d, transparent);
}
</style>
""", unsafe_allow_html=True)

# ============================================================================================
#                🌸 헤더 — Base64 이미지 (너가 쓰던 그대로) + 타이틀 교체
# ============================================================================================

LEFT_FLOWER = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAYAAACtWK6eAAAACXBI..."   # ← 기존 Base64 유지
RIGHT_FLOWER = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAYAAACtWK6eAAAACXBI..."  # ← 기존 Base64 유지

st.markdown(f"""
<div style="text-align:center; padding:50px 0 35px 0;">

    <img class="white-flower" src="{LEFT_FLOWER}">
    <div class="title-main">영원파파와 함께하는 아름다운 웨딩 세리머니</div>
    <img class="white-flower" src="{RIGHT_FLOWER}">

    <div class="gold-line"></div>

    <p class="title-sub">축가 & 사회 전문 의뢰 서비스</p>

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

# ============================================================================================
#                        🎵 축가 정보 (요청한 리스트 100% 반영)
# ============================================================================================

song_pref = None
custom_song = None

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

if "축가" in service:
    st.markdown("### 🎵 축가 정보")
    song_pref = st.radio("원하는 곡이 있나요?", ["네, 있어요", "추천해주세요!"])

    if song_pref == "네, 있어요":
        custom_song = st.text_input("축가 곡명 입력")

    if song_pref == "추천해주세요!":
        custom_song = st.selectbox("추천 축가 리스트", recommended_songs)

# ============================================================================================
#                        🎙️ 사회 스타일
# ============================================================================================

host_style = None
if "사회" in service:
    st.markdown("### 🎙️ 사회 스타일")
    host_style = st.radio("진행 스타일", ["담백·심플 (정석)", "센스 있고 위트 있게"])

# ============================================================================================
#                     ✍️ 연락처 & 기타 요청 사항
# ============================================================================================

st.markdown("### ✍️ 연락처 & 기타 요청사항")
col1, col2 = st.columns(2)
with col1:
    user_email = st.text_input("📧 이메일")
with col2:
    user_phone = st.text_input("📱 핸드폰 번호")

special_request = st.text_area("특이사항 / 기타 요청사항", height=120)

# ============================================================================================
#                                🌸 이메일 전송 함수
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
#                                💌 제출 버튼
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
        "사회 스타일": host_style or "해당 없음",
        "축가 방식": song_pref or "해당 없음",
        "축가 곡명": custom_song or "미입력",
        "기타 요청사항": special_request or "없음",
        "이메일": user_email or "미입력",
        "핸드폰": user_phone or "미입력",
    }

    body = "💒 결혼식 축가·사회 의뢰 신청 내용 💒\n\n"
    for k, v in form_data.items():
        body += f"▪ {k}: {v}\n"
    body += "\n감사합니다 💐\n"

    send_email("hd261818@gmail.com", "[새 의뢰] 결혼식 축가·사회 신청", body)

    if user_email:
        confirm = f"""
안녕하세요, 영원파파입니다 💒

의뢰 신청이 정상 접수되었습니다!
소중한 예식에 함께할 기회를 주셔서 감사합니다.
📌 **3일 이내 빠르게 연락드리겠습니다.**

--- 신청 내용 ---
{body}

인스타그램 @0one.papa 로 편하게 문의주세요 💕
"""
        send_email(user_email, "[영원파파] 의뢰 접수 완료", confirm)
