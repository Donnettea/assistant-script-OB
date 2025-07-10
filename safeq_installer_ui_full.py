import streamlit as st

st.set_page_config(page_title="Générateur de commande SAFEQ", layout="wide")
st.title("🧰 Générateur de ligne de commande SAFEQ Cloud")

st.markdown("### Paramètres principaux")
account_domain = st.text_input("Nom du domaine du compte (/ACCOUNTDOMAIN)", "mondomaine.local")
gateway_address = st.text_input("Adresse de la Gateway (/GATEWAYADDRESS)", "gateway-safeq.mondomaine.local")
apikey = st.text_input("Clé API personnalisée (/APIKEY)", "")
authtype = st.selectbox("Type d’authentification (/AUTHTYPE)", ["0", "1", "2", "3", "5", "6"])
install_path = st.text_input("Chemin d'installation (/D)", "C:\\Program Files\\Y Soft Corporation\\SAFEQ Cloud Client")

st.markdown("### Options booléennes")
agpl_ghostscript = st.checkbox("Activer AGPL Ghostscript (/AGPLGHOSTSCRIPT)", value=False)
allow_config = st.checkbox("Autoriser la configuration (/ALLOWCONFIGURATION)", value=True)
allow_remember_login = st.checkbox("Autoriser mémorisation identifiants (/ALLOWREMEMBERLOGIN)", value=True)
remember_login = st.checkbox("Activer mémorisation de connexion (/REMEMBERLOGIN)", value=False)
certstore = st.checkbox("Utiliser certificat système (/CERTSTORE)", value=False)
color = st.checkbox("Impression couleur par défaut (/COLOR)", value=False)
delete_printers = st.checkbox("Supprimer imprimantes à la déconnexion (/DELETEPRINTERSONLOGOUT)", value=False)
desktop_icons = st.checkbox("Créer icônes bureau (/DESKTOPICONS)", value=False)
direct_offline = st.checkbox("Activer impression directe hors ligne (/DIRECTOFFLINEPRINT)", value=False)
duplex = st.checkbox("Impression recto-verso par défaut (/DUPLEX)", value=True)
keep_default_printer = st.checkbox("Conserver imprimante par défaut (/KEEPDEFAULTPRINTER)", value=True)
offline = st.checkbox("Installation hors ligne (/OFFLINE)", value=False)
secure_session = st.checkbox("Connexion de session sécurisée (/SECURESESSIONLOGIN)", value=True)
server_check = st.checkbox("Vérifier serveur SAFEQ (/SERVERCHECK)", value=True)
upgrade = st.checkbox("Mettre à jour installation existante (/UPGRADE)", value=False)
use_service_account = st.checkbox("Utiliser compte de service (/USESERVICEACCOUNT)", value=False)

st.markdown("### Autres paramètres")
certsubject = st.text_input("Sujet du certificat (/CERTSUBJECT)", "")
login_popup_type = st.selectbox("Type de popup de connexion (/LOGINPOPUPTYPE)", ["0", "1", "2"])
paper = st.selectbox("Format papier par défaut (/PAPER)", ["A4", "A3", "A5", "Letter"])
pdfa = st.selectbox("Conversion PDF/A (/PDFA)", ["none", "2u"])
storage_type = st.selectbox("Type de stockage (/STORAGETYPE)", ["0", "1", "2"])
sync_period = st.number_input("Période de synchronisation (/SYNCPERIOD)", min_value=1, value=60)

if st.button("🔧 Générer la ligne de commande"):
    cmd = "/S"
    cmd += f" /ACCOUNTDOMAIN={account_domain}"
    cmd += f" /GATEWAYADDRESS={gateway_address}"
    cmd += f" /AUTHTYPE={authtype}"
    cmd += f" /D="{install_path}""
    cmd += f" /AGPLGHOSTSCRIPT={'true' if agpl_ghostscript else 'false'}"
    cmd += f" /ALLOWCONFIGURATION={'true' if allow_config else 'false'}"
    cmd += f" /ALLOWREMEMBERLOGIN={'true' if allow_remember_login else 'false'}"
    cmd += f" /REMEMBERLOGIN={'true' if remember_login else 'false'}"
    cmd += f" /CERTSTORE={'true' if certstore else 'false'}"
    if certsubject:
        cmd += f" /CERTSUBJECT={certsubject}"
    cmd += f" /COLOR={'true' if color else 'false'}"
    cmd += f" /DELETEPRINTERSONLOGOUT={'true' if delete_printers else 'false'}"
    cmd += f" /DESKTOPICONS={'true' if desktop_icons else 'false'}"
    cmd += f" /DIRECTOFFLINEPRINT={'true' if direct_offline else 'false'}"
    cmd += f" /DUPLEX={'true' if duplex else 'false'}"
    cmd += f" /KEEPDEFAULTPRINTER={'true' if keep_default_printer else 'false'}"
    cmd += f" /LOGINPOPUPTYPE={login_popup_type}"
    cmd += f" /OFFLINE={'true' if offline else 'false'}"
    cmd += f" /SECURESESSIONLOGIN={'true' if secure_session else 'false'}"
    cmd += f" /SERVERCHECK={'true' if server_check else 'false'}"
    cmd += f" /STORAGETYPE={storage_type}"
    cmd += f" /SYNCPERIOD={sync_period}"
    cmd += f" /UPGRADE={'true' if upgrade else 'false'}"
    cmd += f" /USESERVICEACCOUNT={'true' if use_service_account else 'false'}"
    if apikey:
        cmd += f" /APIKEY={apikey}"
    cmd += f" /PAPER={paper}"
    cmd += f" /PDFA={pdfa}"

    st.markdown("### ✅ Ligne de commande générée :")
    st.code(cmd, language="bash")
