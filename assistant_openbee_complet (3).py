import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Assistant Script Openbee", layout="centered")

# Titre principal
st.title("🧠 Assistant Script Openbee")

# Choix du type de script
script_type = st.selectbox(
    "Quel script voulez-vous générer ?",
    [
        "Script - Récupération depuis le référentiel tiers",
        "Script - Renseigner une valeur grâce à une autre métadonnée"
    ]
)

# Fonction pour transformer un nom d'index en camelCase
def format_variable_name(index: str) -> str:
    parts = index.lower().split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

# Script 1 : Récupération depuis le référentiel tiers
if script_type == "Script - Récupération depuis le référentiel tiers":
    st.subheader("Script : Récupération depuis le référentiel tiers")
    ref_index = st.text_input("Quel est l'index du référentiel tiers ?", value="MAIL_PARTAGE_INDEX")

    if ref_index:
        variable_name = format_variable_name(ref_index)
        script_js = f"""var getThirdPartVariable = function(pID) {{
    for (var i = 0; i < THIRDPART.values.length; i++) {{
        if (THIRDPART.values[i].id === pID)
            return THIRDPART.values[i].rawValue || "";
    }}
    return "";
}};

var {variable_name} = getThirdPartVariable("{ref_index}");
return {variable_name};"""

        st.markdown("### 📝 Script généré :")
        st.code(script_js, language="javascript")
        st.success("Script généré avec succès !")

# Script 2 : Renseigner une valeur selon la présence d'une donnée
elif script_type == "Script - Renseigner une valeur grâce à une autre métadonnée":
    st.subheader("Script : Indiquer une valeur selon la présence d'une donnée")

    index_name = st.text_input("Quel est le nom de l’index de référence ?", value="EMAIL_INDEX")
    value_if_exists = st.text_input("Que doit-on retourner si une valeur existe ?", value="DEMAT")
    value_if_not_exists = st.text_input("Que doit-on retourner si aucune valeur n'existe ?", value="NON DEMAT")

    if index_name and value_if_exists and value_if_not_exists:
        variable_name = format_variable_name(index_name)
        script_js = f"""// Récupération de la valeur de {index_name}
var {variable_name} = getTextFromIndexInfo(getFirstIndexFromID(pParameters, "{index_name}"));

// Vérification de la présence d'une valeur dans {index_name}
if ({variable_name} && {variable_name}.trim() !== "") {{
    return "{value_if_exists}";  // Retourne "{value_if_exists}" si {variable_name} contient quelque chose
}} else {{
    return "{value_if_not_exists}"; // Retourne "{value_if_not_exists}" si {variable_name} est vide ou invalide
}}"""

        st.markdown("### 📝 Script généré :")
        st.code(script_js, language="javascript")
        st.success("Script généré avec succès !")

# Encart informatif pour personnalisation via ChatGPT
st.markdown("---")
st.info("💬 Pour aller plus loin dans la personnalisation de votre script, vous pouvez utiliser [ChatGPT](https://chat.openai.com) en vous connectant à votre compte. Posez vos questions ou collez le script généré pour obtenir des suggestions intelligentes.")
