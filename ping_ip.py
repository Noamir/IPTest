## Option 1

import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping_ip_address(ip_address):
    """
    Returns True if the ip address responds to a ping request.
    """
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c' # -n or -c determine the number of tries to reach the ip address

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', ip_address]

    return subprocess.call(command) == 0 # returns True if ip is reachable, False if unreachable

## Option 2

#import subprocess

#def ping_ip(ip_address):
 #   """
  #  Returns Online if the ip address responds to a ping request.
   # """

    #output = subprocess.Popen(["ping.exe",ip_address],stdout = 
    #subprocess.PIPE).communicate()[0]


    #if b'unreachable' in output:
     ##   return('Offline')
    #return('Online')







    
