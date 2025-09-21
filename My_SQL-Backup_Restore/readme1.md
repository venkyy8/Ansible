# 📚 MySQL with Ansible Backup & Restore Guide

This document provides a basic reference for working with **MySQL databases** and automating backups to **AWS S3 using Ansible** and **cron jobs**.

---

## ⚡ MySQL Basics

after installing MySQL in the Server
### Restart MySQL Service

```bash
sudo systemctl restart mysql
```


### Login to MySQL
```bash
mysql -u root -p
````


---

## 🛠 Database Operations

### Create a Database

```sql
CREATE DATABASE database_name;
```

### Show Databases

```sql
SHOW DATABASES;
```
![A](images/show-databases)
### Use a Database

```sql
USE database_name;
```

---

## 🏗 Table Creation

### Create `users` Table

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Create `employees` Table

```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employeeName VARCHAR(50) NOT NULL,
    experience VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Create `students` Table

```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    studentName VARCHAR(50) NOT NULL,
    age VARCHAR(100)
);
```

---

## 🔍 Table Operations

### Show All Tables

```sql
SHOW TABLES;
```

### Describe Table Structure

```sql
DESCRIBE table_name;
```

Example:

```sql
DESCRIBE users;
```

### Drop Database

```sql
DROP DATABASE database_name;
```

### Drop Table

```sql
DROP TABLE table_name;
```

### After creating Databases we can take backup of this MySQL by running the ansible playbook

ansible-playbook taking_Backup.yml

#### we can cross check once after doing this task under S3 in aws console

![W](images/mysql-backups-s3)
---

## 💾 Restore MySQL Backup

### Step 1: Copy Backup File from AWS S3

```bash
aws s3 cp s3://mysql-backup-from-ansible-venky/mysql_backups/ansible_2025-09-21T09:19:17Z.sql /etc/ansible/playbooks/mysql
```

### Step 2: Create Database

Login to MySQL and create the required database:

```bash
mysql -u root -p
CREATE DATABASE your_database_name;
EXIT;
```

### Step 3: Import the Backup

```bash
mysql -u root -p ansible1 < /etc/ansible/playbooks/mysql/ansible_2025-09-21T09:19:17Z.sql
```

### Step 4: Verify the Import

Login again to MySQL and confirm tables/data are restored.

---

## 🤖 Automating Backups with Cron

### Backup Script

Create a backup script at `/usr/local/bin/backup_mysql_to_s3.sh`:

```bash
#!/bin/bash
# Script to run the MySQL backup playbook

# Run the Ansible playbook
ansible-playbook /etc/ansible/playbooks/mysql_backup.yml
```

Make the script executable:

```bash
sudo chmod +x /usr/local/bin/backup_mysql_to_s3.sh
```

### Schedule with Cron

Edit cron jobs:

```bash
crontab -e
```

Add the following line to run the backup **every day at 2:00 AM**:

```
0 2 * * * /usr/local/bin/backup_mysql_to_s3.sh >> /var/log/mysql_backup.log 2>&1
```

---

## ✅ Summary

* Manage MySQL databases and tables using SQL commands.
* Restore `.sql` backups from **AWS S3** into MySQL.
* Automate daily backups using **Ansible** and **cron jobs**.

---

