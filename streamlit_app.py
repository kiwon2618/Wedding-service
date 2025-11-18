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
@import url("https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Pretendard:wght@500;600;700&family=Gmarket+Sans:wght@700&display=swap");

body, .stApp {
    background: linear-gradient(rgba(255,255,255,0.96), rgba(255,255,255,0.94));
}

.white-flower {
    width: 140px;
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
#                            🌸 헤더 — Base64 이미지 + 텍스트 구성
# ============================================================================================
st.markdown(f"""
<div style="text-align:center; padding:50px 0 35px 0;">

    <img class="white-flower"
         src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAYAAACtWK6eAAAACXBIWXMAAAsTAAALEwEAmpwYAAAFQklEQVR4nO3dS47kMBCF4e9iYZaYhBECQ32npV+yqmSZxRcm4T/DPqVJzpuG1HsfrN7/fh9HAnCQAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOAe6qm7XTudFvPp5nU3lzjOB5nTnZnL5mWZbLOcOX3d1Wbjufnj+d1uO8c/Od5c5idbO45m7t/8m61s05l7t/NQx7dz1sN5vZ/Gn49uN8sVjzN5nYbznx8zzPW8P83Xn+3c+TDH8sV2/uznB/ZLbn8fZxj64uVx/nc067zzvn8PPx9nO/++n/8efOWecc/MPPB6OTY8fTLO8fLLef7b8f6/n5DckzjnL8nZ+Q4vrt85fjjmvzHWl7z/nJc8y9V53nP/j7rPcc8yfTnnHfL8ufPnj9l/PXzrPPzzrM+ybHPec4nH7n6znPPnm2jWZbOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOVWafAf6qcuSgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMB/AHECTHxpaiVfAAAAAElFTkSuQmCC">

    <div class="title-main">영원파파와 함께하는 아름다운 웨딩 세리머니</div>

    <img class="white-flower"
         src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAYAAACtWK6eAAAACXBIWXMAAAsTAAALEwEAmpwYAAAFQElEQVR4nO3dTY4bQRSG4XfDSRVA1nIG8VoWSiV4gCQGxQ+UKC2Ne33GyGY7n5xmPvH7N6N1+7v99P5/wMwkAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgDvoquu67q6b5nL5udiM87hszmdnMznM5Pzzk7rY/O5+u8e85XP83jOf5VnbzOfd85nX8VY/zOfdbu871n3POc+n3nOfT+c9z/v6PH5c87zvfPXL8/OeZ+zj7POc+b3XLec+fPez/nXjufPPNGzPGWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWabOWWafJcH8B5mPaa2wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADgPwHNCEsSfVB1AAAAAElFTkSuQmCC">
