import streamlit as st
from datetime import date
import smtplib
from email.mime.text import MIMEText

st.set_page_config(
    page_title="영원파파 결혼식 축가·사회 의뢰",
    page_icon="💐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CSS (들여쓰기 절대 금지)
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Gmarket+Sans:wght@700&family=Pretendard:wght@400;600;700&display=swap');

html, body, .stApp {
    background: #f8f4ed !important;
    font-family: "Pretendard", sans-serif !important;
    overflow-x: hidden !important;
}

/* Streamlit 기본 컨테이너 제거 */
.main .block-container {
    padding: 0 !important;
    max-width: 100% !important;
    margin: 0 !important;
}

/* 메인 카드 */
.card {
    width: 830px;
    max-width: 95%;
    background: rgba(255, 255, 255, 0.98);
    border-radius: 28px;
    padding: 48px 55px 70px 55px;
    margin: 0 auto;
    margin-top: 40px;
    margin-bottom: 40px;
    box-shadow: 
        0 0 50px rgba(0, 0, 0, 0.08),
        0 10px 60px rgba(0, 0, 0, 0.05),
        inset 0 1px 0 rgba(255, 255, 255, 0.9);
    position: relative;
    overflow: visible;
}

/* 카드 안의 모든 Streamlit 요소 */
.card ~ * {
    display: none !important;
}

.card .element-container,
.card [data-testid],
.card .stMarkdown,
.card .stSelectbox,
.card .stTextInput,
.card .stNumberInput,
.card .stDateInput,
.card .stRadio,
.card .stMultiselect,
.card .stTextArea,
.card .stButton,
.card .stSuccess,
.card .stInfo,
.card .stError {
    width: 100% !important;
    max-width: 100% !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
}

/* 배경 금가루 */
@keyframes goldDust {
    0% { opacity: 0.07; transform: translateY(0) scale(1); }
    50% { opacity: 0.16; transform: translateY(-18px) scale(1.15); }
    100% { opacity: 0.07; transform: translateY(0) scale(1); }
}

.gold-dust {
    position: absolute;
    top: -45px;
    left: 0;
    width: 100%;
    height: 180px;
    background-image: url('https://cdn.pixabay.com/photo/2015/01/08/18/25/gold-593119_1280.jpg');
    background-repeat: repeat-x;
    background-size: cover;
    opacity: 0.08;
    animation: goldDust 5s infinite ease-in-out;
    pointer-events: none;
    z-index: 1;
}

/* 꽃 패턴 */
.header-floral {
    width: 100%;
    height: 120px;
    background-image: url('https://cdn.pixabay.com/photo/2016/11/29/08/09/flower-1867614_1280.png');
    background-repeat: no-repeat;
    background-size: contain;
    background-position: center;
    opacity: 0.25;
    position: relative;
    z-index: 2;
    margin-top: -20px;
}

/* 금박 프레임 */
.header-frame {
    padding: 35px 30px 30px 30px;
    border-radius: 42px;
    border: 6px solid #d6b680;
    background: linear-gradient(135deg, 
        rgba(255, 255, 255, 0.65),
        rgba(250, 240, 230, 0.55),
        rgba(255, 255, 255, 0.65));
    box-shadow: 
        0 0 18px rgba(210, 180, 120, 0.35),
        inset 0 0 25px rgba(250, 240, 220, 0.45),
        inset 0 2px 10px rgba(255, 255, 255, 0.8);
    position: relative;
    z-index: 10;
    backdrop-filter: blur(8px);
}

/* 웨딩 이미지 */
.wedding-img {
    width: 140px;
    max-width: 100%;
    height: auto;
    opacity: 0.65;
    display: block;
    margin: 0 auto 15px auto;
    filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.1));
}

/* 타이틀 */
.title-main-kr {
    font-family: "Gmarket Sans", sans-serif;
    text-align: center;
    font-weight: 900;
    font-size: 2.1rem;
    color: #d36c87;
    margin: 10px 0 5px 0;
    text-shadow: 0 2px 4px rgba(211, 108, 135, 0.15);
    letter-spacing: -0.5px;
}

.title-main-en {
    text-align: center;
    margin-top: 4px;
    color: #8a6b6b;
    font-size: 1.15rem;
    font-weight: 600;
    font-family: "Pretendard", sans-serif;
    letter-spacing: 0.5px;
}

.gold-line {
    width: 55%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #d6b680, transparent);
    margin: 18px auto;
    box-shadow: 0 1px 3px rgba(214, 182, 128, 0.3);
}

.title-sub {
    font-family: "Gowun Batang", serif;
    text-align: center;
    font-size: 0.95rem;
    color: #9c8372;
    margin-top: 12px;
    letter-spacing: 0.3px;
}

/* Streamlit 요소 스타일링 */
.card h3 {
    font-family: "Pretendard", sans-serif;
    font-weight: 700;
    font-size: 1.2rem;
    color: #5a4a42;
    margin-top: 1.8rem;
    margin-bottom: 0.8rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid rgba(214, 182, 128, 0.2);
}

.card .stRadio > div > div > label,
.card .stCheckbox > label {
    font-family: "Pretendard", sans-serif;
    font-size: 1rem;
}

.card .stTextInput > div > div > input,
.card .stNumberInput > div > div > input,
.card .st
