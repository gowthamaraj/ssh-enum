import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.connect('host',username='',password='')
ssh_client.set_missing_host_key_policy(paramiko. AutoAddPolicy())