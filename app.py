import streamlit as st

# Correction ici : ajout des guillemets autour de "centered"
st.set_page_config(page_title="Routage de l'application", layout="centered")

url = "https://ccsnmldanslecloud-5veganhynafcywu6dqndub.streamlit.app/"

# Styles personnalisés pour intégrer proprement le bouton
st.markdown(
    """
    <style>
    /* Supprime les éléments inutiles de Streamlit pour faire "page blanche" */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Style du conteneur de chargement */
    .loader-container {
        text-align: center;
        margin-top: 15%;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .spinner {
        border: 4px solid rgba(0, 0, 0, 0.1);
        width: 40px;
        height: 40px;
        border-radius: 50%;
        border-left-color: #ff4b4b;
        animation: spin 1s linear infinite;
        margin: 0 auto 20px auto;
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    </style>
    
    <div class="loader-container">
        <div class="spinner"></div>
        <h2>Passerelle d'accès au Cloud</h2>
        <p style="color: #666;">Pour des raisons de sécurité de votre navigateur, veuillez valider le lancement ci-dessous!</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Un bouton standard mais habillé pour être l'unique action possible
st.link_button("⚡ Entrer dans l'application", url, use_container_width=True)
