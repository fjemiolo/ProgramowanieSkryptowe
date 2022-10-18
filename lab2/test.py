#-*-coding: utf-8-*-

from skrypt import func
import unittest
import io
import sys


class Test_func(unittest.TestCase):
    def test1(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        func('1pies2koty')
        self.assertEqual(capturedOutput.getvalue(), 'Liczba: 1 2\nWyraz: pies koty\n')

    def test2(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        func('samwyraz')
        self.assertEqual(capturedOutput.getvalue(), 'Wyraz: samwyraz\n')

    def test3(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        func('żółty to 12345')
        self.assertEqual(capturedOutput.getvalue(), 'Liczba: 12345\nWyraz: żółty to\n')

    def test4(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        func('PROGRAMOWANIE SKRYPTOWE ĄĘ')
        self.assertEqual(capturedOutput.getvalue(), 'Wyraz: PROGRAMOWANIE SKRYPTOWE ĄĘ\n')

    def test5(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        func('50 50')
        self.assertEqual(capturedOutput.getvalue(), 'Liczba: 50 50\n')


if __name__ == '__main__':
    unittest.main()

