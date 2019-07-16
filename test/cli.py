#!/usr/bin/python3

import rpyc
import time
conn = rpyc.connect("localhost", 12345)
c = conn.root

fs = c.create_tmpfs()
time.sleep(60)

c.close_tmpfs(fs)
