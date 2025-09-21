# Dynamic Ansible Inventory with AWS EC2
In some cases, you may not have static IP addresses or hostnames. Dynamic inventory allows you to pull inventory data from cloud providers like AWS, GCP, or Azure dynamically.

This repository contains a Python script to **dynamically generate an Ansible inventory** from your AWS EC2 instances using **Boto3**.  
It automatically groups instances by their `env` tag and writes the inventory to a file, ready for Ansible usage.

---

## 📂 Features
- Fetches all EC2 instances in a specified AWS region.  
- Groups instances by the `env` tag (e.g., `dev`, `prod`).  
- Generates a static inventory file in **INI format** usable by Ansible.  
- Easy to integrate into your automation workflows.

---

## 🛠 Prerequisites
- Python 3.x  
- Boto3 library
- AWS credentials with `ec2:DescribeInstances` permission configured (via `~/.aws/credentials` or environment variables).  
- Ansible installed.

Install Boto3 if not already installed:

```bash
pip install boto3
````

---

## ⚡ How It Works

1. The script connects to AWS EC2 in the specified region (`ap-south-1` by default).
2. It retrieves all running instances and their private IP addresses.
3. Instances are grouped based on their `env` tag.
4. The generated inventory is written to `/etc/ansible/dynamic-inventory/inventory.ini`.

---

## 📝 Usage

Run the script:

```bash
python3 dynamic_inventory.py
```

The output will look like this in inventory.ini file

```
[all]
10.0.1.101
10.0.1.102

[dev]
10.0.1.101

[prod]
10.0.1.102
```


