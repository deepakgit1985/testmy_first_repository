import os
import sys
import pytest
import unittest


@pytest.mark.last
class GenerateReport(unittest.TestCase):

    def test_generate_report(self):
        os.system('cmd /c "allure serve ./reports"')
        sys.exit()
