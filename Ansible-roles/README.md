# Create VM's 

/home/ec2-user/Ansible/ansible-project-dev

* ansible-playbook -i localhost, -e '{"instances":["mongodb","catalogue","redis","user","cart","mysql","shipping","rabbitmq","payment","frontend"]}' roboshop.yaml


* ansible-playbook -e component=mongodb roboshop.yaml