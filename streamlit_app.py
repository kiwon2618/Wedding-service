import streamlit as st
from datetime import date
import smtplib
from email.mime.text import MIMEText
import re


# --- 페이지 설정 ---
st.set_page_config(page_title="영원파파 결혼식 축가·사회 의뢰", page_icon="💐", layout="centered")


# --- 이메일 전송 함수 ---
def send_email(to_email: str, subject: str, body: str) -> bool:
    """간단한 SMTP 전송. `st.secrets`에서 비밀번호를 읽습니다."""
    try:
        sender_email = "hd261818@gmail.com"
        sender_pw = None
        # 지원되는 secrets 구조를 확인
        if "gmail" in st.secrets:
            gmail = st.secrets.get("gmail", {})
            sender_pw = gmail.get("password")
            sender_email = gmail.get("user", sender_email)
        if not sender_pw and sender_email in st.secrets:
            sender_pw = st.secrets.get(sender_email, {}).get("password")

        if not sender_pw:


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
    host_style = st.radio(
        "원하시는 진행 스타일을 선택해주세요",
        ["담백하고 심플하게 (정석 스타일)", "센스 있고 위트 있게"],
    )


# --- 축가 선택 시 ---
song_pref = None
custom_song = None
selected_song = None
if "축가" in service:
    st.header("🎵 축가 관련 정보")
    song_pref = st.radio("원하는 노래가 있으신가요?", ["네, 있어요", "추천해주세요!"])
    if song_pref == "네, 있어요":
        custom_song = st.text_input("원하는 곡명을 입력해주세요")
    else:
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
        selected_song = st.selectbox("원하시는 곡을 선택해주세요 💕", song_list)


# --- 신청서 ---
st.header("📝 의뢰 신청서 작성")
col1, col2 = st.columns(2)
with col1:
    user_email = st.text_input("📧 이메일 주소")
with col2:
    user_phone = st.text_input("📱 연락 가능한 전화번호")

special_request = st.text_area("특이사항 / 기타 요청사항을 입력해주세요", height=120)


# --- 안내 문구 (사용자 요청) ---
st.markdown(
    """
    <div style='border-radius:8px;padding:12px 16px;margin-top:8px;background:#fffefc;border:1px solid #f0e6e6;'>
      <p style='color:#000;margin:0;line-height:1.3;'>1~3일 내 최대한 빠르게 확인하여 순차적으로 연락 드릴 예정입니다 :)</p>
      <p style='color:#000;margin:6px 0 0 0;line-height:1.3;'>영원파파를 선택해주셔서 진심으로 감사드립니다!</p>
    </div>
    """,
    unsafe_allow_html=True,
)


# --- 제출 버튼 및 처리 ---
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
            st.write(f"- 축가 곡: {custom_song if custom_song else '미입력'}")
        else:
            st.write(f"- 축가 곡: {selected_song if selected_song else '추천 리스트 중 선택 예정'}")
    if special_request:
        st.write(f"- 기타 요청사항: {special_request}")
    if user_email:
        st.write(f"- 이메일: {user_email}")
    if user_phone:
        st.write(f"- 전화번호: {user_phone}")

    # 이메일 본문 구성
    song_line = ""
    if "축가" in service:
        if song_pref == "네, 있어요":
            song_line = "▪ 축가 곡: " + (custom_song if custom_song else "미입력")
        else:
            song_line = "▪ 축가 곡: " + (selected_song if selected_song else "추천 리스트 중 선택 예정")

    host_line = ""
    if "사회" in service and host_style:
        host_line = "▪ 사회 스타일: " + host_style

    request_line = ""
    if special_request:
        request_line = "▪ 기타 요청사항: " + special_request

    email_body = f"""
💒 결혼식 축가·사회 의뢰 신청 정보 💒

▪ 주인공: {role}
▪ 이름: {name if name else '미입력'}
▪ 만나이: {age}
▪ 예식일: {wedding_date}
▪ 예식 장소: {venue}
▪ 예식장 주소: {venue_address if venue_address else '미입력'}
▪ 예식 분위기: {mood}
▪ 서비스: {', '.join(service)}

{host_line}
{song_line}
{request_line}

--- 연락처 ---
▪ 이메일: {user_email if user_email else '미입력'}
▪ 전화번호: {user_phone if user_phone else '미입력'}
"""

    # 관리자에게 전송
    if send_email("hd261818@gmail.com", "[새 의뢰] 결혼식 축가·사회 신청서", email_body):
        st.success("✅ 신청서가 영원파파에게 전송되었습니다!")
    else:
        st.error("❌ 관리자에게 신청서를 전송하는데 실패했습니다.")

    # 사용자 확인 메일
    if user_email:
        if not is_valid_email(user_email):
            st.warning("⚠️ 입력하신 이메일 주소 형식이 올바르지 않아 확인 메일을 발송하지 않았습니다.")
        else:
            user_msg = f"""
안녕하세요, 영원파파입니다 💒

결혼식 축가·사회 의뢰 신청이 정상적으로 접수되었습니다.
신청해주셔서 진심으로 감사드리며,
1~3일 내 최대한 빠르게 확인하여 순차적으로 연락 드리겠습니다 :)

--- 신청 내용 ---
{email_body}

문의사항이 있으시면 인스타그램 @0one.papa 또는 본 메일에 회신으로 연락주세요.

감사합니다.
"""
            if send_email(user_email, "[영원파파] 의뢰 신청 접수 완료", user_msg):
                st.success("✅ 확인 메일을 신청자에게 발송했습니다!")
            else:
                st.error("❌ 확인 메일 발송에 실패했습니다.")


# --- 인스타그램 링크 ---
st.markdown(
    """
    <div style="text-align: center; padding: 40px 20px;">
        <h3 style="color:#000;">📸 영원파파 인스타그램에서 실제 영상을 확인하세요!</h3>
        <a href="https://www.instagram.com/0one.papa/" target="_blank">
            <button style="background:linear-gradient(45deg,#333,#555);color:white;border:none;padding:12px 26px;border-radius:8px;font-weight:bold;cursor:pointer;">
                📸 Instagram @0one.papa
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)
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
            st.write(f"- 축가 곡: {custom_song if custom_song else '미입력'}")
        else:
            st.write(f"- 축가 곡: {selected_song if selected_song else '추천 리스트 중 선택 예정'}")
    if special_request:
        st.write(f"- 기타 요청사항: {special_request}")
    if user_email:
        st.write(f"- 이메일: {user_email}")
    if user_phone:
        st.write(f"- 전화번호: {user_phone}")

    # --- 이메일 발송 ---
    # 이메일에 들어갈 축가/사회/요청사항 라인 구성
    song_line = ""
    if "축가" in service:
        if song_pref == "네, 있어요":
            song_line = "▪ 축가 곡: " + (custom_song if custom_song else "미입력")
        else:
            song_line = "▪ 축가 곡: " + (selected_song if selected_song else "추천 리스트 중 선택 예정")

    host_line = ""
    if "사회" in service and host_style:
        host_line = "▪ 사회 스타일: " + host_style

    request_line = ""
    if special_request:
        request_line = "▪ 기타 요청사항: " + special_request

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

{host_line}
{song_line}
{request_line}

--- 연락처 ---
▪ 이메일: {user_email if user_email else "미입력"}
▪ 전화번호: {user_phone if user_phone else "미입력"}
"""

    # 관리자에게 전송
    if send_email("hd261818@gmail.com", "[새 의뢰] 결혼식 축가·사회 신청서", email_body):
        st.success("✅ 신청서가 영원파파에게 전송되었습니다!")

    # 사용자 확인 메일
        if user_email:
            if not is_valid_email(user_email):
                st.warning("⚠️ 입력하신 이메일 주소 형식이 올바르지 않아 확인 메일을 발송하지 않았습니다.")
            else:
        user_msg = f"""
안녕하세요, 영원파파입니다 💒

결혼식 축가·사회 의뢰 신청이 정상적으로 접수되었습니다.
신청해주셔서 진심으로 감사드리며,
1~3일 내 최대한 빠르게 확인하여 순차적으로 연락 드리겠습니다 :)

--- 신청 내용 ---
{email_body}

문의사항이 있으시면 인스타그램 @0one.papa 
또는 본 메일에 회신으로 연락주세요.

감사합니다 💐
"""
        
    # 사용자에게 확인 메일 발송
    send_email(user_email, "[영원파파] 의뢰 신청 접수 완료", user_msg)

# --- 인스타그램 링크 ---
st.markdown(
    """
    <div style="text-align: center; padding: 40px 20px;">
        <h3 style="color:#FF69B4;">📸 영원파파 인스타그램에서 실제 영상을 확인하세요!</h3>
        <a href="https://www.instagram.com/0one.papa/" target="_blank">
            <button style="background:linear-gradient(45deg,#f09433,#dc2743,#bc1888);
                           color:white;border:none;padding:15px 30px;
                           border-radius:30px;font-weight:bold;cursor:pointer;">
                📸 Instagram @0one.papa
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)




