# Create VM's 

* ansible-playbook -i localhost,   -e '{"instances":["mongodb","catalogue","redis","user","cart","mysql","shipping","rabbitmq","payment","frontend"]}'  -e action=create roboshop.yaml


* ansible-playbook -e component=mongodb robosho.yaml