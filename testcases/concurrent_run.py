from subprocess import Popen
import glob
import time
import os, sys
from datetime import datetime

start = time.time()
cwd = os.getcwd()
os.chdir('..')
asset_filepath = os.path.join(os.getcwd(), r"testresult-asset_" + str(datetime.today().strftime('%Y%m%d'))+"_"+
                              str(datetime.today().time().strftime('%H%M'))+".xml")
assessment_filepath = os.path.join(os.getcwd(), r"TestResult-Assessments_" + str(datetime.today().strftime('%Y%m%d')) +"_"+
                                   str(datetime.today().time().strftime('%H%M'))+".xml")
map_filepath = os.path.join(os.getcwd(), r"testresult-maps_" + str(datetime.today().strftime('%Y%m%d')) +"_"+
                            str(datetime.today().time().strftime('%H%M'))+".xml")
threatstream_filepath = os.path.join(os.getcwd(), r"testresult-threatstreams_" + str(datetime.today().strftime('%Y%m%d'))+"_"+
                                     str(datetime.today().time().strftime('%H%M'))+".xml")
os.chdir(cwd)

# assessmenttests = glob.glob('assessment*.py')

tests = (['assettest', str(asset_filepath)],
         ['assessmentoverviewtest', assessment_filepath],
         ['maptest', str(map_filepath)],
         ['threatstreamstest', threatstream_filepath])

processes = []

for test in tests:
    processes.append(Popen('nosetests --tests ' + test[0] + ' --xunit-file=' + test[1],  shell=True))

for process in processes:
    process.wait()

print "*" * 50
print "Time taken: %s minutes" % ((time.time() - start) /60)
