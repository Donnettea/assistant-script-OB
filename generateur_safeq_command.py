
def ask_yes_no(question):
    while True:
        response = input(f"{question} (o/n): ").strip().lower()
        if response in ["o", "oui", "y"]:
            return "true"
        elif response in ["n", "non"]:
            return "false"
        print("Réponse invalide. Tapez 'o' pour oui ou 'n' pour non.")

def ask_choice(question, choices):
    print(f"\n{question}")
    for key, value in choices.items():
        print(f"  {key} = {value}")
    while True:
        choice = input("Entrez le code correspondant: ").strip()
        if choice in choices:
            return choice
        print("Choix invalide, réessayez.")

def main():
    cmd = ["/S"]

    # Domaine
    account_domain = input("Quel est le /ACCOUNTDOMAIN (nom de domaine) ? ").strip()
    cmd.append(f"/ACCOUNTDOMAIN={account_domain}")

    # Gateway
    gateway = input("Y a-t-il une passerelle (laisser vide pour utiliser le domaine) ? ").strip()
    if not gateway:
        gateway = account_domain
    cmd.append(f"/GATEWAYADDRESS={gateway}")

    # AuthType
    authtype_choices = {
        "0": "Utilisateur de session (par défaut)",
        "1": "Utilisateur de session + domaine",
        "2": "Connexion personnalisée",
        "3": "Nom d'utilisateur principal",
        "5": "OpenID Connect",
        "6": "SAFEQ Cloud OAuth2"
    }
    authtype = ask_choice("/AUTHTYPE = Type d'authentification de l’utilisateur :", authtype_choices)
    cmd.append(f"/AUTHTYPE={authtype}")

    # StorageType
    storage_choices = {
        "0": "Cloud",
        "1": "Stockage local",
        "2": "Hybride"
    }
    storage = ask_choice("/STORAGETYPE = Type de stockage :", storage_choices)
    cmd.append(f"/STORAGETYPE={storage}")

    # Options booléennes
    if ask_yes_no("Souhaitez-vous faire une mise à jour (upgrade) ?") == "true":
        cmd.append("/UPGRADE=true")
    else:
        cmd.append("/UPGRADE=false")

    cmd.append(f"/RESETCONFIG={ask_yes_no('Réinitialiser la configuration existante ?')}")
    cmd.append(f"/ALLOWCONFIGURATION={ask_yes_no('Autoriser l’utilisateur à modifier la configuration ?')}")
    cmd.append(f"/AGPLGHOSTSCRIPT={ask_yes_no('Accepter la licence AGPL Ghostscript ?')}")
    cmd.append(f"/ALLOWREMEMBERLOGIN={ask_yes_no('Autoriser la mémorisation des identifiants ?')}")

    # Clé API personnalisée
    if ask_yes_no("Souhaitez-vous spécifier une clé API personnalisée ?") == "true":
        apikey = input("Entrez la clé API : ").strip()
        if apikey:
            cmd.append(f"/APIKEY={apikey}")

    print("\n✅ Ligne de commande générée :\n")
    print(" ".join(cmd))

if __name__ == "__main__":
    main()
