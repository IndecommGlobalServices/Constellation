import nose,os
from datetime import date, timedelta, datetime

testfilenamesmoke = "SmokeTestResult_" + str(datetime.today().date()) +"_"+ str(datetime.today().time().hour)+"-"+str(datetime.today().time().minute)+".xml"
testfilename = "TestResult_" + str(datetime.today().date()) +"_"+ str(datetime.today().time().hour)+"-"+str(datetime.today().time().minute)+".xml"
cwd = os.getcwd()
os.chdir('..')
filepathsmoke = os.path.join(os.getcwd(), testfilenamesmoke)
filepath = os.path.join(os.getcwd(), testfilename)

os.chdir(cwd)
nose.run(argv=["","assettest","assessmenttest", "maptest", "threatstreamstest", "--verbosity=3", "-a status=smoke", "--with-xunit",
               "--xunit-file="+filepathsmoke+"", "--nologcapture","-s", "--nocapture"])

#nose.run(argv=["","assettest", "assessmenttest", "maptest", "threatstreamstest", "--verbosity=3"])
nose.run(argv=["","assettest", "--verbosity=3", "--with-xunit",
               "--xunit-file="+filepath+"", "--nologcapture","-s", "--nocapture"])

