from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import sys

def decrypt_shared_key(private_key_content, encrypted_shared_key_path):
    private_key = RSA.import_key(private_key_content)
    cipher_rsa = PKCS1_OAEP.new(private_key)

    with open(encrypted_shared_key_path, "rb") as encrypted_shared_key_file:
        encrypted_shared_key = encrypted_shared_key_file.read()
    

    shared_key = cipher_rsa.decrypt(encrypted_shared_key)

    with open("DecryptedSharedKey", "wb") as shared_key_file:
        shared_key_file.write(shared_key)
    return shared_key

def main():
    if len(sys.argv) != 2:
        print("Usage: python AD6.py [EncryptedSharedKey path]")
        return 1
    
    pvt_k = b'-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEAstraGV3tuedd+jDtpvJIeSm3YkTFv4nocSlZuKAcTTPT4rUY\nInPPYW2TomatNr/D++JsEnNhaQgHcg+QOVYqrzI8WWquOnDmP7I4IHxCnUdDMD0/\nKD7X7hqJ5xvcnyf7R7rhINgY4ZkiF5kzSsfTPCC/snv99OdmfXyakBclorvRKZWz\n3d1wQLX9rqON1yNkTvnZF4A6c6iIFF2chLZx9MUu6E73dLlJm9YXp0OoS82atBf2\nIoO/y9/p0j2QnwKKJvu4GmfHHsuLSnFcEgyFKX9XQfKFgoQ+RfcsbC+v8i6rco4s\noK2nJKrMC1YusYZjfZtEwM2Iw5dYCCreUtKaFQIDAQABAoIBAAoW4HDH5K41CA8i\nDXX6eu4i1U581K7uZ6dijsYkehQ81ToXvynKYKt9U/O4WRMalEK0TiZoTdlv84OS\nry8c1kGV0uO0aemwDr0PH61tdRCMQZUKD3MEwIeVBax83OA5kCpGt4ZzykuHqO2t\n3b/dL+RXcJjv966GEzkG+20fcScR2tXN/RdyELGcrL6TCCnIWLR/SsveDdgClc3a\n9NYknIPMaTBzhXGuImJg9i+DXPuquPTDpqz0dbSFLpU51TIAVeMK1KwjkBaoUpzN\n94szobmIYC7ZGpmD6CZi+ingdTXAdDPizR4cr0lyj/iZHJ0DJ5n1AVo0SWN0CWR/\nJcjv+IECgYEAtwSsN5098Sq3OhkurcaHYfOtW/PcGEJAOTCzZv3UcMx9W7MXh80x\nip/oVhAIoP7XSlnyCfIy0OlsKE7AHpMcnNxHYv4BmIwvemuL4Jl/+LV0+Pwr17Ex\nH+/TIRlzcMTSfSyG9EgyFY2iNzRhBQOX55XPEXZHH5DmlBiTUECZ9vUCgYEA+i0q\nGTOYE9jlMBLxz9/TTW3tDGWStChgOCV2621wU87SG9sUREr6eyhKgYGEz0dxY5GS\nVJGYseF9lOQybHL3uxASu83KFlJSTQk8A82jroK2q5qmqBjAM/1twJ4ZuNOkMvVt\nJiPes02k1tHCLwCyIPqFaQLP1tTVaCYes83S4qECgYEAnviiFtSwnzD5Yq/JCgzu\nP7kIFl0mCrRRUNvqmUVWKHyXTvWrNLyZkc4AY/EdbaqumtiyEs2cMjbvSbvNyUED\nk4ULRQNZo4XxH6cXIwpyTDhh2HxCIOK6xwDsJU4UJhnws+Xfe4TSbEJQax9GPrK2\nWeSYrpRMhzC3+F+4ZfcXRZkCgYAc2fSO73pMX6kewDCO7pspxNGfql8e08E0+G0c\nfYSExcdJWxydO6Bjb6QYB13Poceb2f/sLNZVPVIER8Tg6OlU82eVrQfvRxMiuzvm\nnGKSD5UNeUpa/G++Dy4HFrSUsiOvlMo/qcdXGk82Tv57+TKRxxJ3p9FcTzNFTZAg\n4E2/wQKBgQCi+MkEDNlsTVIRKd0xfaVYuyhDRGr+v0SzvtFJPDiguP9cuhRhC+MU\n1oMGNp0R0YRlaWPZvBwyJ7LGnVyitskxMOQpDz1nR/d0yvnAuIde7eXija5MuO1H\ndyrOUGwla2/XJAewxxlIeBS+FeqfbbIgnKP20nqIizQEh41euTynjw==\n-----END RSA PRIVATE KEY-----'

    try:
        sol = decrypt_shared_key(pvt_k, sys.argv[1])
        print(sol)
        return 0
    except:
        print(f"An error occured decrypting {sys.argv[1]}")

main()