#!/usr/bin/python
import argparse
import boto
parser = argparse.ArgumentParser()
parser.add_argument("hostname", help="hostname of the vm you wish to create")
parser.parse_args()
print args.hostname
