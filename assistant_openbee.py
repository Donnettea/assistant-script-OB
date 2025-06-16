
import streamlit as st

st.set_page_config(page_title="Assistant Script Openbee", layout="centered")

st.title("🧠 Assistant Script Openbee")
st.subheader("Script : Récupérer une valeur d'un référentiel tiers")

# Question à l'utilisateur
ref_index = st.text_input("Quel est l'index du référentiel tiers ?", value="MAIL_PARTAGE_INDEX")

# Génération du script personnalisé
if ref_index:
    script_js = f'''var getThirdPartVariable = function(pID) {{
    for (var i = 0; i < THIRDPART.values.length; i++) {{
        if (THIRDPART.values[i].id === pID)
            return THIRDPART.values[i].rawValue || "";
    }}
    return "";
}};

var mailPartageIndex = getThirdPartVariable("{ref_index}");
return mailPartageIndex;'''

    st.markdown("### 📝 Script généré :")
    st.code(script_js, language="javascript")

    st.success("Script généré avec succès !")
