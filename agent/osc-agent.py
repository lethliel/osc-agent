#!/usr/bin/python3

from fs.tempfs import TempFS
import fs
import time
import rpyc

class OSCPWHANDLING():
  def create_tmpfs(self):
    tmpfs = TempFS(identifier='tmp_test')

    with tmpfs.open('pass_user', 'w') as passw: passw.write('This is a TEST')
    pwfile = tmpfs.open('pass_user')

    password = pwfile.read()
    print(password)
    return tmpfs

  def close_tmpfs(self, tmpfs):
    print("Will close tmpfs again")
    tmpfs.close()

class MyService(rpyc.Service):
  def exposed_create_tmpfs(self):
    return main.create_tmpfs()
  def exposed_close_tmpfs(self, fs=fs):
    return main.close_tmpfs(fs)

from rpyc.utils.server import ThreadedServer
from threading import Thread
server = ThreadedServer(MyService, port = 12345)
t = Thread(target = server.start)
t.daemon = True
t.start()

main = OSCPWHANDLING()
while True:
  time.sleep(1)
