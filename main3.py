import streamlit as st
import pandas as pd
import altair as alt

# Dữ liệu
df = pd.DataFrame({
    "Môn": ["Toán", "Ngữ văn", "Tiếng Anh"],
    "Điểm chuẩn": [37.35, 36.45, 36.35],
    "Số thí sinh": [35, 70, 70]
})

st.title("Phổ điểm thi lớp 10 trường THPT Trần Hưng Đạo (3 môn: Toán, Văn, Anh)")

chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X("Môn:N", title="Môn"),
        y=alt.Y("Số thí sinh:Q", title="Số thí sinh"),
        color=alt.Color("Môn:N", legend=None),
        tooltip=[
            alt.Tooltip("Môn:N"),
            alt.Tooltip("Điểm chuẩn:Q", format=".2f"),
            alt.Tooltip("Số thí sinh:Q")
        ]
    )
    .properties(width=500, height=350)
)

st.altair_chart(chart, use_container_width=True)

st.dataframe(df)