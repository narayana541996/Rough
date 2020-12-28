import paramiko
from scp import SCPClient

def scp_into(ssh_file, hostname, files = r'C:\Users\krish\Downloads\Affiliation_BYE_LAWS.doc'):
    def ssh(ssh_file, hostname):
        client = paramiko.SSHClient()
        client.load_system_host_keys(filename = ssh_file)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname = hostname, port = 22, key_filename = ssh_file )#########check all parameters to be entered.
        return client

    ssh = ssh(ssh_file, hostname)
    #scp_client = SCPClient(ssh.get_transport())
    with SCPClient(ssh.get_transport()) as scp:
        scp.put(files = files)


scp_into(ssh_file = r'C:\Users\krish\Downloads\docker.pem', hostname = r'root@134.209.148.94')