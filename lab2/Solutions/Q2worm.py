 from FileOperations import FileOperations
import subprocess

def find_vulnerable_machines():
    '''
    Output: 
    open_ssh.log or open_telnet.log
    - File of ips with open ports using either ssh or telnet.

    '''
    ip_bytes = "10.13.4
    run = subprocess.run(["bash", "./try_ports.sh", ip_bytes], capture_output=True)
    return run

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
    get_machines = find_vulnerable_machines()
    print(get_machines)