import streamlit as st
import random

st.set_page_config(page_title="Mau Jadi Pacarku?", layout="centered")

# Styling sederhana (mirip HTML kamu)
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 36px;
        color: #7a0040;
    }
    .subtitle {
        text-align: center;
        color: #7a0040;
        margin-bottom: 20px;
    }
    .stButton>button {
        border-radius: 12px;
        padding: 10px 16px;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Judul
st.markdown('<div class="title">Mau nggak jadi pacarku? 😁✨</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Pilih jujur ya… hati-hati tombolnya nakal 😜</div>', unsafe_allow_html=True)

# State untuk posisi tombol "Gamau"
if "x" not in st.session_state:
    st.session_state.x = random.randint(0, 300)
    st.session_state.y = random.randint(0, 100)

def move_button():
    st.session_state.x = random.randint(0, 300)
    st.session_state.y = random.randint(0, 100)

# Layout pakai columns biar mirip tengah
col1, col2 = st.columns(2)

with col1:
    if st.button("Mau! 💚"):
        st.success("Yeay! Kamu resmi jadi kebahagiaanku! 💖")

with col2:
    # Tombol "Gamau" yang pindah-pindah
    st.markdown(
        f"""
        <div style="
            position: relative;
            height: 150px;
        ">
            <form action="" method="post">
                <button 
                    style="
                        position:absolute;
                        left:{st.session_state.x}px;
                        top:{st.session_state.y}px;
                        background-color:#f4511e;
                        color:white;
                        border:none;
                        border-radius:12px;
                        padding:10px 16px;
                        cursor:pointer;
                    "
                >
                    Gamau 🙅‍♀️
                </button>
            </form>
        </div>
        """,
        unsafe_allow_html=True
    )

# Trigger pindah posisi setiap rerun (simulasi hover/click)
move_button()