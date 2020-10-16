from os import path as ospath, mkdir
from struct import unpack, pack
from socket import inet_aton, inet_ntoa
import sqlite3

def db_exec(db, queryStrings):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    for q in queryStrings:
        c.execute(q)
    conn.commit()
    conn.close()

def db_query(db, queryString):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(queryString)
    ret = c.fetchall()
    conn.close()
    return ret

def int2ip(addr):
    return inet_ntoa(pack("!I", addr))

def ip2int(addr):
    return unpack("!I", inet_aton(addr))[0]

class Tester():
    def __init__(self, path):
        self.path = ospath.abspath(path)
        self.db = self.path + '/.gbscan/scan.db'
        if not ospath.isdir(self.path + '/.gbscan'):
            self.setup()
        else:
            self.load()

    def setup(self):
        mkdir(self.path + '/.gbscan')
        mkdir(self.path + '/.gbscan/nmap')
        mkdir(self.path + '/.gbscan/gobuster')
        db_exec(self.db, ['CREATE TABLE targets ( id INTEGER PRIMARY KEY AUTOINCREMENT, ip INTEGER, notes TEXT )'])

    def load(self):
        self.targets = []
        tgts = db_query(self.db, 'SELECT id, ip FROM targets')
        for tup in tgts:
            self.targets.append({'id': tup[0], 'ip': int2ip(tup[1]), 'notes': ''})

    def add_tgt(self, tgtIp):
        try:
            ipInt = ip2int(tgtIp)
            db_exec(self.db, ['INSERT INTO targets ( ip ) VALUES ( {} )'.format(ipInt)])
        except:
            return False
        return True

    def del_tgt(self, tgtId):
        try:
            db_exec(self.db, ['DELETE FROM targets WHERE id = {}'.format(tgtId)])
            for i in range(len(self.targets)):
                if self.targets[i]['id'] == tgtId:
                    del self.targets[i]
                    break
            return True
        except:
            return False

    def getInstance(self):
        return ospath.basename(self.path)
