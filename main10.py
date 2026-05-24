import streamlit as st
import pandas as pd
from datetime import datetime
import re

# =========================
# CÀI ĐẶT TRANG
# =========================
st.set_page_config(
    page_title="Khang's Restaurant",
    page_icon="🍽️",
    layout="wide"
)


# =========================
# HÀM CHUYỂN ĐỔI TÊN TIẾNG VIỆT KHÔNG DẤU (ĐỂ LÀM MÃ ĐƠN)
# =========================
def remove_vietnamese_tones(text):
    text = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', text)
    text = re.sub(r'[ÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴ]', 'A', text)
    text = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', text)
    text = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', text)
    text = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', text)
    text = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', text)
    text = re.sub(r'[ùúụủũưừứựửữ]', 'u', text)
    text = re.sub(r'[ÙÚỤỦŨƯỪỨỰỬỮ]', 'U', text)
    text = re.sub(r'[ìíịỉĩ]', 'i', text)
    text = re.sub(r'[ÌÍỊỈĨ]', 'I', text)
    text = re.sub(r'[ỳýỵỷỹ]', 'y', text)
    text = re.sub(r'[ỲÝỴỶỸ]', 'Y', text)
    text = re.sub(r'[đ]', 'd', text)
    text = re.sub(r'[Đ]', 'D', text)
    # Xóa toàn bộ khoảng trắng để viết liền
    text = text.replace(" ", "")
    return text


# =========================
# CSS GIAO DIỆN
# =========================
st.markdown("""
<style>
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    max-width: 100% !important;
}

.restaurant-title {
    text-align: center;
    color: #d00000;
    background: linear-gradient(90deg, #ffecd2 0%, #fcb69f 100%);
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 30px;
}

div[data-testid="stVVerticalBlockBorder"] {
    height: 100% !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
}

div[data-testid="stImage"] img {
    height: 180px !important;
    object-fit: cover !important;
    border-radius: 10px !important;
}

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

.food-price {
    color: #e63946;
    font-size: 17px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 10px;
}

div[data-testid="stNumberInput"] {
    margin-top: auto !important;
}

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
    "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=1200&q=80",
    use_container_width=True
)

# =========================
# DỮ LIỆU MENU
# =========================
menu_data = {
    "🥗 Món khai vị": {
        "Gỏi cuốn": {
            "price": 30000,
            "image": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=800&q=80"
        },
        "Salad": {
            "price": 40000,
            "image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=800&q=80"
        },
        "Súp cua": {
            "price": 50000,
            "image": "https://images.unsplash.com/photo-1603105037880-880cd4edfb0d?auto=format&fit=crop&w=800&q=80"
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
# HIỂN THỊ MENU MÓN ĂN
# =========================
def show_menu(title, menu, order_dict):
    st.subheader(title)
    cols = st.columns(4)

    for index, (food, info) in enumerate(menu.items()):
        with cols[index % 4]:
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


# =======================================================
# FORM ĐẶT MÓN & THÔNG TIN KHÁCH HÀNG
# =======================================================
with st.form("order_form"):
    st.markdown("### 📞 Thông tin giao hàng")
    c1, c2 = st.columns(2)
    with c1:
        customer_name = st.text_input("Họ và tên khách hàng *", placeholder="Nhập tên của bạn...")
        customer_phone = st.text_input("Số điện thoại *", placeholder="Nhập số điện thoại liên hệ...")
    with c2:
        customer_address = st.text_area("Địa chỉ nhận hàng *",
                                        placeholder="Nhập số nhà, tên đường, phường/xã, quận/huyện...", height=115)

    st.markdown("---")

    current_order = {}
    for category, items in menu_data.items():
        show_menu(category, items, current_order)

    submit = st.form_submit_button(
        "🧾 Xác nhận & Thanh toán",
        use_container_width=True
    )

# =========================
# XỬ LÝ THANH TOÁN & ĐƠN HÀNG
# =========================
if submit:
    if not customer_name.strip() or not customer_phone.strip() or not customer_address.strip():
        st.error("❌ Vui lòng điền đầy đủ Họ tên, Số điện thoại và Địa chỉ để nhà hàng chuẩn bị giao đơn!")
    else:
        ordered_items = {
            k: v for k, v in current_order.items()
            if v[0] > 0
        }

        if not ordered_items:
            st.warning("⚠️ Vui lòng chọn ít nhất một món ăn trước khi bấm thanh toán!")
        else:
            st.success("✅ Đặt món thành công! Khang's Restaurant đang chuẩn bị món ăn cho bạn.")
            st.balloons()

            # Lấy mốc thời gian thực hiện đơn hàng
            now = datetime.now()
            date_str = now.strftime("%Y%m%d")
            time_str = now.strftime("%H%M%S")

            # Chuẩn hóa tên khách hàng thành không dấu, viết liền để đưa vào mã đơn hàng
            clean_name = remove_vietnamese_tones(customer_name)

            # CẬP NHẬT THEO YÊU CẦU: Mã đơn hàng theo thứ tự [Tên]_[SĐT]_[Thời gian]
            # Ví dụ: NguyenVanAn_0901234567_171530
            order_id = f"{clean_name}_{customer_phone}_{time_str}"

            bill_data = []
            total = 0

            for food, value in ordered_items.items():
                qty = value[0]
                price = value[1]
                subtotal = qty * price
                total += subtotal

                bill_data.append({
                    "Mã Đơn Hàng": order_id,
                    "Khách Hàng": customer_name,
                    "Số Điện Thoại": customer_phone,
                    "Địa Chỉ Giao": customer_address,
                    "Món ăn": food,
                    "Số lượng": qty,
                    "Đơn giá": f"{price:,} VNĐ",
                    "Thành tiền": f"{subtotal:,} VNĐ"
                })

            st.markdown(
                f'<h2 class="bill-title">🧾 Hóa đơn của bạn (Mã đơn: <span style="color:#e63946;">{order_id}</span>)</h2>',
                unsafe_allow_html=True
            )

            df = pd.DataFrame(bill_data)
            st.table(df[["Món ăn", "Số lượng", "Đơn giá", "Thành tiền"]])

            st.markdown(
                f"""
                <h3 style='text-align:left; color:#555;'>Người nhận: <b>{customer_name}</b> | SĐT: {customer_phone}</h3>
                <h3 style='text-align:left; color:#555;'>Địa chỉ giao: {customer_address}</h3>
                <h2 style='text-align:right; color:#d00000;'>
                    Tổng cộng: {total:,} VNĐ
                </h2>
                """,
                unsafe_allow_html=True
            )

            csv = df.to_csv(index=False).encode("utf-8-sig")

            # Tên file tải về máy đồng bộ theo mã đơn hàng để quản lý dễ dàng nhất
            file_name_ready = f"hoa_don_{clean_name}_{customer_phone}_{date_str}_{time_str}.csv"

            st.download_button(
                label="📥 Tải hóa đơn CSV",
                data=csv,
                file_name=file_name_ready,
                mime="text/csv",
                use_container_width=True
            )
