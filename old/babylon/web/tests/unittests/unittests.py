import coverage
import unittest

cov = coverage.coverage(branch=True, omit=["*.eggs/*", "*lib/*", "*unittests/*"])
cov.start()


def coverage_func():
    cov.stop()
    cov.save()
    print("\n\nCoverage Report:\n")
    cov.report()
    cov.erase()


def run_unittests(project_folder):
    """
        Only unittest
        :param project_folder:
    """
    tests = unittest.TestLoader().discover(project_folder)
    unittest.TextTestRunner(verbosity=2).run(tests)
    try:
        coverage_func()
    except coverage.misc.CoverageException as e:
        print(e.__str__())
