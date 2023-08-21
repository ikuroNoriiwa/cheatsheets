import logging

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"


logging.basicConfig(level=logging.INFO,format="["+BLUE+"%(levelname)s"+RESET+"] - ["+GREEN+"%(name)s"+RESET+"] - %(message)s")

def fn_test(): 
    logger = logging.getLogger(__name__)
    logger.info("INFO Message")
    logger.debug("DEBUG Message")