import streamlit as st
from datetime import date
import smtplib
from email.mime.text import MIMEText

# ============================================================================================
#                                   🌸 페이지 설정
# ============================================================================================
st.set_page_config(
    page_title="🌸영원파파 결혼식 축가·사회 의뢰🌸",
    page_icon="💐",
    layout="centered"
)

# ============================================================================================
#                               🌸 전체 배경 웨딩 파스텔 톤
# ============================================================================================
st.markdown("""
<style>
@import url("https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Pretendard:wght@500;600;700&family=Gmarket+Sans:wght@700&display=swap");

body, .stApp {
    background: linear-gradient(
        180deg,
        #fff8fb 0%,      /* 아주 연한 핑크 */
        #fffdfc 40%,     /* 아이보리 */
        #fef7fa 100%     /* 웨딩 느낌의 파스텔 */
    );
}

.title-main-kr {
    font-family: "Gmarket Sans", sans-serif;
    font-size: 2.9rem;
    font-weight: 900;
    color: #d36c87;
    margin-top: 30px;
    text-align: center;
}

.title-main-en {
    font-family: "Pretendard", sans-serif;
    font-size: 1.2rem;
    color: #8a6b6b;
    text-align: center;
    margin-top: -8px;
    line-height: 1.4;
}

.title-sub {
    font-family: "Gowun Batang";
    font-size: 1.0rem;
    text-align: center;
    color: #a18478;
    margin-top: 12px;
}

.gold-line {
    width: 55%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #d8bba0, transparent);
    margin: 18px auto;
}
</style>
""", unsafe_allow_html=True)

# ============================================================================================
#                                   🌸 헤더 (이미지 제거됨)
# ============================================================================================
st.markdown("""
<div class="title-main-kr">영원파파</div>

<div class="title-main-en">
Wedding Ceremony with You
</div>

<div class="gold-line"></div>

<p class="title-sub">Singing & Hosting Professional Service</p>
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

# 사회 선택 시 추가 영역
host_style = None
if "사회" in service:
    st.markdown("### 🎙️ 사회 스타일")
    host_style = st.radio("진행 스타일", ["담백·심플 (정석)", "센스 있고 위트 있게"])

# 축가 선택 시 추가 영역
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
with col1:
    user_email = st.text_input("📧 이메일")
with col2:
    user_phone = st.text_input("📱 핸드폰 번호")

special_request = st.text_area("특이사항 / 기타 요청사항", height=120)

# ============================================================================================
#                       🌸 이메일 전송 함수
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
    st.success("의뢰 신청이 정상 접수되었습니다! 3일 이내 순차적으로 회신드리겠습니다!")

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
        "기타 요청사항": special_request or "없음",
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
        confirm_msg = f"""
안녕하세요, 영원파파입니다 💒

의뢰 신청이 정상 접수되었습니다!
영원파파를 선택해주셔서 다시 한번 감사드립니다.

📌 **3일 이내 순차적으로 회신드리겠습니다.**

--- 신청 내용 ---
{email_body}

문의사항은 인스타그램 @0one.papa 로 편하게 연락주세요 💕
"""
        send_email(user_email, "[영원파파] 의뢰 접수 완료", confirm_msg)

# ============================================================================================
#                                   🌸 인스타 버튼
# ============================================================================================
st.markdown("""
<div style="text-align:center; margin-top:40px; margin-bottom:20px;">
    <a href="https://www.instagram.com/0one.papa/" target="_blank"
       style="
            font-size:1.3rem;
            font-family:Pretendard;
            font-weight:700;
            padding:18px 50px;
            background:linear-gradient(45deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888);
            color:white; border-radius:40px;
            text-decoration:none;
            box-shadow:0 6px 20px rgba(255,90,130,0.45);
        ">
        📸 Instagram @0one.papa
    </a>
</div>
""", unsafe_allow_html=True)
