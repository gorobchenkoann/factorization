# coding=utf8
import os
import unittest
import tempfile
import app as app

class TestCase(unittest.TestCase):
  def testFactorizeNormal(self):
    self.assertEqual(app.factorize(15), '15 = 3 * 5')
  def testFactorizeNotNormal(self):
    self.assertEqual(app.factorize(-10), ('Это не натуральное число :(').decode('utf-8'))
  def testFactorizeNotNormals(self):
    self.assertEqual(app.factorize(0), app.factorize(-123))
  def testFactorizeOne(self):
    self.assertEqual(app.factorize(1), ('Это число не раскладывается на множители').decode('utf-8'))

if __name__ == '__main__':
  unittest.main()