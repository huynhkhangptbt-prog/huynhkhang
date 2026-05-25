import streamlit as st
import pandas as pd
import os
from datetime import datetime

FILE = "responses.csv"

st.set_page_config(
    page_title="what do u think about kheng?",
    layout="wide"
)

# =========================
# SAVE DATA
# =========================
def save_response(data):
    df_new = pd.DataFrame([data])

    if os.path.exists(FILE):
        df_old = pd.read_csv(FILE)
        df = pd.concat([df_old, df_new], ignore_index=True)
    else:
        df = df_new

    df.to_csv(FILE, index=False)


# =========================
# LOAD DATA
# =========================
def load_data():
    if os.path.exists(FILE):
        return pd.read_csv(FILE)
    return pd.DataFrame()


# =========================
# SAVE OVERWRITE DATA
# =========================
def save_data(df):
    df.to_csv(FILE, index=False)


# =========================
# MODE
# =========================
mode = st.sidebar.selectbox("Chọn chế độ", ["Người dùng", "Admin"])


# =========================
# USER MODE
# =========================
if mode == "Người dùng":
    st.title("📋 What do u think about Kheng ?")

    with st.form("survey_form"):
        name = st.text_input("1. Bạn tên gì?")
        q2 = st.text_area("2. Qua năm học vừa qua bạn thấy Khang là người như thế nào?")
        q3 = st.text_area("3. Bạn muốn Khang khắc phục những điểm gì?")
        q4 = st.text_area("4. Ghi chú thêm (không bắt buộc)")

        submit = st.form_submit_button("Gửi")

    if submit:
        # =========================
        # VALIDATION
        # =========================
        if not name.strip():
            st.error("❌ Vui lòng nhập tên!")
        elif not q2.strip():
            st.error("❌ Câu 2 là bắt buộc!")
        elif not q3.strip():
            st.error("❌ Câu 3 là bắt buộc!")
        else:
            data = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "name": name,
                "q2": q2,
                "q3": q3,
                "q4": q4
            }

            save_response(data)
            st.success("Đã gửi phản hồi!")


# =========================
# ADMIN MODE
# =========================
elif mode == "Admin":
    st.title("🔐 Trang quản trị")

    password = st.text_input("Nhập mật khẩu", type="password")
    ADMIN_PASSWORD = "2503"

    if password == ADMIN_PASSWORD:
        st.success("Đăng nhập thành công!")

        df = load_data()

        if df.empty:
            st.warning("Chưa có dữ liệu.")
        else:
            # =========================
            # TABLE VIEW
            # =========================
            st.subheader("📊 Danh sách phản hồi")

            st.dataframe(
                df,
                use_container_width=True,
                height=650
            )

            # =========================
            # DELETE SINGLE ROW
            # =========================
            st.subheader("🗑️ Xoá từng phản hồi")

            index_to_delete = st.number_input(
                "Nhập index dòng muốn xoá",
                min_value=0,
                max_value=len(df) - 1,
                step=1
            )

            if st.button("Xoá dòng này"):
                df = df.drop(index=index_to_delete).reset_index(drop=True)
                save_data(df)
                st.success(f"Đã xoá dòng {index_to_delete}")
                st.rerun()

            # =========================
            # DELETE ALL
            # =========================
            st.subheader("💣 Xoá toàn bộ dữ liệu")

            if st.button("Xoá tất cả"):
                if os.path.exists(FILE):
                    os.remove(FILE)
                st.warning("Đã xoá toàn bộ dữ liệu!")
                st.rerun()

            # =========================
            # DOWNLOAD CSV
            # =========================
            st.download_button(
                "📥 Tải CSV",
                df.to_csv(index=False),
                file_name="responses.csv",
                mime="text/csv"
            )

    elif password:
        st.error("Sai mật khẩu!")