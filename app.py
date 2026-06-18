import streamlit as st

st.set_page_config(
    page_title="ML in the Cloud – Présentation du Devoir · Streamlit", 
    page_icon="🧠", 
    layout="centered"
)

url = "https://ccsnmldanslecloud-5veganhynafcywu6dqndub.streamlit.app/"

# Style pour centrer les éléments et styliser le bouton
st.markdown(
    """
    <style>
    /* Supprime les en-têtes et pieds de page natifs */
    [data-testid="stHeader"], footer {display: none !important;}
    
    .loader-container {
        text-align: center;
        margin-top: 15%;
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
    }
    .spinner {
        border: 4px solid rgba(0, 0, 0, 0.05);
        width: 45px;
        height: 45px;
        border-radius: 50%;
        border-left-color: #FF4B4B;
        animation: spin 0.8s linear infinite;
        margin: 0 auto 20px auto;
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    </style>
    
    <div class="loader-container">
        <div class="spinner"></div>
        <h2 style="color: #31333F; font-weight: 600;">Chargement de l'application...</h2>
        <p style="color: #76777F;">Préparation de votre espace Machine Learning</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Bouton officiel Streamlit qui prendra automatiquement le thème Light du config.toml
st.link_button("⚡ Entrer dans l'application", url, use_container_width=True)
