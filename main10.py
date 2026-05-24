import streamlit as st
import pandas as pd

# =========================
# LABEL TÊN NHÀ HÀNG
# =========================
st.markdown(
    """
    <h1 style='text-align: center;
               color: darkred;
               background-color: #ffe6cc;
               padding: 15px;
               border-radius: 15px;'>
        🍽️ Khang's Restaurant 🍽️
    </h1>
    """,
    unsafe_allow_html=True
)

st.write("## Chào mừng bạn đến với nhà hàng của Khang 😋")

# =========================
# HÌNH ẢNH BANNER
# =========================
st.image(
    "https://images.unsplash.com/photo-1504674900247-0877df9cc836",
    caption="Thưởng thức những món ăn ngon nhất",
    use_container_width=True
)

# =========================
# MENU MÓN ĂN
# =========================

# Món khai vị
khai_vi = {
    "Gỏi cuốn": 30000,
    "Salad": 40000,
    "Súp cua": 50000,
    "Khoai tây chiên": 35000
}

# Món chính
mon_chinh = {
    "Cơm chiên": 60000,
    "Bò bít tết": 150000,
    "Pizza": 120000,
    "Mì Ý": 90000
}

# Món tráng miệng
trang_mieng = {
    "Kem": 25000,
    "Bánh ngọt": 40000,
    "Trái cây": 30000,
    "Pudding": 35000
}

# =========================
# FORM GỌI MÓN
# =========================
with st.form("food_form"):

    order = {}

    # =========================
    # MÓN KHAI VỊ
    # =========================
    st.subheader("🥗 Món khai vị")

    for food, price in khai_vi.items():

        col1, col2, col3 = st.columns([4, 2, 2])

        with col1:
            st.write(food)

        with col2:
            st.write(f"{price:,} VNĐ")

        with col3:
            qty = st.number_input(
                "Số lượng",
                min_value=0,
                max_value=20,
                step=1,
                key=food
            )

        order[food] = (qty, price)

    st.write("---")

    # =========================
    # MÓN CHÍNH
    # =========================
    st.subheader("🍛 Món chính")

    for food, price in mon_chinh.items():

        col1, col2, col3 = st.columns([4, 2, 2])

        with col1:
            st.write(food)

        with col2:
            st.write(f"{price:,} VNĐ")

        with col3:
            qty = st.number_input(
                "Số lượng",
                min_value=0,
                max_value=20,
                step=1,
                key=food
            )

        order[food] = (qty, price)

    st.write("---")

    # =========================
    # MÓN TRÁNG MIỆNG
    # =========================
    st.subheader("🍰 Món tráng miệng")

    for food, price in trang_mieng.items():

        col1, col2, col3 = st.columns([4, 2, 2])

        with col1:
            st.write(food)

        with col2:
            st.write(f"{price:,} VNĐ")

        with col3:
            qty = st.number_input(
                "Số lượng",
                min_value=0,
                max_value=20,
                step=1,
                key=food
            )

        order[food] = (qty, price)

    # =========================
    # NÚT THANH TOÁN
    # =========================
    submit = st.form_submit_button("🧾 Thanh toán")

# =========================
# HÓA ĐƠN
# =========================
if submit:

    st.success("✅ Đặt món thành công!")

    st.write("# 🧾 Hóa đơn của bạn")

    total = 0

    bill_data = []

    # Header bảng
    col1, col2, col3, col4 = st.columns([4, 2, 2, 2])

    with col1:
        st.markdown("### Tên món")

    with col2:
        st.markdown("### Giá")

    with col3:
        st.markdown("### Số lượng")

    with col4:
        st.markdown("### Thành tiền")

    st.write("---")

    # Hiển thị món đã chọn
    for food, data in order.items():

        qty, price = data

        if qty > 0:

            subtotal = qty * price
            total += subtotal

            # Lưu dữ liệu hóa đơn
            bill_data.append({
                "Tên món": food,
                "Giá": price,
                "Số lượng": qty,
                "Thành tiền": subtotal
            })

            col1, col2, col3, col4 = st.columns([4, 2, 2, 2])

            with col1:
                st.write(food)

            with col2:
                st.write(f"{price:,} VNĐ")

            with col3:
                st.write(qty)

            with col4:
                st.write(f"{subtotal:,} VNĐ")

    st.write("---")
    st.subheader(f"💰 Tổng cộng: {total:,} VNĐ")

    # =========================
    # XUẤT FILE HÓA ĐƠN CSV
    # =========================
    df = pd.DataFrame(bill_data)

    # Thêm dòng tổng cộng
    total_row = pd.DataFrame([{
        "Tên món": "TỔNG CỘNG",
        "Giá": "",
        "Số lượng": "",
        "Thành tiền": total
    }])

    df = pd.concat([df, total_row], ignore_index=True)

    csv = df.to_csv(index=False).encode("utf-8-sig")

    st.download_button(
        label="📥 Tải hóa đơn CSV",
        data=csv,
        file_name="hoa_don_khang_restaurant.csv",
        mime="text/csv"
    )

    # =========================
    # ẢNH CẢM ƠN
    # =========================
    st.image(
        "https://images.unsplash.com/photo-1490645935967-10de6ba17061",
        caption="Cảm ơn quý khách đã dùng bữa tại Khang's Restaurant ❤️",
        use_container_width=True
    )