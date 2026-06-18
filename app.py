import streamlit as st

st.set_page_config(layout="centered")

url = "https://ccsnmldanslecloud-5veganhynafcywu6dqndub.streamlit.app/"

# Message visuel propre
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

# Nouvelle méthode officielle 2026 pour injecter le script de redirection
st.iframe(
    srcdoc=f"""
    <script>
        window.top.location.replace("{url}");
    </script>
    """,
    height=0,
    width=0
)
