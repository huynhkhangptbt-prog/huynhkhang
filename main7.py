import streamlit as st

st.set_page_config(page_title="Trắc nghiệm tính cách", layout="wide")

animals = {
    "Mèo": "Bạn là người độc lập, thích sự yên tĩnh và có chiều sâu nội tâm.",
    "Chó": "Bạn thân thiện, trung thành và luôn quan tâm đến người khác.",
    "Sư tử": "Bạn tự tin, mạnh mẽ và có tố chất lãnh đạo.",
    "Cá heo": "Bạn thông minh, sáng tạo và rất hòa đồng.",
    "Thiên nga": "Bạn thanh lịch, tinh tế và yêu cái đẹp."
}

# Khởi tạo state
if "selected" not in st.session_state:
    st.session_state.selected = None

# UI chính
st.title("Hãy chọn một con vật bạn yêu thích")
cols = st.columns(5)

for i, animal in enumerate(animals.keys()):
    if cols[i].button(animal):
        st.session_state.selected = animal
        st.rerun()  # 👈 ép reload để sidebar update ngay

# Sidebar (render SAU khi state đã đổi)
with st.sidebar:
    st.title("Trắc nghiệm tính cách")

    if st.session_state.selected:
        st.success(f"Bạn đã chọn: {st.session_state.selected}")
    else:
        st.info("Bạn chưa chọn con vật nào.")

# Nội dung chính
if st.session_state.selected:
    with st.expander(st.session_state.selected, expanded=True):
        st.write(animals[st.session_state.selected])