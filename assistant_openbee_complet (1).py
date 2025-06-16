import streamlit as st
import re

def to_camel_case(s):
    parts = s.lower().split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])

st.set_page_config(page_title="Assistant Script Openbee", layout="centered")
st.title("🧠 Assistant Script Openbee")
st.subheader("Script : Indiquer une valeur selon la présence d'une donnée")

script_type = st.selectbox("Choisissez le type de script à générer :", ["Présence d'une donnée", "Récupération d'une valeur"])

index_name = st.text_input("Quel est le nom de l’index de référence ?", value="EMAIL_INDEX")
value_if_exists = st.text_input("Que doit-on retourner si une valeur existe ?", value="DEMAT")
value_if_not_exists = st.text_input("Que doit-on retourner si aucune valeur n'existe ?", value="NON DEMAT")

if index_name and value_if_exists and value_if_not_exists:
    variable_name = to_camel_case(index_name)

    if script_type == "Présence d'une donnée":
        script_js = f"""// Récupération de la valeur de {index_name}
var {variable_name} = getTextFromIndexInfo(getFirstIndexFromID(pParameters, \"{index_name}\"));

// Vérification de la présence d'une valeur dans {index_name}
if ({variable_name} && {variable_name}.trim() !== \"") {{
    return \"{value_if_exists}\";  // Retourne \"{value_if_exists}\" si {variable_name} contient quelque chose
}} else {{
    return \"{value_if_not_exists}\"; // Retourne \"{value_if_not_exists}\" si {variable_name} est vide ou invalide
}}"""
    else:
        script_js = f"""// Récupération de la valeur de l’index {index_name}
var {variable_name} = getTextFromIndexInfo(getFirstIndexFromID(pParameters, \"{index_name}\"));
return {variable_name};"""

    st.markdown("### 📝 Script généré :")
    st.code(script_js, language="javascript")
    st.success("Script généré avec succès !")
