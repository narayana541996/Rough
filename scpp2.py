from subprocess import call
def scp_from_into():#source_ip, target_ip, file_path, ssh_key
    print(call(r'scp -i C:\Users\krish\Downloads\docker.pem  C:\Users\krish\Downloads\Affiliation_BYE_LAWS.doc root@134.209.148.94:/root/'.split(' ')))
#.format(ssh_key,file_path, target_ip)
scp_from_into()