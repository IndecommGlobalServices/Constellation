import nose,os
from datetime import date, timedelta, datetime

testfilename = "TestResult - tests_in_Assessments_" + str(datetime.today().date()) +"_"+ str(datetime.today().time().hour)+"-"+str(datetime.today().time().minute)+".xml"
cwd = os.getcwd()
os.chdir('..')

filepath = os.path.join(os.getcwd(), testfilename)

os.chdir(cwd)
nose.run(argv=["","assessmenttest","assessmentoverviewtest","assessmentschooldatatest","assessmentschoolinfrastructuretest",
               "--verbosity=3","--with-xunit", "--xunit-file="+filepath+"", "--nologcapture","-s", "--nocapture"])

