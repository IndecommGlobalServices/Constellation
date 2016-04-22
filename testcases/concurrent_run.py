from subprocess import Popen
import glob
import time, sys
import os, nose
from datetime import datetime
from time import sleep
import xml.etree.ElementTree as ET

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
os.chdir(cwd)

# assessmenttests = glob.glob('assessment*.py')

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
          ['threatstreamstest', str(threatstream_filepath), 'ThreatStreamtest'])
#
# testsordered1 = (['threatstreamstest', str(threatstream_filepath), 'ThreatStreamtest'],
#                  ['assessmenttest', str(assessment_filepath), 'Assessmenttest'],
#                  ['assessmentoverviewtest', str(assessmentoverviewtest_filepath), 'AssessmentOverviewtest'],
#                  ['logintest', str(login_filepath), 'Logintest'],
#                  ['assessmentschooldatatest', str(assessmentschooldatatest_filepath), 'AssessmentSchoolDatatest'])
#
# testsordered2 = (['threatstreamstest', str(threatstream_filepath), 'ThreatStreamtest'],
#                  ['assessmentoverviewtest', str(assessmentoverviewtest_filepath), 'AssessmentOverviewtest'],
#                  ['assessmentpoliciesandplanningtest', str(assessmentpolicies_filepath), 'AssessmentPoliciesandPlanningtest'])

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

# for test in testsordered1:
#     processes.append(os.system('nosetests --tests ' + test[0] + ' --xunit-file=' + test[1] + ' --xunit-testsuite-name=' + test[2]))
#     sleep(2)
#
# for test in testsordered1:
#     processes.append(Popen('nosetests --tests ' + test[0] + ' --xunit-file=' + test[1] + ' --xunit-testsuite-name=' + test[2] , shell=True))
#     sleep(2)
#
# for process in processes:
#     process.wait()
#
# for test in testsordered2:
#     processes.append(Popen('nosetests --tests ' + test[0] + ' --xunit-file=' + test[1] + ' --xunit-testsuite-name=' + test[2] , shell=True))
#     sleep(2)
# for test in testsordered2:
#     processes.append(os.system('nosetests --tests ' + test[0] + ' --xunit-file=' + test[1] + ' --xunit-testsuite-name=' + test[2]))
#     sleep(2)
# for process in processes:
#     process.wait()

print "*" * 50
print "Time taken: %s minutes" % ((time.time() - start) /60)

# xml_files = glob.glob("..\\"+path+"\\*.xml")
# xml_element_tree = None
# for xml_file in xml_files:
#     print xml_file
#     # get root
#     data = ET.parse(xml_file).getroot()
#     for result in data.iter('testsuite'):
#         if xml_element_tree is None:
#             xml_element_tree = result
#         else:
#             xml_element_tree.append(result)
# if xml_element_tree is not None:
#     ET.ElementTree(xml_element_tree).write(testresult)
