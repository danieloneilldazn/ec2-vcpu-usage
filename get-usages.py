#!/usr/local/bin/python3

import boto3
import sys
import csv


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

        with open('instancetypes.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Instance type'] == instance.instance_type:
                    total_vcpu += int(row['vCPUs'])
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

