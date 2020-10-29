from subprocess import run, DEVNULL
import xml.etree.ElementTree as xml
from os import path

def scan_quick(target, d):
    f = '{}/nmap/quick.xml'.format(d)
    c = None
    if not path.exists(f):
        c = 'nmap -F -oX {} {}'.format(f, target)
        s = run(c.split(), stdout=DEVNULL).returncode == 0
        if (not s): return (c, False)
    return (c, read_ports(f)[target])

def read_ports(f):
    output = {}
    tree = xml.parse(f)
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