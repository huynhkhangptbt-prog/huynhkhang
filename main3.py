import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Phổ Điểm Thi Tuyển Sinh Lớp 10", layout="wide")

st.title("Phổ Điểm Thi Tuyển Sinh Lớp 10 thành phố Phan Thiết")

# Dữ liệu mẫu
toan = pd.DataFrame({
    "Điểm": list(range(11)),
    "Số học sinh": [10, 45, 110, 230, 310, 540, 610, 420, 310, 180, 45]
})

van = pd.DataFrame({
    "Điểm": list(range(11)),
    "Số học sinh": [5, 15, 30, 80, 170, 420, 690, 520, 310, 110, 8]
})

anh = pd.DataFrame({
    "Điểm": list(range(11)),
    "Số học sinh": [25, 65, 140, 210, 320, 490, 410, 360, 310, 220, 90]
})


def draw_chart(df, title, color):
    chart = (
        alt.Chart(df)
        .mark_bar(cornerRadiusTopLeft=4, cornerRadiusTopRight=4)
        .encode(
            x=alt.X("Điểm:O", title="Điểm"),
            y=alt.Y("Số học sinh:Q", title="Số lượng học sinh"),
            color=alt.value(color),
            tooltip=["Điểm", "Số học sinh"]
        )
        .properties(
            title=title,
            width=900,
            height=450
        )
    )
    st.altair_chart(chart, use_container_width=True)


tab1, tab2, tab3 = st.tabs(["Môn Toán", "Môn Ngữ Văn", "Môn Tiếng Anh"])

with tab1:
    st.header("Phổ điểm chi tiết môn Toán")
    draw_chart(toan, "Phổ điểm môn Toán", "#E74C3C")

with tab2:
    st.header("Phổ điểm chi tiết môn Ngữ Văn")
    draw_chart(van, "Phổ điểm môn Ngữ Văn", "#F4B400")

with tab3:
    st.header("Phổ điểm chi tiết môn Tiếng Anh")
    draw_chart(anh, "Phổ điểm môn Tiếng Anh", "#4A90E2")