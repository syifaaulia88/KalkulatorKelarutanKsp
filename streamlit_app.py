import streamlit as st
import math

# Konfigurasi Halaman Web
st.set_page_config(page_title="Kalkulator Kelarutan dan Ksp", layout="centered")

# Judul dan Deskripsi
st.title("🧪 Kalkulator Kelarutan dan Ksp")
st.markdown("Aplikasi berbasis web untuk menghitung **Kelarutan (s)** dan **Tetapan Hasil Kali Kelarutan (Ksp)** untuk berbagai jenis senyawa. Dibuat berdasarkan prinsip kesetimbangan kimia.")
st.markdown("---")

# Pilihan Mode Perhitungan (Sesuai Fitur Makalah 2.5)
mode = st.radio("Pilih Jenis Perhitungan:", 
                ("Hitung Kelarutan (s) dari nilai Ksp", "Hitung Ksp dari nilai Kelarutan (s)"))

# Pilihan Jenis Senyawa (Sesuai Fitur Makalah 2.5)
senyawa_type = st.selectbox("Pilih Jenis Senyawa (Berdasarkan Stoikiometri):", 
                            ("AB (Contoh: AgCl, BaSO₄)", 
                             "AB₂ atau A₂B (Contoh: PbCl₂, Ag₂CrO₄)", 
                             "AB₃ atau A₃B (Contoh: Al(OH)₃, Ag₃PO₄)", 
                             "A₂B₃ atau A₃B₂ (Contoh: As₂S₃)"))

st.markdown("---")

# Logika Perhitungan: Kelarutan (s) dari Ksp
if mode == "Hitung Kelarutan (s) dari nilai Ksp":
    # Input nilai Ksp menggunakan notasi ilmiah (e.g., 1.0e-10)
    ksp_val = st.number_input("Masukkan Nilai Ksp (Gunakan format e, contoh: 1.0e-10):", 
                              value=1.0e-10, format="%.2e", step=1e-11)
    
    if st.button("Hitung Kelarutan (s)"):
        if "AB " in senyawa_type: # Tipe AB
            s = math.sqrt(ksp_val)
            rumus = r"K_{sp} = s^2 \implies s = \sqrt{K_{sp}}"
        elif "AB₂" in senyawa_type: # Tipe AB2 / A2B
            s = (ksp_val / 4.0) ** (1.0 / 3.0)
            rumus = r"K_{sp} = 4s^3 \implies s = \sqrt[3]{\frac{K_{sp}}{4}}"
        elif "AB₃" in senyawa_type: # Tipe AB3 / A3B
            s = (ksp_val / 27.0) ** (1.0 / 4.0)
            rumus = r"K_{sp} = 27s^4 \implies s = \sqrt[4]{\frac{K_{sp}}{27}}"
        elif "A₂B₃" in senyawa_type: # Tipe A2B3 / A3B2
            s = (ksp_val / 108.0) ** (1.0 / 5.0)
            rumus = r"K_{sp} = 108s^5 \implies s = \sqrt[5]{\frac{K_{sp}}{108}}"
        
        # Menampilkan Hasil
        st.success(f"**Kelarutan (s) = {s:.4e} mol/L**")
        st.info("Rumus yang digunakan:")
        st.latex(rumus)

# Logika Perhitungan: Ksp dari Kelarutan (s)
else:
    # Input nilai Kelarutan
    s_val = st.number_input("Masukkan Nilai Kelarutan (s) dalam mol/L (contoh: 1.0e-5):", 
                            value=1.0e-5, format="%.2e", step=1e-6)
    
    if st.button("Hitung Nilai Ksp"):
        if "AB " in senyawa_type: # Tipe AB
            ksp = s_val ** 2
            rumus = r"K_{sp} = s^2"
        elif "AB₂" in senyawa_type: # Tipe AB2 / A2B
            ksp = 4 * (s_val ** 3)
            rumus = r"K_{sp} = 4s^3"
        elif "AB₃" in senyawa_type: # Tipe AB3 / A3B
            ksp = 27 * (s_val ** 4)
            rumus = r"K_{sp} = 27s^4"
        elif "A₂B₃" in senyawa_type: # Tipe A2B3 / A3B2
            ksp = 108 * (s_val ** 5)
            rumus = r"K_{sp} = 108s^5"
            
        # Menampilkan Hasil
        st.success(f"**Nilai Ksp = {ksp:.4e}**")
        st.info("Rumus yang digunakan:")
        st.latex(rumus)

# Footer / Disclaimer
st.markdown("---")
st.caption("Aplikasi ini dibuat sebagai alat bantu. Pastikan Anda tetap memahami konsep dasar kesetimbangan kimia sesuai saran dalam makalah.")
