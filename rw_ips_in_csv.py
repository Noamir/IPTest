import csv
import pandas as pd


def read_ips_from_csv(path_to_ips_csv):
    """the function gets a csv file with ip addresses and returns a list you can work with """

    #in1 = pd.read_csv(path_to_ips_csv)
    with open(path_to_ips_csv, newline='') as file:
        reader = csv.reader(file)
        ips_list = list(reader)
        ips_list = [row[0] for row in ips_list] # flatting the list, since it returns nested list by default for csv, but we use only 1 column
        return(ips_list)

def write_ip_status_to_csv(path_to_ip_status_csv, ip_address, status):
    """the function gets an ip address and write it to a csv file, 
    can get status for the ip - optional"""
    with open(path_to_ip_status_csv, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ip_address, status])
