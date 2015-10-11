import nose,os
from datetime import date, timedelta, datetime

testfilename = "TestResult - tests_in_Assets_" + str(datetime.today().date()) +"_"+ str(datetime.today().time().hour)+"-"+str(datetime.today().time().minute)+".xml"
cwd = os.getcwd()
os.chdir('..')

filepath = os.path.join(os.getcwd(), testfilename)

os.chdir(cwd)
nose.run(argv=["","assettest", "--verbosity=3","--with-xunit", "--xunit-file="+filepath+"", "--nologcapture","-s", "--nocapture"])

#nose.run(argv=["","assettest", "assessmenttest", "maptest", "threatstreamstest", "--verbosity=3"])
#nose.run(argv=["","maptest", "--verbosity=3", "-a status=smoke", "--with-xunit",
               #"--xunit-file="+filepath+"", "--nologcapture","-s", "--nocapture"])

