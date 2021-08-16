from WasRun import WasRun
from TestCase import TestCase

class PassOrStackTrace(TestCase):
    def runTest(self):
        test = WasRun("testMethod")
        print(test.wasRun)
        assert(not test.wasRun)
        test.run()
        print(test.wasRun)
        assert(test.wasRun)

PassOrStackTrace("runTest").run()  
