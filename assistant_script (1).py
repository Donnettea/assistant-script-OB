import streamlit as st
import re

# Dictionnaire contenant les scripts en dur
scripts = {
    "Script pour récupérer dans un référentiel tiers": """var getThirdPartVariable = function(pID) {
  for (var i = 0; i < THIRDPART.values.length; i++) {
    if (THIRDPART.values[i].id === pID)
      return THIRDPART.values[i].rawValue;
  }
  return "";
};
""",
    "Script pour récupérer une partie d'une métadonnée": """var dateIndex = getTextFromIndexInfo(getFirstIndexFromID(pParameters, "DATE_1_INDEX"));
if (dateIndex && dateIndex.trim() !== "") {
  var dateParts = dateIndex.split("/");
  if (dateParts.length === 3) {
    var annee = dateParts[2];
    return annee;
  }
}
return "Date invalide";
""",
    "Script Contrôle de Cohérence entre un référentiel et un index": """if (emailIndex === bpeEmailIndex) {
  return "OK";
} else {
  return "NON";
}
""",
    "Script pour mettre demat ou non suite à une valeur": """var emailIndex = getTextFromIndexInfo(getFirstIndexFromID(pParameters, "EMAIL_INDEX"));
if (emailIndex && emailIndex.trim() !== "") {
  return "DEMAT";
} else {
  return "NON DEMAT";
}
""",
    "Script pour Séparer un code barre": """var cbIndex = getTextFromIndexInfo(getFirstIndexFromID(pParameters, "CB_INDEX"));
if (cbIndex && cbIndex.trim() !== "") {
  var parts = cbIndex.split("*");
  return parts[1];

  if (parts[1]) {
    setTextIntoIndexFromID(pParameters, "CODE_TIERS_INDEX", parts[1]);
  }
  return "Partie avant le premier * : " + parts[0] + " \n Partie entre les * : " + parts[1];
} else {
  return "CB vide ou invalide";
}
""",
    "Script pour des erreurs OCR": """var mailIndex = getTextFromIndexInfo(getFirstIndexFromID(pParameters, "MAIL_INDEX"));

if (mailIndex && mailIndex.trim() !== "") {
  var emailPattern = /^([^@]+)@(.*)$/;
  var match = mailIndex.match(emailPattern);

  if (match) {
    var username = match[1];
    var domain = match[2].toLowerCase();
    var correctedEmail = mailIndex;

    if (domain.includes("hotmaail")) {
      correctedEmail = `${username}@hotmail.fr`;
    } else if (domain.includes("sffr") || domain.includes("sfrr")) {
      correctedEmail = `${username}@sfr.fr`;
    } else if (domain.includes("orange..")) {
      correctedEmail = `${username}@orange.fr`;
    } else if (domain.includes("hootmail")) {
      correctedEmail = `${username}@hotmail.fr`;
    }

    return correctedEmail;
  } else {
    return mailIndex;
  }
} else {
  return "NON";
}
"""
}

st.title("🧠 Assistant de génération de scripts personnalisés")

# Choix du script
script_name = st.selectbox("Choisissez un script modèle :", list(scripts.keys()))

# Script sélectionné
script_template = scripts[script_name]

# Détection des variables personnalisables (ex: EMAIL_INDEX, CB_INDEX, etc.)
placeholders = sorted(set(re.findall(r'\"([A-Z0-9_]+)\"', script_template)))

# Saisie des valeurs personnalisées
st.subheader("🔧 Personnalisez les variables")
user_values = {}
for var in placeholders:
    user_values[var] = st.text_input(f"{var} :", value=var)

# Génération du script final
if st.button("🎯 Générer le script personnalisé"):
    final_script = script_template
    for var, val in user_values.items():
        final_script = final_script.replace(f'\"{var}\"', f'\"{val}\"')
    st.subheader("📄 Script généré")
    st.code(final_script, language="javascript")

    # Téléchargement
    st.download_button("💾 Télécharger le script", data=final_script, file_name="script_personnalise.js", mime="text/javascript")
