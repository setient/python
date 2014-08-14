#!/usr/bin/python
#This script will create a vm in aws and give it a hostname and setup dns.
import argparse
import boto
parser = argparse.ArgumentParser()
parser.add_argument("hostname", help="hostname of the vm you wish to create")
parser.parse_args()
print args.hostname
