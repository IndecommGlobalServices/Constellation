import unittest, assettest, assessmenttest,maptest, basetestcase, hometest, logintest
import json, os

cwd = os.getcwd()
os.chdir('..')
L1 = os.path.join(os.getcwd(), "data\json_testsuite.json")
os.chdir(cwd)


loader = unittest.TestLoader()
asset_suite = loader.loadTestsFromModule(assettest)
assessment_suite = loader.loadTestsFromModule(assessmenttest)
map_suite = loader.loadTestsFromModule(maptest)
global_suite = unittest.TestSuite()
global_suite.addTest(assessment_suite)
global_suite.addTest(map_suite)
global_suite.addTest(asset_suite)
unittest.TextTestRunner(verbosity=3).run(global_suite)


'''

from testcases.assettest import assettest
from testcases.hometest import basetestcase
from testcases.basetestcase import hometest
from testcases.logintest import logintest


home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
base_page_tests = unittest.TestLoader().loadTestsFromTestCase(BaseTestCase)
login_page_tests = unittest.TestLoader().loadTestsFromTestCase(LoginPageTest)
asset_page_tests = unittest.TestLoader().loadTestsFromTestCase(AssetPageTest)

# create a test suite combining search_test and home_page_test
#smoke_tests = unittest.TestSuite([base_page_tests, home_page_tests, login_page_tests, asset_page_tests ])
smoke_tests = unittest.TestSuite([asset_page_tests])

# run the suite
unittest.TextTestRunner(verbosity=2).run(smoke_tests)

'''

