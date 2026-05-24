import streamlit as st
import random
import time
import json
import os

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="💰 Tài Xỉu Casino",
    page_icon="🎲",
    layout="centered"
)

# =========================
# DATABASE FILE
# =========================
DB_FILE = "users.json"

# Tạo file nếu chưa có
if not os.path.exists(DB_FILE):

    default_users = {
        "admin": {
            "password": "123",
            "balance": 1000,
            "level": 1,
            "exp": 0,
            "win_streak": 0,
            "history": []
        }
    }

    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(default_users, f, indent=4)

# =========================
# LOAD DATABASE
# =========================
with open(DB_FILE, "r", encoding="utf-8") as f:
    users_data = json.load(f)

st.session_state.users = users_data

# =========================
# SAVE DATABASE
# =========================
def save_users():

    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(
            st.session_state.users,
            f,
            indent=4
        )

# =========================
# LOGIN STATE
# =========================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "current_user" not in st.session_state:
    st.session_state.current_user = ""

if "game_message" not in st.session_state:
    st.session_state.game_message = None

# =========================
# LOGIN / REGISTER
# =========================
if not st.session_state.logged_in:

    st.title("🎮 Casino Login System")

    menu = st.tabs(["🔐 Đăng nhập", "📝 Đăng ký"])

    # =====================
    # LOGIN
    # =====================
    with menu[0]:

        st.subheader("🔐 Đăng nhập")

        login_user = st.text_input(
            "Tên đăng nhập",
            key="login_user"
        )

        login_pass = st.text_input(
            "Mật khẩu",
            type="password",
            key="login_pass"
        )

        if st.button("Đăng nhập"):

            users = st.session_state.users

            if (
                login_user in users and
                users[login_user]["password"] == login_pass
            ):

                st.session_state.logged_in = True
                st.session_state.current_user = login_user

                st.success("Đăng nhập thành công!")

                st.rerun()

            else:

                st.error("Sai tài khoản hoặc mật khẩu!")

    # =====================
    # REGISTER
    # =====================
    with menu[1]:

        st.subheader("📝 Đăng ký")

        reg_user = st.text_input(
            "Tên tài khoản",
            key="reg_user"
        )

        reg_pass = st.text_input(
            "Mật khẩu",
            type="password",
            key="reg_pass"
        )

        if st.button("Tạo tài khoản"):

            users = st.session_state.users

            if reg_user in users:

                st.warning("Tài khoản đã tồn tại!")

            elif len(reg_user) < 3:

                st.warning("Tên quá ngắn!")

            elif len(reg_pass) < 3:

                st.warning("Mật khẩu quá ngắn!")

            else:

                users[reg_user] = {
                    "password": reg_pass,
                    "balance": 1000,
                    "level": 1,
                    "exp": 0,
                    "win_streak": 0,
                    "history": []
                }

                save_users()

                st.session_state.logged_in = True
                st.session_state.current_user = reg_user

                st.success("🎉 Đăng ký thành công!")

                st.rerun()

    st.stop()

# =========================
# LOAD USER DATA
# =========================
username = st.session_state.current_user

if username not in st.session_state.users:

    st.session_state.logged_in = False
    st.stop()

user_data = st.session_state.users[username]

# =========================
# TITLE
# =========================
st.title("🎲 Sòng Bạc Tài Xỉu")

st.caption(f"Xin chào {username} 😎")

# =========================
# GAME MESSAGE
# =========================
if st.session_state.game_message:

    msg_type = st.session_state.game_message["type"]
    msg_text = st.session_state.game_message["text"]

    if msg_type == "success":
        st.success(msg_text)

    elif msg_type == "error":
        st.error(msg_text)

    elif msg_type == "warning":
        st.warning(msg_text)

    st.session_state.game_message = None

# =========================
# TUTORIAL
# =========================
with st.expander("📖 Hướng dẫn chơi"):

    st.markdown("""
    ## 🎲 Cách chơi Tài Xỉu

    - Chọn số tiền muốn cược
    - Chọn cửa:
        - 🎯 Tài = tổng xúc xắc từ 11 → 18
        - 🎯 Xỉu = tổng xúc xắc từ 3 → 10
    - Nhấn nút 🔥 ĐẶT CƯỢC để chơi

    ---

    ## 💰 Phần thưởng

    ### 🎉 Thắng thường
    - Nhận đúng số xu đã cược

    ### 💎 Critical x2
    - 10% tỉ lệ xuất hiện
    - Tiền thắng nhân đôi

    ### 🎰 Jackpot x3
    - Khi ra 3 xúc xắc giống nhau
    - Tiền thưởng x3

    ---

    ## ⭐ EXP & Level

    - Mỗi trận thắng nhận EXP ngẫu nhiên
    - Đủ EXP sẽ lên cấp
    - Lên cấp nhận thưởng xu

    ---

    ## 🔥 Win Streak

    - Thắng liên tiếp 5 trận:
        - nhận bonus 500 xu

    ---

    ## 💀 Cháy túi

    Khi hết tiền:
    - Có thể reset tài khoản
    - Nhận lại 1000 xu
    """)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("👤 Profile")

st.sidebar.write(f"🧑 User: {username}")

st.sidebar.metric(
    "💰 Số dư",
    f"{user_data['balance']} xu"
)

st.sidebar.metric(
    "🏆 Level",
    user_data["level"]
)

st.sidebar.metric(
    "🔥 Win Streak",
    user_data["win_streak"]
)

# =========================
# EXP BAR
# =========================
need_exp = user_data["level"] * 100

st.sidebar.write("⭐ EXP")

st.sidebar.progress(
    min(user_data["exp"] / need_exp, 1.0)
)

st.sidebar.write(
    f"{user_data['exp']} / {need_exp}"
)

# =========================
# LOGOUT
# =========================
if st.sidebar.button("🚪 Đăng xuất"):

    st.session_state.logged_in = False

    if "current_user" in st.session_state:
        del st.session_state["current_user"]

    st.rerun()

# =========================
# GAME INPUT
# =========================
bet_amount = st.number_input(
    "💵 Số tiền cược:",
    min_value=1,
    max_value=max(1, user_data["balance"]),
    value=100
)

choice = st.radio(
    "🎯 Chọn cửa:",
    ["Tài", "Xỉu"],
    horizontal=True
)

# =========================
# PLAY BUTTON
# =========================
if st.button("🔥 ĐẶT CƯỢC"):

    if bet_amount > user_data["balance"]:

        st.error("❌ Không đủ tiền!")

    else:

        with st.spinner("🎲 Đang lắc xúc xắc..."):
            time.sleep(2)

        # =====================
        # ROLL
        # =====================
        xuc_xac = [random.randint(1, 6) for _ in range(3)]

        tong = sum(xuc_xac)

        ket_qua = "Tài" if tong >= 11 else "Xỉu"

        # =====================
        # DISPLAY
        # =====================
        st.subheader(f"🎲 Xúc xắc: {xuc_xac}")

        st.write(f"👉 Tổng: {tong}")

        st.write(f"🏁 Kết quả: {ket_qua}")

        # =====================
        # JACKPOT
        # =====================
        jackpot = (
            xuc_xac[0] ==
            xuc_xac[1] ==
            xuc_xac[2]
        )

        # =====================
        # WIN
        # =====================
        if choice == ket_qua:

            reward = bet_amount

            # Critical
            if random.randint(1, 10) == 1:

                reward *= 2

                st.success("💎 CRITICAL x2!")

            # Jackpot
            if jackpot:

                reward *= 3

                st.success("🎰 JACKPOT x3!")

                st.snow()

            # Money
            user_data["balance"] += reward

            # Streak
            user_data["win_streak"] += 1

            # EXP
            gain_exp = random.randint(20, 50)

            user_data["exp"] += gain_exp

            st.success(
                f"⭐ +{gain_exp} EXP"
            )

            st.success(
                f"🎉 THẮNG +{reward} xu"
            )

            st.balloons()

            st.session_state.game_message = {
                "type": "success",
                "text": f"🎉 Bạn thắng +{reward} xu!"
            }

        # =====================
        # LOSE
        # =====================
        else:

            user_data["balance"] -= bet_amount

            user_data["win_streak"] = 0

            st.error(
                f"💀 THUA -{bet_amount} xu"
            )

            st.session_state.game_message = {
                "type": "error",
                "text": f"💀 Bạn thua -{bet_amount} xu!"
            }

        save_users()

        st.rerun()

# =========================
# LEVEL UP
# =========================
need_exp = user_data["level"] * 100

if user_data["exp"] >= need_exp:

    user_data["exp"] -= need_exp

    user_data["level"] += 1

    level_reward = user_data["level"] * 200

    user_data["balance"] += level_reward

    save_users()

    st.success(
        f"🎉 LEVEL UP → Lv.{user_data['level']}"
    )

    st.success(
        f"💰 Thưởng {level_reward} xu"
    )

    st.balloons()

# =========================
# WIN STREAK BONUS
# =========================
if user_data["win_streak"] == 5:

    bonus = 500

    user_data["balance"] += bonus

    user_data["win_streak"] = 0

    save_users()

    st.success(
        f"🔥 WIN STREAK BONUS +{bonus}"
    )

# =========================
# GAME OVER
# =========================
if user_data["balance"] <= 0:

    st.warning("💀 Bạn cháy túi!")

    if st.button("🔄 Reset tài khoản"):

        user_data["balance"] = 1000
        user_data["level"] = 1
        user_data["exp"] = 0
        user_data["win_streak"] = 0
        user_data["history"] = []

        save_users()

        st.rerun()
