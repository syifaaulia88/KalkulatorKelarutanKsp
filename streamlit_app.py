import streamlit as st

# 1. Bagian Judul dan Deskripsi
st.title("🧪 Kalkulator Prediksi Endapan")
st.write("Aplikasi ini membandingkan nilai Qsp dan Ksp untuk memprediksi apakah endapan akan terbentuk.")

# 2. Input Ksp dari Pengguna
# format="%e" memungkinkan pengguna memasukkan notasi ilmiah (contoh: 1.8e-10)
st.subheader("Data Konstanta")
ksp = st.number_input("Masukkan nilai Ksp:", format="%e", value=1.0e-10)

# 3. Membagi layar menjadi 2 kolom untuk input ion
st.subheader("Konsentrasi Ion dalam Larutan")
kolom_kation, kolom_anion = st.columns(2)

with kolom_kation:
    st.markdown("**Kation (Ion Positif)**")
    konsentrasi_kation = st.number_input("Konsentrasi Kation (M):", format="%e", value=1.0e-5)
    koefisien_kation = st.number_input("Pangkat/Koefisien Kation:", min_value=1, value=1)

with kolom_anion:
    st.markdown("**Anion (Ion Negatif)**")
    konsentrasi_anion = st.number_input("Konsentrasi Anion (M):", format="%e", value=1.0e-5)
    koefisien_anion = st.number_input("Pangkat/Koefisien Anion:", min_value=1, value=1)

# 4. Tombol dan Logika Perhitungan Kimia
st.divider() # Membuat garis batas

if st.button("Hitung & Prediksi"):
    # Rumus Qsp: [Kation]^x * [Anion]^y
    # Di Python, simbol ** digunakan untuk pangkat
    qsp = (konsentrasi_kation ** koefisien_kation) * (konsentrasi_anion ** koefisien_anion)
    
    st.write(f"**Nilai $Q_{{sp}}$ yang dihitung:** {qsp:.2e}")
    
    # 5. Logika if/else untuk kesimpula
    if qsp > ksp:
        st.error("Hasil: Qsp > Ksp. **Terjadi Endapan!** ⬇️")
    elif qsp == ksp:
        st.warning("Hasil: Qsp = Ksp. **Larutan Tepat Jenuh** (Belum mengendap).")
    else:
        st.success("Hasil: Qsp < Ksp. **Tidak Terjadi Endapan** (Semua larut). 💧")
