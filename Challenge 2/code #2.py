import boto3
import json


def get_instances():
    ec2 = boto3.resource('ec2')
    data = ec2.instances.filter(Filters=[{'Name':'tag:Project','Values': ['Web']}])
    for instance in data:
        for tag in instance.tags:
            if 'Name' in tag['Key']:
                name = tag['Value']
        ec2_info = {
             "Name": name,
             "Instance_Id": str(instance.id),
             "State": instance.state["Name"],
             "Private_IP": instance.private_ip_address,
             }
        data = json.dumps(ec2_info,indent=4,sort_keys=True)

get_instances()

if __name__ = __main__
    get_instances()
    print(data)
