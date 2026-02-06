# 🚀 Ansible – Configuration Management & Automation

Ansible is an open-source configuration management, application deployment, and IT automation tool that enables DevOps engineers to automate infrastructure using simple YAML-based playbooks.

This repository contains hands-on Ansible examples, best practices, and real-world automation use cases.

# 📌 Why Ansible?

Agentless (uses SSH / WinRM)

Simple YAML syntax

Idempotent (safe to run multiple times)

Push-based automation

Huge built-in module ecosystem

Easy to learn & scale

# 🧩 Ansible Architecture
Control Node
   |
   |--- SSH / WinRM
   |
Managed Nodes


Control Node: Machine where Ansible is installed

Managed Nodes: Target servers

Inventory: Hosts & groups

Playbooks: Automation logic

Modules: Units of work

Plugins: Extend Ansible functionality

```
📁 Repository Structure
Ansible/
├── inventory/
│   ├── hosts
│   └── prod
├── playbooks/
│   ├── install_nginx.yml
│   ├── users.yml
│   └── services.yml
├── roles/
│   └── nginx/
│       ├── tasks/
│       ├── handlers/
│       ├── templates/
│       ├── vars/
│       └── defaults/
├── group_vars/
├── host_vars/
├── ansible.cfg
└── README.md
```

📦 Inventory File
[web]
web1 ansible_host=192.168.1.10
web2 ansible_host=192.168.1.11

[db]
db1 ansible_host=192.168.1.20

▶️ Sample Playbook
---
- name: Install and start nginx
  hosts: web
  become: yes
  tasks:
    - name: Install nginx
      package:
        name: nginx
        state: present

    - name: Start nginx service
      service:
        name: nginx
        state: started
        enabled: yes

🔐 Privilege Escalation (become)
become: yes
become_user: root


Used when:

Installing packages

Managing services

Editing system files

📦 Built-in Modules (Why They’re Better)
🔹 package module
package:
  name: httpd
  state: present


✔ Works across distros (yum / apt)
✔ Idempotent
✔ Cleaner than shell scripts

🔹 service module
service:
  name: nginx
  state: restarted


✔ OS-aware
✔ Handles enable/start/restart safely

🔁 Variables in Ansible
vars
vars:
  app_port: 8080

vars_files
vars_files:
  - vars/common.yml

vars_prompt
vars_prompt:
  - name: username
    prompt: "Enter username"
    private: no

# 🧠 Facts & Conditionals
when: ansible_os_family == "RedHat"

- debug:
    msg: "{{ ansible_hostname }}"

🔄 Handlers
handlers:
  - name: restart nginx
    service:
      name: nginx
      state: restarted


# Triggered using:

notify: restart nginx

🎭 Roles (Best Practice)
ansible-galaxy init nginx


# Benefits:

Reusability

Clean structure

Easy scaling

Team collaboration

🧪 Ansible Commands
ansible all -m ping
ansible-playbook playbooks/install_nginx.yml
ansible-playbook site.yml --check
ansible-playbook site.yml --syntax-check

# 🔐 Ansible Vault
ansible-vault encrypt secrets.yml
ansible-vault decrypt secrets.yml


Use for:

Passwords

API keys

Tokens

# 🚫 Shell Script vs Ansible
Shell Script	Ansible
Not idempotent	Idempotent
OS dependent	Cross-platform
Hard to scale	Highly scalable
Manual error handling	Built-in checks

# 💡 Real-World Use Cases

Server provisioning

Application deployment

User & permission management

Patch management

CI/CD integration

Cloud & hybrid automation

# 🛠️ Tools Used

Ansible

YAML

SSH

Git & GitHub

Linux

# 🎯 Best Practices

Use roles

Prefer built-in modules

Avoid shell unless required

Use handlers

Store secrets in Vault

Keep inventories environment-specific

# 📚 Learning Resources

Official Docs: https://docs.ansible.com

Ansible Galaxy

Hands-on labs & demos

# 🤝 Contributions

Contributions, issues, and feature requests are welcome!
Feel free to fork and raise a PR 🚀

# 👨‍💻 Author

Velanati Naveen Kumar
DevOps Engineer
Skills: CI/CD | AWS | Kubernetes | Terraform | GitOps | Automation
📞 +91 9848545101