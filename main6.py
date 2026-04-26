import streamlit as st
from datetime import date

# 1. Cấu hình trang
st.set_page_config(page_title="Giới thiệu bản thân", page_icon="📝")
st.title("📝 Form Giới Thiệu Bản Thân")
st.write("Hãy điền các thông tin bên dưới và nhấn nút Gửi để hoàn tất.")

# 2. Các ô nhập liệu
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Họ và tên")
    # Sử dụng format để hiển thị ngày/tháng/năm
    dob = st.date_input(
        "Ngày tháng năm sinh",
        value=None,
        min_value=date(1900, 1, 1),
        max_value=date.today(),
        format="DD/MM/YYYY"
    )

with col2:
    gender = st.selectbox("Giới tính", [None, "Nam", "Nữ", "Khác"], index=0)
    hobby = st.text_input("Sở thích")

bio = st.text_area("Giới thiệu ngắn về bản thân")

# 3. Logic tính toán tiến độ (Thời gian thực)
fields = [name, dob, gender, bio, hobby]
filled_fields = sum(1 for field in fields if field is not None and field != "")
total_fields = len(fields)
progress = filled_fields / total_fields

st.write("---")
st.write("Tiến độ hoàn thành:")
st.progress(progress)

# 4. Nút Submit (Xử lý khi nhấn nút)
if st.button("Gửi thông tin"):
    if progress == 1.0:
        # Nếu đã đủ 100%
        st.balloons()
        st.success("Chúc mừng! Bạn đã hoàn thành toàn bộ thông tin.")

        # Hiển thị kết quả
        st.write("### Thông tin cá nhân của bạn:")
        st.write(f"- **Họ và tên:** {name}")
        st.write(f"- **Ngày sinh:** {dob.strftime('%d/%m/%Y')}")
        st.write(f"- **Giới tính:** {gender}")
        st.write(f"- **Sở thích:** {hobby}")
        st.write(f"- **Giới thiệu:** {bio}")
    else:
        # Nếu chưa đủ 100%
        st.warning(f"Vui lòng điền đầy đủ các thông tin còn thiếu. Bạn mới chỉ hoàn thành {int(progress * 100)}%.")