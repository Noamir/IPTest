import csv
from rw_ips_in_csv import read_ips_from_csv, write_ip_status_to_csv
from ping_ip import ping_ip_address



#ips_list = ['172.217.16.12', '10.10.10.10', '1.1.1.1', '100.25.13.12', '216.58.208.36']

ips_list = read_ips_from_csv('C:\\Users\\neta5\\Desktop\\Python\\IPTest\\ips_list.csv')




for ip_address in ips_list:
    status = ping_ip_address(ip_address)
    write_ip_status_to_csv('C:\\Users\\neta5\\Desktop\\Python\\IPTest\\ips_ping_status.csv', ip_address, status)
    
    











