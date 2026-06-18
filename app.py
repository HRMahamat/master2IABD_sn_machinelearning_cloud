import streamlit as st

st.set_page_config(
    page_title="ML in the Cloud – Présentation du Devoir · Streamlit", 
    page_icon="🧠", 
    layout="centered"
)

url = "https://ccsnmldanslecloud-5veganhynafcywu6dqndub.streamlit.app/"

# 1. Utilisation de la nouvelle fonction de 2026 st.html pour forcer le thème sombre global
st.html(
    """
    <style>
        /* Force le fond sombre officiel partout */
        [data-testid="stAppViewContainer"], [data-testid="stHeader"], .stApp {
            background-color: #0E1117 !important;
        }
        
        /* Masque les éléments inutiles de l'interface */
        [data-testid="stToolbar"], footer, header {
            display: none !important;
        }

        /* Centre le contenu verticalement */
        .stMainBlockContainer {
            padding-top: 15% !important;
            max-width: 450px !important;
            margin: 0 auto !important;
        }

        /* Style de notre loader */
        .custom-loader {
            text-align: center;
            font-family: sans-serif;
            margin-bottom: 30px;
        }

        .spinner {
            border: 4px solid rgba(255, 255, 255, 0.1);
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

        /* Relooking du VRAI bouton Streamlit pour qu'il soit gros, rouge et magnifique */
        button[data-testid="stBaseButton-secondary"] {
            width: 100% !important;
            background-color: #FF4B4B !important;
            color: #FFFFFF !important;
            border: none !important;
            padding: 14px 24px !important;
            font-size: 16px !important;
            font-weight: 500 !important;
            border-radius: 8px !important;
            height: auto !important;
            box-shadow: rgba(0, 0, 0, 0.3) 0px 4px 6px 0px !important;
        }
        
        button[data-testid="stBaseButton-secondary"]:hover {
            background-color: #E03E3E !important;
            color: #FFFFFF !important;
        }
    </style>
    """
)

# 2. Affichage textuel du Loader
st.markdown(
    """
    <div class="custom-loader">
        <div class="spinner"></div>
        <h2 style="color: #FAFAFA; font-weight: 600; font-family: sans-serif;">Chargement de l'application...</h2>
        <p style="color: #A3A8B8; font-family: sans-serif;">Préparation de votre espace Machine Learning</p>
    </div>
    """,
    unsafe_allow_html=True
)

# 3. Le VRAI bouton Streamlit (qui intercepte le clic à 100%) relié à une action de redirection
if st.button("⚡ Entrer dans l'application", use_container_width=True):
    st.html(
        f"""
        <script>
            window.top.location.href = "{url}";
        </script>
        """
    )
