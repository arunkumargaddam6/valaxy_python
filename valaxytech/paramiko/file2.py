#2. windows to linux
import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#username and password
ssh.connect(hostname='3.92.79.119',username='ec2-user', password='paramiko123',port=22)
stdin, stdout, stderr = ssh.exec_command('free -m')

print(stdout.read())