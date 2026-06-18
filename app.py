import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="ML in the Cloud – Présentation du Devoir · Streamlit", 
    page_icon="🧠", 
    layout="centered"
)

url = "https://ccsnmldanslecloud-5veganhynafcywu6dqndub.streamlit.app/"

# On utilise components.html pour injecter une page HTML autonome et auto-stylisée.
# On lui donne une hauteur (height) suffisante pour occuper l'espace visuel.
components.html(
    f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        html, body {{
            background-color: #FFFFFF !important;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }}
        
        .box {{
            text-align: center;
            max-width: 400px;
            width: 100%;
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
            color: #31333F;
            font-weight: 600;
            font-size: 1.6rem;
            margin-bottom: 8px;
        }}
        
        p {{
            color: #76777F;
            font-size: 0.95rem;
            margin-bottom: 30px;
        }}
        
        .btn {{
            display: block;
            background-color: #FF4B4B;
            color: #FFFFFF;
            text-decoration: none;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: 500;
            border-radius: 8px;
            box-shadow: rgba(0, 0, 0, 0.05) 0px 1px 2px 0px;
            transition: background-color 0.2s;
        }}
        
        .btn:hover {{
            background-color: #E03E3E;
        }}
    </style>
    </head>
    <body>

    <div class="box">
        <div class="spinner"></div>
        <h2>Chargement de l'application...</h2>
        <p>Préparation de votre espace Machine Learning</p>
        <a href="{url}" target="_top" class="btn">⚡ Entrer dans l'application</a>
    </div>

    </body>
    </html>
    """,
    height=600
)
