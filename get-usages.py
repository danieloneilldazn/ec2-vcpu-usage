import boto3
import sys

vcpus = {
    "nano": 2,
    "micro": 2,
    "small": 2,
    "medium": 2,
    "large": 2,
    "xlarge": 4,
    "2xlarge": 8
}

if len(sys.argv) < 2 :
    print()
    print("ERROR: provide comma separated regions as argument.")
    print()
    sys.exit(1)

regions = sys.argv[1].split(",")

if len(regions) == 0 :
    print()
    print("ERROR: provide comma separated regions as argument.")
    print()
    sys.exit(1)

print("\nGetting vCPU usages for region(s):\n    -" + "\n    -".join(regions))
print()

for region in regions:
    metadata={}
    print("[{}]".format(region))
    ec2 = boto3.resource('ec2', region_name=region)
    instances = ec2.instances.all()
    total=0
    total_vcpu=0
    for instance in instances:
        total+=1
        if instance.instance_type in metadata.keys():
            metadata[instance.instance_type] += 1
        else:
            metadata[instance.instance_type] = 1
        total_vcpu += vcpus[instance.instance_type.split(".")[1]]
        print(instance.id, instance.instance_type)

    print()
    print("Total instances: {}".format(total))
    print()
    print("By Type: ")
    for key in metadata.keys():
        print(key, metadata[key])
    print()
    print("Total vCPUs: {}".format(total_vcpu))
    print()
    print("=" * 40)
    total=0