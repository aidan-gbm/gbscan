#!/usr/bin/env python3

import argparse
from os import geteuid
from ipaddress import IPv4Address, AddressValueError

import modules.scanning as scan
import modules.output as out


def main():
    parser = argparse.ArgumentParser(prog='gbscan')
    parser.add_argument('-t', '--target', required=True, help='The target IPv4 address.')
    parser.add_argument('-p', '--path', help='The folder to store output. Defaults to target name.')
    args = parser.parse_args()

    try:
        tgt = IPv4Address(args.target)
    except AddressValueError:
        out.err('Invalid IPv4 address as target.')
        return 1
    
    out.log('Starting gbscan...')
    scan.is_host_up(tgt)
    scan.fingerprint_os(tgt)


if __name__ == '__main__':
    if geteuid() != 0:
        out.err('Must be run as root.')
        exit(1)

    exit(main())
