import streamlit as st
import pandas as pd

# =========================
# CÀI ĐẶT TRANG
# =========================
st.set_page_config(
    page_title="Khang's Restaurant",
    page_icon="🍽️",
    layout="wide"
)

# =========================
# CSS GIAO DIỆN (ÉP KHUNG BẰNG NHAU)
# =========================
st.markdown("""
<style>
/* Tiêu đề chính */
.restaurant-title {
    text-align: center;
    color: #d00000;
    background: linear-gradient(90deg, #ffecd2 0%, #fcb69f 100%);
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 30px;
}

/* 1. ÉP CÁC CONTAINER CÓ CHIỀU CAO BẰNG NHAU TRÊN CÙNG HÀNG */
div[data-testid="stVVerticalBlockBorder"] {
    height: 100% !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
}

/* 2. CỐ ĐỊNH CHIỀU CAO ẢNH VÀ CHỐNG MÉO ẢNH */
div[data-testid="stImage"] img {
    height: 180px !important;
    object-fit: cover !important;
    border-radius: 10px !important;
}

/* 3. ĐỒNG BỘ KHOẢNG TRỐNG TÊN MÒN ĂN (Bất kể 1 hay 2 dòng) */
.food-name {
    font-size: 19px;
    font-weight: bold;
    text-align: center;
    margin-top: 10px;
    min-height: 55px; 
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Giá tiền */
.food-price {
    color: #e63946;
    font-size: 17px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 10px;
}

/* 4. ĐẨY Ô NHẬP SỐ LƯỢNG DÍNH CHẶT VÀO ĐÁY KHUNG CARD */
div[data-testid="stNumberInput"] {
    margin-top: auto !important;
}

/* Tiêu đề hóa đơn */
.bill-title {
    margin-top: 30px;
    color: #d00000;
}
</style>
""", unsafe_allow_html=True)

# =========================
# TIÊU ĐỀ & BANNER
# =========================
st.markdown(
    '<h1 class="restaurant-title">🍽️ Khang\'s Restaurant 🍽️</h1>',
    unsafe_allow_html=True
)

st.write("## Chào mừng bạn đến với nhà hàng của Khang 😋")

st.image(
    "https://images.unsplash.com/photo-1504674900247-0877df9cc836",
    use_container_width=True
)

# =========================
# DỮ LIỆU MENU
# =========================
menu_data = {
    "🥗 Món khai vị": {
        "Gỏi cuốn": {
            "price": 30000,
            "image": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80"
        },
        "Salad": {
            "price": 40000,
            "image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=800&q=80"
        },
        "Súp cua": {
            "price": 50000,
            "image": "https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=800&q=80"
        },
        "Khoai tây chiên": {
            "price": 35000,
            "image": "https://images.unsplash.com/photo-1576107232684-1279f390859f?auto=format&fit=crop&w=800&q=80"
        }
    },
    "🍛 Món chính": {
        "Cơm chiên": {
            "price": 60000,
            "image": "https://images.unsplash.com/photo-1512058564366-18510be2db19?auto=format&fit=crop&w=800&q=80"
        },
        "Bò bít tết": {
            "price": 150000,
            "image": "https://images.unsplash.com/photo-1558030006-450675393462?auto=format&fit=crop&w=800&q=80"
        },
        "Pizza": {
            "price": 120000,
            "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=800&q=80"
        },
        "Mì Ý": {
            "price": 90000,
            "image": "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?auto=format&fit=crop&w=800&q=80"
        }
    },
    "🍰 Món tráng miệng": {
        "Kem": {
            "price": 25000,
            "image": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?auto=format&fit=crop&w=800&q=80"
        },
        "Bánh ngọt": {
            "price": 40000,
            "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=800&q=80"
        },
        "Trái cây": {
            "price": 30000,
            "image": "https://images.unsplash.com/photo-1619566636858-adf3ef46400b?auto=format&fit=crop&w=800&q=80"
        },
        "Pudding": {
            "price": 35000,
            "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=800&q=80"
        }
    }
}


# =========================
# HIỂN THỊ MENU
# =========================
def show_menu(title, menu, order_dict):
    st.subheader(title)
    cols = st.columns(4)

    for index, (food, info) in enumerate(menu.items()):
        with cols[index % 4]:
            # Tạo khối Card bo góc đồng bộ cao rộng bằng nhau
            with st.container(border=True):
                st.image(info['image'], use_container_width=True)

                st.markdown(f"<div class='food-name'>{food}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='food-price'>{info['price']:,} VNĐ</div>", unsafe_allow_html=True)

                qty = st.number_input(
                    "Số lượng",
                    min_value=0,
                    max_value=20,
                    step=1,
                    key=f"qty_{food}",
                    label_visibility="collapsed"
                )

                order_dict[food] = (qty, info["price"])


# =========================
# FORM ĐẶT MÓN
# =========================
with st.form("order_form"):
    current_order = {}

    for category, items in menu_data.items():
        show_menu(category, items, current_order)

    submit = st.form_submit_button(
        "🧾 Xác nhận & Thanh toán",
        use_container_width=True
    )

# =========================
# THANH TOÁN & XUẤT HÓA ĐƠN
# =========================
if submit:
    ordered_items = {
        k: v for k, v in current_order.items()
        if v[0] > 0
    }

    if not ordered_items:
        st.warning("⚠️ Vui lòng chọn ít nhất một món ăn!")
    else:
        st.success("✅ Đặt món thành công!")
        st.balloons()

        bill_data = []
        total = 0

        for food, value in ordered_items.items():
            qty = value[0]
            price = value[1]
            subtotal = qty * price
            total += subtotal

            bill_data.append({
                "Món ăn": food,
                "Số lượng": qty,
                "Đơn giá": f"{price:,} VNĐ",
                "Thành tiền": f"{subtotal:,} VNĐ"
            })

        st.markdown(
            '<h2 class="bill-title">🧾 Hóa đơn của bạn</h2>',
            unsafe_allow_html=True
        )

        df = pd.DataFrame(bill_data)
        st.table(df)

        st.markdown(
            f"""
            <h2 style='text-align:right; color:#d00000;'>
                Tổng cộng: {total:,} VNĐ
            </h2>
            """,
            unsafe_allow_html=True
        )

        # Download hóa đơn dạng CSV
        csv = df.to_csv(index=False).encode("utf-8-sig")

        st.download_button(
            label="📥 Tải hóa đơn CSV",
            data=csv,
            file_name="hoa_don_khang_restaurant.csv",
            mime="text/csv",
            use_container_width=True
        )
