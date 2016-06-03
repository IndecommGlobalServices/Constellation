from subprocess import Popen
import time, os
from datetime import datetime
from time import sleep


start = time.time()
cwd = os.getcwd()
os.chdir('..')
path = os.path.join(os.getcwd(), "testresults_"+str(datetime.today().strftime('%Y%m%d'))+"_"+str(datetime.today().time().strftime('%H%M')))
if not os.path.exists(path):
   os.makedirs(path)
os.chdir(path)

testresult = os.path.join(os.getcwd(), r"Testresult_" + str(datetime.today().strftime('%Y%m%d'))+"_"+
                              str(datetime.today().time().strftime('%H%M'))+".xml")
asset_filepath = os.path.join(os.getcwd(), r"Testresult-asset_" + str(datetime.today().strftime('%Y%m%d'))+"_"+
                              str(datetime.today().time().strftime('%H%M'))+".xml")
assessment_filepath = os.path.join(os.getcwd(), r"TestResult-Assessments_" + str(datetime.today().strftime('%Y%m%d')) +"_"+
                                   str(datetime.today().time().strftime('%H%M'))+".xml")
map_filepath = os.path.join(os.getcwd(), r"Testresult-maps_" + str(datetime.today().strftime('%Y%m%d')) +"_"+
                            str(datetime.today().time().strftime('%H%M'))+".xml")
threatstream_filepath = os.path.join(os.getcwd(), r"Testresult-threatstreams_" + str(datetime.today().strftime('%Y%m%d'))+"_"+
                                     str(datetime.today().time().strftime('%H%M'))+".xml")
assessmentschooldatatest_filepath = os.path.join(os.getcwd(), r"TestResult-AssessmentsSchooldata_" + str(datetime.today().strftime('%Y%m%d')) +"_"+
                                   str(datetime.today().time().strftime('%H%M'))+".xml")
assessmentoverviewtest_filepath = os.path.join(os.getcwd(), r"TestResult-AssessmentsOverview_" + str(datetime.today().strftime('%Y%m%d')) +"_"+
                                   str(datetime.today().time().strftime('%H%M'))+".xml")
assessmentpolicies_filepath = os.path.join(os.getcwd(), r"TestResult-AssessmentsPolicies_" + str(datetime.today().strftime('%Y%m%d')) +"_"+
                                   str(datetime.today().time().strftime('%H%M'))+".xml")
assessmentinfra_filepath = os.path.join(os.getcwd(), r"TestResult-AssessmentsInfra_" + str(datetime.today().strftime('%Y%m%d')) +"_"+
                                   str(datetime.today().time().strftime('%H%M'))+".xml")
assessmentphysical_filepath = os.path.join(os.getcwd(), r"TestResult-AssessmentsPhysical_" + str(datetime.today().strftime('%Y%m%d')) +"_"+
                                   str(datetime.today().time().strftime('%H%M'))+".xml")
assessmenttrainning_filepath = os.path.join(os.getcwd(), r"TestResult-AssessmentsTrainning_" + str(datetime.today().strftime('%Y%m%d')) +"_"+
                                  str(datetime.today().time().strftime('%H%M'))+".xml")
login_filepath = os.path.join(os.getcwd(), r"TestResult-Login_" + str(datetime.today().strftime('%Y%m%d')) +"_"+
                                  str(datetime.today().time().strftime('%H%M'))+".xml")
timeline_filepath = os.path.join(os.getcwd(), r"TestResult-TimeLine_" + str(datetime.today().strftime('%Y%m%d')) +"_"+
                                  str(datetime.today().time().strftime('%H%M'))+".xml")
events_filepath = os.path.join(os.getcwd(), r"TestResult-Events_" + str(datetime.today().strftime('%Y%m%d')) +"_"+
                                  str(datetime.today().time().strftime('%H%M'))+".xml")
fieldinterviews_filepath = os.path.join(os.getcwd(), r"TestResult-FieldInterviews_" + str(datetime.today().strftime('%Y%m%d')) +"_"+
                                  str(datetime.today().time().strftime('%H%M'))+".xml")
os.chdir(cwd)

tests1 = (['assessmentschoolinfrastructuretest', str(assessmentinfra_filepath), 'AssessmentSchoolInfrastructuretest'],
          ['assettest', str(asset_filepath), 'Assettest'],
          ['assessmentphysicalsecuritytest', str(assessmentphysical_filepath), 'AssessmentPhysicalSecuritytest'],
          ['assessmenttest', str(assessment_filepath), 'Assessmenttest'],
          ['assessmentoverviewtest', str(assessmentoverviewtest_filepath), 'AssessmentOverviewtest'],
          ['logintest', str(login_filepath), 'Logintest'],
          ['assessmentschooldatatest', str(assessmentschooldatatest_filepath), 'AssessmentSchoolDatatest'])

test2 =  (['maptest', str(map_filepath), 'Maptest'],
          ['assessmentpoliciesandplanningtest', str(assessmentpolicies_filepath), 'AssessmentPoliciesandPlanningtest'],
          ['assessmenttrainingandexercisetest', str(assessmenttrainning_filepath), 'AssessmentTrainingandExercisetest'],
          ['threatstreamstest', str(threatstream_filepath), 'ThreatStreamtest'],
          ['eventtest', str(events_filepath), 'Eventtest'],
          ['timelinetest', str(timeline_filepath), 'Timelinetest'],
          ['fieldinterviewstest', str(fieldinterviews_filepath), 'Fieldinterviewstest'])

processes = []

for test in tests1:
    processes.append(Popen('nosetests --tests ' + test[0] + ' --xunit-file=' + test[1] + ' --xunit-testsuite-name=' + test[2], shell=True))
    sleep(2)

sleep(650)

for test in test2:
    processes.append(Popen('nosetests --tests ' + test[0] + ' --xunit-file=' + test[1] + ' --xunit-testsuite-name=' + test[2], shell=True))
    sleep(2)

for process in processes:
    process.wait()

print "*" * 50
print "Time taken: %s minutes" % ((time.time() - start) /60)
