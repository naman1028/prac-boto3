import csv
import boto3







def load_csv():
    with open("instance.csv") as f:
        reader = csv.DictReader(f)
        for x1 in reader:
            print(x1.get("instance-name"))
            print(x1.get("instance-type"))
            create_instance(x1.get("instance-name"),x1.get("instance-type"),x1.get("pkg"))





def create_instance(instance_name,instance_type,pkg):
    machine_input = instance_name

    if machine_input:
       ec2 = boto3.resource('ec2')
       userdata = """#!/bin/bash
       apt update
       apt install {0}  -y
       
       
       
       """
       instance = ec2.create_instances(
               ImageId="ami-024c319d5d14b463e",
               InstanceType=instance_type,
               KeyName="naman",
               MaxCount=1,
               MinCount=1,
               UserData=userdata.format(pkg)
       )
       for x1 in instance:
           x1.create_tags(Tags=[{'Key': 'Name','Value': machine_input},])
           print(">>>>",machine_input)

load_csv()