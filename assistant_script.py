
import streamlit as st
import os
import re

# Dictionnaire des scripts disponibles
scripts = {
    "Script pour récupérer dans un référentiel tiers": "Script pour récupérer dans un référentiel tiers 1.txt",
    "Script pour récupérer une partie d'une métadonne": "Script pour récupérer une partie d'une métadonne  1.txt",
    "Script Contrôle de Cohérence entre un référentiel et un index": "Script Contrôle de Cohérence entre un référentiel et un index 1.txt",
    "Script pour mettre demat ou non suite à une valeur": "Script pour mettre demat ou non suite à une valeur .txt",
    "Script pour Séparer un code barre": "Script pour Séparer un code barre.txt",
    "Script pour des erreurs OCR": "Script pour des erreurs OCR .txt"
}

# Fonction pour charger le contenu d'un script
def load_script(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return f.read()

# Fonction pour détecter les variables personnalisables (ex: NOM_VARIABLE)
def detect_variables(script_text):
    return sorted(set(re.findall(r"\b[A-Z_]{2,}\b", script_text)))

# Fonction pour remplacer les variables par les valeurs saisies
def personalize_script(script_text, replacements):
    for var, val in replacements.items():
        script_text = script_text.replace(var, val)
    return script_text

# Interface Streamlit
st.title("🛠️ Assistant de génération de scripts personnalisés")

# Choix du script
script_name = st.selectbox("Choisissez un script de base :", list(scripts.keys()))

if script_name:
    script_file = scripts[script_name]
    if os.path.exists(script_file):
        script_content = load_script(script_file)
        st.subheader("🔍 Aperçu du script original")
        st.code(script_content, language="javascript")

        # Détection des variables personnalisables
        variables = detect_variables(script_content)
        st.subheader("✏️ Personnalisation des variables")
        replacements = {}
        for var in variables:
            val = st.text_input(f"Valeur pour {var} :", key=var)
            replacements[var] = val

        # Génération du script personnalisé
        if st.button("✅ Générer le script personnalisé"):
            final_script = personalize_script(script_content, replacements)
            st.subheader("📄 Script généré")
            st.code(final_script, language="javascript")

            # Téléchargement
            st.download_button(
                label="📥 Télécharger le script",
                data=final_script,
                file_name=f"{script_name.replace(' ', '_')}_personnalise.js",
                mime="text/javascript"
            )
    else:
        st.error(f"Le fichier {script_file} est introuvable.")
