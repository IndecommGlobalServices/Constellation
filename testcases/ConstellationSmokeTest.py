__author__ = 'Deepa.Sivadas'
import nose,os
from datetime import date, timedelta, datetime

testfilenamesmoke = "TestResult - Smoketests_" + str(datetime.today().date()) +"_"+ str(datetime.today().time().hour)+"-"+str(datetime.today().time().minute)+".xml"
cwd = os.getcwd()
os.chdir('..')
filepathsmoke = os.path.join(os.getcwd(), testfilenamesmoke)
os.chdir(cwd)
nose.run(argv=["","assettest", "--verbosity=3", "-a status=smoke", "--with-xunit",
               "--xunit-file="+filepathsmoke+"", "--nologcapture","-s", "--nocapture"])


