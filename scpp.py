import paramiko
from scp import SCPClient
from scp import SCPException
import os
import shutil
from subprocess import *
from datetime import datetime

response = ''
def scp_(source_ssh_file, source_username, source_host, target_ssh_file, copy_filepath, target_username, target_host, target_directory_path, recursive, establish_trust, source_password = '', target_password = '', target_key_file_on_source = '', create_key_bits = '1024'):
    filename = copy_filepath.split('/')[-1]
    global response
    def scp_to(scp_client, target_directory_path, recursive, files = filename):
        global response
        print(f'copying {files} to {target_directory_path}...')
        try:
            scp_client.put(files = files, remote_path = format(target_directory_path.strip()), recursive = recursive)##scp.SCPException: scp: root/: Is a directory
        except SCPException as e:
            if 'not a regular file' in str(e):
                response = f'-1-\n{files} doesn\'t look like some regular file(s), recursion must be turned on to continue.\nDo you wish to turn on recursion?'
            elif 'ambiguous target' in str(e):
                response = f'-2-Cannot find the target folder path. Please check the folder path entered and try again.'
            else:
                raise
        except FileNotFoundError:
            response = f'\n-3-Cannot find the file to be copied, please make sure that the path entered is correct, or if you\'re trying to copy a folder, turn on recursion.'
            print('scp_to filenotfound: ',response)
            return
        except PermissionError as e:
            response = f'\n-4-Couldn\'t access {str(e).split(":")[-1]}. Permission denied.'
            print('scp_to permissionerror: ',response)
            return

    def scp_from(scp_client, source_filepath, recursive):
        global response
        print(f'copying from {source_filepath}...')
        try:
            scp_client.get(remote_path = source_filepath.strip(), recursive = recursive)
        except SCPException as e:
            if 'not a regular file' in str(e):
                response = f'\n-5-{source_filepath} doesn\'t look like some regular file(s), recursion must be turned on to continue.\nDo wish to turn on recursion?'
            else:
                raise
        except FileNotFoundError:
            response = f'\n-6-Cannot find the file to be copied, please make sure that the path entered is correct, or if you\'re trying to copy a folder, turn on recursion.'
            print('scp_from filenotfounderror: ',response)
            return
        except PermissionError as e:
            response = f'\n-7-Couldn\'t access {str(e).split(":")[-1]}. Permission denied.'
            print('scp_from permissionerror: ',response)
            return

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
        except FileNotFoundError:
            response = '-8-Cannot find the key file, please check the path entered and try again.'
            return
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
        except paramiko.ssh_exception.NoValidConnectionsError:
            response = '-9-Cannot connect to the server, please check the IP addresses and try again.'
            return
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
                    response = f'-10-Cannot access {hostname} with the given username and key. Please check the username entered or try using a different key or password.'
                    #return f'Cannot access {username}@{hostname} with the given key. Please try using a different key or password.'
                    return
        except TimeoutError:
            response = f'-11-{hostname} isn\'t responding, please make sure that the server is up and running and that the entered values are correct and try again.'
            return
        else:
            print(hostname,' connected.')
        return client

    if (f'Cannot access {source_username}@{source_host} with the given key. Please try using a different key or password.' not in response) and (f'Cannot access {target_username}@{target_host} with the given key. Please try using a different key or password.' not in response):
        ssh_source = ssh(ssh_file = source_ssh_file, hostname = source_host, username = source_username, password = source_password)
        ssh_target = ssh(ssh_file = target_ssh_file, hostname = target_host, username = target_username, password = target_password)    
        if ssh_source:
            source_scp_client = SCPClient(ssh_source.get_transport())
        else:
            return response
        if ssh_target:
            scp_from(source_scp_client, copy_filepath, recursive)
        else:
            return response
        target_scp_client = SCPClient(ssh_target.get_transport())
        scp_to(target_scp_client, target_directory_path, recursive)
        if os.path.isdir(filename):
            shutil.rmtree(filename)
        if os.path.isfile(filename):
            os.remove(filename)
        if ('doesn\'t look like some regular file'not in response.lower()) and ('cannot find the file to be copied' not in response.lower()) and ('permission denied' not in response.lower()):
            response = f'-12-Copied {copy_filepath} from {source_username}@{source_host} to {target_username}@{target_host}.'
        else:
            return response
        print('establish_trust: ',establish_trust)
        if establish_trust:######if establish_trust is true, try to establish trust, else, skip establishing trust.
            stdin2, stdout2, stderr2 = ssh_source.exec_command(f'ssh {target_username}@{target_host}')
            print('stdout2: ',stdout2.read(),' stderr2: ',stderr2.read())
            if not stdout2.read():######Try to ssh into the target, if it gives no output,
                                ####proceed to establish trust, else, show that trust is already established. 
                #####If trust is not yet established, try connecting with an existing key, to the target. If it gives no output,
                ####create a new key-pair and copy the new public key to target's authorized_keys.
                #stdin1, stdout1, stderr1 = ssh_source.exec_command(f'ssh-copy-id -f -o "IdentityFile ~/.ssh/{target_ssh_file.split("/")[-1]}" -i ~/.ssh/{target_key_file_on_source} {target_username}@{target_host}')
                #print('old stdout1: ',stdout1.read(),' stderr1: ',stderr1.read())
                #if not stdout1.read() and ('error' not in str(stdout1.read()).lower()):
                create_key_filename = generate_key(target_username, target_host, ssh_source, create_key_bits)
                print('create_key_filename: ',create_key_filename)
                target_filename = ''
                if not target_key_file_on_source:
                    #scp_to(scp_client = source_scp_client, target_directory_path = '~/.ssh', recursive = recursive, files = target_ssh_file)
                    if target_ssh_file:
                        source_scp_client.put(files = target_ssh_file, remote_path = '~/.ssh', recursive = recursive)
                        target_filename = target_ssh_file.split("/")[-1]
                        chin, chout, cherr = ssh_source.exec_command(f'chmod 0600 ~/.ssh/{target_filename}')
                        print('chout: ',chout.read(),' cherr: ',cherr.read())
                        stdin1, stdout1, stderr1 = ssh_source.exec_command(f'ssh-copy-id -f -o "IdentityFile ~/.ssh/{target_filename}" -i ~/.ssh/{create_key_filename} {target_username}@{target_host}')
                    else:
                        response = f'{response}\nCouldn\'t establish trust between {source_username}@{source_host} and {target_username}@{target_host}.'
                        return response
                else:
                    stdin1, stdout1, stderr1 = ssh_source.exec_command(f'ssh-copy-id -f -o "IdentityFile {target_key_file_on_source}" -i ~/.ssh/{create_key_filename} {target_username}@{target_host}')
                print('new stdout1: ',stdout1.read(),' stderr1: ',stderr1.read())
                chin2, chout2, cherr2 = ssh_source.exec_command(f'chmod 0700 ~/.ssh')
                print('chout2: ',chout2.read(),' cherr2: ',cherr2.read())
                if target_filename:
                    rmin, rmout, rmerr = ssh_source.exec_command(f'rm ~/.ssh/{target_filename}')
                    print('rmout: ',rmout.read(),' rmerr: ',rmerr.read())
                stdin2, stdout2, stderr2 = ssh_source.exec_command(f'ssh {target_username}@{target_host}')
                print('stdout2: ', stdout2.read(),' stderr2: ', stderr2.read())
                if stdout2.read() and ('error' not in str(stdout2.read()).lower()):
                    response = f'-13-{response}\nEstablished Trust between {source_username}@{source_host} and {target_username}@{target_host}.'
                elif 'permission denied (publickey)' in str(stdout2.read()).lower() or ('permission denied (publickey)' in str(stderr2.read().lower())):
                    stdin2, stdout2, stderr2 = ssh_source.exec_command(f'ssh -i {create_key_filename} {target_username}@{target_host}')
                    if stdout2.read() and ('error' not in stdout2.read().lower()):
                        response = f'-14-{response}\nCouldn\'t establish trust between {source_username}@{source_host} and {target_username}@{target_host},\ncreated a key-pair to allow the source to access the target instead.'
                        return resonse
                    else:
                        response = f'-15-{response}\nCouldn\'t establish trust between {source_username}@{source_host} and {target_username}@{target_host}.'
                        return response
                else:
                    response = f'-16-{response}\nCouldn\'t establish trust between {source_username}@{source_host} and {target_username}@{target_host}.'
                    return response
            else:
                print('Trust already established...')
                reponse = f'17{response}\nTrust already established.'
        
        print('Done!')
        print('Response: ',response)
        ssh_source.close()
        ssh_target.close()
    return response
if __name__ == '__main__':
    scp_(source_ssh_file = r'C:/Users/krish/Downloads/inst-trial-3.pem', source_username ='ubuntu', source_host = '13.233.154.105', source_password = '', target_ssh_file = r'C:/Users/krish/Downloads/inst-trial-3.pem', copy_filepath = '/home/ubuntu/upload_test', target_username = 'ubuntu', target_host = '13.233.194.231', target_directory_path = '~/', recursive = True, target_password = '', target_key_file_on_source = '~/.ssh/id_dsa', establish_trust = True)
