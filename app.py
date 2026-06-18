import streamlit as st

st.set_page_config(layout="centered")

url = "https://ccsnmldanslecloud-5veganhynafcywu6dqndub.streamlit.app/"

# Utilisation combinée d'un script JS qui cible la fenêtre principale (window.top)
st.markdown(
    f"""
    <script>
        // Force la page parente globale à changer d'adresse
        window.top.location.href = "{url}";
    </script>
    """,
    unsafe_allow_html=True
)

# Message et secours visuel indispensable pendant la micro-seconde de chargement
st.markdown(
    f"""
    <div style="text-align: center; margin-top: 20%; font-family: sans-serif;">
        <h3>Redirection vers l'application cible...</h3>
        <p>Si l'application ne s'ouvre pas automatiquement, 
        <a href="{url}" target="_top" style="color: #ff4b4b; font-weight: bold;">cliquez ici</a>.</p>
    </div>
    """,
    unsafe_allow_html=True
)
