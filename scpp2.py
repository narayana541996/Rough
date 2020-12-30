from subprocess import *
def scp_from_into(source_username, source_ip, source_filepath, file_path, target_username, target_ip, target_directory, source_key_file_path = None, target_key_file_path = None):#source_ip, target_ip, file_path, ssh_key
    #print(call(r'scp -i C:\Users\krish\Downloads\docker.pem  C:\Users\krish\Downloads\Affiliation_BYE_LAWS.doc root@134.209.148.94:/root/'.split(' ')))
    #copy target_key_file to the source
    if target_key_file_path and not source_key_file_path:#If only target_key_file_path is given, same key is used for source_key_file_path
        source_key_file_path = target_key_file_path
    elif source_key_file_path and not target_key_file_path:#If only source_key_file_path is given, same key is used for target_key_file_path
        target_key_file_path = source_key_file_path
    #print(r'scp -i {} {} {}@{}:{}'.format(source_key_file_path,target_key_file_path, source_username, source_ip, source_filepath))
    out = getoutput(r'scp -i {} {} {}@{}:{}'.format(source_key_file_path,target_key_file_path, source_username, source_ip, source_filepath).split(' '))
    print('out: ',out)
    #enter the source server
    print(r'ssh -i {} {}@{}'.format(source_key_file_path, source_username, source_ip))
    print(call(r'ssh -i {} {}@{}'.format(source_key_file_path, source_username, source_ip).split(' ')))
    #get target_key_file from the target_key_file_path
    target_key_file = target_key_file_path.split('/')[-1]
    print('target_key_file: ', target_key_file)
    #set the target_key_file permissions to read and write
    print(call(r'chmod 600 {}'.format(target_key_file).split(' ')))
    print(call(r'scp -i {} {} {}@{}:{}'.format(target_key_file, file_path, target_username, target_ip, target_directory).split(' ')))
    print(call(r'rm {}'.format(target_key_file).split(' ')))
    print(call('exit'.split()))
#.format(ssh_key,file_path, target_ip)
scp_from_into( source_key_file_path = r'C:/Users/krish/Downloads/inst-trial-2.pem', target_key_file_path = r'C:/Users/krish/Downloads/docker.pem', source_username = 'ubuntu', source_ip = '65.0.19.49', source_filepath = 'home/ubuntu/', file_path = 'home/ubuntu/laborum/laborum.py', target_username = 'root', target_ip = '134.209.148.94', target_directory = 'root/')
