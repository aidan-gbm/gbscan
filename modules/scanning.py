from ipaddress import IPv4Address
from os.path import exists, isfile
import xml.etree.ElementTree as xml

import modules.output as out
from subprocess import run, DEVNULL


def ping_host(tgt: IPv4Address):
    cmd = ['ping', '-c', '1', '-W', '3', str(tgt)]
    res = run(cmd, capture_output=True)
    up = (res.returncode == 0)

    return (up, res.stdout.decode()) if up else (up, res.stderr.decode())


def is_host_up(tgt: IPv4Address):
    up = False
    out.log(f'Checking if {tgt} is up...')
    up, txt = ping_host(tgt)

    if up:
        out.success('Host is up.')
    else:
        out.fail('Host is down.')

    return up


def fingerprint_os(tgt: IPv4Address):
    os = None
    out.log('Attempting to fingerprint OS...')
    up, txt = ping_host(tgt)

    if not up:
        out.fail('Host is now offline?')
        return os
    
    ttl = 0
    for part in txt.split():
        if 'ttl' in part:
            ttl = int(part.split('=')[1])
    
    if ttl > 64:
        os = 'Windows'
        out.success(f'Detected Windows with TTL {ttl}')

    elif ttl > 0:
        os = 'Linux'
        out.success(f'Detected Linux with TTL {ttl}')
    
    else:
        out.fail('Could not detect OS using TTL.')
    return os


def parse_xml_ports(xml_file: str):
    output = {}
    tree = xml.parse(xml_file)
    root = tree.getroot()
    for host in root.findall('host'):
        addr = host.find('address').attrib['addr']
        state = host.find('status').attrib['state']
        if (state == 'up'):
            output[addr] = {}
            for port in host.find('ports').findall('port'):
                output[addr][int(port.attrib['portid'])] = {
                    'proto': port.attrib['protocol'],
                    'state': port.find('state').attrib['state'],
                    'service': port.find('service').attrib['name']
                }
    return output


def portscan_quick(tgt: IPv4Address, dir: str):
    ports = None
    outfile = f'{dir}/nmap/quick.xml'
    if exists(outfile):
        if isfile(outfile):
            out.log('Found existing quick port scan.')
            ports = parse_xml_ports(outfile)
        else:
            out.err(f'{outfile} exists but isn\'t a normal file...')
    
    else:
        out.log('Running quick port scan...')
        cmd = ['nmap', '-F', '-oX', outfile, str(tgt)]
        res = run(cmd, capture_output=True)
        if res.returncode != 0:
            out.err(res.stderr.decode())
        else:
            ports = parse_xml_ports(outfile)
    
    open_ports = [p for p, d in ports[str(tgt)].items() if d['state'] == 'open']
    out.success('Open ports: ' + (', '.join(open_ports) or 'None'))
    return ports
