st.markdown("""
<style>
@import url("https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&family=Pretendard:wght@600;700;800&family=Gmarket+Sans:wght@700&display=swap");

body, .stApp {
    background:
        linear-gradient(rgba(255,255,255,0.94), rgba(255,255,255,0.92)),
        url("https://www.transparenttextures.com/patterns/white-feather.png"),
        url("https://www.transparenttextures.com/patterns/white-floral.png"),
        url("https://images.unsplash.com/photo-1508973376-37031c9f9a43?w=1600&q=80") center/cover fixed;
    background-blend-mode: normal, screen, overlay, multiply;
}

.title-main {
    font-family: "Gmarket Sans", sans-serif;
    font-size: 3.6rem;
    font-weight: 800;
    color: #d37288;
    text-shadow: 0 0 6px rgba(255,200,210,0.6);
}

.title-sub {
    font-family: "Pretendard", sans-serif;
    font-size: 1.2rem;
    color: #8d6f62;
    font-weight: 600;
    margin-top: -5px;
}

.gold-line {
    width: 55%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #d8bba0, transparent);
    margin: 15px auto;
}

.white-flowers {
    width: 90px;
    filter: drop-shadow(0 3px 6px rgba(200,180,180,0.4));
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div style="text-align:center; padding:40px 0 25px 0;">
    <img class="white-flowers" src="https://cdn-icons-png.flaticon.com/512/7665/7665330.png">
    <div class="title-main">영원파파</div>
    <img class="white-flowers" src="https://cdn-icons-png.flaticon.com/512/7665/7665330.png">
    <div class="gold-line"></div>
    <p class="title-sub">Wedding Singer & Host Service</p>
    <p style="font-family:'Gowun Batang'; color:#a18478; font-size:0.92rem; margin-top:3px;">
        당신의 가장 특별한 순간을 더욱 아름답게 만들어드립니다
    </p>
</div>
""", unsafe_allow_html=True)
