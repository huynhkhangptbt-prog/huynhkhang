import streamlit as st

st.title("Ứng dụng đếm từ")

van_ban = st.text_area("Nhập văn bản vào đây:")


danh_sach_tu = van_ban.split()
so_luong = len(danh_sach_tu)

if st.button("dem"):
    st.write(f"Số từ trong văn bản của bạn là: **{so_luong}**")