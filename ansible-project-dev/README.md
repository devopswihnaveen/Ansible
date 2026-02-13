# Create VM's 

* ansible-playbook -i localhost,   -e '{"instances":["mongodb","catalogue","redis","user","cart","mysql","shipping","rabbitmq","payment","frontend"]}'  -e action=create roboshop.yaml

# MONGO DB Setup
* ansible-playbook -i inventory.ini mongodb.yaml

# catalogue Setup
* ansible-playbook -i inventory.ini catalogue.yaml

# REDIS Setup 
* ansible-playbook -i inventory.ini redis.yaml

# User Setup
* ansible-playbook -i inventory.ini user.yaml

# cart Setup
* ansible-playbook -i inventory.ini cart.yaml

# MySql DB Setup
* ansible-playbook -i inventory.ini mysql.yaml

# shipping Setup
* ansible-playbook -i inventory.ini shipping.yaml

# Rabbitmq Setup
* ansible-playbook -i inventory.ini rabbitmq.yaml

# Payment Setup
* ansible-playbook -i inventory.ini payment.yaml

# Dispatch Setup
* ansible-playbook -i inventory.ini dispatch.yaml

# Frontend Setup
* ansible-playbook -i inventory.ini frontend.yaml