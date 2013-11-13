#!/usr/bin/env python
import makeCalls
import re
import unittest

class TestCallsignClass( unittest.TestCase ):
	def setUp(self):
		self.DUT = makeCalls.makeCalls()
	def testThatDenmarkExists(self):
		self.assertTrue( 'OZ' in self.DUT.prefixes )
	def testThatGenerateOneGeneratesAValidCallsign( self ):
		test = self.DUT.generate(1)
		self.assertIsNotNone( re.search('^[0-9]?[A-Z]{1,2}[0-9][A-Z]{1,3}$', test[0] ) )
		self.assertIn( test[0][:2], self.DUT.prefixes )
	def testThatGenerateReturnsAList( self ):
		test = self.DUT.generate(1)
		self.assertIsInstance( test, list )
	def testThatGenerate2GeneratesAListOfLength2(self):
		test = self.DUT.generate(2)
		self.assertEqual(len(test),2)

	def testThatGenerate2DoesNotGenerateEqualValues( self ):
		test = self.DUT.generate(9)
		self.assertEqual(len(test),len(set(test)))


	def testThatALetterRaisesAParameterException( self ):
		with self.assertRaises( TypeError ):
			self.DUT.generate('hest')


if __name__ == '__main__':
	unittest.main()
