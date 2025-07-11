
import streamlit as st

st.set_page_config(page_title="Générateur de commande SAFEQ", layout="centered")
st.title("🖨️ Générateur de ligne de commande SAFEQ Cloud")

account_domain = st.text_input("Nom du domaine du compte (/ACCOUNTDOMAIN)", "mondomaine.local")
use_gateway = st.radio("Y a-t-il une passerelle Gateway ?", ["Oui", "Non"])
gateway_address = st.text_input("Adresse de la Gateway (/GATEWAYADDRESS)", "gateway-safeq.mondomaine.local") if use_gateway == "Oui" else account_domain
authtype = st.selectbox(
    "Type d’authentification (/AUTHTYPE)",
    options=[("0", "0 = Utilisateur de session (par défaut)"), ("1", "1 = Utilisateur + Domaine"),
             ("2", "2 = Connexion personnalisée"), ("3", "3 = Nom d'utilisateur principal"),
             ("5", "5 = OpenID Connect"), ("6", "6 = SAFEQ Cloud OAuth2")],
    format_func=lambda x: x[1]
)[0]

# Booléens
agpl_ghostscript = st.checkbox("Activer AGPL Ghostscript (/AGPLGHOSTSCRIPT)", value=True)
allow_config = st.checkbox("Autoriser configuration utilisateur (/ALLOWCONFIGURATION)", value=True)
remember_login_ui = st.checkbox("Autoriser mémorisation identifiants UI (/ALLOWREMEMBERLOGIN)", value=True)
remember_login_driver = st.checkbox("Activer /REMEMBERLOGIN", value=False)
upgrade = st.checkbox("Mettre à jour si déjà installé (/UPGRADE)", value=False)
offline = st.checkbox("Installation hors ligne (/OFFLINE)", value=False)
server_check = st.checkbox("Connexion serveur (/SERVERCHECK)", value=True)
cert_store = st.checkbox("Utiliser un certificat système (/CERTSTORE)", value=False)
cert_subject = st.text_input("Objet du certificat (/CERTSUBJECT)", "") if cert_store else ""
color = st.checkbox("Impression couleur (/COLOR)", value=False)
duplex = st.checkbox("Impression recto-verso (/DUPLEX)", value=True)
delete_on_logout = st.checkbox("Suppression des imprimantes à la déconnexion (/DELETEPRINTERSONLOGOUT)", value=False)
desktop_icons = st.checkbox("Créer des icônes bureau (/DESKTOPICONS)", value=False)
direct_offline = st.checkbox("Activer impression hors ligne (/DIRECTOFFLINEPRINT)", value=False)
keep_default = st.checkbox("Conserver imprimante par défaut (/KEEPDEFAULTPRINTER)", value=True)
secure_session = st.checkbox("Connexion de session sécurisée (/SECURESESSIONLOGIN)", value=True)
use_service_account = st.checkbox("Utiliser compte de service virtuel (/USESERVICEACCOUNT)", value=False)

# Listes déroulantes et champs libres
login_popup = st.selectbox("Type de popup de connexion (/LOGINPOPUPTYPE)", options=["0", "1", "2"], index=0)
storage_type = st.selectbox("Type de stockage (/STORAGETYPE)", options=["0", "1", "2"], index=0)
sync_period = st.number_input("Période de synchronisation (min) (/SYNCPERIOD)", min_value=1, value=60)
paper_format = st.selectbox("Format papier par défaut (/PAPER)", ["A4", "A3", "A5", "Letter"], index=0)
pdfa = st.selectbox("PDF/A (/PDFA)", ["none", "2u"], index=1)
install_path = st.text_input("Chemin d'installation (/D)", "C:\\Program Files\\Y Soft Corporation\\SAFEQ Cloud Client")
apikey = st.text_input("Clé API personnalisée (/APIKEY)", "")

if st.button("🔧 Générer la ligne de commande"):
    cmd = f"/S /ACCOUNTDOMAIN={account_domain} /GATEWAYADDRESS={gateway_address} /AUTHTYPE={authtype}"
    cmd += f" /AGPLGHOSTSCRIPT={'true' if agpl_ghostscript else 'false'}"
    cmd += f" /ALLOWCONFIGURATION={'true' if allow_config else 'false'}"
    cmd += f" /ALLOWREMEMBERLOGIN={'true' if remember_login_ui else 'false'}"
    cmd += f" /REMEMBERLOGIN={'true' if remember_login_driver else 'false'}"
    cmd += f" /UPGRADE={'true' if upgrade else 'false'}"
    cmd += f" /OFFLINE={'true' if offline else 'false'}"
    cmd += f" /SERVERCHECK={'true' if server_check else 'false'}"
    cmd += f" /CERTSTORE={'true' if cert_store else 'false'}"
    if cert_subject:
        cmd += f" /CERTSUBJECT={cert_subject}"
    cmd += f" /COLOR={'true' if color else 'false'}"
    cmd += f" /DUPLEX={'true' if duplex else 'false'}"
    cmd += f" /DELETEPRINTERSONLOGOUT={'true' if delete_on_logout else 'false'}"
    cmd += f" /DESKTOPICONS={'true' if desktop_icons else 'false'}"
    cmd += f" /DIRECTOFFLINEPRINT={'true' if direct_offline else 'false'}"
    cmd += f" /KEEPDEFAULTPRINTER={'true' if keep_default else 'false'}"
    cmd += f" /SECURESESSIONLOGIN={'true' if secure_session else 'false'}"
    cmd += f" /USESERVICEACCOUNT={'true' if use_service_account else 'false'}"
    cmd += f" /LOGINPOPUPTYPE={login_popup}"
    cmd += f" /STORAGETYPE={storage_type}"
    cmd += f" /SYNCPERIOD={sync_period}"
    cmd += f" /PAPER={paper_format}"
    cmd += f" /PDFA={pdfa}"
    cmd += f" /D="{install_path}""
    if apikey:
        cmd += f" /APIKEY={apikey}"
    st.code(cmd, language="bash")
    st.success("✅ Ligne de commande générée avec succès !")
