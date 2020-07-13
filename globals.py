import os

#TODO: move this to ini file
REAL_TIME_FEED_LINK = "http://datamine.mta.info/mta_esi.php?key={0}&feed_id={1}"

'''
MTA trains are grouped into these feed numbers.
Grouping details available on: http://datamine.mta.info/list-of-feeds
'''
LIST_OF_FEEDS = [1, 2, 11, 16, 21, 26, 31, 36, 51]

PROJECT_DIR = os.path.dirname(os.getcwd())

def parse_file_name(abs_file_path):
    """
    this auxiliary function would be used to set:
    .py filename and dict variable name generated by generate_dictionary()

    :return: name of the file (without file extension)
    """
    os_filepath_map = {
        'posix': '/',
        'nt': '\\'
    }

    try:
        path_delim = os_filepath_map.get(os.name)
    except KeyError:
        print("Operating System: " + os.name + " is not supported by this function.\n " +
                                               "Add proper key -> value into" + parse_file_name.__name__)

    list_split = abs_file_path.split(path_delim)
    return list_split[len(list_split)-1].split('.')[0]