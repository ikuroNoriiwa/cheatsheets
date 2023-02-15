from requests import get, post
from json import loads
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

# TODO : certificat SSL pour valider requetes https ?
disable_warnings(InsecureRequestWarning)


def get_vault_token(self):
    """
    ### Description:
    Get vault token
    Retrieve connexion token for vault

    #### [DEBUG]
    `ValueError - Can't get hvault token`
    """
    self.logger.info("get_vault_token")
    req = "/auth/cert/login"
    headers = {"X-Vault-Namespace": self.vault_namespace}
    cert = (self.path_to_crt, self.path_to_key)
    data = {"name": self.secret_vault}
    response = post(self.vault_base_url + self.vault_api_version + req, headers=headers, cert=cert, data=data,
                     verify=False)

    token = None
    try:
        if response.status_code == 200:
            js = loads(response.content.decode("utf-8"))
            token = js["auth"]["client_token"]
    except ValueError:
        self.logger.debug("ValueError - Can't get hvault token")
        pass
    finally:
        return token

def get_my_credentials(self, token):
    """
    ### Description:
    Get My specific credential
    Retrieve credential for the specified app

    ### Args:
    `token`: token for hvault, returned by get_vault_token

    #### [DEBUG]
    `ValueError - Can't get hvault credentials`
    """
    self.logger.info("get_my_credentials, args : {}".format(token))
    req = "/secret/data/{}".format(self.secret_path)
    headers = {"X-Vault-Namespace": self.vault_namespace,
               "X-Vault-Token" : token}
    cert = (self.path_to_crt, self.path_to_key)

    response = get(self.vault_base_url + self.vault_api_version + req, headers=headers, cert=cert, verify=False)
    credential = None

    try:
        if response.status_code == 200:
            js = loads(response.content.decode("utf-8"))
            credential = js["data"]["data"]

    except ValueError:
        self.logger.debug("ValueError - Can't get hvault credentials")
        pass
    finally:
        return credential