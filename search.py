#!/usr/bin/python
#-*- coding:utf-8 -*-
import struct, sys, os, time
from ip2Region import Ip2Region

def Search():
    llen = len(sys.argv)
    location  = os.path.dirname(os.path.realpath(__file__))
    os.chdir(location)
    dbFile    = './ip2region.db'
    method    = 1
    algorithm = "b-tree"
    ip_file = './ip'
    searcher = Ip2Region(dbFile);
    with open(ip_file,"rt") as f:
        for line in f:
            line = line.strip()
            if line == "":
                print("[Error]: Invalid ip address.")
                continue

            if line == "quit" or line == "exit":
                print("[Info]: Thanks for your use, Bye.")
                break

            if not searcher.isip(line):
                print("[Error]: Invalid ip address.")
                continue

            data = searcher.btreeSearch(line)

            if isinstance(data, dict):
                print("%s|%s" % (line, data["region"].decode('utf-8')))
            else:
                print("[Error]: ", data)
    searcher.close()

if __name__ == "__main__":
    Search()
