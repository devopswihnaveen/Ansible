# generste a python script for ec2 instance monitor
def get_ec2_instances():
    """Retrieve all EC2 instances and their status"""
    client = boto3.client('ec2')
    response = client.describe_instances()
    
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append({
                'InstanceId': instance['InstanceId'],
                'InstanceType': instance['InstanceType'],
                'State': instance['State']['Name'],
                'LaunchTime': instance['LaunchTime'],
                'PublicIpAddress': instance.get('PublicIpAddress', 'N/A')
            })
    return instances

def monitor_instances():
    """Monitor EC2 instances and display their status"""
    instances = get_ec2_instances()
    print(f"Total EC2 Instances: {len(instances)}\n")
    
    for instance in instances:
        print(f"Instance ID: {instance['InstanceId']}")
        print(f"Type: {instance['InstanceType']}")
        print(f"State: {instance['State']}")
        print(f"Launch Time: {instance['LaunchTime']}")
        print(f"Public IP: {instance['PublicIpAddress']}\n")

if __name__ == "__main__":
    monitor_instances()
import boto3