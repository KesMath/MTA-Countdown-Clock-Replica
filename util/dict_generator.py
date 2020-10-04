"""
metaprogramming script to transform certain comma-separated values in
txt_files/*.txt into simple key value pairs located in config/*_dict.py
"""
from util.os_func import os, PROJECT_DIR, read_file, write_file
from util.custom_exceptions import FileExtensionException

SAVE_TO_DIRECTORY = 'config'


def generate_dictionary(relative_path, filename, key_index, value_index):
    """
    :return: generates a new .py file containing a dictionary variable
             whose key->values pairing is created from parametrized values
            which corresponds to list indices after string split occurs
    """
    if key_index < 0 or value_index < 0:
        raise ValueError("Both index values must be greater than or equal to 0")

    if filename[-4:] != ".txt":
        raise FileExtensionException(filename +\
                                     " is not a txt file!")

    else:

        data = read_file(relative_path=relative_path, file_name=filename, mode='r')[1:]

        dict_name = filename.split('.')[0]
        dict_str = """\"\"\"This python file was generated from """\
                   + generate_dictionary.__name__ + "()\"\"\"\n\n"\
                   + dict_name.upper() + " = { \n"

        directional_indicator_exists = True if dict_name == 'stops' and key_index == 0 else False

        for index, row in enumerate(data):
            csv_delim_list = row.split(',')
            row_len = len(csv_delim_list)

            #rows within txt file has a probability of being jagged hence it's necessary to check per iteration
            if key_index < row_len and value_index < row_len:
                """ NOTE: this patch ignores all keys without 'N' or 'S' indicator
                    because they do not return any results when api is called
                """
                if directional_indicator_exists:
                    direction_indicator = csv_delim_list[key_index][-1]
                    if direction_indicator == 'N' or direction_indicator == 'S':
                        dict_str += "   '" + csv_delim_list[key_index] + "': \"" + csv_delim_list[value_index] + "\",\n"
                else:
                    dict_str += "   '" + csv_delim_list[key_index] + "': \"" + csv_delim_list[value_index] + "\",\n"
            else:
                raise IndexError("Row " + str(index) + " of size " + str(row_len) +
                                 " cannot be accessed with one of these index values: ("
                                                + str(key_index) + "," + str(value_index) + ")")

        dict_str += "}"
        write_file(relative_path=os.path.join(PROJECT_DIR, SAVE_TO_DIRECTORY),
                   file_name=dict_name + "_dict.py", mode='w', content=dict_str)

def main():
    generate_dictionary(relative_path=os.path.join(PROJECT_DIR, 'txt_files'), filename='stops.txt',
                        key_index=0, value_index=2)


if __name__ == '__main__':
    main()