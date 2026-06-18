import streamlit as st

st.set_page_config(
    page_title="ML in the Cloud – Présentation du Devoir · Streamlit", 
    page_icon="🧠", 
    layout="centered"
)

url = "https://ccsnmldanslecloud-5veganhynafcywu6dqndub.streamlit.app/"

# Injection du bloc HTML/CSS en mode sombre avec fix du clic bouton
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
        /* Force un bloc sombre fixe sur l'intégralité de l'écran */
        .global-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-color: #0E1117 !important;
            z-index: 99999;
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
            position: relative;
            z-index: 100000; /* Passe au-dessus du calque de fond pour intercepter le clic */
        }}
        
        .spinner {{
            border: 4px solid rgba(255, 255, 255, 0.1);
            width: 45px;
            height: 45px;
            border-radius: 50%;
            border-left-color: #FF4B4B;
            animation: spin 0.8s linear infinite;
            margin: 0 auto 24px auto;
        }}
        
        @keyframes spin {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}
        
        h2 {{
            color: #FAFAFA !important;
            font-weight: 600;
            font-size: 1.6rem;
            margin-bottom: 8px;
            font-family: sans-serif;
        }}
        
        p {{
            color: #A3A8B8 !important;
            font-size: 0.95rem;
            margin-bottom: 32px;
            font-family: sans-serif;
        }}
        
        /* Bouton HTML pur cliquable */
        .custom-btn {{
            display: block;
            background-color: #FF4B4B !important;
            color: #FFFFFF !important;
            text-decoration: none !important;
            padding: 14px 24px;
            font-size: 16px;
            font-weight: 500;
            border-radius: 8px;
            box-shadow: rgba(0, 0, 0, 0.3) 0px 4px 6px 0px;
            transition: background-color 0.2s, transform 0.1s;
            font-family: sans-serif;
            position: relative;
            z-index: 100001; /* Priorité absolue pour le clic souris */
            cursor: pointer !important;
        }}
        
        .custom-btn:hover {{
            background-color: #E03E3E !important;
        }}
        
        .custom-btn:active {{
            transform: scale(0.98);
        }}
    </style>
    """,
    unsafe_allow_html=True
)
