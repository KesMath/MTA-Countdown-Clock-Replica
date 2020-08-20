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
    :param ciphertext: encrypted text
    :return: plaintext format needed to be executed by app logic
    """
    fernet = Fernet(read_file(relative_path=PROJECT_DIR, file_name=KEY_FILE, mode="rb")[0])
    return fernet.decrypt(ciphertext)


def generate_key():
    """
    :return: saves key to 'private_key.key' file
    """
    write_file(relative_path=PROJECT_DIR, file_name=KEY_FILE, mode="wb", content=Fernet.generate_key())


if __name__ == '__main__':
    ''''*********** |EXPOSE API KEY|*********** '''
    from configparser import ConfigParser
    parser = ConfigParser()
    parser.read(PROJECT_DIR + '/config/mta_config.ini')
    API_KEY = parser.get('keys', 'API_KEY')

    #convert to bytes
    cipher_text = str.encode(API_KEY)

    api_key = decrypt(cipher_text)
    print(api_key)

