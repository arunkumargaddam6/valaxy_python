# how to transfer a file from local server to remote server or vice versa
from subprocess import BELOW_NORMAL_PRIORITY_CLASS
import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='3.92.79.119',username='ec2-user', password='paramiko123',port=22)

sftp_client = ssh.open_sftp()

#download file from remote to local



#sftp_client.get('source path', 'dest path')

#if you dont want use path do the below

# sftp_client.chdir("/home/ec2-user")
# print(sftp_client.getcwd())

# sftp_client.get('source file','dest path')



# transfer file from local to remote
sftp_client.put("source path", "dest path")

sftp_client.close()
ssh.close()