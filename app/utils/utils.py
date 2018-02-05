import os
import re
import ipaddress
import json
import yaml

import requests


def process_ips(my_ip):
    ip_addrs = []
    with open('app/utils/ips.txt') as f:
        ips = f.readlines()

    for ip in ips:
        ip = ip.split(';')[0].strip()

        if "/" in ip:
            ip_addr = ipaddress.ip_network(ip)
            address = ip_addr.network_address.exploded
            if ip_addr.prefixlen == 16:
                pattern = re.compile("\d+\d{1,3}.\d{1,3}")
                ip_addr = re.search(pattern, address).group(0)
            elif ip_addr.prefixlen == 24:
                pattern = re.compile("\d{1,3}.\d{1,3}.\d{1,3}")
                ip_addr = re.search(pattern, address).group(0)
        else:
            ip_addr = ipaddress.ip_address(ip)

        ip_addrs.append(ip_addr)

    myip = ipaddress.ip_address(my_ip)
    if myip not in ip_addrs:
        ip_addrs.append(myip)

    return ip_addrs


def get_public_ip():
    resp = json.loads(requests.get(url='https://api.ipify.org/?format=json').content)
    return resp['ip']


current_dir = os.path.dirname(__file__)
rel_path = '../../dsas_credentials.yaml'
credentials_file_path = os.path.join(current_dir, rel_path)

def parse_dsas_crendentials():

    with open(credentials_file_path, 'r') as stream:
        try:
            yaml_file = yaml.load(stream)
            return yaml_file['dsas']['username'], yaml_file['dsas']['password'], yaml_file['dsas']['tenant']
        except yaml.YAMLError as exc:
            print(exc)


def parse_aws_crendentials():

    with open(credentials_file_path, 'r') as stream:
        try:
            yaml_file = yaml.load(stream)
            return yaml_file['aws']['access_key'], yaml_file['aws']['secret_key']
        except yaml.YAMLError as exc:
            print(exc)


def parse_elb_url():
    with open(credentials_file_path, 'r') as stream:
        try:
            yaml_file = yaml.load(stream)
            return yaml_file['elb']['url']
        except yaml.YAMLError as exc:
            print(exc)

