import paramiko
from scp import SCPClient
import os

def scp(source_ssh_file, source_username, source_host, target_ssh_file, copy_filepath, target_username, target_host, target_directory_path):
    filename = copy_filepath.split('/')[-1]
    def scp_to(scp_client, target_directory_path):
        scp_client.put(files = filename, remote_path = format(target_directory_path.strip()))##scp.SCPException: scp: root/: Is a directory

    def scp_from(scp_client, source_filepath):
        scp_client.get(source_filepath.strip())

    def ssh(ssh_file, hostname, username):

        client = paramiko.SSHClient()
        print('ssh_file: ',ssh_file)
        key = paramiko.RSAKey.from_private_key_file(filename = ssh_file)
        #client.load_system_host_keys(filename = ssh_file)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname = hostname, username = username, port = 22, pkey = key)
        print('connected.')
        #print(client.exec_command('scp -i {} {} {}@{}:{}'.format(target_key.split('/')[-1], copy_filepath, target_username, target_host, target_directory_path)))
        #print(client.exec_command('rm {}'.format(target_key)))
        #print('ls: ',client.exec_command('ls'))
        return client

    ssh_source = ssh(ssh_file = source_ssh_file, hostname = source_host, username = source_username)
    source_scp_client = SCPClient(ssh_source.get_transport())
    scp_from(source_scp_client, copy_filepath)
    ssh_target = ssh(ssh_file = target_ssh_file, hostname = target_host, username = target_username)
    target_scp_client = SCPClient(ssh_target.get_transport())
    scp_to(target_scp_client, target_directory_path)
    os.remove(filename)
    

    #with SCPClient(ssh.get_transport()) as scp:
     #   scp.get(files = files)
    ssh_source.close()
    ssh_target.close()
if __name__ == '__main__':
    scp(source_ssh_file = r'C:/Users/krish/Downloads/inst-trial-2.pem', source_username ='ubuntu', source_host = '52.66.31.152', target_ssh_file = r'C:/Users/krish/Downloads/docker.pem', copy_filepath = '/home/ubuntu/laborum/laborum.py', target_username = 'root', target_host = '134.209.148.94', target_directory_path = '/root/')
