import streamlit as st
st.image("logo.jpg")
# =========================
# CẤU HÌNH ỨNG DỤNG
# =========================
st.set_page_config(
    page_title="Tính lãi gửi tiết kiệm",
    page_icon="💰",
    layout="centered"
)

# =========================
# TIÊU ĐỀ
# =========================
st.title("💰 APP TÍNH LÃI GỬI TIẾT KIỆM_ĐOÀN THỊ HOÀI VY")
st.write("Nhập thông tin khoản tiền gửi để tính tiền lãi.")

st.divider()

# =========================
# NHẬP DỮ LIỆU
# =========================
st.subheader("📋 Thông tin tiền gửi")

so_tien_gui = st.number_input(
    "💵 Số tiền gửi (VNĐ)",
    min_value=0,
    value=10000000,
    step=1000000,
    format="%d"
)

ky_han = st.number_input(
    "📅 Kỳ hạn (tháng)",
    min_value=1,
    max_value=120,
    value=12,
    step=1
)

lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.1,
    format="%.2f"
)

hinh_thuc = st.selectbox(
    "💳 Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

# =========================
# NÚT TÍNH
# =========================
if st.button("🧮 TÍNH LÃI", use_container_width=True):

    if so_tien_gui <= 0:
        st.error("Vui lòng nhập số tiền gửi lớn hơn 0.")

    elif lai_suat < 0:
        st.error("Lãi suất không hợp lệ.")

    else:

        # Chuyển lãi suất % sang số thập phân
        lai_suat_nam = lai_suat / 100

        # ==========================================
        # 1. NHẬN LÃI CUỐI KỲ
        # ==========================================
        if hinh_thuc == "Cuối kỳ":

            tong_tien_lai = (
                so_tien_gui
                * lai_suat_nam
                * ky_han
                / 12
            )

            tien_lai_dinh_ky = tong_tien_lai

            tong_tien = so_tien_gui + tong_tien_lai

            st.subheader("📊 KẾT QUẢ")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "💵 Tiền lãi cuối kỳ",
                    f"{tien_lai_dinh_ky:,.0f} VNĐ"
                )

            with col2:
                st.metric(
                    "💰 Tổng tiền lãi",
                    f"{tong_tien_lai:,.0f} VNĐ"
                )

            st.metric(
                "🏦 Tổng tiền gốc + lãi",
                f"{tong_tien:,.0f} VNĐ"
            )

            st.info(
                f"Bạn nhận **{tong_tien_lai:,.0f} VNĐ tiền lãi** "
                f"vào cuối kỳ."
            )

        # ==========================================
        # 2. NHẬN LÃI HÀNG THÁNG
        # ==========================================
        elif hinh_thuc == "Hàng tháng":

            lai_moi_thang = (
                so_tien_gui
                * lai_suat_nam
                / 12
            )

            tong_tien_lai = lai_moi_thang * ky_han

            tong_tien = so_tien_gui + tong_tien_lai

            st.subheader("📊 KẾT QUẢ")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "💵 Tiền lãi mỗi tháng",
                    f"{lai_moi_thang:,.0f} VNĐ"
                )

            with col2:
                st.metric(
                    "💰 Tổng tiền lãi",
                    f"{tong_tien_lai:,.0f} VNĐ"
                )

            st.metric(
                "🏦 Tổng tiền gốc + lãi",
                f"{tong_tien:,.0f} VNĐ"
            )

            # Bảng chi tiết
            st.subheader("📋 Chi tiết tiền lãi hàng tháng")

            for thang in range(1, int(ky_han) + 1):

                st.write(
                    f"**Tháng {thang}:** "
                    f"{lai_moi_thang:,.0f} VNĐ"
                )

        # ==========================================
        # 3. NHẬN LÃI HÀNG QUÝ
        # ==========================================
        elif hinh_thuc == "Hàng quý":

            # Một năm có 4 quý
            lai_moi_quy = (
                so_tien_gui
                * lai_suat_nam
                / 4
            )

            so_quy = ky_han / 3

            tong_tien_lai = lai_moi_quy * so_quy

            tong_tien = so_tien_gui + tong_tien_lai

            st.subheader("📊 KẾT QUẢ")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "💵 Tiền lãi mỗi quý",
                    f"{lai_moi_quy:,.0f} VNĐ"
                )

            with col2:
                st.metric(
                    "💰 Tổng tiền lãi",
                    f"{tong_tien_lai:,.0f} VNĐ"
                )

            st.metric(
                "🏦 Tổng tiền gốc + lãi",
                f"{tong_tien:,.0f} VNĐ"
            )

            # Bảng chi tiết
            st.subheader("📋 Chi tiết tiền lãi hàng quý")

            so_quy = int(ky_han // 3)

            for quy in range(1, so_quy + 1):

                st.write(
                    f"**Quý {quy}:** "
                    f"{lai_moi_quy:,.0f} VNĐ"
                )

# =========================
# CÔNG THỨC
# =========================
st.divider()

st.subheader("📌 Công thức tính")

st.write(
    "**Tiền lãi = Số tiền gửi × Lãi suất năm × Kỳ hạn / 12**"
)

st.caption(
    "Ứng dụng sử dụng phương pháp tính lãi đơn, "
    "không nhập lãi vào gốc và không tái tục."
)
