import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Assistant Script Openbee", layout="centered")

# Titre et sous-titre
st.title("🧠 Assistant Script Openbee")
st.subheader("Script : Indiquer une valeur selon la présence d'une donnée")

# Champs de saisie utilisateur
index_name = st.text_input("Quel est le nom de l’index de référence ?", value="EMAIL_INDEX")
value_if_exists = st.text_input("Que doit-on retourner si une valeur existe ?", value="DEMAT")
value_if_not_exists = st.text_input("Que doit-on retourner si aucune valeur n'existe ?", value="NON DEMAT")

# Génération du script si tous les champs sont remplis
if index_name and value_if_exists and value_if_not_exists:
    script_js = f"""// Récupération de la valeur de {index_name}
var emailIndex = getTextFromIndexInfo(getFirstIndexFromID(pParameters, \"{index_name}\"));

// Vérification de la présence d'une valeur dans {index_name}
if (emailIndex && emailIndex.trim() !== \"") {{
    return \"{value_if_exists}\";  // Retourne \"{value_if_exists}\" si emailIndex contient quelque chose
}} else {{
    return \"{value_if_not_exists}\"; // Retourne \"{value_if_not_exists}\" si emailIndex est vide ou invalide
}}"""

    # Affichage du script généré
    st.markdown("### 📝 Script généré :")
    st.code(script_js, language="javascript")
    st.success("Script généré avec succès !")
