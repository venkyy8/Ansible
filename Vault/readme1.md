

Here’s the file:


# Ansible Vault - Guide

Ansible Vault is a feature used to securely store and manage sensitive data like passwords, API keys, and private certificates within your playbooks.

---

## 1. Creating an Encrypted Vault File

To create a new encrypted vault file:

```bash
ansible-vault create secrets.yml
````

* When prompted, enter a password (e.g., Secure\_Password).
* Add your secret data in the file, such as:

```yaml
db_password: "SuperSecretDB123"
api_key: "ABCDEF123456"
```

Save and exit. Your `secrets.yml` file is now encrypted.

---

## 2. Editing an Encrypted Vault File

To edit the encrypted vault file:

```bash
ansible-vault edit secrets.yml
```

You will be prompted for the password you set (e.g., `Secure_Password`). After editing, save and exit.

---

## 3. Encrypting an Existing Plaintext File

To encrypt an existing plaintext file:

```bash
ansible-vault encrypt secrets.yml
```

---

## 4. Decrypting a Vault File

To decrypt and view the contents of the vault file:

```bash
ansible-vault decrypt secrets.yml
```

You will be prompted for the password (`Secure_Password`).

---

## 5. Using Vault in Playbooks

Reference your encrypted vault in a playbook:

```yaml
---
- hosts: localhost
  vars_files:
    - secrets.yml

  tasks:
    - name: Show the database password
      debug:
        msg: "Database password is {{ db_password }}"
```

---

## 6. Running a Playbook with Vault

To run a playbook that uses the vault:

```bash
ansible-playbook playbook.yml --ask-vault-pass
```

You will be prompted for the vault password.

Alternatively, use a password file:

```bash
ansible-playbook playbook.yml --vault-password-file .vault_pass.txt
```
we can see the output

![A](images/vault)

---

## 7. Using Vault Password File

To avoid typing the vault password each time, create a file `.vault_pass.txt` containing the password:

```bash
echo "Secure_Password" > .vault_pass.txt
```

---

## Vault Command Summary

| Command                                         | Description                                  |
| ----------------------------------------------- | -------------------------------------------- |
| `ansible-vault create <file>`                   | Create an encrypted vault file               |
| `ansible-vault edit <file>`                     | Edit an existing encrypted vault file        |
| `ansible-vault encrypt <file>`                  | Encrypt an existing plaintext file           |
| `ansible-vault decrypt <file>`                  | Decrypt an encrypted vault file              |
| `ansible-playbook --ask-vault-pass`             | Run a playbook and prompt for vault password |
| `ansible-playbook --vault-password-file <file>` | Run playbook using vault password file       |

---

## Troubleshooting

If you encounter issues:

1. Ensure the password in `.vault_pass.txt` is correct.
2. Check for extra spaces or newlines in the `.vault_pass.txt`.
3. Verify that the vault file is properly encrypted using:

```bash
ansible-vault view <file>
```

---

## Notes

* Vault Password Management: Keep your `.vault_pass.txt` file secure.
* Automation: You can automate decryption using CI/CD pipelines, but make sure to handle the vault password securely.

---
