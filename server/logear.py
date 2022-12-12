import os, time
from threading import Lock

def escribir_log(log, lock, thread):
    lock.acquire()
    logs = open('log.txt', 'a')
    print('cierro lock desde thread #', thread)
    time.sleep(5)
    logs.write(log)
    logs.close()
    print('abro lock  desde thread #', thread)
    lock.release()