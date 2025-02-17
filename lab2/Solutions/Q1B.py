import sys
from Parasite import IdentifyTarget, Parasite

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 Q1B.py [target_file]\n")
        return 1
    
    virus = Parasite(target_file = sys.argv[1],
                     payload_file = "Q1B_payload.py",
                     output_path = "Q1B.out")
    
    id = IdentifyTarget(file=sys.argv[1])

    if id.run() == 0:
        return 1
    virus.inject()
    
    return 0
    
main()