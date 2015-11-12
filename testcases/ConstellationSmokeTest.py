__author__ = 'Deepa.Sivadas'
import nose,os
from datetime import date, timedelta, datetime
testfilenamesmoke = "testresult-smoketest_" + str(datetime.today().strftime('%Y%m%d')) +"_"+ str(datetime.today().time().strftime('%H%M'))+".xml"
cwd = os.getcwd()
os.chdir('..')
filepathsmoke = os.path.join(os.getcwd(), testfilenamesmoke)
os.chdir(cwd)
nose.run(argv=["","assettest","assessmenttest", "maptest", "threatstreamstest", "--verbosity=3", "-a status=smoke", "--with-xunit",
               "--xunit-file="+filepathsmoke+"", "--nologcapture","-s", "--nocapture"])


