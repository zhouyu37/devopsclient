from M2Crypto import RSA,BIO
private_key_str = file('/root/.ssh/id_rsa', 'rb').read()

print(private_key_str)
