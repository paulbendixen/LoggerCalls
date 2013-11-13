#!/usr/bin/env python

import random

class makeCalls:
	"""A simple class to generate call signs from the countries sorrounding Denmark
"""

	def __init__(self, simple = False ):
		#Denmark (incl. Faroe island and Greenland )	
		self.prefixes = ['OU', 'OV', 'OW', 'OX', 'OY', 'OZ', 'XP', '5P', '5Q']
		#Norway
		self.prefixes += ['JW', 'JX', 'LA', 'LN', 'LB', 'LC', 'LD', 'LE', 'LF', 'LG', 'LH', 'LI', 'LJ', 'LK', 'LL', 'LM', 'LN', '3Y']
		# Sweden
		self.prefixes += ['SA', 'SB', 'SC', 'SD', 'SE', 'SF', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', '7S', '8S']
		# Germany
		# DA - DR
		for l in range(ord('A'),ord('S')):
			tmp = ['D' + chr(l)]
			self.prefixes += tmp
		# GB et. al
		self.prefixes += 'G'
		for l in range(ord('A'),ord('Z')+1):
			tmp = ['2'+chr(l)]
			self.prefixes += tmp
		for l in range(ord('A'),ord('Z')+1):
			tmp = ['G'+chr(l)] + ['M' +chr( l ) ]
			self.prefixes += tmp
		self.prefixes += ['VP', 'VQ', 'VS']
		for l in range(ord('A'),ord('I')+1):
			tmp = ['P'+chr(l)]
			self.prefixes += tmp

		# Ireland ( is _not_ GB ;) )
		self.prefixes += [ 'EI', 'EJ']
		# Spain 
		self.prefixes += ['AM', 'AN', 'AO']
		for l in range(ord('A'),ord('H')+1):
			tmp = ['E'+chr(l)]
			self.prefixes += tmp
		# Switzerland ( and Liechtenstein )
		self.prefixes += ['HB', 'HE']
		# Poland 
		self.prefixes += ['3Z', 'HF']
		for l in range(ord('N'),ord('R')+1):
			tmp = ['S'+chr(l)]
			self.prefixes += tmp
		# France (better remember them or they will get mad )
		self.prefixes += ['F', 'FU', 'FV', 'HW', 'HX', 'HY', 'TH', 'TQ' ]
		for l in range(ord('V'),ord('X')+1):
			tmp = ['T'+chr(l)]
			self.prefixes += tmp
	
		# This is for Belgium
		for l in range(ord('N'),ord('T')+1):
			tmp = ['O'+chr(l)]
			self.prefixes += tmp

		# Chekoslovakia (yes I know they're two different countries )
		for l in range(ord('K'),ord('M')+1):
			tmp = ['O'+chr(l)]
			self.prefixes += tmp
		
		# Italy (I cant't figure out their system, so these are the ones that gets picked
		self.prefixes += ['I', 'IK','IA']

		if ( simple == True ):
			self.prefixes = ['OZ','LA','SM','G','GM', 'DA', 'DB', 'DC', 'DD','DJ','DK','OY', 'OX', 'F', 'I', 'HB', 'SP', 'EA', 'EI', 'ON', 'OK', 'OM']
			

	def generate( self, numberOfCalls ):
		if ( isinstance( numberOfCalls, int ) == False ):
			raise( TypeError, "The number of calls generated must be an integer" )
		random.seed(1)
		calls = ['5P5E']
		for i in range(1, numberOfCalls ):
			callNow = self.prefixes[random.randint(0,len(self.prefixes)-1)] + str(random.randint(0,9))
			letters = random.randint(1,3)
			for j in range(letters ):
				callNow += chr(random.randint(65,90))
			calls.append( callNow )
		return calls

if __name__ == "__main__":
	caller = makeCalls( True );
	calls = caller.generate( 50 )
	while ( len(calls) != len(set(calls))):
		calls = caller.generate( 50 )
	for t in calls:
	 	print t
