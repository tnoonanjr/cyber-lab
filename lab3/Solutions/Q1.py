from checksum import bruteforce_find_checksum_match

candidate_path = "../../lab3/Q1files"
scan = bruteforce_find_checksum_match(candidate_path)
print(scan)

# expected answer: suslik.exe
