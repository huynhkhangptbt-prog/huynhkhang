import streamlit as st
import pandas as pd
from datetime import datetime
import re

# =========================
# CÀI ĐẶT TRANG
# =========================
st.set_page_config(
    page_title="Khang's Restaurant & Cafe",
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
    text = text.replace(" ", "")
    return text


# =========================
# CSS GIAO DIỆN CẢI TIẾN
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

.item-name {
    font-size: 18px;
    font-weight: bold;
    text-align: center;
    margin-top: 10px;
    min-height: 55px; 
    display: flex;
    align-items: center;
    justify-content: center;
}

.item-price {
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
.sub-bill-title {
    color: #2a9d8f;
    margin-top: 20px;
    margin-bottom: 5px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# TIÊU ĐỀ & BANNER
# =========================
st.markdown(
    '<h1 class="restaurant-title">🍽️ Khang\'s Restaurant & Cafe ☕</h1>',
    unsafe_allow_html=True
)

st.write("## Chào mừng bạn đến với Không gian Ẩm thực & Đồ uống của Khang 😋")

st.image(
    "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=1200&q=80",
    use_container_width=True
)

# =========================
# DỮ LIỆU MENU ĐỒ ĂN
# =========================
food_menu = {
    "🥗 Món khai vị": {
        "Gỏi cuốn": {"price": 30000, "image": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=800&q=80"},
        "Salad": {"price": 40000, "image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=800&q=80"},
        "Súp cua": {"price": 50000, "image": "https://images.unsplash.com/photo-1603105037880-880cd4edfb0d?auto=format&fit=crop&w=800&q=80"},
        "Khoai tây chiên": {"price": 35000, "image": "https://images.unsplash.com/photo-1576107232684-1279f390859f?auto=format&fit=crop&w=800&q=80"}
    },
    "🍛 Món chính": {
        "Cơm chiên": {"price": 60000, "image": "https://images.unsplash.com/photo-1512058564366-18510be2db19?auto=format&fit=crop&w=800&q=80"},
        "Bò bít tết": {"price": 150000, "image": "https://images.unsplash.com/photo-1558030006-450675393462?auto=format&fit=crop&w=800&q=80"},
        "Pizza": {"price": 120000, "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=800&q=80"},
        "Mì Ý": {"price": 90000, "image": "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?auto=format&fit=crop&w=800&q=80"}
    },
    "🍰 Món tráng miệng": {
        "Kem": {"price": 25000, "image": "https://images.unsplash.com/photo-1563805042-7684c019e1cb?auto=format&fit=crop&w=800&q=80"},
        "Bánh ngọt": {"price": 40000, "image": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=800&q=80"},
        "Trái cây": {"price": 30000, "image": "https://images.unsplash.com/photo-1619566636858-adf3ef46400b?auto=format&fit=crop&w=800&q=80"},
        "Pudding": {"price": 35000, "image": "https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=800&q=80"}
    }
}

# =========================
# DỮ LIỆU MENU ĐỒ UỐNG (ĐÃ THÊM MÓN MỚI)
# =========================
drink_menu = {
    "☕ Cà phê truyền thống": {
        "Cà phê sữa đá": {
            "price": 29000,
            "image": "https://asianinspirations.com.au/wp-content/uploads/2018/12/R01583_Vietnamese_Iced_Coffee.jpg"
        },
        "Cà phê đen đá": {
            "price": 25000,
            "image": "https://cafesongao.com/wp-content/uploads/2021/07/ca-phe-den-da.png"
        },
        "Bạc xỉu": {
            "price": 32000,
            "image": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?auto=format&fit=crop&w=800&q=80"
        },
        "Cappuccino": {
            "price": 45000,
            "image": "https://images.unsplash.com/photo-1534778101976-62847782c213?auto=format&fit=crop&w=800&q=80"
        }
    },
    "🧋 Trà & Trà sữa giải nhiệt": {
        "Trà sữa trân châu": {
            "price": 40000,
            "image": "https://www.disneycooking.com/wp-content/uploads/2020/09/tra-sua-tran-chau.jpg"
        },
        "Trà đào cam sả": {
            "price": 39000,
            "image": "https://lypham.vn/wp-content/uploads/2024/09/cach-lam-tra-dao-cam-sa.jpg"
        },
        "Trà mãng cầu xiêm": {
            "price": 39000,
            "image": "https://images.unsplash.com/photo-1597481499750-3e6b22637e12?auto=format&fit=crop&w=800&q=80"
        },
        "Trà vải lài": {
            "price": 39000,
            "image": "https://bizweb.dktcdn.net/100/421/036/files/cach-lam-tra-vai-thom-ngon-giai-nhiet-mua-he-4.jpg?v=1617091580018"
        }
    },
    "🥤 Sinh tố & Nước ép tươi": {
        "Nước ép cam tươi": {
            "price": 35000,
            "image": "https://images.unsplash.com/photo-1613478223719-2ab802602423?auto=format&fit=crop&w=800&q=80"
        },
        "Nước ép dưa hấu": {
            "price": 35000,
            "image": "https://chuyengiupviec.vn/wp-content/uploads/2023/07/cach-lam-nuoc-ep-dua-hau.jpg"
        },
        "Sinh tố bơ sáp": {
            "price": 45000,
            "image": "https://barona.vn/storage/meo-vat/183/cach-lam-sinh-to-bo.jpg"
        },
        "Chanh dây hạt chia": {
            "price": 32000,
            "image": "https://cdn.tgdd.vn/2021/05/CookRecipe/GalleryStep/tra-chanh-day-trai-cay-21.jpg"
        }
    }
}


# =========================
# HÀM HIỂN THỊ MENU CHUNG
# =========================
def show_menu(title, menu, order_dict, prefix):
    st.subheader(title)
    cols = st.columns(4)

    for index, (name, info) in enumerate(menu.items()):
        with cols[index % 4]:
            with st.container(border=True):
                st.image(info['image'], use_container_width=True)

                st.markdown(f"<div class='item-name'>{name}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='item-price'>{info['price']:,} VNĐ</div>", unsafe_allow_html=True)

                qty = st.number_input(
                    "Số lượng",
                    min_value=0,
                    max_value=20,
                    step=1,
                    key=f"qty_{prefix}_{name}",
                    label_visibility="collapsed"
                )

                order_dict[name] = (qty, info["price"])


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
                                        placeholder="Nhập địa chỉ giao hàng cụ thể hoặc số bàn...", height=115)

    st.markdown("---")
    st.markdown("### 📋 Lựa chọn Menu thực đơn")

    # Tạo 2 từ điển riêng biệt để phân biệt rõ ràng giữa Đồ ăn và Đồ uống
    food_order = {}
    drink_order = {}

    tab_food, tab_drink = st.tabs(["🍔 THỰC ĐƠN ĐỒ ĂN", "🍹 MENU ĐỒ UỐNG"])

    with tab_food:
        for category, items in food_menu.items():
            show_menu(category, items, food_order, prefix="food")

    with tab_drink:
        for category, items in drink_menu.items():
            show_menu(category, items, drink_order, prefix="drink")

    st.markdown("---")
    submit = st.form_submit_button(
        "🧾 Xác nhận & Thanh toán Đơn hàng",
        use_container_width=True
    )

# =========================
# XỬ LÝ THANH TOÁN & ĐƠN HÀNG
# =========================
if submit:
    if not customer_name.strip() or not customer_phone.strip() or not customer_address.strip():
        st.error("❌ Vui lòng điền đầy đủ Họ tên, Số điện thoại và Địa chỉ để nhà hàng chuẩn bị giao đơn!")
    else:
        # Lọc riêng các món đồ ăn đã chọn
        ordered_foods = {k: v for k, v in food_order.items() if v[0] > 0}
        # Lọc riêng các món đồ uống đã chọn
        ordered_drinks = {k: v for k, v in drink_order.items() if v[0] > 0}

        if not ordered_foods and not ordered_drinks:
            st.warning("⚠️ Vui lòng chọn ít nhất một món ăn hoặc thức uống trước khi bấm thanh toán!")
        else:
            st.success("✅ Đặt món thành công! Khang's Restaurant & Cafe đang chuẩn bị cho bạn.")
            st.balloons()

            now = datetime.now()
            date_str = now.strftime("%Y%m%d")
            time_str = now.strftime("%H%M%S")

            clean_name = remove_vietnamese_tones(customer_name)
            order_id = f"{clean_name}_{customer_phone}_{time_str}"

            bill_all_data = []  # Dữ liệu gộp chung cho file CSV
            food_bill_data = [] # Dữ liệu riêng của đồ ăn để tạo bảng
            drink_bill_data = [] # Dữ liệu riêng của đồ uống để tạo bảng
            total = 0

            # 1. Thu thập dữ liệu phần Đồ ăn
            for item, value in ordered_foods.items():
                qty = value[0]
                price = value[1]
                subtotal = qty * price
                total += subtotal

                row_info = {
                    "Phân loại": "Đồ ăn",
                    "Tên món": item,
                    "Số lượng": qty,
                    "Đơn giá": f"{price:,} VNĐ",
                    "Thành tiền": f"{subtotal:,} VNĐ"
                }
                food_bill_data.append(row_info)
                bill_all_data.append({**{"Mã Đơn Hàng": order_id, "Khách Hàng": customer_name, "Số Điện Thoại": customer_phone, "Địa Chỉ Giao": customer_address}, **row_info})

            # 2. Thu thập dữ liệu phần Đồ uống
            for item, value in ordered_drinks.items():
                qty = value[0]
                price = value[1]
                subtotal = qty * price
                total += subtotal

                row_info = {
                    "Phân loại": "Đồ uống",
                    "Tên món": item,
                    "Số lượng": qty,
                    "Đơn giá": f"{price:,} VNĐ",
                    "Thành tiền": f"{subtotal:,} VNĐ"
                }
                drink_bill_data.append(row_info)
                bill_all_data.append({**{"Mã Đơn Hàng": order_id, "Khách Hàng": customer_name, "Số Điện Thoại": customer_phone, "Địa Chỉ Giao": customer_address}, **row_info})

            # HIỂN THỊ HOÁ ĐƠN TRÊN GIAO DIỆN CHIA THÀNH 2 PHẦN
            st.markdown(
                f'<h2 class="bill-title">🧾 Hóa đơn tổng hợp (Mã đơn: <span style="color:#e63946;">{order_id}</span>)</h2>',
                unsafe_allow_html=True
            )

            # Khởi tạo cột Layout (Cột trái hiển thị Đồ ăn, Cột phải hiển thị Đồ uống)
            col_b1, col_b2 = st.columns(2)

            with col_b1:
                if food_bill_data:
                    st.markdown('<h3 class="sub-bill-title">🍔 DANH SÁCH MÓN ĂN</h3>', unsafe_allow_html=True)
                    df_food = pd.DataFrame(food_bill_data)
                    st.table(df_food[["Tên món", "Số lượng", "Đơn giá", "Thành tiền"]])
                else:
                    if ordered_drinks: # Nếu chỉ đặt nước thì thông báo trống
                        st.info("💡 Không có món ăn nào được chọn trong đơn hàng này.")

            with col_b2:
                if drink_bill_data:
                    st.markdown('<h3 class="sub-bill-title">🍹 DANH SÁCH ĐỒ UỐNG</h3>', unsafe_allow_html=True)
                    df_drink = pd.DataFrame(drink_bill_data)
                    st.table(df_drink[["Tên món", "Số lượng", "Đơn giá", "Thành tiền"]])
                else:
                    if ordered_foods: # Nếu chỉ đặt đồ ăn thì thông báo trống
                        st.info("💡 Không có đồ uống nào được chọn trong đơn hàng này.")

            # Thông tin người nhận và Tổng tiền chung ở phía dưới
            st.markdown(
                f"""
                <hr>
                <h3 style='text-align:left; color:#555;'>Người nhận: <b>{customer_name}</b> | SĐT: {customer_phone}</h3>
                <h3 style='text-align:left; color:#555;'>Địa chỉ giao: {customer_address}</h3>
                <h2 style='text-align:right; color:#d00000;'>
                    Tổng cộng thanh toán: {total:,} VNĐ
                </h2>
                """,
                unsafe_allow_html=True
            )

            # Xuất toàn bộ dữ liệu ra file CSV lưu trữ
            df_all = pd.DataFrame(bill_all_data)
            csv = df_all.to_csv(index=False).encode("utf-8-sig")
            file_name_ready = f"hoa_don_chi_tiet_{clean_name}_{customer_phone}_{date_str}_{time_str}.csv"

            st.download_button(
                label="📥 Tải hóa đơn chi tiết phân loại CSV",
                data=csv,
                file_name=file_name_ready,
                mime="text/csv",
                use_container_width=True
            )