from subprocess import Popen
import glob
import time
import os
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
os.chdir(cwd)

# assessmenttests = glob.glob('assessment*.py')

tests = (['assessmenttest', str(assessment_filepath), 'Assessmenttest'],
         ['threatstreamstest', str(threatstream_filepath), 'ThreatStreamtest'],
         ['maptest', str(map_filepath), 'Maptest'])
         # ['assessmentoverviewtest', str(assessmentoverviewtest_filepath), 'AssessmentOverviewtest'],
         # ['assessmentschooldatatest', str(assessmentschooldatatest_filepath), 'AssessmentSchoolDatatest'],
         # ['assessmentpoliciesandplanningtest', str(assessmentpolicies_filepath), 'AssessmentPoliciesandPlanningtest'],
         # ['assessmentschoolinfrastructuretest', str(assessmentinfra_filepath), 'AssessmentSchoolInfrastructuretest'],
         # ['assessmentphysicalsecuritytest', str(assessmentphysical_filepath), 'AssessmentPhysicalSecuritytest'],
         # ['assessmenttrainingandexercisetest', str(assessmenttrainning_filepath), 'AssessmentTrainingandExercisetest'])

processes = []

for test in tests:
    processes.append(Popen('nosetests --tests ' + test[0] + ' --xunit-file=' + test[1] + ' --xunit-testsuite-name=' + test[2] , shell=True))
    sleep(2)

sleep(20)
processes.append(Popen('nosetests --tests assettest --xunit-file=' + str(asset_filepath) + ' --xunit-testsuite-name=Assettest' , shell=True))

for process in processes:
    process.wait()

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
