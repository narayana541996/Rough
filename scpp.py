import paramiko
from scp import SCPClient

def scp_into(ssh_file, hostname, files = r'C:\Users\krish\Downloads\Affiliation_BYE_LAWS.doc'):
    def ssh(ssh_file, hostname):
        client = paramiko.SSHClient()
        key = paramiko.RSAKey.from_private_key_file(filename = ssh_file)
        #client.load_system_host_keys(filename = ssh_file)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname = hostname, username = 'ubuntu', port = 22, pkey = key)#########check all parameters to be entered.
        print('connected.')
        return client

    ssh = ssh(ssh_file, hostname)
    #scp_client = SCPClient(ssh.get_transport())
    with SCPClient(ssh.get_transport()) as scp:
        scp.put(files = files)


scp_into(ssh_file = r'C:\Users\krish\Downloads\inst-trial-2.pem', hostname = '65.0.19.49')