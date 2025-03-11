from checksum import ChecksumMethods

candidate_path = "../../lab3/Q3files"
key_path = "../../lab3/Q3pk.pem"
scan = Checksum.sign_compare(candidate_path, key_path)
print(scan)
