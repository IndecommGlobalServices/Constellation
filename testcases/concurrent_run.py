from subprocess import Popen
import glob
import time
import os

start = time.time()

tests = glob.glob('ConstellationTest*.py')
processes = []
for test in tests:
    processes.append(Popen('nosetests --tests ' + test, shell=True))

for process in processes:
    process.wait()

print "*" * 50
print "Time taken: %s minutes" % ((time.time() - start) /60)
