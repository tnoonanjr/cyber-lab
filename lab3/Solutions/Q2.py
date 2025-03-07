from checksum import Checksum

candidate_path = "../../lab3/Q2files"
target_path = "../../lab3/Q2hash.txt"
scan = Checksum.hash_compare(candidate_path, target_path)
print(scan)

# expectred answer: indulged.exe