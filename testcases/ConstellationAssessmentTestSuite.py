import nose,os
from datetime import date, timedelta, datetime

filename = "TestResult - tests_in_Assessments_" + str(datetime.today().date()) +"_"+ str(datetime.today().time().hour)+"-"+str(datetime.today().time().minute)+".xml"
cwd = os.getcwd()
os.chdir('..')

filepath = os.path.join(os.getcwd(), filename)

os.chdir(cwd)
nose.run(argv=["","assessmentoverviewtest",
               "--verbosity=3","--with-xunit", "--xunit-file="+filepath+"", "--nologcapture","-s", "--nocapture"])





