import os, unittest

DEPTH = 2
DIS_PATH = os.path.abspath(__file__).split('\\')
SUPER_PATH = '\\'.join(DIS_PATH[:-DEPTH])
SISTER_PATHS = [SUPER_PATH + '\\' + i for i in os.listdir(SUPER_PATH)
               if '.' not in i and i != DIS_PATH[-DEPTH]]

def main():
    testmodules = []
    for dir_ in SISTER_PATHS:
        if os.path.isdir(dir_+'\\test'):
            base = '.'.join(dir_.split('\\')[-2:])
            testmodules += [base + '.test.' + i.replace('.py','')
                            for i in os.listdir(dir_+'\\test') if'test' in i]

    suite = unittest.TestSuite()

    for test in testmodules:
        print(test)
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))

    unittest.TextTestRunner().run(suite)