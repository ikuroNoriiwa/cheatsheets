from hvault import GetCredential
from sys import exit

def get_open_data_token(logger):
    """
    ### Description:
    Get Credential From Vault
    Get all OpenData Credentials from vault (EC002I000770)

    """
    logger.info("get_open_data_token")

    crt = r"" # TODO cert file
    key = r"" # TODO key file
    namespace = "" # TODO Namespace
    secret_path = "" # TODO secret path
    secret_vault = "" # TODO security policy name
    credentials = GetCredential(crt, key, namespace, secret_path, secret_vault, logger)

    token = credentials.get_vault_token()
    if token is None:
        logger.debug("Impossible de récupérer le token HVAULT, vérifier les certificats")
        exit("Problème connexion hvault")

    return credentials.get_my_credentials(token)

