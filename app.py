import streamlit as st
from PIL import Image

st.set_page_config(page_title="Spektrum IR", page_icon="🔬", layout="centered")

# Tampilan awal / beranda
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color: teal;'>🔬 Selamat Datang di Aplikasi Interpretasi Spektrum IR</h1>
        <p>Aplikasi ini dirancang untuk membantu Anda mengidentifikasi gugus fungsi dari data spektrum Inframerah (IR)!</p>
    </div>
""", unsafe_allow_html=True)

# Navigasi halaman
menu = st.sidebar.selectbox("📂 Navigasi", ["Beranda", "Petunjuk Penggunaan", "Teori IR", "Tujuan Aplikasi", "Pembuat Aplikasi"])

if menu == "Beranda":
    st.info("""
        Silakan gunakan menu di samping kiri untuk membaca teori, memahami petunjuk penggunaan,
        atau langsung mencoba fitur interpretasi spektrum IR.
    """)

elif menu == "Petunjuk Penggunaan":
    st.markdown("""
    ## 🧭 Petunjuk Penggunaan
    1. Masukkan satu atau dua bilangan gelombang (dalam cm⁻¹) hasil dari spektrum IR.
    2. Klik tombol **Identifikasi** untuk melihat kemungkinan gugus fungsi yang sesuai.
    3. Jika Anda memasukkan dua bilangan gelombang, aplikasi akan mencoba mendeteksi gugus kompleks seperti asam karboksilat.
    4. Hasil akan ditampilkan bersama dengan gambar struktur gugus fungsi.
    """)

elif menu == "Teori IR":
    st.markdown("""
    ## 🧪 Teori Dasar Spektroskopi Inframerah (IR)
    Spektroskopi Inframerah (IR) adalah teknik analisis yang digunakan untuk **mengidentifikasi gugus fungsi** dalam molekul.

    ### 🔬 Prinsip Dasar
    - Molekul menyerap radiasi IR → menyebabkan ikatan atom bergetar.
    - Jenis getaran:
        - **Regangan (stretching)**: perubahan panjang ikatan.
        - **Tekukan (bending)**: perubahan sudut ikatan.

    ### 📏 Bilangan Gelombang
    - Diukur dalam satuan **cm⁻¹**.
    - Setiap gugus fungsi menyerap IR pada rentang tertentu (pita serapan).

    ### 📌 Contoh Pita Serapan Umum
    | Bilangan Gelombang (cm⁻¹) | Gugus Fungsi              | Keterangan                        |
    |---------------------------|---------------------------|-----------------------------------|
    | ~1700                     | **C=O**                   | Karbonil (keton, aldehid, ester) |
    | >3200                     | **O–H** (lebar)           | Alkohol, Asam karboksilat        |
    | ~2250                     | **C≡N** atau **C≡C**       | Nitril atau Alkuna               |
    | 1600–1500                 | **C=C** aromatik          | Senyawa aromatik                 |
    | ~3300                     | **N–H**, ≡C–H             | Amina, Asetilenik                |

    ### 🎯 Kegunaan IR
    - Mengidentifikasi **struktur senyawa**
    - Menentukan **gugus fungsi** dalam kimia organik
    - Digunakan di bidang farmasi, lingkungan, dan bahan kimia
    """, unsafe_allow_html=True)

elif menu == "Tujuan Aplikasi":
    st.success("""
    Aplikasi ini bertujuan:
    - Membantu pengguna menginterpretasikan data IR secara cepat dan akurat.
    - Menghubungkan data spektrum IR dengan struktur gugus fungsi.
    - Meningkatkan efisiensi dalam praktikum dan analisis laboratorium kimia.
    """)

elif menu == "Pembuat Aplikasi":
    st.warning("""
    ### 👨‍💻 Tim Pengembang Aplikasi
    Aplikasi ini dibuat oleh:
    
    - **Annisa Balqis Salsabila**
    - **Fachria Ilmi Dwikanya Atikasari**
    - **Marsya Putri Naisyila**
    - **Nasywa Arta Fatehah**
    - **Silmi Kaffah**
    
    📌 Sebagai bagian dari proyek tugas mata kuliah dan inovasi praktikum berbasis Python & Streamlit.
    """)
