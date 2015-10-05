import nose
nose.run(argv=["","assettest", "assessmenttest", "maptest", "threatstreamstest", "--verbosity=3", "-a status=smoke"])
#nose.run(argv=["","assettest", "assessmenttest", "maptest", "threatstreamstest", "--verbosity=3"])
nose.run(argv=["","assettest", "--verbosity=3"])

