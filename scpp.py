import paramiko
from scp import SCPClient
import os
import shutil
from subprocess import *
from datetime import datetime

############check current date and time in the name of the new key created.
def scp(source_ssh_file, source_username, source_host, target_ssh_file, copy_filepath, target_username, target_host, target_directory_path, recursive, establish_trust = True, source_password = '', target_password = '', create_key_filename = datetime.now().strftime('%b-%d-%y-%X')+' new_scpp_key', create_key_bits = '1024'):
    filename = copy_filepath.split('/')[-1]
    def scp_to(scp_client, target_directory_path, recursive, files = filename):
        print(f'copying to {target_directory_path}...')
        scp_client.put(files = files, remote_path = format(target_directory_path.strip()), recursive = recursive)##scp.SCPException: scp: root/: Is a directory

    def scp_from(scp_client, source_filepath, recursive):
        print(f'copying from {source_filepath}...')
        scp_client.get(remote_path = source_filepath.strip(), recursive = recursive)

    def generate_key(client, create_key_filename, bits = '1024'):
        #paramiko.RSAKey.generate(bits = int(bits)).write_private_key_file(create_key_filename, create_key_password)
        #if create_key_password == None or create_key_password == '':#######check if the file already exists.
        stdin, stdout, stderr = client.exec_command(f'ssh-keygen -b {bits} -f ~/.ssh/{create_key_filename}')
        #else:
        #stdin, stdout, stderr = client.exec_command(f'ssh-keygen -b {bits} -f ~/.ssh/{create_key_filename} -N {create_key_password}')
        stdin2, stdout2, stderr2 = client.exec_command(f'chmod 0600 ~/.ssh/{create_key_filename}')
        #print('generate_key:\nstdout: ', stdout.read(),' stderr: ', stderr.read(),' stdout2: ',stdout2.read(),' stderr2: ', stderr2.read())
        #return create_key_filename

    def ssh(ssh_file, hostname, username, password = None):
        
        client = paramiko.SSHClient()
        key = paramiko.RSAKey.from_private_key_file(filename = ssh_file)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname = hostname, username = username, port = 22, pkey = key)
        except paramiko.AuthenticationException:
            try:
                print('ssh_file: ',ssh_file)
                os.chmod(os.path.expanduser('~/.ssh'), 0o700)
                os.chmod(ssh_file, 0o600)
                #run(['chmod','0644', ssh_file])#cannot find file
                print('run chmod')
                client.connect(hostname = hostname, username = username, port = 22, pkey = key)

            except paramiko.AuthenticationException:
                if password:
                    client.connect(hostname = hostname, username = username, port = 22, password = password)
                else:
                    print(f'Cannot access {username}@{hostname} with the given key. Please try using a different key or password.')
                    #return f'Cannot access {username}@{hostname} with the given key. Please try using a different key or password.'
                    exit()
        else:
            print(hostname,' connected.')
        return client

    ssh_source = ssh(ssh_file = source_ssh_file, hostname = source_host, username = source_username, password = source_password)
    
    ssh_target = ssh(ssh_file = target_ssh_file, hostname = target_host, username = target_username, password = target_password)
    
    
    source_scp_client = SCPClient(ssh_source.get_transport())
    scp_from(source_scp_client, copy_filepath, recursive)
    target_scp_client = SCPClient(ssh_target.get_transport())
    scp_to(target_scp_client, target_directory_path, recursive)
    if establish_trust:
        ####check if the trust is already established.
        generate_key(ssh_source, create_key_filename, create_key_bits)
        #run(['scp','-i',target_ssh_file, '-o', f"PubkeyAuthentication {source_ssh_file}", f'{source_username}@{source_host}:~/.ssh'])
        print('target_ssh_file: ',target_ssh_file.split("/"))
        scp_to(scp_client = source_scp_client, target_directory_path = '~/.ssh', recursive = recursive, files = target_ssh_file)
        chin, chout, cherr = ssh_source.exec_command(f'chmod 0600 ~/.ssh/{target_ssh_file.split("/")[-1]}')
        print('chout: ',chout.read(),' cherr: ',cherr.read())
        stdin1, stdout1, stderr1 = ssh_source.exec_command(f'ssh-copy-id -i ~/.ssh/{create_key_filename} -o "IdentityFile ~/.ssh/{target_ssh_file.split("/")[-1]}" {target_username}@{target_host}')
        print('stdout1: ',stdout1.read(),' stderr1: ',stderr1.read())
        stdin2, stdout2, stderr2 = ssh_source.exec_command(f'ssh {target_username}@{target_host}')
        print('stdout2: ', stdout2.read(),' stderr2: ', stderr2.read())
        print('Established trust.')
    if os.path.isdir(filename):
        shutil.rmtree(filename)
    if os.path.isfile(filename):
        os.remove(filename)
    print('Done!')
    ssh_source.close()
    ssh_target.close()
if __name__ == '__main__':
    scp(source_ssh_file = r'C:/Users/krish/Downloads/inst-trial-3.pem', source_username ='ubuntu', source_host = '13.233.68.105', source_password = '', target_ssh_file = r'C:/Users/krish/.ssh/id_rsa', copy_filepath = '/home/ubuntu/upload_test', target_username = 'root', target_host = '134.209.148.94', target_directory_path = '~/', recursive = True, target_password = '')
