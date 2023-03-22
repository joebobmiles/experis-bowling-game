import subprocess
import time
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        # java -jar path-to/sikulixapi.jar -p
        self.sikuli_api_server = subprocess.Popen([
            "java",
            "-jar",
            "./test/sikulixapi-2.0.5.jar",
            "-p"
        ])
        time.sleep(5)

        self.sikuli =  __import__("sikulix4python")

        self.sikuli.addImagePath("./screenshots")

    def tearDown(self):
        self.sikuli_api_server.terminate()

    def test_example(self):
        pass
