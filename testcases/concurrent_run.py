from subprocess import Popen
import glob
import time
import os, sys
from datetime import datetime
from xml.etree import ElementTree

start = time.time()
cwd = os.getcwd()
os.chdir('..')
testresult = os.path.join(os.getcwd(), r"testresult_" + str(datetime.today().strftime('%Y%m%d'))+"_"+
                              str(datetime.today().time().strftime('%H%M'))+".xml")
asset_filepath = os.path.join(os.getcwd(), r"testresult-asset_" + str(datetime.today().strftime('%Y%m%d'))+"_"+
                              str(datetime.today().time().strftime('%H%M'))+".xml")
assessment_filepath = os.path.join(os.getcwd(), r"TestResult-Assessments_" + str(datetime.today().strftime('%Y%m%d')) +"_"+
                                   str(datetime.today().time().strftime('%H%M'))+".xml")
map_filepath = os.path.join(os.getcwd(), r"testresult-maps_" + str(datetime.today().strftime('%Y%m%d')) +"_"+
                            str(datetime.today().time().strftime('%H%M'))+".xml")
threatstream_filepath = os.path.join(os.getcwd(), r"testresult-threatstreams_" + str(datetime.today().strftime('%Y%m%d'))+"_"+
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

tests = (['assettest', str(asset_filepath)],
         ['maptest', str(map_filepath)],
         ['threatstreamstest', str(threatstream_filepath)],
         ['assessmenttest', str(assessment_filepath)],
         ['assessmentschooldatatest', str(assessmentschooldatatest_filepath)],
         ['assessmentoverviewtest', str(assessmentoverviewtest_filepath)],
         ['assessmentpoliciesandplanningtest', str(assessmentpolicies_filepath)],
         ['assessmentschoolinfrastructuretest', str(assessmentinfra_filepath)],
         ['assessmentphysicalsecuritytest', str(assessmentphysical_filepath)],
         ['assessmenttrainingandexercisetest', str(assessmenttrainning_filepath)])

processes = []

for test in tests:
    processes.append(Popen('nosetests --tests ' + test[0] + ' --xunit-file=' + test[1],  shell=True))

for process in processes:
    process.wait()

print "*" * 50
print "Time taken: %s minutes" % ((time.time() - start) /60)





# xml_files = glob.glob("..//*.xml")
# xml_element_tree = None
# tree = ElementTree.ElementTree()
# for xml_file in xml_files:
#     # get root
#     data = ElementTree.parse(xml_file).getroot()
#     for result in data.iter('testsuite'):
#         if xml_element_tree is None:
#             xml_element_tree = data
#         else:
#             xml_element_tree.extend(result)
# if xml_element_tree is not None:
#     print ElementTree.tostring(xml_element_tree)
#     ElementTree.ElementTree.write(tree, testresult)
