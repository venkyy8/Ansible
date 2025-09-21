import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2', region_name='ap-south-1')

# Define the file path
INVENTORY_FILE_PATH = '/etc/ansible/dynamic-inventory/inventory.ini'

def get_instances():
    response = ec2.describe_instances()
    instances_by_env = {'all': []}
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            private_ip = instance.get('PrivateIpAddress')
            if private_ip:
                instances_by_env['all'].append(private_ip)
                
                # Get the 'env' tag value
                env_tag = None
                for tag in instance.get('Tags', []):
                    if tag['Key'] == 'env':
                        env_tag = tag['Value']
                        break
                if env_tag:
                    if env_tag not in instances_by_env:
                        instances_by_env[env_tag] = []
                    instances_by_env[env_tag].append(private_ip)
    return instances_by_env

def generate_inventory():
    instances_by_env = get_instances()
    
    inventory = "[all]\n"
    for ip in instances_by_env['all']:
        inventory += f"{ip}\n"
    
    for env, ips in instances_by_env.items():
        if env != 'all':  
            inventory += f"\n[{env}]\n"
            for ip in ips:
                inventory += f"{ip}\n"
    
    return inventory

def write_inventory_to_file():
    inventory = generate_inventory()
    with open(INVENTORY_FILE_PATH, 'w') as file:
        file.write(inventory)
    print(f"Inventory written to {INVENTORY_FILE_PATH}")

def main():
    write_inventory_to_file()

if __name__ == "__main__":
    main()
