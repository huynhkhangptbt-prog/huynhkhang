import streamlit as st

# Cấu hình trang
st.set_page_config(page_title="Trắc nghiệm tính cách", layout="wide")

# Dữ liệu con vật
animals = {
    "Mèo": "Bạn là người độc lập, thích sự yên tĩnh và có chiều sâu nội tâm.",
    "Chó": "Bạn thân thiện, trung thành và luôn quan tâm đến người khác.",
    "Sư tử": "Bạn tự tin, mạnh mẽ và có tố chất lãnh đạo.",
    "Cá heo": "Bạn thông minh, sáng tạo và rất hòa đồng.",
    "Thiên nga": "Bạn thanh lịch, tinh tế và yêu cái đẹp."
}

# Sidebar
st.sidebar.title("Trắc nghiệm tính cách")

if "selected" not in st.session_state:
    st.session_state.selected = None

if st.session_state.selected:
    st.sidebar.write(f"Con vật bạn chọn là: **{st.session_state.selected}**")
else:
    st.sidebar.write("Bạn chưa chọn con vật nào.")

# Tiêu đề chính
st.title("Hãy chọn một con vật bạn yêu thích")

# Tạo 5 cột cho button
cols = st.columns(5)

for i, animal in enumerate(animals.keys()):
    if cols[i].button(animal):
        st.session_state.selected = animal

# Hiển thị kết quả
if st.session_state.selected:
    with st.expander(st.session_state.selected, expanded=True):
        st.write(animals[st.session_state.selected])