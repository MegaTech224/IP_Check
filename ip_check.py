import socket
import urllib.request
import logging

def get_public_ip():
    public_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    host_name = socket.gethostname()
    # log_file_name = 'Public_ip_' + host_name + '.log'
    # log_location = '/Data/Stack/Python/' + log_file_name
    logging.basicConfig(
        filename='/mnt/stack/Python/IP_Check/Public_ip_' + host_name + '.log',
        filemode='w',
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

    logging.info('Hostname: ' + host_name)
    logging.info('Public IP: ' + public_ip)
    return public_ip

get_public_ip()
