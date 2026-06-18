import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="centered")

url = "https://ccsnmldanslecloud-5veganhynafcywu6dqndub.streamlit.app/"

# 1. Message d'attente propre
st.markdown(
    f"""
    <div style="text-align: center; margin-top: 15%; font-family: sans-serif;">
        <h2 style="color: #31333F;">Chargement de l'application...</h2>
        <p style="color: #76777F;">Veuillez patienter pendant la redirection.</p>
        <p style="font-size: 0.9em; color: #A3A3A3;">Si rien ne se produit après quelques secondes, 
        <a href="{url}" target="_top" style="color: #ff4b4b; font-weight: bold; text-decoration: none;">cliquez ici pour forcer l'accès</a>.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# 2. Utilisation d'un composant HTML isolé avec privilèges d'exécution parent
components.html(
    f"""
    <script type="text/javascript">
        // On force la redirection au niveau le plus haut possible (l'onglet du navigateur)
        // en contournant le bac à sable (sandbox) de Streamlit
        try {{
            window.top.location.replace("{url}");
        }} catch (e) {{
            window.parent.location.href = "{url}";
        }}
    </script>
    """,
    height=0,
    width=0
)
