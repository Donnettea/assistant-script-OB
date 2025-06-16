
import streamlit as st

def to_camel_case(s):
    parts = s.lower().split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])

st.set_page_config(page_title="Assistant Script Openbee", layout="centered")

st.title("🧠 Assistant Script Openbee")
st.subheader("Script : Récupérer une valeur d'un référentiel tiers")

# Question à l'utilisateur
ref_index = st.text_input("Quel est l'index du référentiel tiers ?", value="MAIL_PARTAGE_INDEX")

# Génération du script personnalisé
if ref_index:
    variable_name = to_camel_case(ref_index)
    script_js = f'''var getThirdPartVariable = function(pID) {{
    for (var i = 0; i < THIRDPART.values.length; i++) {{
        if (THIRDPART.values[i].id === pID)
            return THIRDPART.values[i].rawValue || "";
    }}
    return "";
}};

var {variable_name} = getThirdPartVariable("{ref_index}");
return {variable_name};'''

    st.markdown("### 📝 Script généré :")
    st.code(script_js, language="javascript")

    st.success("Script généré avec succès !")
