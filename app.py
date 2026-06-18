import streamlit as st

st.set_page_config(
    page_title="ML in the Cloud – Présentation du Devoir · Streamlit", 
    page_icon="🧠", 
    layout="centered"
)

url = "https://ccsnmldanslecloud-5veganhynafcywu6dqndub.streamlit.app/"

# Injection CSS avec forçage global ( !important ) sur les conteneurs natifs de Streamlit
st.markdown(
    """
    <style>
    /* 1. Force le fond blanc pur sur toute l'application Streamlit */
    [data-testid="stAppViewContainer"], 
    [data-testid="stHeader"], 
    .stApp {
        background-color: #FFFFFF !important;
    }

    /* 2. Masque complètement les éléments parasites de l'interface */
    [data-testid="stToolbar"], 
    footer, 
    header {
        display: none !important;
        visibility: hidden !important;
    }
    
    /* 3. Style de la zone centrale de chargement */
    .loader-container {
        text-align: center;
        margin-top: 15%;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    .spinner {
        border: 4px solid rgba(0, 0, 0, 0.05);
        width: 45px;
        height: 45px;
        border-radius: 50%;
        border-left-color: #FF4B4B; /* Rouge Streamlit officiel */
        animation: spin 0.8s linear infinite;
        margin: 0 auto 20px auto;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    .loader-title {
        color: #31333F !important;
        font-weight: 600 !important;
        font-size: 1.75rem !important;
        margin-bottom: 8px !important;
    }

    .loader-subtitle {
        color: #76777F !important;
        font-size: 1rem !important;
        margin-bottom: 30px !important;
    }

    /* 4. Refonte totale du bouton pour qu'il ressemble à un bouton d'action système */
    .stButton > button {
        width: 100% !important;
        background-color: #FF4B4B !important;
        color: #FFFFFF !important;
        border: 1px solid #FF4B4B !important;
        padding: 10px 24px !important;
        font-size: 16px !important;
        font-weight: 500 !important;
        border-radius: 8px !important;
        box-shadow: rgba(0, 0, 0, 0.05) 0px 1px 2px 0px !important;
        transition: all 0.2s ease-in-out !important;
    }
    
    .stButton > button:hover {
        background-color: #E03E3E !important;
        border-color: #E03E3E !important;
        color: #FFFFFF !important;
    }
    </style>
    
    <div class="loader-container">
        <div class="spinner"></div>
        <h2 class="loader-title">Chargement de l'application...</h2>
        <p class="loader-subtitle">Préparation de votre espace Machine Learning</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Bouton officiel enveloppé par notre CSS global
st.link_button("⚡ Entrer dans l'application", url, use_container_width=True)
