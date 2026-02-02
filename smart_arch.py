import streamlit as st
import random

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Smart Arch Prompter",
    page_icon="🏡",
    layout="centered"
)

# --- 2. DATABASE OPSI (BANK DATA) ---
# Data ini digunakan untuk pilihan dropdown dan fitur acak (random)
DB_TIPE = [
    "Modern Minimalist House", "Grand Mosque (Masjid)", "Tropical Villa", 
    "Industrial Office", "Futuristic Skyscraper", "Bamboo Eco-Lodge",
    "Luxury Penthouse", "Cultural Center", "Parametric Pavilion"
]

DB_GAYA = [
    "Futuristic", "Contemporary", "Islamic Modern", "Biophilic/Green", 
    "Brutalist", "Zaha Hadid Style", "Parametric Design", 
    "Scandinavian", "Japanese Zen"
]

DB_MATERIAL = [
    "concrete, glass, and wood accents", "white marble and gold trim", 
    "exposed brick and steel", "sustainable bamboo and stone", 
    "reflective glass facade", "weathered corten steel",
    "polished travertin stone"
]

DB_SUASANA = [
    "Golden Hour (Sunset)", "Blue Hour (Twilight)", "Sunny Day", 
    "Foggy Morning", "Cinematic Night Lighting", "Rainy Cyberpunk Mood",
    "Overcast Soft Light"
]

DB_ENGINE = [
    "Unreal Engine 5", "V-Ray Render", "Octane Render", 
    "Corona Render", "Lumion Render"
]

# --- 3. FUNGSI LOGIKA ---

def generate_prompt_text(tipe, gaya, material, pencahayaan, render_engine):
    """Fungsi untuk menyusun string prompt akhir"""
    prompt = f"/imagine prompt: Hyper-realistic architectural render of a {tipe}, designed in {gaya} style. "
    prompt += f"Featuring {material} facade details. "
    prompt += f"Atmosphere: {pencahayaan}. "
    prompt += f"High quality, 8k resolution, detailed texture, photorealistic, {render_engine}, --ar 16:9 --v 6.0"
    return prompt

def acak_semua():
    """Callback function untuk mengacak nilai di session state"""
    st.session_state.k_tipe = random.choice(DB_TIPE)
    st.session_state.k_gaya = random.choice(DB_GAYA)
    st.session_state.k_material = random.choice(DB_MATERIAL)
    st.session_state.k_suasana = random.choice(DB_SUASANA)
    st.session_state.k_engine = random.choice(DB_ENGINE)

# --- 4. INISIALISASI SESSION STATE ---
# Langkah ini penting agar variabel tidak kosong saat pertama load
if 'k_tipe' not in st.session_state: st.session_state.k_tipe = DB_TIPE[0]
if 'k_gaya' not in st.session_state: st.session_state.k_gaya = DB_GAYA[0]
if 'k_material' not in st.session_state: st.session_state.k_material = DB_MATERIAL[0]
if 'k_suasana' not in st.session_state: st.session_state.k_suasana = DB_SUASANA[0]
if 'k_engine' not in st.session_state: st.session_state.k_engine = DB_ENGINE[0]

# --- 5. TAMPILAN UI (USER INTERFACE) ---

st.title("🏡 Smart Arch Prompter")
st.write("Generator prompt otomatis untuk visualisasi arsitektur DED & Desain.")
st.markdown("---")

# Tombol Random Surprise
# Menggunakan callback 'on_click' agar form terupdate otomatis sebelum re-run
st.button("🎲 Random Surprise Me! (Acak Ide)", type="secondary", on_click=acak_semua, use_container_width=True)

st.write("") # Spacer

# Area Form Input
# Kita gunakan st.container untuk merapikan layout
with st.container(border=True):
    col1, col2 = st.columns(2)

    with col1:
        # Parameter 'key' menghubungkan widget langsung ke session_state
        st.selectbox("Tipe Bangunan", DB_TIPE, key='k_tipe')
        st.selectbox("Gaya Desain", DB_GAYA, key='k_gaya')

    with col2:
        # Text input juga bisa diacak karena kita set value-nya dari session_state
        st.text_input("Material Utama", key='k_material') 
        st.selectbox("Pencahayaan / Suasana", DB_SUASANA, key='k_suasana')

    st.markdown("---")
    st.radio("Engine Style", DB_ENGINE, horizontal=True, key='k_engine')

# --- 6. OUTPUT SECTION ---
st.write("") # Spacer
if st.button("✨ Generate Prompt Akhir", type="primary", use_container_width=True):
    
    # Memanggil fungsi penyusun teks
    final_prompt = generate_prompt_text(
        st.session_state.k_tipe,
        st.session_state.k_gaya,
        st.session_state.k_material,
        st.session_state.k_suasana,
        st.session_state.k_engine
    )
    
    st.success("Prompt Berhasil Dibuat! 👇")
    st.code(final_prompt, language="text")
    st.caption("Copy kode di atas dan paste ke Midjourney atau AI Image Generator lain.")

# Footer
st.markdown("---")
st.caption("Developed for Civil & Arch Engineering | v1.0")
  
