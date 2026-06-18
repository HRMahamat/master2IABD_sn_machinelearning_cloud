import streamlit as st

# Application du Favicon de l'application cible (le cerveau 🧠)
st.set_page_config(
    page_title="ML in the Cloud – Présentation du Devoir · Streamlit", 
    page_icon="🧠", 
    layout="centered"
)

url = "https://ccsnmldanslecloud-5veganhynafcywu6dqndub.streamlit.app/"

# Injection CSS imitant la structure Streamlit Cloud reçue
st.markdown(
    """
    <style>
    /* 1. Recréation de l'arrière-plan Streamlit Cloud standard (#FFFFFF) */
    .stApp {
        background-color: #FFFFFF !important;
    }

    /* 2. Suppression de tous les éléments d'interface natifs pour le clonage */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 3. Zone de chargement calquée sur l'esthétique du code source */
    .loader-container {
        text-align: center;
        margin-top: 18%;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        color: #31333F;
    }
    
    .spinner {
        border: 3px solid rgba(38, 39, 48, 0.1);
        width: 36px;
        height: 36px;
        border-radius: 50%;
        border-left-color: #FF4B4B; /* Le rouge signature de Streamlit */
        animation: spin 0.8s linear infinite;
        margin: 0 auto 24px auto;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    /* 4. Personnalisation du bouton Streamlit pour qu'il s'intègre parfaitement */
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B !important;
        color: white !important;
        border: none !important;
        padding: 12px 24px !important;
        font-size: 16px !important;
        font-weight: 500 !important;
        border-radius: 8px !important;
        transition: background-color 0.2s ease !important;
        box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.05) !important;
    }
    
    .stButton>button:hover {
        background-color: #D33636 !important;
        color: white !important;
    }
    </style>
    
    <div class="loader-container">
        <div class="spinner"></div>
        <h2 style="font-weight: 600; font-size: 1.8rem; margin-bottom: 8px;">Chargement de l'application...</h2>
        <p style="color: #76777F; font-size: 1rem; margin-bottom: 24px;">Préparation de votre espace Machine Learning</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Le bouton d'accès direct habillé aux couleurs de la marque
st.link_button("⚡ Entrer dans l'application", url, use_container_width=True)
