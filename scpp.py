import paramiko
from scp import SCPClient
import os
import shutil
from subprocess import *

def scp(source_ssh_file, source_username, source_host, target_ssh_file, copy_filepath, target_username, target_host, target_directory_path, recursive, establish_trust = True, target_password = ''):
    filename = copy_filepath.split('/')[-1]
    def scp_to(scp_client, target_directory_path, recursive):
        print('working on it...')
        scp_client.put(files = filename, remote_path = format(target_directory_path.strip()), recursive = recursive)##scp.SCPException: scp: root/: Is a directory

    def scp_from(scp_client, source_filepath, recursive):
        print('working on it...')
        scp_client.get(remote_path = source_filepath.strip(), recursive = recursive)

    def ssh(ssh_file, hostname, username):
        
        client = paramiko.SSHClient()
        #print('ssh_file: ',ssh_file)
        key = paramiko.RSAKey.from_private_key_file(filename = ssh_file)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname = hostname, username = username, port = 22, pkey = key)
        print(hostname,' connected.')
        return client

    ssh_source = ssh(ssh_file = source_ssh_file, hostname = source_host, username = source_username)
    source_scp_client = SCPClient(ssh_source.get_transport())
    scp_from(source_scp_client, copy_filepath, recursive)
    ssh_target = ssh(ssh_file = target_ssh_file, hostname = target_host, username = target_username)
    target_scp_client = SCPClient(ssh_target.get_transport())
    scp_to(target_scp_client, target_directory_path, recursive)
    #if establish_trust:
     #   copy_key(source_ssh_file, source_username, source_host, target_username, target_host, target_password)#######replace source path with the path in the other server
      #  print('Established trust.')
    if os.path.isdir(filename):
        shutil.rmtree(filename)
    if os.path.isfile(filename):
        os.remove(filename)
    print('Done!')

def copy_key(ssh_file, source_username, source_host, target_username, target_ip, target_password = ''):
    #call('ssh-copy-id -i {} {}@{}'.format(ssh_file, target_username, target_ip))
    #copy = Popen(['ssh-copy-id', '-i', ssh_file, f'{target_username}@{target_ip}'], shell = False, stdout = PIPE, stderr = PIPE)
    run(['ssh','-i',f'{ssh_file}',f'{source_username}@{source_host}'], text = True, input = 'yes')
    out = run('ssh-copy-id -i {} {}@{}'.format(ssh_file, target_username, target_ip).split(), text = True, capture_output = True, input = target_password)
    print('copy out: ', out)
    return stdout

def generate_key():
    #call(['ssh-keygen'])
    key_gen = Popen(['ssh-keygen'], shell = False, stdout = PIPE, stderr = PIPE)
    key = key_gen.stdout.readlines()
    if key == []:
        key = key_gen.stderr.readlines()
    print('generate stdout: ', stdout)
    return key
    #with SCPClient(ssh.get_transport()) as scp:
     #   scp.get(files = files)
    ssh_source.close()
    ssh_target.close()
if __name__ == '__main__':
    scp(source_ssh_file = r'C:/Users/krish/Downloads/inst-trial-2.pem', source_username ='ubuntu', source_host = '13.127.7.213', target_ssh_file = r'C:/Users/krish/Downloads/docker.pem', copy_filepath = '/home/ubuntu/laborum/laborum.py', target_username = 'root', target_host = '134.209.148.94', target_directory_path = '/root/', recursive = True)
