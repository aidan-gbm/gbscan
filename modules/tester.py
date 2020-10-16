from os import path, mkdir
import sqlite3

class Tester():
    def __init__(self, path):
        self.path = path.abspath(path)
        self.db = self.path + '/.gbscan/scan.db'
        if not path.isdir(self.path + '/.gbscan'):
            self.setup()
        else:
            self.load()

    def setup(self):
        mkdir(self.path + '/.gbscan')
        mkdir(self.path + '/.gbscan/nmap')
        mkdir(self.path + '/.gbscan/gobuster')

    def load(self):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        c.execute('SELECT ip FROM targets')
        self.targets = c.fetchall()
        c.close()

    def getInstance(self):
        return path.basename(self.path)
