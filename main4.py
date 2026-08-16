import streamlit as st

st.title("Tính Tiền Gửi Tiết Kiệm")

goc = st.number_input("Nhập số tiền gửi ban đầu", min_value=0.0, value=10000000.0)

lai_suat = st.number_input(
    "Nhập lãi suất (%/tháng)",
    min_value=0.0,
    value=0.5
)

ky_han = st.number_input(
    "Nhập kỳ hạn (tháng)",
    min_value=1,
    value=12
)

gui_them = st.number_input(
    "Nhập số tiền gửi thêm mỗi tháng",
    min_value=0.0,
    value=1000000.0
)

if st.button("Tính toán"):

    tong_tien = goc

    for i in range(int(ky_han)):
        tong_tien = tong_tien * (1 + lai_suat / 100)
        tong_tien += gui_them

    st.success(f"Số tiền nhận được sau {ky_han} tháng là:")
    st.write(f"**{tong_tien:,.0f} VNĐ**")