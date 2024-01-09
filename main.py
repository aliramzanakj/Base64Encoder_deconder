import base64

def encrypt_pass(password):
    encoded_pass = base64.b64encode(password.encode())
    return encoded_pass


def decrypt_pass(password):
    decoded  = base64.b64decode(password)
    decoded_data = decoded.decode()

    return decoded_data

password = input("ENTER YOUR PASSWORD:")
encrypt = encrypt_pass(password)

print("Your Encoded Password : {}".format(encrypt))


print("Your Decoded Password: {}".format(decrypt_pass(encrypt)))
