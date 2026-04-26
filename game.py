import streamlit as st
import random
import time

st.set_page_config(page_title="Tài Xỉu Siêu Cấp", page_icon="💰")

# Khởi tạo dữ liệu người chơi
if 'balance' not in st.session_state:
    st.session_state.balance = 1000  # Bắt đầu với 1000 xu

st.title("💰 Welcome to sòng Bạc xỉu của Khàng")
st.sidebar.metric(label="Số dư hiện tại", value=f"{st.session_state.balance} 🪙")

# Input cho người chơi
bet_amount = st.number_input("Số tiền cược:", min_value=1, max_value=st.session_state.balance, value=100)
choice = st.radio("Lựa chọn của bạn:", ["Tài", "Xỉu"], horizontal=True)

if st.button("🔥 ĐẶT CƯỢC VÀ LẮC"):
    if bet_amount > st.session_state.balance:
        st.error("Số dư không đủ!")
    else:
        with st.spinner("Đang lắc..."):
            time.sleep(1)

            xuc_xac = [random.randint(1, 6) for _ in range(3)]
            tong = sum(xuc_xac)
            ket_qua = "Tài" if tong >= 11 else "Xỉu"

            # Tính toán kết quả
            if choice == ket_qua:
                st.session_state.balance += bet_amount
                st.success(f"THẮNG! Tổng là {tong}. Bạn nhận được {bet_amount} xu.")
            else:
                st.session_state.balance -= bet_amount
                st.error(f"THUA! Tổng là {tong}. Bạn mất {bet_amount} xu.")

            st.write(f"Kết quả xúc xắc: {xuc_xac}")

# Nút reset nếu cháy túi
if st.session_state.balance <= 0:
    st.warning("Bạn đã hết tiền!")
    if st.button("Chơi lại từ đầu"):
        st.session_state.balance = 1000
        st.rerun()

st.write("---")
st.caption("Chúc bạn chơi vui vẻ! (Nhớ đừng để thua hết nhé!)")