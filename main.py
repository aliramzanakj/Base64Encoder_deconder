import base64

def encrypt_pass(password):
    encoded_pass = base64.b64encode(password.encode())
    return encoded_pass


password = input("ENTER YOUR PASSWORD:")

print("Your Encoded Password : {}".format(encrypt_pass(password)))
