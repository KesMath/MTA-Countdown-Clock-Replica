import os


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


def read_file(absolute_path):
    """
    :param absolute_path: full path including file name
    :return: entire file is returned as a list of strings
    """
    if os.path.isfile(absolute_path) is True:
        try:
            with open(absolute_path, "r") as f:
                data = f.readlines()
                return data

        except OSError as e:
            print(e)

    else:
        raise OSError(absolute_path + " is an invalid file!")


def write_file(relative_path, name, mode, content):
    """
    :param relative_path:
    :param name:
    :param mode:
    :param content:
    :return:
    """
    #TODO: prevent special characters from being passed through name parameter
    #TODO: need to limit characters being passed in to mode param

    if os.path.isdir(relative_path) is True:
        with open(os.path.join(relative_path + name), mode) as f:
            try:
                f.write(content)

            except OSError as e:
                print(e)
    else:
        raise OSError(relative_path + " is an invalid directory!")