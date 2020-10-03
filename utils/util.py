import hashlib


def create_dict(**kwargs):
    return kwargs

def urlencode(encode_letter):
    return str(encode_letter.encode('unicode-escape').decode('utf-8')).replace('\\', '%')

def urldecode(decode_letter):
    decode_letter = decode_letter.replace('%', '\\')
    return decode_letter.encode().decode('unicode-escape')

def password_encode(password_letter):
    encode_password = password_letter.encode('utf-8')
    hash_password = hashlib.sha256(encode_password).hexdigest()
    return str(hash_password)

if __name__ == '__main__':
    print(urlencode('テスト'))
    print(urldecode('%u30c6%u30b9%u30c8'))