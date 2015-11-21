__author__ = 'Deepa.Sivadas'
import nose,os
from datetime import datetime
cwd = os.getcwd()
os.chdir('..')
smoketest_filepath = os.path.join(os.getcwd(), r"testresult-smoketest_" + str(datetime.today().strftime('%Y%m%d')) +"_"+
                             str(datetime.today().time().strftime('%H%M'))+".xml")
os.chdir(cwd)
nose.run(argv=["","assettest","assessmenttest", "maptest", "threatstreamstest", "-a status=smoke",
               "--xunit-file="+smoketest_filepath+""])


