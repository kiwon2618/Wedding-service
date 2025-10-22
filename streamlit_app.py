import streamlit as st
from datetime import date
import pandas as pd
import smtplib
from email.mime.text import MIMEText

# --- 페이지 설정 ---
st.set_page_config(page_title="영원파파 결혼식 축가·사회 의뢰", page_icon="💐", layout="centered")

# --- 이메일 전송 함수 ---
def send_email(to_email, subject, body):
    """SMTP를 통한 이메일 전송"""
    try:
        sender_email = "hd261818@gmail.com"
        sender_pw = st.secrets["email"]["password"]  # Gmail 앱 비밀번호 필요

        msg = MIMEText(body, _charset="utf-8")
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = to_email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, sender_pw)
            smtp.send_message(msg)
        return True
    except Exception as e:
        st.error(f"❌ 이메일 전송 실패: {e}")
        return False

# --- 스타일 (요약) ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Jua&display=swap');
    body, .stApp {
        background: linear-gradient(rgba(255,255,255,0.9), rgba(255,245,250,0.95)),
                    url('https://images.unsplash.com/photo-1519741497674-611481863552?w=1600&q=80') center/cover fixed !important;
        font-family: 'Gowun Batang', serif !important;
    }
    h1 { color:#FF69B4; text-align:center; font-family:'Jua',sans-serif; text-shadow:2px 2px 5px rgba(255,182,193,0.5); }
    label, p, div, span { color:#333 !important; }
    .stButton>button {
        background: linear-gradient(135deg,#FF69B4,#FFB6C1);
        color:white; border:none; border-radius:35px;
        padding:15px 40px; font-size:1.2rem; font-weight:bold;
        box-shadow:0 5px 15px rgba(255,105,180,0.4);
        font-family:'Jua',sans-serif;
    }
    .stButton>button:hover { transform:scale(1.05); }
    </style>
    """,
    unsafe_allow_html=True
)

# --- 헤더 ---
st.title("💒 영원파파 결혼식 축가·사회 의뢰")

st.markdown("""
<p style='text-align:center;color:#FF69B4;font-size:1.2rem;font-family:"Gowun Batang";'>
✨ 특별한 날을 더욱 특별하게 만들어드립니다 ✨
</p>
""", unsafe_allow_html=True)

# --- 서비스 선택 ---
st.header("🎤 의뢰 서비스 선택")
service = st.multiselect("원하시는 서비스를 선택해주세요", ["축가", "사회"])

# --- 기본 정보 입력 ---
st.header("👰🤵 기본 정보 입력")
role = st.radio("결혼식의 주인공을 선택해주세요", ["신랑", "신부"])
name = st.text_input("이름을 입력해주세요")
age = st.number_input("만 나이를 입력해주세요", min_value=18, max_value=80, step=1)
wedding_date = st.date_input("예식일을 선택해주세요", value=date.today())

# --- 예식 정보 ---
st.header("🏩 예식 정보")
venue = st.selectbox("예식 장소를 선택해주세요", ["호텔", "하우스 웨딩", "야외", "컨벤션", "기타"])
venue_address = st.text_input("예식장 상세 주소", placeholder="지역과 예식장명만 적어주시면 됩니다!")
mood = st.radio("예식 분위기를 선택해주세요", ["낭만적 💞", "유쾌하고 즐겁게 😄", "격식 있고 포멀하게 🎩"])

# --- 사회 선택 시 ---
host_style = None
if "사회" in service:
    st.header("📋 사회 스타일 선택")
    st.info("※ 모든 식순은 해당 식장 정보를 참고할 예정입니다.")
    host_style = st.radio(
        "원하시는 진행 스타일을 선택해주세요",
        ["담백하고 심플하게 (정석 스타일)", "센스 있고 위트 있게"]
    )

# --- 축가 선택 시 ---
song_pref, custom_song = None, None
if "축가" in service:
    st.header("🎵 축가 관련 정보")
    song_pref = st.radio("원하는 노래가 있으신가요?", ["네, 있어요", "추천해주세요!"])
    if song_pref == "네, 있어요":
        custom_song = st.text_input("원하는 곡명을 입력해주세요")
    else:
        st.write("🎶 추천곡 리스트 (예시)")
        song_list = [
            '1. 임영웅 - 이제 나만 믿어요',
            '2. 유해준 - 나에게 그대만이 (탑현 ver. 가능)',
            '3. 윤종신 - 오르막길',
            '4. 이석훈 - 그대를 사랑하는 10가지 이유',
            '5. 이준호 - 넌',
            '6. 허각 - 언제나',
            '7. 허각 - 물론',
            '8. 정승환 - 사뿐',
            '9. 유리상자 - 신부에게',
            '10. 김범수 - 사랑의 시작은 고백에서부터 (전상근 ver. 가능)',
            '11. 김범수 - 오직 너만',
            '12. 한동근 - 그대라는 사치',
            '13. 윤종신 - 그대 없이는 못살아 (늦가을 ver.)'
        ]
        df_songs = pd.DataFrame(song_list, columns=["추천곡 리스트"])
        st.dataframe(df_songs, use_container_width=True)
        st.caption("🎤 분위기와 취향에 따라 곡 분위기를 조정해드립니다. (탑현/전상근 ver. 가능)")

# --- 신청서 ---
st.header("📝 의뢰 신청서 작성")
col1, col2 = st.columns(2)
with col1:
    user_email = st.text_input("📧 이메일 주소")
with col2:
    user_phone = st.text_input("📱 연락 가능한 전화번호")

special_request = st.text_area("특이사항 / 기타 요청사항을 입력해주세요", height=120)

# --- 제출 버튼 ---
if st.button("💌 신청서 제출하기 💌"):
    st.success("의뢰 신청이 완료되었습니다! 💐")
    st.write("입력하신 정보 요약:")
    st.write(f"- 주인공: {role}")
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
    if user_email:
        st.write(f"- 이메일: {user_email}")
    if user_phone:
        st.write(f"- 전화번호: {user_phone}")

    # --- 이메일 발송 ---
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

--- 연락처 ---
▪ 이메일: {user_email if user_email else "미입력"}
▪ 전화번호: {user_phone if user_phone else "미입력"}
"""

    # 관리자에게 전송
    if send_email("hd261818@gmail.com", "[새 의뢰] 결혼식 축가·사회 신청서", email_body):
        st.success("✅ 신청서가 영원파파에게 전송되었습니다!")

    # 사용자 확인 메일
    if user_email:
        user_msg = f"""
안녕하세요, 영원파파입니다 💒

결혼식 축가·사회 의뢰 신청이 정상적으로 접수되었습니다.
신청해주셔서 진심으로 감사드리며,
📅 **7일 이내로 회신드리겠습니다.**

--- 신청 내용 ---
{email_body}

문의사항이 있으시면 인스타그램 @kiwon2618 
또는 본 메일에 회신으로 연락주세요.

감사합니다 💐
"""
        send_email(user_email, "[영원파파] 의뢰 신청 접수 완료", user_msg)

# --- 인스타그램 링크 ---
st.markdown(
    """
    <div style="text-align: center; padding: 40px 20px;">
        <h3 style="color:#FF69B4;">📸 영원파파 인스타그램에서 실제 영상을 확인하세요!</h3>
        <a href="https://www.instagram.com/kiwon2618/" target="_blank">
            <button style="background:linear-gradient(45deg,#f09433,#dc2743,#bc1888);
                           color:white;border:none;padding:15px 30px;
                           border-radius:30px;font-weight:bold;cursor:pointer;">
                📸 Instagram @kiwon2618
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)



