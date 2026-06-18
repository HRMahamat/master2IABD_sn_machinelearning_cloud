import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="centered")

url = "https://ccsnmldanslecloud-5veganhynafcywu6dqndub.streamlit.app/"

# Message visuel d'attente
st.markdown(
    f"""
    <div style="text-align: center; margin-top: 15%; font-family: sans-serif;">
        <h2>Redirection vers l'application cible...</h2>
        <p>Si la page ne se charge pas automatiquement, 
        <a href="{url}" target="_top" style="color: #ff4b4b; font-weight: bold;">cliquez ici</a>.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Injection du script via la méthode de composant stable
# On utilise window.location au cas où window.top soit bloqué par le bac à sable
components.html(
    f"""
    <script>
        try {{
            window.top.location.replace("{url}");
        }} catch (e) {{
            window.location.replace("{url}");
        }}
    </script>
    """,
    height=0,
    width=0
)
