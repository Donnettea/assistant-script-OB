import streamlit as st

st.set_page_config(page_title="Générateur de commande SAFEQ", layout="wide")
st.title("🧰 Générateur de ligne de commande SAFEQ Cloud")

st.markdown("Ce formulaire vous permet de générer une ligne de commande pour l'installation silencieuse du client SAFEQ Cloud avec tous les paramètres disponibles.")

# Paramètres principaux
st.header("🔧 Paramètres principaux")
account_domain = st.text_input("Nom du domaine du compte (/ACCOUNTDOMAIN)", "mondomaine.local")
gateway_address = st.text_input("Adresse de la passerelle (/GATEWAYADDRESS)", "gateway-safeq.mondomaine.local")
apikey = st.text_input("Clé API personnalisée (/APIKEY)", "")
install_path = st.text_input("Chemin d'installation (/D)", "C:\\Program Files\\Y Soft Corporation\\SAFEQ Cloud Client")

# Authentification
st.header("🔐 Authentification")
authtype = st.selectbox("Type d’authentification (/AUTHTYPE)", [
    "0 = Utilisateur de session",
    "1 = Utilisateur + Domaine",
    "2 = Connexion personnalisée",
    "3 = Nom d'utilisateur principal",
    "5 = OpenID Connect",
    "6 = SAFEQ Cloud OAuth2"
]).split(" ")[0]

secure_session = st.checkbox("Connexion de session sécurisée (/SECURESESSIONLOGIN)", value=True)

# Options booléennes
st.header("⚙️ Options booléennes")
agpl_ghostscript = st.checkbox("Accepter AGPL Ghostscript (/AGPLGHOSTSCRIPT)", value=True)
allow_config = st.checkbox("Autoriser la configuration (/ALLOWCONFIGURATION)", value=True)
allow_remember_login = st.checkbox("Autoriser mémorisation identifiants (/ALLOWREMEMBERLOGIN)", value=True)
remember_login = st.checkbox("Activer mémorisation de connexion (/REMEMBERLOGIN)", value=False)
certstore = st.checkbox("Utiliser certificat système (/CERTSTORE)", value=False)
desktop_icons = st.checkbox("Créer icônes bureau (/DESKTOPICONS)", value=False)
direct_offline = st.checkbox("Impression directe hors ligne (/DIRECTOFFLINEPRINT)", value=False)
duplex = st.checkbox("Impression recto-verso (/DUPLEX)", value=True)
delete_printers = st.checkbox("Supprimer imprimantes à la déconnexion (/DELETEPRINTERSONLOGOUT)", value=False)
keep_default_printer = st.checkbox("Conserver imprimante par défaut (/KEEPDEFAULTPRINTER)", value=True)
offline = st.checkbox("Installation hors ligne (/OFFLINE)", value=False)
server_check = st.checkbox("Vérifier le serveur (/SERVERCHECK)", value=True)
upgrade = st.checkbox("Mettre à jour si déjà installé (/UPGRADE)", value=False)
use_service_account = st.checkbox("Utiliser compte de service (/USESERVICEACCOUNT)", value=False)

# Autres paramètres
st.header("📦 Autres paramètres")
cert_subject = st.text_input("Sujet du certificat (/CERTSUBJECT)", "")
color = st.selectbox("Impression couleur (/COLOR)", ["true", "false"])
login_popup = st.selectbox("Type de popup de connexion (/LOGINPOPUPTYPE)", ["0", "1", "2"])
paper = st.selectbox("Format de papier (/PAPER)", ["A4", "A3", "A5", "Letter"])
pdfa = st.selectbox("Conversion PDF/A (/PDFA)", ["none", "2u"])
storage_type = st.selectbox("Type de stockage (/STORAGETYPE)", ["0", "1", "2"])
sync_period = st.number_input("Période de synchronisation (/SYNCPERIOD)", min_value=1, value=60)

# Génération de la commande
if st.button("🔧 Générer la ligne de commande"):
    cmd = "/S"
    cmd += f" /ACCOUNTDOMAIN={account_domain}"
    cmd += f" /GATEWAYADDRESS={gateway_address}"
    cmd += f" /AUTHTYPE={authtype}"
    cmd += f" /AGPLGHOSTSCRIPT={'true' if agpl_ghostscript else 'false'}"
    cmd += f" /ALLOWCONFIGURATION={'true' if allow_config else 'false'}"
    cmd += f" /ALLOWREMEMBERLOGIN={'true' if allow_remember_login else 'false'}"
    cmd += f" /REMEMBERLOGIN={'true' if remember_login else 'false'}"
    cmd += f" /CERTSTORE={'true' if certstore else 'false'}"
    if cert_subject:
        cmd += f" /CERTSUBJECT={cert_subject}"
    cmd += f" /COLOR={color}"
    cmd += f" /D="{install_path}""
    cmd += f" /DELETEPRINTERSONLOGOUT={'true' if delete_printers else 'false'}"
    cmd += f" /DESKTOPICONS={'true' if desktop_icons else 'false'}"
    cmd += f" /DIRECTOFFLINEPRINT={'true' if direct_offline else 'false'}"
    cmd += f" /DUPLEX={'true' if duplex else 'false'}"
    cmd += f" /KEEPDEFAULTPRINTER={'true' if keep_default_printer else 'false'}"
    cmd += f" /LOGINPOPUPTYPE={login_popup}"
    cmd += f" /OFFLINE={'true' if offline else 'false'}"
    cmd += f" /SERVERCHECK={'true' if server_check else 'false'}"
    cmd += f" /STORAGETYPE={storage_type}"
    cmd += f" /SYNCPERIOD={sync_period}"
    cmd += f" /SECURESESSIONLOGIN={'true' if secure_session else 'false'}"
    cmd += f" /UPGRADE={'true' if upgrade else 'false'}"
    cmd += f" /USESERVICEACCOUNT={'true' if use_service_account else 'false'}"
    if apikey:
        cmd += f" /APIKEY={apikey}"

    st.code(cmd, language="bash")
    st.success("Ligne de commande générée avec succès !")
