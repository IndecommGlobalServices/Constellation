# Constellation
Keep track of threats to your organization and mission. It is easy to make informed decisions.
Catalog your assets, track incidents, and perform assessments. Monitor the threats that may affect you.
Collect intelligence from the field.

Selenium with Python:

It contains test scripts for Constellation.

Pre-requisites:
- Python 2.7
- Firefox browser
- Selenium Python bindings
- pyvirtualdisplay
- nose


Setup:
1.Python and Selenium setup
$ sudo apt-get install openjdk-7-jre-headless
$ sudo apt-get install python       #Installs Python

$ sudo apt-get install python-pip
$ sudo pip install selenium     #Install Selenium Python bindings

$ sudo pip install pyvirtualdisplay      #Plugin to run the script headless in linux box

$ sudo apt install firefox

$ sudo pip install -U nose        #Unittest framework


Execution:

1.To run the smoke test:
$ cd testing
$ bash smoketest.sh

2.To create smoketest.sh file
$mv smoketest.sh smoketest_old.sh
$vi smoketest.sh
    (enter the following lines to the smoketest.sh)
    #!/bin/bash

    cd testcases
    python ConstellationSmokeTest.py

3.To run the test suite:
$ cd testing
$ bash constellationLinux.sh

4.To create smoketest.sh file
$mv constellationLinux.sh constellationLinux_old.sh
$vi constellationLinux.sh
    (enter the following lines to the constellationLinux.sh)
    #!/bin/bash

    cd testcases
    python concurrent_run.py

5.To run individual asset test cases:
$ cd testing
$ cd testcases
$ nosetests --tests assettest.py --verbosity=3 --with-xunit --nologcapture -s --nocapture


Results:
1.XML reports are generated and available in ./testing
2.Screenshots of failed test are generated and available in ./testing/Screenshots



