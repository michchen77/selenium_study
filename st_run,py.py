import unittest

from .sel_study_note import St

class StTestRunner():
    def run_tests(self):
        suite = unittest.TestSuite()
        suite.addTest(St('test_st'))
        runner = unittest.TextTestRunner()
        runner.run(suite)

if __name__ == "__main__":
    st_test_runner = StTestRunner()
    st_test_runner.run_tests()