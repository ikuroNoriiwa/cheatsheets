from logging import basicConfig, getLogger
from os.path import basename

class GetCredential:
    """
    ## Description
    Class to get hvault token

    ## Atributes:
    `path_to_crt`: path to certificate file

    `path_to_key`: path to key file

    `namespace`: Hvault namespace for the required resources

    `secret_path`: part of the url, in this case "microseg/opendata"

    `secret_vault`: secret vault name (policy option), in this case "getlabel"

    `vault_base_url`: hvault base url

    `vault_api_version`: hvault Api version

    `logger`: Logger object from logging.getLogger

    ## Methods
    *get_vault_token():*
                    Get token for hvault

    *get_my_credentials(token):*
                    Get credentials 
    """
    def __init__(self, path_to_crt, path_to_key, namespace, secret_path, secret_vault, logger=None):
        """
        ### Description 
        Constructs all the necessary attributes for GetCredential Object
        
        ### Parameters:
        `path_to_crt`: path to the crt file
        `path_to_key`: path to the private key
        `namespace`: Namespace of the cluster, in this case "UPM_FRB/RESFR/EC002I000770"
        `secret_path`: part of the url, in this case "microseg/opendata"
        `secret_vault`: secret vault name, in this case "getlabel"
        """
        if logger is None:
            basicConfig(
                format="[%(asctime)s - %(filename)s:l.%(lineno)d](%(levelname)s): %(message)s",
            )
            logger = getLogger(basename(__file__))
            logger.setLevel("INFO")
        logger.info("__init__ vault")
        self.path_to_crt = path_to_crt
        self.path_to_key = path_to_key

        self.vault_namespace = namespace
        self.secret_path = secret_path
        self.secret_vault = secret_vault

        self.vault_base_url = "HVAULT URL" #TODO setup URL
        self.vault_api_version = "/v1" #TODO setup Version

        self.logger = logger

    from .vault import (
        get_vault_token,
        get_my_credentials,
    )
