import nose,os
from datetime import date, timedelta, datetime

filename = "testresult-constellationtest_" + str(datetime.today().strftime('%Y%m%d')) +"_"+\
                    str(datetime.today().time().strftime('%H%M'))+".xml"
cwd = os.getcwd()
os.chdir('..')
filepath = os.path.join(os.getcwd(), filename)
os.chdir(cwd)
nose.run(argv=["", "logintest",
               "assettest",
               "assessmenttest",
               "assessmentoverviewtest",
               "assessmentschooldatatest",
               "assessmentphysicalsecuritytest",
               "assessmentpoliciesandplanningtest",
               "assessmentschoolinfrastructuretest",
               "assessmenttrainingandexercisetest",
               "eventtest",
               "fieldinterviewstest",
               "maptest",
               "threatstreamstest",
               "timelinetest"
               "--verbosity=3","--with-xunit",
               "--xunit-file="+filepath+"", "--nologcapture","-s", "--nocapture"])




