import paramiko
from scp import SCPClient
import os
import shutil
from subprocess import *
from datetime import datetime

response = ''
def scp(source_ssh_file, source_username, source_host, target_ssh_file, copy_filepath, target_username, target_host, target_directory_path, recursive, establish_trust = True, source_password = '', target_password = '', connect_target_key_file = '', create_key_bits = '1024'):
    filename = copy_filepath.split('/')[-1]
    global response
    def scp_to(scp_client, target_directory_path, recursive, files = filename):
        print(f'copying {files} to {target_directory_path}...')
        scp_client.put(files = files, remote_path = format(target_directory_path.strip()), recursive = recursive)##scp.SCPException: scp: root/: Is a directory

    def scp_from(scp_client, source_filepath, recursive):
        print(f'copying from {source_filepath}...')
        scp_client.get(remote_path = source_filepath.strip(), recursive = recursive)

    def generate_key(target_username, target_host, client, bits = '1024'):
        create_key_filename = f'scpp_key_{datetime.now().strftime("%d-%b-%y-%X")}'
        stdin, stdout, stderr = client.exec_command(f'ssh-keygen -b {bits} -f ~/.ssh/{create_key_filename}')
        stdin2, stdout2, stderr2 = client.exec_command(f'chmod 0600 ~/.ssh/{create_key_filename}')
        #print('generate_key:\nstdout: ', stdout.read(),' stderr: ', stderr.read(),' stdout2: ',stdout2.read(),' stderr2: ', stderr2.read())
        return create_key_filename

    def ssh(ssh_file, hostname, username, password = None):
        global response
        client = paramiko.SSHClient()
        try:
            key = paramiko.RSAKey.from_private_key_file(filename = ssh_file)
        except paramiko.SSHException as e:
            print('sshexception: ',e)
            if 'encountered EC key' in str(e):
                key = paramiko.ECDSAKey.from_private_key_file(filename = ssh_file)
            elif 'encountered DSA key' in str(e):
                key = paramiko.DSSKey.from_private_key_file(filename = ssh_file)
            elif 'unpack requires a buffer of 4 bytes' in str(e):
                key = paramiko.Ed25519Key.from_private_key_file(filename = ssh_file)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname = hostname, username = username, port = 22, pkey = key)
        except paramiko.AuthenticationException:
            try:
                print('ssh_file: ',ssh_file)
                os.chmod(os.path.expanduser('~/.ssh'), 0o700)
                os.chmod(ssh_file, 0o600)
                #run(['chmod','0644', ssh_file])#cannot find file
                client.connect(hostname = hostname, username = username, port = 22, pkey = key)

            except paramiko.AuthenticationException:
                if password:
                    client.connect(hostname = hostname, username = username, port = 22, password = password)
                else:
                    response = f'Cannot access {username}@{hostname} with the given key. Please try using a different key or password.'
                    #return f'Cannot access {username}@{hostname} with the given key. Please try using a different key or password.'
                    exit()
        else:
            print(hostname,' connected.')
        return client

    if response != f'Cannot access {source_username}@{source_host} with the given key. Please try using a different key or password.' and response != f'Cannot access {target_username}@{target_host} with the given key. Please try using a different key or password.':
        ssh_source = ssh(ssh_file = source_ssh_file, hostname = source_host, username = source_username, password = source_password)
        ssh_target = ssh(ssh_file = target_ssh_file, hostname = target_host, username = target_username, password = target_password)    
        source_scp_client = SCPClient(ssh_source.get_transport())
        scp_from(source_scp_client, copy_filepath, recursive)
        target_scp_client = SCPClient(ssh_target.get_transport())
        scp_to(target_scp_client, target_directory_path, recursive)
        response = f'Copied {copy_filepath} from {source_username}@{source_host} to {target_username}@{target_host}.'
        if establish_trust:######if establish_trust is true, try to establish trust, else, skip establishing trust.
            stdin2, stdout2, stderr2 = ssh_source.exec_command(f'ssh {target_username}@{target_host}')
            print('stdout2: ',stdout2.read(),' stderr2: ',stderr2.read())
            if not stdout2.read():######Try to ssh into the target, if it gives no output,
                                ####proceed to establish trust, else, show that trust is already established. 
                #####If trust is not yet established, try connecting with an existing key, to the target. If it gives no output,
                ####create a new key-pair and copy the new public key to target's authorized_keys.
                stdin1, stdout1, stderr1 = ssh_source.exec_command(f'ssh-copy-id -f -o "IdentityFile ~/.ssh/{target_ssh_file.split("/")[-1]}" -i ~/.ssh/{connect_target_key_file} {target_username}@{target_host}')
                print('old stdout1: ',stdout1.read(),' stderr1: ',stderr1.read())
                if not stdout1.read() and ('error' not in str(stdout1.read()).lower()):
                    create_key_filename = generate_key(target_username, target_host, ssh_source, create_key_bits)
                    print('create_key_filename: ',create_key_filename)
                    scp_to(scp_client = source_scp_client, target_directory_path = '~/.ssh', recursive = recursive, files = target_ssh_file)
                    target_filename = target_ssh_file.split("/")[-1]
                    chin, chout, cherr = ssh_source.exec_command(f'chmod 0600 ~/.ssh/{target_filename}')
                    print('chout: ',chout.read(),' cherr: ',cherr.read())
                    stdin1, stdout1, stderr1 = ssh_source.exec_command(f'ssh-copy-id -f -o "IdentityFile ~/.ssh/{target_filename}" -i ~/.ssh/{create_key_filename} {target_username}@{target_host}')
                    print('new stdout1: ',stdout1.read(),' stderr1: ',stderr1.read())
                    chin2, chout2, cherr2 = ssh_source.exec_command(f'chmod 0700 ~/.ssh')
                    print('chout2: ',chout2.read(),' cherr2: ',cherr2.read())
                    #rmin, rmout, rmerr = ssh_source.exec_command(f'rm ~/.ssh/{target_filename}')
                    #print('rmout: ',rmout.read(),' rmerr: ',rmerr.read())
                    stdin2, stdout2, stderr2 = ssh_source.exec_command(f'ssh {target_username}@{target_host}')
                    print('stdout2: ', stdout2.read(),' stderr2: ', stderr2.read())
                print('Establishing trust...')
                if stdout2.read() and 'error' not in stdout2.read().lower():
                    response = response + f'\nEstablished Trust between {source_username}@{source_host} and {target_username}@{target_host}.'
            else:
                print('Trust already established...')
                reponse = response + '\nTrust already established.'
        if os.path.isdir(filename):
            shutil.rmtree(filename)
        if os.path.isfile(filename):
            os.remove(filename)
        print('Done!')
        ssh_source.close()
        ssh_target.close()
    return response
if __name__ == '__main__':
    scp(source_ssh_file = r'C:/Users/krish/Downloads/inst-trial-3.pem', source_username ='ubuntu', source_host = '15.206.151.159', source_password = '', target_ssh_file = r'C:/Users/krish/Downloads/inst-trial-3.pem', copy_filepath = '/home/ubuntu/upload_test', target_username = 'ubuntu', target_host = '15.207.115.212', target_directory_path = '~/', recursive = False, target_password = '', connect_target_key_file = '~/.ssh/id_dsa')
