from cryptography.fernet import Fernet
from util.os_func import PROJECT_DIR, read_file, write_file

KEY_FILE = "private_key.key"

def encrypt(plaintext):
    """
    :param plaintext: sensitive text needed to be concealed
    :return: cipher text that can be exposed publically
    """
    fernet = Fernet(read_file(relative_path=PROJECT_DIR, file_name=KEY_FILE, mode="rb")[0])
    return fernet.encrypt(plaintext)



def decrypt(ciphertext):
    """
    :param ciphertext: encrypted text as string type
    :return: plaintext format needed to be executed by app logic
    """
    fernet = Fernet(read_file(relative_path=PROJECT_DIR, file_name=KEY_FILE, mode="rb")[0])
    return fernet.decrypt(str.encode(ciphertext))


def generate_keyfile():
    """
    :return: saves key to 'private_key.key' file
    """
    write_file(relative_path=PROJECT_DIR, file_name=KEY_FILE, mode="wb", content=Fernet.generate_key())


if __name__ == '__main__':
    #TODO: write these procedures into functions

    ''''*********** |EXPOSE API KEY|*********** '''
    #reading encrypted key from config file
    from configparser import ConfigParser
    parser = ConfigParser()
    parser.read(PROJECT_DIR + '/config/mta_config.ini')
    API_KEY = parser.get('keys', 'API_KEY')

    #decrypt hidden text - function will fail without 'private_key.key' file!
    api_key = decrypt(API_KEY)
    print(api_key)

#==============================================================================

    # ''''*********** |GENERATE NEW PRIVATE KEY & CIPHER TEXT PAIRING|*********** '''
    # PLAINTEXT_KEY = b'<API KEY HERE>'
    # generate_keyfile()
    # cipher = encrypt(PLAINTEXT_KEY)
    # print(cipher)
    # #manually update mta_config.ini with new cipher text
    # assert(PLAINTEXT_KEY == decrypt(cipher.decode("utf-8")))



