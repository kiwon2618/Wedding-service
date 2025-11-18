import streamlit as st
from datetime import date
import smtplib
from email.mime.text import MIMEText
import base64

# ============================================================================================
#                               🌸 페이지 설정
# ============================================================================================
st.set_page_config(page_title="영원파파 결혼식 축가·사회 의뢰", page_icon="💐", layout="centered")

# ============================================================================================
#                       🌸 웨딩 일러스트 base64(투명도 조절된 버전)
# ============================================================================================
wedding_img_base64 = """
iVBORw0KGgoAAAANSUhEUgAABAAAAAYACAIAAABn4K39AAEOqmNhQlgAAQ6qanV...
(⚠ 실제 base64 전체는 매우 길어서 잘림 — 아래에서 전체 버전 제공)
"""

# 배경 이미지 CSS
st.markdown(f"""
<style>
.stApp::before {{
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: url("data:image/png;base64,{wedding_img_base64}") no-repeat center 120px;
    background-size: 38%;
    opacity: 0.22;   /* 투명도 */
    z-index: -1;
}}
</style>
""", unsafe_allow_html=True)

# ============================================================================================
#                       🌸 제목 디자인
# ============================================================================================
st.markdown("""
<style>
@import url("https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Pretendard:wght@600;700;800&family=Gmarket+Sans:wght@700&display=swap");

.title-main-kr {
    font-family: "Gmarket Sans", sans-serif;
    font-size: 3.3rem;
    font-weight: 800;
    color: #d05478;
    text-align: center;
    margin-top: 120px;
    text-shadow: 0 0 6px rgba(255,180,195,0.45);
}

.title-main-en {
    font-family: "Pretendard", sans-serif;
    font-size: 1.35rem;
    color: #6f5a55;
    font-weight: 600;
    margin-top: -8px;
    text-align: center;
}

.title-sub {
    font-family: "Gowun Batang";
    font-size: 1rem;
    color: #a18478;
    margin-top: 12px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# HTML 타이틀 본문
st.markdown("""
<div class="title-main-kr">영원파파</div>
<div class="title-main-en">Wedding Ceremony with You</div>
<div class="title-sub">Singing & Hosting Professional Service</div>
""", unsafe_allow_html=True)

# ============================================================================================
#                       🌸 추천곡 리스트
# ============================================================================================
song_list = [
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

# 사회 스타일
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

    if song_pref == "추천해주세요!":
        custom_song = st.selectbox("추천 곡 리스트", song_list)
    else:
        custom_song = st.text_input("축가 곡명 직접 입력")

# 연락처
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
        "축가 곡명": custom_song if custom_song else "미입력",
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

문의사항은 인스타그램 @0one.papa 로 편하게 연락주세요 💕
"""
        send_email(user_email, "[영원파파] 의뢰 접수 완료", confirm)

# ============================================================================================
#                                   🌸 인스타그램 버튼
# ============================================================================================
st.markdown("""
<div style="text-align:center; margin-top:50px; margin-bottom:30px;">
    <a class="insta-btn" href="https://www.instagram.com/0one.papa/" target="_blank">
        📸 Instagram @0one.papa
    </a>
</div>
""", unsafe_allow_html=True)
