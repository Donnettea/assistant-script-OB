
import streamlit as st

st.set_page_config(page_title="Générateur de commande SAFEQ", layout="centered")

st.title("🖨️ Générateur de ligne de commande SAFEQ Cloud")

# Paramètres principaux
account_domain = st.text_input("Nom du domaine du compte (/ACCOUNTDOMAIN)", "mondomaine.local")

use_gateway = st.radio("Y a-t-il une passerelle Gateway ?", ["Oui", "Non"])
if use_gateway == "Oui":
    gateway_address = st.text_input("Adresse de la Gateway (/GATEWAYADDRESS)", "gateway-safeq.mondomaine.local")
else:
    gateway_address = account_domain

authtype = st.selectbox(
    "Type d’authentification (/AUTHTYPE)",
    options=[
        ("0", "0 = Utilisateur de session (par défaut)"),
        ("1", "1 = Utilisateur + Domaine"),
        ("2", "2 = Connexion personnalisée"),
        ("3", "3 = Nom d'utilisateur principal"),
        ("5", "5 = OpenID Connect"),
        ("6", "6 = SAFEQ Cloud OAuth2"),
    ],
    format_func=lambda x: x[1]
)[0]

# Options booléennes
agpl_ghostscript = st.checkbox("Activer AGPL Ghostscript (/AGPLGHOSTSCRIPT)", value=True)
allow_config = st.checkbox("Autoriser la configuration (/ALLOWCONFIGURATION)", value=False)
remember_login = st.checkbox("Autoriser à mémoriser les identifiants (/ALLOWREMEMBERLOGIN)", value=True)
upgrade = st.checkbox("Mettre à jour si déjà installé (/UPGRADE)", value=False)
reset_config = st.checkbox("Réinitialiser la configuration existante (/RESETCONFIG)", value=True)

# API key
apikey = st.text_input("Clé API personnalisée (/APIKEY)", "")

if st.button("🔧 Générer la ligne de commande"):
    cmd = f"/S /ACCOUNTDOMAIN={account_domain} /GATEWAYADDRESS={gateway_address} /AUTHTYPE={authtype}"
    cmd += f" /AGPLGHOSTSCRIPT={'true' if agpl_ghostscript else 'false'}"
    cmd += f" /ALLOWCONFIGURATION={'true' if allow_config else 'false'}"
    cmd += f" /ALLOWREMEMBERLOGIN={'true' if remember_login else 'false'}"
    cmd += f" /UPGRADE={'true' if upgrade else 'false'}"
    cmd += f" /RESETCONFIG={'true' if reset_config else 'false'}"
    if apikey:
        cmd += f" /APIKEY={apikey}"

    st.code(cmd, language="bash")
    st.success("Ligne de commande générée avec succès !")
