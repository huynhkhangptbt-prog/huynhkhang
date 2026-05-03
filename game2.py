import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Quiz Game Pro", layout="centered")

# ===== CSS =====
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #020617, #0f172a);
    padding: 20px;
    border-radius: 20px;
}

h1, h2 {
    text-align: center;
    color: #38bdf8;
}

.question-box {
    background: #1e293b;
    padding: 20px;
    border-radius: 20px;
    border: 2px solid #38bdf8;
}

.score {
    font-size: 40px;
    text-align: center;
    color: #facc15;
}
</style>
""", unsafe_allow_html=True)

# ===== STATE =====
if "screen" not in st.session_state:
    st.session_state.screen = "start"
if "q" not in st.session_state:
    st.session_state.q = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "hate" not in st.session_state:
    st.session_state.hate = ""
if "saved" not in st.session_state:
    st.session_state.saved = False

# ===== QUESTIONS =====
questions = [
    {"type": "mc", "q": "Món ăn yêu thích?", "options": ["Phở", "Pizza", "Trà sữa", "Cơm tấm"], "correct": "Phở"},
    {"type": "mc", "q": "Lúc rảnh làm gì?", "options": ["Ngủ", "Chơi game", "Xem phim", "Đọc sách"], "correct": "Chơi game"},
    {"type": "mc", "q": "Ghét nhất?", "options": ["Nóng", "Lạnh", "Mưa", "Bài tập"], "correct": "Nóng"},
    {"type": "mc", "q": "Hay nói gì?", "options": ["Đại đại đi", "Từ từ", "ha?", "Zạy đi"], "correct": "Zạy đi"},
    {"type": "mc", "q": "Màu thích?", "options": ["Đỏ", "Xanh dương", "Đen", "Trắng"], "correct": "Xanh dương"},
    {"type": "text", "q": "Bạn nghĩ tôi quý ai nhứt :33"}
]

FILE = "leaderboard.csv"

# ===== START =====
if st.session_state.screen == "start":
    st.title("🎮 QUIZ GAME DZUI DẺ")

    name = st.text_input("👤 Nhập tên:")

    if st.button("🚀 BẮT ĐẦU"):
        if name == "":
            st.warning("Nhập tên đã!")
        else:
            st.session_state.name = name
            st.session_state.screen = "game"
            st.session_state.saved = False
            st.rerun()

# ===== GAME =====
elif st.session_state.screen == "game":
    q_index = st.session_state.q
    total = len(questions)

    st.progress(q_index / total)

    q_data = questions[q_index]

    st.markdown('<div class="question-box">', unsafe_allow_html=True)

    if q_data["type"] == "mc":
        answer = st.radio(
            f"Câu {q_index+1}: {q_data['q']}",
            q_data["options"],
            index=None
        )
    else:
        answer = st.text_input(f"Câu {q_index+1}: {q_data['q']}")

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("➡️ NEXT"):
        if answer is None or answer == "":
            st.warning("Trả lời đã!")
        else:
            if q_data["type"] == "mc":
                if answer == q_data["correct"]:
                    st.session_state.score += 1
            else:
                st.session_state.hate = answer

            st.session_state.q += 1

            if st.session_state.q >= total:
                st.session_state.screen = "result"

            st.rerun()

# ===== RESULT =====
elif st.session_state.screen == "result":
    st.title("🏆 KẾT QUẢ")

    score = st.session_state.score
    name = st.session_state.name
    hate = st.session_state.hate

    st.markdown(f'<div class="score">{score}/5</div>', unsafe_allow_html=True)

    if score == 5:
        st.balloons()
        st.success("🔥 bạn hỉu Kheng phết :33")
    elif score >= 3:
        st.info("👍 Cũng cũng")
    else:
        st.warning("Bạn chẳng hỉu mình gì cả 😢")

    # ===== AUTO SAVE =====
    if not st.session_state.saved:
        new = pd.DataFrame({
            "Tên": [name],
            "Điểm": [score],
            "Quý ai": [hate]
        })

        if os.path.exists(FILE):
            old = pd.read_csv(FILE)
            data = pd.concat([old, new], ignore_index=True)
        else:
            data = new

        data = data.sort_values(by="Điểm", ascending=False)
        data.to_csv(FILE, index=False)

        st.session_state.saved = True

    # ===== LEADERBOARD =====
    if os.path.exists(FILE):
        st.subheader("🏆 LEADERBOARD")
        df = pd.read_csv(FILE)
        st.dataframe(df, use_container_width=True)

    # ===== RESTART =====
    if st.button("🔄 CHƠI LẠI"):
        st.session_state.q = 0
        st.session_state.score = 0
        st.session_state.hate = ""
        st.session_state.screen = "start"
        st.session_state.saved = False
        st.rerun()