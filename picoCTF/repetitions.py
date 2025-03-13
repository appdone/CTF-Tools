from base64 import b64decode

with open("enc_flag", "r") as file:
    enc_flag = file.read()

while "picoCTF" not in str(enc_flag):
    enc_flag = str(enc_flag).replace('\n', '')
    enc_flag = b64decode(enc_flag).decode()

print(enc_flag)
