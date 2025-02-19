 from FileOperations import FileOperations
import subprocess

def find_vulnerable_machines(ip_bytes):
    '''
    Input:
    First three bytes of an ip; Assuming a /24 subnet where there are 254 available ips.

    Output: 
    None.
    Creates open_ssh.log and open_telnet.log;
    File of addresses with open ports using either ssh or telnet.

    '''
    # Runs try_ports.sh
    subprocess.run(["bash", "./try_ports.sh", ip_bytes], capture_output=True)

def find_vulnerable_accounts():
    '''
    Input: 
    ssh_accounts.log, telnet_accounts.log;
    

    Output:
    None.
    Edits open_telnet
    '''
    pass

def extract_and_infect():
    '''
    
    
    '''
    pass

if __name__ == '__main__':
    ip_bytes = "10.13.4
    find_vulnerable_machines(ip_bytes)