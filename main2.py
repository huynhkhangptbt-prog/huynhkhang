import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="Quản lý điểm số",
    page_icon="📊",
    layout="centered"
)

# ===================== CSS =====================
st.markdown("""
<style>

/* Nền */
.stApp{
    background:#0f172a;
}

/* Tiêu đề */
h1{
    color:#60a5fa;
    text-align:center;
}

/* Nút */
.stButton>button{
    background:linear-gradient(90deg,#2563eb,#7c3aed);
    color:white;
    border:none;
    border-radius:10px;
    padding:8px 20px;
    font-weight:bold;
    font-size:16px;
}

.stButton>button:hover{
    background:linear-gradient(90deg,#1d4ed8,#6d28d9);
}

/* Bảng */
div[data-testid="stDataFrame"]{
    border:2px solid #334155;
    border-radius:10px;
    overflow:hidden;
}

/* Header */
div[data-testid="stDataFrame"] th{
    background:#2563eb !important;
    color:white !important;
    text-align:center !important;
    font-size:14px;
}

/* Ô dữ liệu */
div[data-testid="stDataFrame"] td{
    text-align:center !important;
    padding:6px !important;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# ===================== DỮ LIỆU =====================

students = [
    "Vĩnh Khang",
    "Tấn Khang",
    "Phú",
    "Luân"
]

subjects = [
    "Toán", "Văn", "Anh", "Lý", "Hóa",
    "Sinh", "Sử", "Địa", "Tin", "CN"
]

def random_scores():
    data = []

    for student in students:
        row = {"Học sinh": student}

        for subject in subjects:
            row[subject] = round(random.uniform(0, 10), 1)

        data.append(row)

    return pd.DataFrame(data)

if "df" not in st.session_state:
    st.session_state.df = random_scores()

# ===================== GIAO DIỆN =====================

st.title("📊 Quản lý Điểm số")
st.caption("Bảng điểm ngẫu nhiên của 4 học sinh")

if st.button("🎲 Random dữ liệu"):
    st.session_state.df = random_scores()

st.dataframe(
    st.session_state.df,
    hide_index=True,
    use_container_width=False,
    height=185
)