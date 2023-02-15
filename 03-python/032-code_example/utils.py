from logging import  basicConfig, getLogger
from os.path import basename

def create_logger():
    basicConfig(
        format="[%(asctime)s - %(filename)s:l.%(lineno)d](%(levelname)s): %(message)s",
    )
    logger = getLogger(basename(__file__))
    logger.setLevel("INFO")
    logger.info("Test Logger ")


def clean_str_all(self):
    return self.replace(' ', '').replace("\r", '').replace('\n', '')

def clean_str_special_char(self):
    return self.replace("\r", '').replace('\n', '')

def drop_duplicates_dict(tab):
    return [dict(t) for t in {tuple(d.items()) for d in tab}]

def get_separator(strc: str):
        """
        trouve le séparateur principal d'une string
        :param strc: string à analyser
        :return: le séparateur
        """
        count_sep = [str(strc).count('\n'), str(strc).count(','), str(strc).count(';'), str(strc).count('\r')]
        index_sep = count_sep.index(max(count_sep))
        separator = None

        if index_sep == 0:
            separator = '\n'
        elif index_sep == 1:
            separator = ','
        elif index_sep == 2:
            separator = ';'
        elif index_sep == 3:
            separator = '\r'

        return separator
