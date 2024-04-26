import streamlit as st

def berat_badan_ideal(tinggi, jenis_kelamin):
    """Fungsi untuk menghitung berat badan ideal berdasarkan tinggi dan jenis kelamin"""
    jenis_kelamin = jenis_kelamin.lower()  # Normalisasi input jenis kelamin
    if jenis_kelamin == 'pria':
        berat_ideal = 22 * (tinggi ** 2)
    elif jenis_kelamin == 'wanita':
        berat_ideal = 21 * (tinggi ** 2)
    else:
        return "Jenis kelamin tidak valid. Masukkan 'pria' atau 'wanita'."
    return berat_ideal

def hitung_kalori(berat_badan_ideal, umur, jenis_kelamin):
    """Fungsi untuk menghitung jumlah kalori yang harus dikonsumsi setiap hari untuk mencapai berat badan ideal"""
    jenis_kelamin = jenis_kelamin.lower()  # Normalisasi input jenis kelamin
    if jenis_kelamin == 'pria':
        kalori = (10 * berat_badan_ideal) + (6.25 * 100) - (5 * umur) + 5
    elif jenis_kelamin == 'wanita':
        kalori = (10 * berat_badan_ideal) + (6.25 * 100) - (5 * umur) - 161
    else:
        return "Jenis kelamin tidak valid. Masukkan 'pria' atau 'wanita'."
    return kalori

def hitung_persen_kalori(berat_badan_ideal):
    """Fungsi untuk menghitung persentase kalori dari protein, karbohidrat, dan lemak"""
    protein_kalori = 4 * berat_badan_ideal * 0.20
    karbohidrat_kalori = 4 * berat_badan_ideal * 0.50
    lemak_kalori = 9 * berat_badan_ideal * 0.30
    total_kalori = protein_kalori + karbohidrat_kalori + lemak_kalori
    persen_protein = (protein_kalori / total_kalori) * 100
    persen_karbohidrat = (karbohidrat_kalori / total_kalori) * 100
    persen_lemak = (lemak_kalori / total_kalori) * 100
    return persen_protein, persen_karbohidrat, persen_lemak

def hitung_kebutuhan_air(berat_badan):
    """Fungsi untuk menghitung kebutuhan air dalam sehari"""
    air = 35 * berat_badan
    return air

def get_sources_nutrients(nutrient):
    sources = {
        "Protein": ["Ayam   (295kkal/100 gram)", "Daging   (143,4kkal/100 gram)", "Ikan   (167kkal/100 gram)", "Telur   (155,1kkal/100 gram)", "Tahu   (80kkal/100 gram)", "Quinoa   (374kkal/100 gram)", "Yogurt   (72kkal/100 gram)", "Salmon   (140kkal/100 gram)"],
        "Lemak": ["Alpukat   (160kkal/100 gram)", "Kacang Polong  (339kkal/100 gram)", "Keju   (402,5kkal/100 gram)", "Dark Chocolate   (581kkal/100 gram)", "Mentega   (358,5-360kkal/50 gram)"],
        "Karbohidrat": ["Nasi Merah   (110kkal/100 gram)", "Kentang   (21,08kkal/100 gram)","Umbi-umbian   (100-120kkal/100 gram)", "Roti Gandum   (250-300kkal/100 gram)", "Oats    (379kkal/100 gram)", "Sagu   (330kkal/100 gram)", "Pisang   (89kkal/100 gram)", "Berries   (30-50kkal/100 gram)", "Jagung   (86-96kkal/100 gram)"]
    }

    return sources.get(nutrient, [])

st.title("PANGAN SEHAT")
st.subheader("Platform Interaktif Untuk Informasi Nutrisi Tubuh yang Ideal")

tinggi_cm = st.number_input("Masukkan tinggi badan Anda (dalam cm):", min_value=0.0)
tinggi_m = tinggi_cm / 100  # Konversi tinggi ke meter
umur = st.number_input("Masukkan umur Anda:", min_value=0, max_value=150, step=1)
jenis_kelamin = st.radio("Jenis Kelamin:", ('Pria', 'Wanita'))

if st.button("Hitung Semua"):
    if tinggi_cm <= 0:  # Validasi tinggi badan
        st.error("Tinggi badan harus lebih besar dari 0.")
    else:
        berat_ideal = berat_badan_ideal(tinggi_m, jenis_kelamin)
        kalori_harian = hitung_kalori(berat_ideal, umur, jenis_kelamin)
        persen_protein, persen_karbohidrat, persen_lemak = hitung_persen_kalori(berat_ideal)
        kebutuhan_air = hitung_kebutuhan_air(berat_ideal)
        
        st.write("Berat Badan Ideal Anda:", "{:.2f}".format(berat_ideal), "kg")
        st.write("Kalori Harian yang Harus Dikonsumsi:", "{:.2f}".format(kalori_harian), "kalori per hari")
        st.write("Persentase Kalori dari Protein:", "{:.2f}".format(persen_protein), "%")
        st.write("Persentase Kalori dari Karbohidrat:", "{:.2f}".format(persen_karbohidrat), "%")
        st.write("Persentase Kalori dari Lemak:", "{:.2f}".format(persen_lemak), "%")
        st.write("Kebutuhan Air Anda:", "{:.2f}".format(kebutuhan_air), "ml per hari")

st.title("Sumber Nutrisi")
st.subheader("Temukan Sumber-Sumber Umum untuk Protein, Lemak, dan Karbohidrat")

selected_nutrient = st.selectbox("Pilih jenis nutrisi:", ["Protein", "Lemak", "Karbohidrat"])

st.write("Berikut adalah sumber-sumber umum untuk", selected_nutrient, ":")
sources_list = get_sources_nutrients(selected_nutrient)
for source in sources_list:
    st.write("- ", source)