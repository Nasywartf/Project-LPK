            import streamlit as st
from PIL import Image

# Konfigurasi halaman
st.set_page_config(page_title="Interpretasi Spektrum IR", page_icon="🔬", layout="centered")

# Tampilan utama dengan warna dan header
st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h1 style='color: teal;'>🔬 Aplikasi Interpretasi Spektrum IR</h1>
        <h4 style='color: gray;'>Membantu memahami gugus fungsi melalui panjang gelombang IR</h4>
    </div>
""", unsafe_allow_html=True)

# Sidebar navigasi
menu = st.sidebar.selectbox("📂 Navigasi", ["🏠 Beranda", "📖 Teori & Latar Belakang", "🛠️ Petunjuk Penggunaan", "🎯 Tujuan Aplikasi", "👨‍💻 Pembuat Aplikasi"])

if menu == "🏠 Beranda":
    st.success("👋 Selamat datang di aplikasi Interpretasi Spektrum IR!")
    st.markdown("""
    Aplikasi ini dirancang untuk membantu pelajar, mahasiswa, dan analis kimia dalam:
    - Mengidentifikasi **gugus fungsi** dari panjang gelombang IR
    - Menyederhanakan analisis data IR secara **cepat & akurat**
    - Meningkatkan pemahaman hubungan **struktur molekul dan spektrum IR**
    
    Silakan navigasi menggunakan **menu di samping kiri** untuk memulai 📂
    """)

elif menu == "📖 Teori & Latar Belakang":
    st.header("📖 Teori dan Latar Belakang")
    st.markdown("""
**Spektroskopi Inframerah (IR)** adalah teknik untuk menganalisis senyawa berdasarkan interaksi antara molekul dan radiasi inframerah.  
Energi IR menyebabkan ikatan antar atom dalam molekul mengalami **getaran** seperti:

- 🔁 **Stretching** (regangan)
- 🔂 **Bending** (tekukan)

### 📚 Latar Belakang
- Spektrum IR dihasilkan saat gugus fungsi menyerap energi tertentu.
- Tiap gugus menyerap pada **rentang cm⁻¹ khas**, membentuk pola pita unik.
- **IR sangat berguna dalam identifikasi senyawa organik**: alkohol, asam, ester, keton, dan lainnya.

### 📊 Tabel Pita Serapan Umum

| Bilangan Gelombang (cm⁻¹) | Gugus Fungsi              | Keterangan                        |
|---------------------------|---------------------------|-----------------------------------|
| ~1700                     | **C=O**                   | Karbonil                          |
| >3200                     | **O–H** (lebar)           | Alkohol, Asam Karboksilat        |
| ~2250                     | **C≡N** / **C≡C**          | Nitril / Alkuna                  |
| 1600–1500                 | **C=C**                   | Alkena, Aromatik                 |
| ~3300                     | **N–H**, ≡C–H             | Amina, Alkinil                   |

""", unsafe_allow_html=True)

elif menu == "🛠️ Petunjuk Penggunaan":
    st.header("🛠️ Petunjuk Penggunaan")
    st.markdown("""
1. Masukkan **nilai bilangan gelombang IR** (dalam cm⁻¹) pada kolom input.
2. Gunakan dua nilai jika ingin mendeteksi **gugus fungsi kompleks** seperti asam karboksilat (misal: 1700 dan 3200 cm⁻¹).
3. Klik tombol **"🔍 Identifikasi"** untuk melihat hasil interpretasi.
4. Gambar struktur dan keterangan gugus akan ditampilkan.

> ⚠️ Jika nilai tidak dikenali, pastikan berada dalam rentang umum IR: **400–4000 cm⁻¹**
""")

elif menu == "🎯 Tujuan Aplikasi":
    st.header("🎯 Tujuan Aplikasi")
    st.markdown("""
Aplikasi ini bertujuan untuk:
- 💡 Membantu pengguna mengenali **gugus fungsi** berdasarkan spektrum IR
- 🧪 Meningkatkan pemahaman **korelasi struktur senyawa & data IR**
- ⏱️ Mempercepat proses identifikasi dalam praktikum dan riset kimia organik
""")

elif menu == "👨‍💻 Pembuat Aplikasi":
    st.header("👨‍💻 Tentang Pembuat")
    st.markdown("""
- **Nama**: [Nama Anda]
- **Institusi**: [Politeknik AKA Bogor, atau universitas Anda]
- **Keterangan**: Aplikasi ini dikembangkan menggunakan **Python + Streamlit** sebagai proyek edukatif dalam bidang **analisis kimia organik**.
""")

# ==== Bagian utama input nilai IR ====
st.divider()
st.markdown("### 🔎 Mulai Interpretasi")

# Input
nilai1 = st.number_input("Masukkan panjang gelombang IR pertama (cm⁻¹)", min_value=400, max_value=4000, step=1)
nilai2 = st.number_input("Masukkan panjang gelombang IR kedua (opsional)", min_value=0, max_value=4000, step=1)

# Data
gugus_fungsi = [
    {"rentang": (1820, 1660), "gugus": "C=O (Karbonil)", "img": "https://i.imgur.com/7h7TTzu.png"},
    {"rentang": (3400, 2400), "gugus": "O–H (Asam Karboksilat)", "img": "https://i.imgur.com/purxZOP.png"},
    {"rentang": (3600, 3300), "gugus": "O–H (Alkohol/Fenol)", "img": "https://i.imgur.com/HNEtgnP.png"},
    {"rentang": (3500, 3500), "gugus": "N–H (Amina/Amida)", "img": "https://i.imgur.com/XJL9zVu.png"},
    {"rentang": (2850, 2750), "gugus": "C–H (Aldehid)", "img": "https://i.imgur.com/XyXMHdo.png"},
    {"rentang": (1300, 1000), "gugus": "C–O (Ester/Alkohol)", "img": "https://i.imgur.com/nfVPzkH.png"},
    {"rentang": (1650, 1450), "gugus": "C=C (Aromatik)", "img": "https://i.imgur.com/0uEzgkT.png"},
    {"rentang": (2250, 2250), "gugus": "C≡N (Nitril)", "img": "https://i.imgur.com/OZXhZ4g.png"},
    {"rentang": (2150, 2150), "gugus": "C≡C (Alkuna)", "img": "https://i.imgur.com/ZDw1d6Q.png"},
]

# Tombol interpretasi
if st.button("🔍 Identifikasi"):

    hasil = []

    # Cek kombinasi asam karboksilat
    if (
        (1820 >= nilai1 >= 1660 and 3400 >= nilai2 >= 2400) or
        (1820 >= nilai2 >= 1660 and 3400 >= nilai1 >= 2400)
    ):
        st.success("🔴 *Kemungkinan besar: Asam Karboksilat (–COOH)*")
        st.image("https://i.imgur.com/purxZOP.png", caption="Struktur Asam Karboksilat", use_column_width=True)

    # Cek nilai satu per satu
    for nilai in [nilai1, nilai2]:
        if nilai == 0:
            continue
        cocok = False
        for item in gugus_fungsi:
            low, high = item["rentang"]
            if low >= nilai >= high or low <= nilai <= high:
                with st.container():
                    col1, col2 = st.columns([2, 1])
                    with col1:
                        st.success(f"✓ {nilai} cm⁻¹ → {item['gugus']}")
                    with col2:
                        st.image(item["img"], width=100)
                cocok = True
        if not cocok:
            st.error(f"✖ {nilai} cm⁻¹ → Tidak cocok dengan database.")
