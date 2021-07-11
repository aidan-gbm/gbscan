from ipaddress import IPv4Address

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