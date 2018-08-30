import json
import requests
import getpass
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings( InsecureRequestWarning )

s = requests.Session()
s.verify = False


# Function to get the vCenter server session
def get_vc_session(vcip, username, password):
    s.post( vcip + '/rest/com/vmware/cis/session', auth=(username, password) )
    return s

# Function to get all the VMs from vCenter inventory
def get_vms(vcip):
    vms = s.get( vcip + '/rest/vcenter/vm' )
    return vms

vcip = input('Enter the Pcc FQDN. Eg. https:/pcc-x-x-x-x.ovh.us:')#"147.135.13.17"  # vCenter server ip address/FQDN
USERNAME = input('Enter username:')
PASSWORD = getpass.getpass('Password:')

# Get vCenter server session and can be used as needed. pass vcenter username & password
vcsession = get_vc_session( vcip, USERNAME, PASSWORD )

# Get all the VMs from inventory
vms = get_vms( vcip )

# Parsing the JSON response we got from above function call (it has all the Vms present in inventory
vm_response = json.loads( vms.text )
json_data = vm_response["value"]

print("VM name : Power Status, vCPU, Memory")
print("============================")
for vm in json_data:
    print(vm.get( "name" ) + " : " + vm.get( "power_state" )+", " +str(vm.get("cpu_count"))+" vcpu, "+ str(vm.get("memory_size_MiB"))+" MB Memory")

