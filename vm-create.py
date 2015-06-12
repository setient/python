#!/usr/bin/python
#set your aws access keys in your environment before running this script
import boto.ec2
import boto.vpc
import re
import time
import argparse
import sys
import os
import boto
from pprint import pprint

# You can uncomment and set these, or set the env variables AWSAccessKeyId & AWSSecretKey
# AWS_ACCESS_KEY_ID="aaaaaaaaaaaaaaaaaaaa"
# AWS_SECRET_ACCESS_KEY="bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"

try:
        AWS_ACCESS_KEY_ID
except NameError:
        try:
                AWS_ACCESS_KEY_ID=os.environ['AWS_ACCESS_KEY']
                AWS_SECRET_ACCESS_KEY=os.environ['AWS_SECRET_KEY']
        except KeyError:
                print "Please set env variable"
                sys.exit(1)

parser = argparse.ArgumentParser()
#adds the environment
parser.add_argument('--hostname', help='hostname')
#adds the machine type aka what app will be deployed to it.
parser.add_argument('--machine', help='instance type')
parser.add_argument('--amiid', help='ami-id, default is our base-ami', default='some-ami-id-here')
parser.add_argument('--subnetid', help='subnet id')
parser.add_argument('--sgroup', help='security group id list, default is none', default='some-security-group-id-here')
parser.add_argument('--pgroup', help='pgroup, default is our none and does not have to be set')

#parses the arguements
args = parser.parse_args()
amiid = args.amiid
hostname = args.hostname
machine = args.machine
subnetid = args.subnetid
pgroup = args.pgroup
sgroup = []

# Commenting out this security group logic for now and just putting in the defaults so it works
if args.sgroup:
	sgroup.append(args.sgroup)

conn = boto.ec2.connect_to_region("us-east-1", aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

#conn.run_instances('ami-89ac9be0', key_name='vpc1', instance_type=machine, security_groups=['ssh'], user_data=hostname)
if pgroup:
	#print 
	conn.run_instances(image_id=amiid, key_name='vpc1', instance_type=machine, security_group_ids=sgroup, user_data=hostname, subnet_id=subnetid, placement_group=pgroup)
	print sgroup
else:
	conn.run_instances(image_id=amiid, key_name='vpc1', instance_type=machine, security_group_ids=sgroup, user_data=hostname, subnet_id=subnetid)
	print sgroup
#connects to ec2

