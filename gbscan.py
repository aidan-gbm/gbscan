#!/usr/bin/env python3

import argparse
from os import mkdir
from os import geteuid
from os.path import normpath, exists, isdir, join
from ipaddress import IPv4Address, AddressValueError

import modules.scanning as scan
import modules.output as out


def main():

    # Parse Command Line Arguments
    parser = argparse.ArgumentParser(prog='gbscan')
    parser.add_argument('-t', '--target', required=True, help='The target IPv4 address.')
    parser.add_argument('-p', '--path', help='The folder to store output. Defaults to target name.')
    args = parser.parse_args()

    try:
        tgt = IPv4Address(args.target)
    except AddressValueError:
        out.err('Invalid IPv4 address as target.')
        return -1

    # Setup Save Directory
    out.log('Starting gbscan...')
    if args.path is not None:
        path = normpath(args.path)
    else:
        path = normpath(str(args.target))
    
    if exists(path) and isdir(path):
        out.success(f'Found existing work at {path}')
    else:
        out.log(f'Creating new directory at {path}')
        mkdir(path)
        mkdir(join(path, 'nmap'))
    
    # Begin Scanning Target
    if not scan.is_host_up(tgt):
        return 1
    
    scan.fingerprint_os(tgt)
    scan.portscan_quick(tgt, path)


if __name__ == '__main__':
    if geteuid() != 0:
        out.err('Must be run as root.')
        exit(-1)

    exit(main())
