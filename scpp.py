import paramiko
from scp import SCPClient

def scp_into(ssh_file, hostname):
    def ssh(ssh_file, hostname):
        client = paramiko.SSHClient()
        client.load_system_host_keys(filename = ssh_file)
        client.connect(hostname = hostname)#########check all parameters to be entered.
        return client

    ssh = ssh(ssh_file, hostname)
    scp_client = SCPClient(ssh.get_transport())


scp_into(ssh_file = r'C:\Users\krish\Downloads\docker.pem', hostname = r'root@134.209.148.94')