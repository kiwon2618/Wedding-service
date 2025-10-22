import streamlit as st
from datetime import date
import pandas as pd
import smtplib
from email.mime.text import MIMEText

# --- 페이지 설정 ---
st.set_page_config(page_title="영원파파 결혼식 축가·사회 의뢰", page_icon="💐", layout="centered")

# --- 스타일 (귀여운 결혼식 전문 의뢰 사이트) ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Jua&family=Cute+Font&family=Gamja+Flower&display=swap');
    
    body {
        background: 
            linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 245, 250, 0.9)),
            url('https://images.unsplash.com/photo-1519741497674-611481863552?w=1600&q=80') center/cover fixed !important;
        font-family: 'Gowun Batang', serif !important;
    }
    
    .stApp {
        background: 
            linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 245, 250, 0.9)),
            url('https://images.unsplash.com/photo-1519741497674-611481863552?w=1600&q=80') center/cover fixed !important;
    }
    
    /* 헤더 디자인 */
    h1 {
        font-family: 'Jua', sans-serif !important;
        color: #FF6B9D !important;
        font-size: 2.5rem !important;
        text-align: center !important;
        padding: 20px 0 !important;
        text-shadow: 3px 3px 6px rgba(255, 182, 193, 0.5) !important;
        letter-spacing: 2px !important;
    }
    
    h2, h3 {
        font-family: 'Gamja Flower', cursive !important;
        color: #FF69B4 !important;
        margin-top: 30px !important;
        font-size: 1.5rem !important;
    }
    
    /* 콘텐츠 컨테이너 */
    .block-container {
        background: rgba(255, 255, 255, 0.95) !important;
        padding: 40px 30px !important;
        border-radius: 25px !important;
        box-shadow: 0 10px 40px rgba(255, 105, 180, 0.2) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    /* 입력 필드 스타일 */
    .stTextInput > div > div > input, 
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > div,
    .stNumberInput input, 
    .stDateInput input {
        background-color: #FFF !important;
        border: 3px solid #FFD4E5 !important;
        border-radius: 15px !important;
        color: #333 !important;
        font-family: 'Gowun Batang', serif !important;
        font-size: 1rem !important;
        padding: 10px 15px !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus, 
    .stTextArea > div > div > textarea:focus {
        border-color: #FF69B4 !important;
        box-shadow: 0 0 15px rgba(255, 105, 180, 0.4) !important;
        transform: scale(1.02) !important;
    }
    
    /* 버튼 스타일 */
    .stButton > button {
        background: linear-gradient(135deg, #FF69B4 0%, #FFB6C1 50%, #FFC0CB 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 35px !important;
        padding: 18px 50px !important;
        font-size: 1.3rem !important;
        font-weight: bold !important;
        box-shadow: 0 8px 25px rgba(255, 105, 180, 0.5) !important;
        transition: all 0.4s ease !important;
        font-family: 'Jua', sans-serif !important;
        letter-spacing: 3px !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-5px) scale(1.05) !important;
        box-shadow: 0 12px 35px rgba(255, 105, 180, 0.7) !important;
        background: linear-gradient(135deg, #FF1493 0%, #FF69B4 50%, #FFB6C1 100%) !important;
    }
    
    /* 라벨 스타일 */
    label {
        color: #FF1493 !important;
        font-weight: 700 !important;
        font-family: 'Gamja Flower', cursive !important;
        font-size: 1.1rem !important;
    }
    
    /* 인포 박스 */
    .stAlert {
        background: linear-gradient(135deg, #FFF0F5 0%, #FFE4E9 100%) !important;
        border-left: 5px solid #FF69B4 !important;
        border-radius: 15px !important;
        font-family: 'Gowun Batang', serif !important;
        box-shadow: 0 4px 15px rgba(255, 105, 180, 0.15) !important;
    }
    
    /* 성공 메시지 */
    .stSuccess {
        background: linear-gradient(135deg, #F0FFF4 0%, #E8F5E9 100%) !important;
        color: #2D5F3F !important;
        border-radius: 15px !important;
        border-left: 5px solid #4CAF50 !important;
        font-family: 'Jua', sans-serif !important;
        box-shadow: 0 4px 15px rgba(76, 175, 80, 0.2) !important;
    }
    
    /* 데이터프레임 */
    .stDataFrame {
        border-radius: 15px !important;
        box-shadow: 0 4px 15px rgba(255, 105, 180, 0.15) !important;
    }
    
    /* 라디오/체크박스 */
    .stRadio > div, .stMultiSelect > div {
        background: rgba(255, 255, 255, 0.8) !important;
        padding: 15px !important;
        border-radius: 15px !important;
        border: 2px solid #FFE4E9 !important;
    }
    
    /* 구분선 */
    hr {
        border: none !important;
        height: 3px !important;
        background: linear-gradient(90deg, transparent, #FF69B4, transparent) !important;
        margin: 40px 0 !important;
    }
    
    /* 텍스트 */
    p {
        font-family: 'Gowun Batang', serif !important;
        line-height: 1.8 !important;
    }
    
    /* 스크롤바 커스터마이징 */
    ::-webkit-scrollbar {
        width: 10px;
    }
    ::-webkit-scrollbar-track {
        background: #FFE4E9;
    }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #FF69B4, #FFB6C1);
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- 상단 헤더 ---
st.markdown(
    """
    <div style="text-align: center; padding: 30px 20px; background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(255, 240, 245, 0.95)); border-radius: 25px; box-shadow: 0 10px 30px rgba(255, 105, 180, 0.3); margin-bottom: 30px; border: 3px solid #FFE4E9;">
        <div style="font-size: 4rem; margin-bottom: 15px; animation: float 3s ease-in-out infinite;">
            💕 🌸 💐 🌸 💕
        </div>
        <h1 style="margin: 0; font-family: 'Jua', sans-serif; color: #FF1493; font-size: 2.8rem; text-shadow: 3px 3px 8px rgba(255, 105, 180, 0.4);">
            영원파파
        </h1>
        <p style="color: #FF69B4; font-size: 1.4rem; margin: 15px 0; font-family: 'Gamja Flower', cursive; font-weight: bold;">
            결혼식 축가·사회 전문 의뢰
        </p>
        <p style="color: #999; font-size: 1rem; margin-top: 10px; font-family: 'Gowun Batang', serif;">
            ✨ 특별한 날을 더욱 특별하게 만들어드립니다 ✨
        </p>
        <div style="font-size: 2.5rem; margin-top: 15px;">
            💒 ❤️ 🎀
        </div>
    </div>
    
    <style>
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- 구분선 ---
st.markdown("<div style='text-align: center; font-size: 2rem; margin: 20px 0;'>🌺 🌺 🌺</div>", unsafe_allow_html=True)

# --- 서비스 선택 (맨 위로 이동) ---
st.markdown(
    """
    <div style='background: linear-gradient(135deg, #FFF5F8, #FFE4EC); padding: 20px; border-radius: 20px; border: 2px solid #FFD4E5; margin-bottom: 20px;'>
        <h3 style='margin: 0; font-family: "Gamja Flower", cursive; color: #FF1493; font-size: 1.8rem;'>🎤 의뢰 서비스 선택</h3>
        <p style='color: #999; font-size: 1rem; margin: 10px 0 0 0; font-family: "Gowun Batang", serif;'>원하시는 서비스를 선택해주세요</p>
    </div>
    """,
    unsafe_allow_html=True
)
service = st.multiselect("", ["축가", "사회"], label_visibility="collapsed")

st.markdown("<div style='text-align: center; font-size: 1.5rem; margin: 30px 0;'>💕 💕 💕</div>", unsafe_allow_html=True)

# --- 기본 정보 입력 ---
st.markdown(
    """
    <div style='background: linear-gradient(135deg, #FFF5F8, #FFE4EC); padding: 20px; border-radius: 20px; border: 2px solid #FFD4E5; margin-bottom: 20px;'>
        <h3 style='margin: 0; font-family: "Gamja Flower", cursive; color: #FF1493; font-size: 1.8rem;'>👰🤵 기본 정보 입력</h3>
        <p style='color: #999; font-size: 1rem; margin: 10px 0 0 0; font-family: "Gowun Batang", serif;'>신랑신부의 기본 정보를 알려주세요</p>
    </div>
    """,
    unsafe_allow_html=True
)
role = st.radio("결혼식의 주인공을 선택해주세요", ["신랑", "신부"])
name = st.text_input("이름을 입력해주세요")
age = st.number_input("만 나이를 입력해주세요", min_value=18, max_value=80, step=1)
wedding_date = st.date_input("예식일을 선택해주세요", value=date.today())

st.markdown("<div style='text-align: center; font-size: 1.8rem; margin: 30px 0;'>🌹 ✨ 🌹</div>", unsafe_allow_html=True)

# --- 예식 장소 & 분위기 ---
st.markdown(
    """
    <div style='background: linear-gradient(135deg, #FFF5F8, #FFE4EC); padding: 20px; border-radius: 20px; border: 2px solid #FFD4E5; margin-bottom: 20px;'>
        <h3 style='margin: 0; font-family: "Gamja Flower", cursive; color: #FF1493; font-size: 1.8rem;'>🏩💒 예식 정보</h3>
        <p style='color: #999; font-size: 1rem; margin: 10px 0 0 0; font-family: "Gowun Batang", serif;'>예식 장소와 분위기를 알려주세요</p>
    </div>
    """,
    unsafe_allow_html=True
)
venue = st.selectbox("예식 장소를 선택해주세요", ["호텔", "하우스 웨딩", "야외", "컨벤션", "기타"])
venue_address = st.text_input("예식장 상세 주소", placeholder="지역과 예식장명만 적어주시면 됩니다!")
mood = st.radio("예식 분위기를 선택해주세요", ["낭만적 💞", "유쾌하고 즐겁게 😄", "격식 있고 포멀하게 🎩"])

# --- 사회 선택 시 ---
host_style = None
if "사회" in service:
    st.markdown("<div style='text-align: center; font-size: 1.8rem; margin: 30px 0;'>🎙️ ✨ 🎙️</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style='background: linear-gradient(135deg, #FFF5F8, #FFE4EC); padding: 20px; border-radius: 20px; border: 2px solid #FFD4E5; margin-bottom: 20px;'>
            <h3 style='margin: 0; font-family: "Gamja Flower", cursive; color: #FF1493; font-size: 1.8rem;'>📋🎤 사회 스타일 선택</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.info("※ 모든 식순은 해당 식장 정보를 참고할 예정입니다.")
    host_style = st.radio(
        "원하시는 진행 스타일을 선택해주세요",
        ["담백하고 심플하게 (정석 스타일)", "센스 있고 위트 있게"]
    )

# --- 축가 선택 시 ---
song_pref, custom_song = None, None
if "축가" in service:
    st.markdown("<div style='text-align: center; font-size: 1.8rem; margin: 30px 0;'>🎵 ✨ 🎶</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style='background: linear-gradient(135deg, #FFF5F8, #FFE4EC); padding: 20px; border-radius: 20px; border: 2px solid #FFD4E5; margin-bottom: 20px;'>
            <h3 style='margin: 0; font-family: "Gamja Flower", cursive; color: #FF1493; font-size: 1.8rem;'>🎤🎵 축가 관련 정보</h3>
            <p style='color: #999; font-size: 1rem; margin: 10px 0 0 0; font-family: "Gowun Batang", serif;'>원하시는 축가 곡을 알려주세요</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    song_pref = st.radio("원하는 노래가 있으신가요?", ["네, 있어요", "추천해주세요!"])
    if song_pref == "네, 있어요":
        custom_song = st.text_input("원하는 곡명을 입력해주세요")
    else:
        st.write("🎶 추천곡 리스트 (예시)")
        sample_songs = ["사랑하나요 - 유리상자", "두사람 - 박정현", "Marry Me - Jason Derulo", "축가 추천 리스트.csv"]
        st.dataframe(pd.DataFrame(sample_songs, columns=["추천곡"]))
        st.caption("※ 추후 직접 파일로 교체 가능합니다.")

st.markdown("<div style='text-align: center; font-size: 1.8rem; margin: 30px 0;'>✍️ 💌 ✍️</div>", unsafe_allow_html=True)

# --- 신청서 ---
st.markdown(
    """
    <div style='background: linear-gradient(135deg, #FFF5F8, #FFE4EC); padding: 20px; border-radius: 20px; border: 2px solid #FFD4E5; margin-bottom: 20px;'>
        <h3 style='margin: 0; font-family: "Gamja Flower", cursive; color: #FF1493; font-size: 1.8rem;'>📝💕 의뢰 신청서 작성</h3>
        <p style='color: #999; font-size: 1rem; margin: 10px 0 0 0; font-family: "Gowun Batang", serif;'>연락처와 추가 요청사항을 남겨주세요</p>
    </div>
    """,
    unsafe_allow_html=True
)

# 연락처 입력 (두 칸으로 분리)
col1, col2 = st.columns(2)
with col1:
    user_email = st.text_input("📧 연락 가능한 이메일")
with col2:
    user_phone = st.text_input("📱 연락 가능한 핸드폰번호")

special_request = st.text_area("특이사항 / 기타 요청사항을 입력해주세요", height=120)

# --- 이메일 전송 함수 ---
def send_email(to_email, subject, body):
    """SMTP를 통한 이메일 전송"""
    try:
        # st.secrets에서 이메일 설정 가져오기
        if "email" not in st.secrets:
            st.warning("⚠️ 이메일 설정이 필요합니다. 아래 내용을 관리자에게 전달해주세요.")
            st.code(body)
            return False
            
        sender_email = st.secrets["email"]["address"]
        sender_pw = st.secrets["email"]["password"]

        msg = MIMEText(body, _charset="utf-8")
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = to_email

        # Gmail SMTP 사용
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, sender_pw)
            smtp.send_message(msg)
        return True
    except KeyError:
        st.warning("⚠️ 이메일 설정이 없습니다. 신청 내용:")
        st.code(body)
        return False
    except Exception as e:
        st.error(f"❌ 이메일 전송 실패: {e}")
        st.info("📋 신청 내용 (수동으로 전달해주세요):")
        st.code(body)
        return False

# --- 제출 버튼 ---
st.markdown("<div style='text-align: center; margin: 40px 0 20px 0;'>", unsafe_allow_html=True)
if st.button("💌 신청서 제출하기 💌"):
    st.success("의뢰 신청이 완료되었습니다! 💐")
    st.write("입력하신 정보 요약:")
    st.write(f"- 주인공: {role}")
    if name:
        st.write(f"- 이름: {name}")
    st.write(f"- 만나이: {age}")
    st.write(f"- 예식일: {wedding_date}")
    st.write(f"- 예식 장소: {venue}")
    if venue_address:
        st.write(f"- 예식장 주소: {venue_address}")
    st.write(f"- 예식 분위기: {mood}")
    st.write(f"- 서비스: {', '.join(service)}")

    if "사회" in service:
        st.write(f"- 사회 스타일: {host_style}")
    if "축가" in service:
        if song_pref == "네, 있어요":
            st.write(f"- 축가 곡: {custom_song}")
        else:
            st.write("- 축가: 추천 리스트 중 선택 예정")
    if special_request:
        st.write(f"- 기타 요청사항: {special_request}")
    
    # 연락처 정보 표시
    if user_email:
        st.write(f"- 이메일: {user_email}")
    if user_phone:
        st.write(f"- 핸드폰: {user_phone}")

    # --- 이메일 자동 발송 ---
    if user_email or user_phone:
        # 신청서 본문 작성
        email_body = f"""
💒 결혼식 축가·사회 의뢰 신청 정보 💒

▪ 주인공: {role}
▪ 이름: {name if name else "미입력"}
▪ 만나이: {age}
▪ 예식일: {wedding_date}
▪ 예식 장소: {venue}
▪ 예식장 주소: {venue_address if venue_address else "미입력"}
▪ 예식 분위기: {mood}
▪ 서비스: {', '.join(service)}

{"▪ 사회 스타일: " + host_style if host_style else ""}
{"▪ 축가 곡: " + custom_song if custom_song else ""}
{"▪ 기타 요청사항: " + special_request if special_request else ""}

--- 연락처 정보 ---
▪ 이메일: {user_email if user_email else "미입력"}
▪ 핸드폰: {user_phone if user_phone else "미입력"}

감사합니다 💐
        """
        
        # 관리자(영원파파)에게 신청서 전송
        admin_email = "hd261818@gmail.com"
        if send_email(admin_email, "[새 의뢰] 결혼식 축가·사회 신청서", email_body):
            st.success(f"✅ 신청서가 영원파파에게 전송되었습니다!")
        
        # 사용자에게 확인 메일 전송 (이메일을 입력한 경우)
        if user_email:
            user_confirm_body = f"""
안녕하세요, 영원파파입니다! 💒

결혼식 축가·사회 의뢰 신청이 정상적으로 접수되었습니다.
빠른 시일 내에 연락드리겠습니다.

--- 신청 내용 ---
{email_body}

문의사항이 있으시면 인스타그램 @kiwon2618 또는 회신 메일로 연락주세요.

감사합니다 💐
            """
            send_email(user_email, "[영원파파] 의뢰 신청 접수 완료", user_confirm_body)

st.markdown("</div>", unsafe_allow_html=True)

# --- 인스타그램 링크 (맨 마지막) ---
st.markdown("<div style='text-align: center; font-size: 1.5rem; margin: 50px 0 30px 0;'>🌸 💗 🌸</div>", unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align: center; padding: 30px 20px; background: linear-gradient(135deg, #FFF 0%, #FFF5F8 100%); border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin: 20px 0;">
        <div style="font-size: 1.8rem; margin-bottom: 15px;">
            📸 ✨ 💕
        </div>
        <p style="font-size: 1.2rem; color: #D4516A; font-weight: bold; margin-bottom: 10px; font-family: 'Noto Serif KR', serif;">
            영상 정보 참고하기
        </p>
        <p style="font-size: 0.9rem; color: #888; margin-bottom: 20px;">
            실제 축가·사회 영상을 인스타그램에서 확인하세요!
        </p>
        <a href="https://www.instagram.com/kiwon2618/" target="_blank" style="text-decoration: none;">
            <button style="
                background: linear-gradient(45deg, #f09433 0%,#e6683c 25%,#dc2743 50%,#cc2366 75%,#bc1888 100%); 
                color: white; 
                border: none; 
                padding: 15px 35px; 
                border-radius: 30px; 
                font-size: 1.1rem; 
                font-weight: bold;
                cursor: pointer;
                box-shadow: 0 4px 15px rgba(225, 48, 108, 0.4);
                transition: all 0.3s ease;
                font-family: 'Nanum Gothic', sans-serif;
            " onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 6px 20px rgba(225, 48, 108, 0.6)';" 
               onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 15px rgba(225, 48, 108, 0.4)';">
                📸 Instagram @kiwon2618
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# --- 푸터 ---
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px; padding: 20px; color: #999; font-size: 0.85rem;">
        <p style="margin: 5px 0;">💒 영원파파 결혼식 축가·사회 의뢰</p>
        <p style="margin: 5px 0;">특별한 날을 더욱 특별하게</p>
        <div style="font-size: 1.2rem; margin-top: 15px;">
            💐 ✨ 💐
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


