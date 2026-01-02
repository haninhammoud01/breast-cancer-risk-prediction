import streamlit as st
import pandas as pd
import joblib

# ==============================
# Konfigurasi Halaman
# ==============================
st.set_page_config(
    page_title="Prediksi Kanker Payudara ",
    layout="centered"
)

# ==============================
# Judul Aplikasi
# ==============================
st.title(" Prediksi Kanker Payudara")
st.markdown("""
Selamat datang di aplikasi **Prediksi Kanker Payudara**!  
Masukkan nilai-nilai karakteristik sel di bawah ini, lalu klik tombol **Prediksi**  
untuk mengetahui apakah hasilnya **JINAK** atau **GANAS**.
""")

# ==============================
# Muat Model
# ==============================
try:
    model = joblib.load("model_rf.pkl")
    st.success(" Model berhasil dimuat!")
except Exception as e:
    st.error(f" Gagal memuat model: {e}")

# ==============================
# Layout Input Data
# ==============================
st.markdown("### 🔍 Masukkan Data Fitur")

col1, col2, col3 = st.columns(3)

with col1:
    clump_thickness = st.slider("Clump Thickness", 1, 10, 1)
    uniform_cell_size = st.slider("Uniformity of Cell Size", 1, 10, 1)
    uniform_cell_shape = st.slider("Uniformity of Cell Shape", 1, 10, 1)

with col2:
    marginal_adhesion = st.slider("Marginal Adhesion", 1, 10, 1)
    single_epithelial_size = st.slider("Single Epithelial Cell Size", 1, 10, 1)
    bare_nuclei = st.slider("Bare Nuclei", 1, 10, 1)

with col3:
    bland_chromatin = st.slider("Bland Chromatin", 1, 10, 1)
    normal_nucleoli = st.slider("Normal Nucleoli", 1, 10, 1)
    mitoses = st.slider("Mitoses", 1, 10, 1)

# ==============================
# Buat DataFrame dari Input
# ==============================
data = pd.DataFrame({
    "Clump Thickness": [clump_thickness],
    "Uniformity of Cell Size": [uniform_cell_size],
    "Uniformity of Cell Shape": [uniform_cell_shape],
    "Marginal Adhesion": [marginal_adhesion],
    "Single Epithelial Cell Size": [single_epithelial_size],
    "Bare Nuclei": [bare_nuclei],
    "Bland Chromatin": [bland_chromatin],
    "Normal Nucleoli": [normal_nucleoli],
    "Mitoses": [mitoses]
})

st.markdown("### 🧩 Data yang Dimasukkan")
st.dataframe(data, use_container_width=True)

# ==============================
# Prediksi
# ==============================
if st.button(" Prediksi Sekarang"):
    try:
        prediction = model.predict(data)[0]

        if prediction == 4 or str(prediction).lower() == "ganas":
            st.error("🔬 Hasil Prediksi: **GANAS (Malignant)**")
        else:
            st.success("🩺 Hasil Prediksi: **JINAK (Benign)**")

        st.markdown("---")
        st.caption("Model: Random Forest Classifier | Dataset: Breast Cancer Wisconsin Original")

    except Exception as e:
        st.error(f"Terjadi kesalahan saat prediksi: {e}")

# ==============================
# Footer
# ==============================
st.markdown("""
---
 *Aplikasi ini dikembangkan untuk membantu proses edukasi dan penelitian.*  
Tidak menggantikan diagnosis medis profesional.|Dibuat oleh: Kelompok 4 
""")
