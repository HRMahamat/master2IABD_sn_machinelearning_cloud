import streamlit as st

st.set_page_config(page_title="Redirection", layout="centered")

# L'URL vers laquelle vous voulez aller
url = "https://ccsnmldanslecloud-5veganhynafcywu6dqndub.streamlit.app/"

st.markdown(
    """
    <div style="text-align: center; margin-top: 10%;">
        <h2>Portail de Redirection</h2>
        <p>Pour accéder à votre application de Machine Learning, veuillez cliquer sur le bouton ci-dessous :</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Utilisation de la méthode officielle moderne (Zéro JavaScript, Zéro Iframe bloquée)
st.link_button("🚀 Ouvrir l'application cible", url, use_container_width=True)

st.markdown(
    f"""
    <div style="text-align: center; margin-top: 5%; color: gray; font-size: 0.85em;">
        <p>Note : Si après avoir cliqué vous revenez sur cette même page, vérifiez que le dépôt GitHub de l'application cible n'est pas le même que celui-ci.</p>
    </div>
    """,
    unsafe_allow_html=True
)
