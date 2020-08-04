"""
metaprogramming script to transform certain comma-separated values in
txt_files/*.txt into simple key value pairs
"""
from util.os_func import PROJECT_DIR, parse_file_name
from util.custom_exceptions import FileExtensionException

SAVE_TO_DIRECTORY = '/config/'


def generate_dictionary(abs_file_path, key_index, value_index):
    """
    :return: generates a new .py file containing a dictionary variable
             whose key->values pairing is created from parametrized values
            which corresponds to list indices after string split occurs
    """
    if key_index < 0 or value_index < 0:
        raise ValueError("Both index values must be greater than or equal to 0")

    if abs_file_path[-4:] != ".txt":
        raise FileExtensionException(abs_file_path +\
                                     " is not a txt file!")

    else:
        try:
            with open(abs_file_path, "r") as f:
                data = f.readlines()[1:] #removing header row

        except OSError as e:
            print(e)

        dict_name = parse_file_name(abs_file_path)
        dict_str = """\"\"\"This python file was generated from """\
                   + generate_dictionary.__name__ + "()\"\"\"\n\n"\
                   + dict_name.upper() + " = { \n"

        for index, row in enumerate(data):
            csv_delim_list = row.split(',')
            row_len = len(csv_delim_list)

            #rows within txt file has a probability of being jagged hence it's necessary to check per iteration
            if key_index < row_len and value_index < row_len:
                dict_str += "   '" + csv_delim_list[key_index] + "': \"" + csv_delim_list[value_index] + "\",\n"
            else:
                raise IndexError("Row " + str(index) + " of size " + str(row_len) +
                                 " cannot be accessed with one of these index values: ("
                                                + str(key_index) + "," + str(value_index) + ")")

        dict_str += "}"
        with open(PROJECT_DIR + SAVE_TO_DIRECTORY + dict_name + "_dict.py", "w") as f1:
            f1.write(dict_str)

def main():
    generate_dictionary(abs_file_path=PROJECT_DIR + '/txt_files/stops.txt',
                        key_index=0, value_index=2)


if __name__ == '__main__':
    main()