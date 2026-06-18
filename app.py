import streamlit as st

# Configuration de la page avec le titre et le Favicon cible
st.set_page_config(
    page_title="ML in the Cloud – Présentation du Devoir · Streamlit", 
    page_icon="🧠", 
    layout="centered"
)

url = "https://ccsnmldanslecloud-5veganhynafcywu6dqndub.streamlit.app/"

# Un espacement propre en pur Python pour centrer le contenu sans casser le JS
st.write("")
st.write("")
st.write("")

# Structure de texte standard Streamlit (compatible mode sombre automatique)
st.title("🧠 Portail de Redirection")
st.subheader("Préparation de votre espace Machine Learning")
st.write("Pour des raisons de sécurité liées à l'encapsulation Cloud, veuillez valider l'accès ci-dessous.")

# Le bouton officiel de redirection (Impossible à bloquer ou à rendre inactif)
st.link_button("⚡ Entrer dans l'application", url, use_container_width=True)
