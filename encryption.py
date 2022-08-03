import hashlib, hmac, base64, binascii

def create_sha256_signature(key, message):
    byte_key = binascii.unhexlify(key)
    message = message.encode()
    return hmac.new(byte_key, message, hashlib.sha256).hexdigest().lower()

secretKey = "iexoocaquaenogoob7xoosaingeofoh9ighoh4eevoshaiNaN2gahHieYaix7iem"
# message = 'EURTestExtParam123998:roulettebalanceqauser_151238785931919_EUR'

# secretKey = "kam288vlh6y5145gkrd1hqi7i6vgi0m17mkvd10jlyui7fmamwna6hsitnjvcjlm"
message = 'OK'



hash = hashlib.new('sha256')
key = secretKey.encode('utf-8')
updt = hash.update(key)
secretHash = hash.hexdigest()
# print('secret hash', secretHash)

print(create_sha256_signature(secretHash, message))





