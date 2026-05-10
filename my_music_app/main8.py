import streamlit as st
import os

# Cấu hình trang
st.set_page_config(page_title="Music Profiles", layout="wide")

# Hàm lấy file nhạc (Đã sửa để chạy trên Server Deploy)
def get_audio_file(file_name):
    # Khi deploy, app sẽ tìm file ngay trong thư mục gốc của GitHub
    return file_name

st.title("🎧 Hệ thống Nghệ sĩ & MV yêu thích")

# Danh sách tên nghệ sĩ để quản lý Tab
artist_names = ["AMEE", "SƠN TÙNG M-TP", "ĐEN VÂU", "HOÀNG THÙY LINH"]
tabs = st.tabs(artist_names)

# --- TAB 1: AMEE ---
with tabs[0]:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://gionghatvietnhi.com.vn/wp-content/uploads/2024/05/1208-2.jpg")
        st.markdown("### Nghệ danh: **AMEE**")
        st.write("""
        Trần Huyền My (AMEE) là nữ ca sĩ đại diện cho làn sóng Pop Gen Z tại Việt Nam. 
        Cô nổi tiếng với hình ảnh kẹo ngọt, giọng hát trong trẻo và những bản hit 
        đứng đầu các bảng xếp hạng âm nhạc trẻ.
        """)
    with col2:
        st.header("MV & Audio")
        st.subheader("🎵 Bài hát: MỘNG YU")
        # Đã đổi tên file thành không dấu để tránh lỗi Server
        st.audio(get_audio_file("mong_yu.mp3"))
        st.subheader("🎬 MV: ex's hate me")
        st.video("https://www.youtube.com/watch?v=95ahbau-rJk")

# --- TAB 2: SƠN TÙNG M-TP ---
with tabs[1]:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://media-cdn-v2.laodong.vn/Storage/NewsPortal/2019/7/1/741911/Hay-Trao-Cho-Anh-2.jpg")
        st.markdown("### Nghệ danh: **SƠN TÙNG M-TP**")
        st.write("""
        Sơn Tùng M-TP là biểu tượng của âm nhạc Việt đương đại, sở hữu phong cách 
        âm nhạc đa dạng và đẳng cấp quốc tế. Anh là nghệ sĩ đầu tiên của Việt Nam 
        đạt được những kỷ lục vô tiền khoáng hậu trên YouTube.
        """)
    with col2:
        st.header("MV & Audio")
        st.subheader("🎵 Bài hát: CHẠY NGAY ĐI")
        st.audio(get_audio_file("chay_ngay_di.mp3"))
        st.subheader('🎬 MV: ĐỪNG LÀM TRÁI TIM ANH ĐAU')
        st.video("https://www.youtube.com/watch?v=abPmZCZZrFA")

# --- TAB 3: ĐEN VÂU ---
with tabs[2]:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://cdn.24h.com.vn/upload/1-2023/images/2023-03-27/Bat-ngo-so-tien-rapper-den-Vau-kiem-duoc-tu-kenh-YouTube-anh-1-1679890371-701-width740height548.jpg")
        st.markdown("### Nghệ danh: **ĐEN VÂU**")
        st.write("""
        Nguyễn Đức Cường (Đen Vâu) là nghệ sĩ rap với phong cách mộc mạc và chân thành. 
        Âm nhạc của anh luôn mang đậm hơi thở cuộc sống, sự trải nghiệm và triết lý 
        gần gũi với giới trẻ.
        """)
    with col2:
        st.header("MV & Audio")
        st.subheader("🎵 Bài hát: Ngày Khác Lạ")
        st.audio(get_audio_file("ngay_khac_la.mp3"))
        st.subheader('🎬 MV: Vị nhà')
        st.video("https://www.youtube.com/watch?v=Hqmbo0ROBQw")

# --- TAB 4: HOÀNG THÙY LINH ---
with tabs[3]:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://media.vietnam.vn/vietnam.vn/2024/01/giai-ma-ly-do-see-tinh-hoang-thuy-linh-gay-sot-20230207082618-5845.jpeg")
        st.markdown("### Nghệ danh: **HOÀNG THÙY LINH**")
        st.write("""
        Hoàng Thùy Linh là nữ ca sĩ hàng đầu trong việc kết hợp âm hưởng dân gian 
        truyền thống vào âm nhạc hiện đại. Những album của cô luôn gây tiếng vang 
        nhờ sự sáng tạo văn hóa độc đáo.
        """)
    with col2:
        st.header("MV & Audio")
        st.subheader("🎵 Bài hát: Để Mị Nói Cho Mà Nghe")
        st.audio(get_audio_file("de_mi_noi_cho_ma_ghe.mp3"))
        st.subheader("🎬 MV: Kẻ Cắp Gặp Bà Già")
        st.video("https://www.youtube.com/watch?v=bA1MhSK8wBE")