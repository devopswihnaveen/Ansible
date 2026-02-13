# Create VM's 

* ansible-playbook -i localhost,   -e '{"instances":["mongodb","catalogue","redis","user","cart","mysql","shipping","rabbitmq","payment","frontend"]}'  -e action=create roboshop.yaml

### 1. MONGO DB Setup
* ansible-playbook -i inventory.ini mongodb.yaml

### 2. catalogue Setup
* ansible-playbook -i inventory.ini catalogue.yaml

### 3. REDIS Setup 
* ansible-playbook -i inventory.ini redis.yaml

### 4. User Setup
* ansible-playbook -i inventory.ini user.yaml

### 5. cart Setup
* ansible-playbook -i inventory.ini cart.yaml

### 6. MySql DB Setup
* ansible-playbook -i inventory.ini mysql.yaml

### 7. Shipping Setup
* ansible-playbook -i inventory.ini shipping.yaml

### 8. Rabbitmq Setup
* ansible-playbook -i inventory.ini rabbitmq.yaml

### 9. Payment Setup
* ansible-playbook -i inventory.ini payment.yaml

### 10. Dispatch Setup
* ansible-playbook -i inventory.ini dispatch.yaml

### 11. Frontend Setup
* ansible-playbook -i inventory.ini frontend.yaml


# Destroy VM's 

* ansible-playbook -i localhost,   -e '{"instances":["mongodb","catalogue","redis","user","cart","mysql","shipping","rabbitmq","payment","frontend"]}'  -e action=destroy roboshop.yaml