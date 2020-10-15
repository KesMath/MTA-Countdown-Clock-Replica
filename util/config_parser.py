from configparser import ConfigParser
from util.os_func import PROJECT_DIR

parser = ConfigParser()
parser.read(PROJECT_DIR + '/config/mta_config.ini')

def get_config_value(section, option):
    """
    :param section: section within *.ini file indicated by [X]
    :param option: unique variable names listed under section
    :return: value associated with key
    """
    if parser.has_section(section=section):
        if parser.has_option(section=section, option=option):
            return parser.get(section=section, option=option)
        raise KeyError(option + " does not exist within [" + section + "]")
    raise KeyError(section + " does not exist within [" + str(parser.sections()) + "]")