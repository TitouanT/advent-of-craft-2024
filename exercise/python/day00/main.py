import encryption_email
import tests.utils

def main():
    with open('./tests/resources/EncryptedEmail.txt') as f:
        content = f.read()

    key = tests.utils.convert_key('Advent Of Craft')
    iv = tests.utils.convert_iv('2024')
    enc = encryption_email.Encryption(key, iv)
    decrypted_content = enc.decrypt(content)
    print(decrypted_content)

if __name__ == '__main__':
    main()
