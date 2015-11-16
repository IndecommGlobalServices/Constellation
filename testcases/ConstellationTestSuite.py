import nose,os
from datetime import date, timedelta, datetime

filename = "testresult - asset_" + str(datetime.today().strftime('%Y%m%d')) +"_"+\
                    str(datetime.today().time().strftime('%H%M'))+".xml"
cwd = os.getcwd()
os.chdir('..')
filepath = os.path.join(os.getcwd(), filename)
os.chdir(cwd)
nose.run(argv=["", "assettest",  "--verbosity=3","--with-xunit",
               "--xunit-file="+filepath+"", "--nologcapture","-s", "--nocapture"])




