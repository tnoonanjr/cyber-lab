from FileOperations import FileOperations
import subprocess

def find_vulnerable_machines():
    '''
    Output: 
    open_ssh.log or open_telnet.log
    - File of ips with open ports using either ssh or telnet.

    '''
    ip_bytes = "10.13.4"

    for ip_last_byte in range(256):
        subprocess.run(["./try_ports.sh", f"{ip_bytes}.{ip_last_byte}"])

def find_vulnerable_users():
    '''
    Output: 
    ssh_accounts.log
    telnet_accounts.log
    - File in ip,user,passwd format of cracked users.

    '''
    pass

def extract_and_infect():
    '''
    
    
    '''
    pass

if __name__ == '__main__':
    find_vulnerable_machines()