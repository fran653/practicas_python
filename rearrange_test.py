#!/usr/bin/env python3
import unittest
from rearrange import rearrange_name
class TestRearrange(unittest.TestCase):
  def test_basic(self):
    testcase = "Lovelace, Ada"
    expected = "Ada Lovelace"
    self.assertEqual(rearrange_name(testcase), expected)

'''chmod +x rearrange_test.py 
./rearrange_test.py '''