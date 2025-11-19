import streamlit as st
from datetime import date
import smtplib
from email.mime.text import MIMEText

st.set_page_config(page_title="영원파파 결혼식 신청", layout="centered")

# =========================================================
# CSS (절대 들여쓰기 없음)
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gmarket+Sans:wght@700&family=Gowun+Batang:wght@400;700&Pretendard:wght@400;600;700&display=swap');

html,body,.stApp {background:#f6f2ea; font-family:Pretendard;}
.gold-card {width:860px; max-width:92%; margin:0 auto; padding:40px 50px; background:white; border-radius:32px; box-shadow:0 0 40px rgba(180,150,90,0.25);}
.header-box {padding:35px 20px; border-radius:32px; border:7px solid; border-image:linear-gradient(135deg,#bf9f63,#f6e9c8,#d6b67a) 1; background:rgba(255,255,255,0.65); box-shadow:inset 0 0 18px rgba(250,220,180,0.40);}
.title-kr {text-align:center; font-family:"Gmarket Sans"; font-size:1.5rem; font-weight:900; background:linear-gradient(90deg,#d1b06a,#f3e6c8,#c19d58); -webkit-background-clip:text; -webkit-text-fill-color:transparent;}
.title-en {text-align:center; font-size:2rem; font-weight:800; margin-top:6px; background:linear-gradient(90deg,#c8a266,#f0e4c2,#b78c4e); -webkit-background-clip:text; -webkit-text-fill-color:transparent;}
.gold-line {width:55%; height:2px; margin:20px auto; background:linear-gradient(90deg,transparent,#cbb27c,transparent);}
.title-sub {text-align:center; font-family:"Gowun Batang"; font-size:1.1rem; color:#8c7a66;}
.section-title {font-family:"Gmarket Sans"; font-size:1.25rem; color:#5a4a3a; margin-top:40px;}
.recommend-box {width:85%; margin:35px auto 0 auto; padding:28px 35px; background:white; border-radius:22px; border:4px solid; border-image:linear-gradient(135deg,#c9a564,#f3e6c5,#b89152) 1;}
.recommend-title {text-align:center; font-family:"Gmarket Sans"; font-size:1.45rem; margin-bottom:12px; background:linear-gradient(90deg,#d1b27a,#f3e4c3,#b89457); -webkit-background-clip:text; -webkit-text-fill-color:transparent;}
.song-item {padding:9px 0; font-size:1.05rem; border-bottom:1px solid #e8dcc7;}
.gold-divider {width:70%; height:4px; margin:40px auto; background:linear-gradient(90deg,transparent,#d2b67e,#f4e6c4,#d2b67e,transparent); border-radius:3px;}
.insta-box {margin-top:40px; text-align:center; padding:22px; border-radius:25px; border:4px solid; border-image:linear-gradient(135deg,#c9a564,#f3e6c5,#b89152) 1;}
.insta-box a {font-size:1.2rem; font-family:"Gmarket Sans"; text-decoration:none; color:#b89252;}
.insta-box a:hover {color:#d1ab6c;}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 헤더
# =========================================================
st.markdown("""
<div class="gold-card">
<div class="header-box">
<div class="title-kr">영원파파</div>
<div class="title-en">Wedding Ceremony with You</div>
<div class="gold-line"></div>
<div class="title-sub">Singing & Hosting Professional Service</div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 입력폼
# =========================================================
st.markdown('<div class="section-title">🎤 의뢰 서비스 선택</div>', unsafe_allow_html=True)
service = st.multiselect("", ["축가", "사회"], label_visibility="collapsed")

st.markdown('<div class="section-title">👰 기본 정보</div>', unsafe_allow_html=True)
role = st.radio("결혼식 주인공", ["신랑", "신부"])
name = st.text_input("이름")
age = st.number_input("만 나이", 18, 80)
wedding_date = st.date_input("예식일", value=date.today())

st.markdown('<div class="section-title">🏩 예식 정보</div>', unsafe_allow_html=True)
venue = st.selectbox("예식 장소", ["호텔", "하우스 웨딩", "야외", "컨벤션", "기타"])
venue_address = st.text_input("예식장 주소")
mood = st.radio("예식 분위기", ["낭만적 💞", "유쾌하게 😄", "격식 있게 🎩"])

host_style = None
if "사회" in service:
    st.markdown('<div class="section-title">🎙️ 사회 스타일</div>', unsafe_allow_html=True)
    host_style = st.radio("진행 스타일", ["담백·심플 (정석)", "센스 있고 위트 있게"])

song_pref = None
custom_song = None

if "축가" in service:
    st.markdown('<div class="section-title">🎵 축가 정보</div>', unsafe_allow_html=True)
    song_pref = st.radio("원하는 곡이 있나요?", ["네, 있어요", "추천해주세요!"])
    if song_pref == "네, 있어요":
        custom_song = st.text_input("축가 곡명 입력")

email = st.text_input("📧 이메일")
phone = st.text_input("📱 전화번호")
special_request = st.text_area("기타 요청사항")

# =========================================================
# 추천곡 + 인스타 (선택 시에만)
# =========================================================
if "축가" in service and song_pref == "추천해주세요!":
    st.markdown("""
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
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="insta-box">
    <a href="https://instagram.com/0one.papa" target="_blank">📸 영원파파 인스타그램 바로가기</a>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# 이메일 함수
# =========================================================
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

# =========================================================
# 제출 버튼
# =========================================================
if st.button("💌 신청서 제출하기"):

    st.success("의뢰 신청이 완료되었습니다! 💐")

    form_data = f"""
[영원파파 결혼식 의뢰 신청서]

주인공: {role}
이름: {name}
나이: {age}
예식일: {wedding_date}
예식 장소: {venue}
주소: {venue_address}
분위기: {mood}

선택 서비스: {", ".join(service)}
사회 스타일: {host_style}
축가 요청: {song_pref}
축가 곡명: {custom_song}

이메일: {email}
전화번호: {phone}
기타 요청사항:
{special_request}
"""

    send_email("hd261818@gmail.com", "[새 의뢰 신청]", form_data)

    if email:
        send_email(email, "[영원파파] 의뢰 접수 완료", "안녕하세요, 영원파파입니다!\n의뢰가 정상 접수되었습니다.\n3일 이내에 연락드리겠습니다.\n감사합니다💐")

# =========================================================
# 카드 닫기
# =========================================================
st.markdown("</div>", unsafe_allow_html=True)
