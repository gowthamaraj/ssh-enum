import paramiko
import argparse
import socket

parse = argparse.ArgumentParser(description='SSHEnum Arguments')
parse.add_argument('-t',action='store',dest='host',help='SSH server Address',required=True)
parse.add_argument('--u',dest='username',default='root', help='Username of the SSH server')
parse.add_argument('--p',dest='password',default='toor', help='Password of the SSH server')

args = vars(parse.parse_args())

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
    ssh_client = paramiko.SSHClient()
    paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    response = ssh_client.connect(args['host'],port = 22,username=args['username'],password=args['password'])
    print(response)
except Exception as E:
    print(bcolors.FAIL+f"Error Connecting : {E}"+bcolors.ENDC)