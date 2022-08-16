from pydoc import describe
import boto3

# Creating a function with no parameters
def create_ec2_instance():
    try:
        print ("Creating new EC2 Instance")    
        resource_ec2 = boto3.client("ec2") # Creating a resource variable
        resource_ec2.run_instances( #Run an instance using aws configure sso boto3 client using the parameters below
            ImageId="ami-090fa75af13c156b4",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="boto3_jz_sandbox"
        )
    except Exception as e:
        print(e)

def describe_ec2_instance ():
    try:
        print ("Describing our new EC2 Instance")
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.describe_instances())
    except Exception as e:
        print(e)

create_ec2_instance() #Call the function
describe_ec2_instance() #Call the function