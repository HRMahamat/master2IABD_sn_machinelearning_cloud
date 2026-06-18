import streamlit as st

st.set_page_config(
    page_title="ML in the Cloud – Présentation du Devoir · Streamlit", 
    page_icon="🧠", 
    layout="centered"
)

url = "https://ccsnmldanslecloud-5veganhynafcywu6dqndub.streamlit.app/"

# Injection d'un bloc HTML fixe qui va recouvrir TOUTE la page Streamlit
st.markdown(
    f"""
    <div class="global-overlay">
        <div class="box">
            <div class="spinner"></div>
            <h2>Chargement de l'application...</h2>
            <p>Préparation de votre espace Machine Learning</p>
            <a href="{url}" target="_top" class="custom-btn">⚡ Entrer dans l'application</a>
        </div>
    </div>

    <style>
        /* Force un bloc blanc fixe sur l'intégralité de l'écran par-dessus Streamlit */
        .global-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-color: #FFFFFF !important;
            z-index: 999999; /* S'assure de passer au-dessus du thème sombre */
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }}
        
        .box {{
            text-align: center;
            width: 90%;
            max-width: 400px;
            padding: 20px;
        }}
        
        .spinner {{
            border: 4px solid rgba(0, 0, 0, 0.05);
            width: 45px;
            height: 45px;
            border-radius: 50%;
            border-left-color: #FF4B4B;
            animation: spin 0.8s linear infinite;
            margin: 0 auto 20px auto;
        }}
        
        @keyframes spin {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}
        
        h2 {{
            color: #31333F !important;
            font-weight: 600;
            font-size: 1.6rem;
            margin-bottom: 8px;
            font-family: sans-serif;
        }}
        
        p {{
            color: #76777F !important;
            font-size: 0.95rem;
            margin-bottom: 30px;
            font-family: sans-serif;
        }}
        
        /* Bouton HTML pur, indépendant des caprices de Streamlit */
        .custom-btn {{
            display: block;
            background-color: #FF4B4B !important;
            color: #FFFFFF !important;
            text-decoration: none !important;
            padding: 14px 24px;
            font-size: 16px;
            font-weight: 500;
            border-radius: 8px;
            box-shadow: rgba(0, 0, 0, 0.05) 0px 1px 2px 0px;
            transition: background-color 0.2s;
            font-family: sans-serif;
        }}
        
        .custom-btn:hover {{
            background-color: #E03E3E !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)
