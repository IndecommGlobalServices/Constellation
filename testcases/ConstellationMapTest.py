import nose,os
from datetime import date, timedelta, datetime

assettestfilename = "testresult-maptest_" + str(datetime.today().strftime('%Y%m%d')) +"_"+\
                    str(datetime.today().time().strftime('%H%M'))+".xml"
cwd = os.getcwd()
os.chdir('..')
assetfilepath = os.path.join(os.getcwd(), assettestfilename)
os.chdir(cwd)
nose.run(argv=["", "maptest", "--verbosity=3","--with-xunit", "--xunit-file="+assetfilepath+"", "--nologcapture","-s",
               "--nocapture"])



