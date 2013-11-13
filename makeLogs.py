#!/usr/bin/env python
import makeCalls as mc

class makeLogs:
	def __init__(self, numberOfLogs = 50):
		self.calls = mc.makeCalls( True )
		self.numberOfLogs = numberOfLogs
		self.head = """\\documentclass[a4paper]{article}
\\usepackage{a4wide}

\\begin{document}
\\thispagestyle{empty}
\\begin{centering}
\\Huge
Log for """
		self.top = """

\\vspace{1cm}
\\begin{tabular}{|p{.70\\textwidth}|p{.10\\textwidth}|p{.20\\textwidth}|}
	\\hline
	\\huge{Call} & \\huge{QSO} & \\huge{Nummer} \\\\  
	\\hline
"""
		self.foot = """\\end{tabular}
\\end{centering}
\\end{document}
"""
	
	
	def generate(self, lines = 18):
		call = self.calls.generate(self.numberOfLogs)
		for c in call:
			filename = 'pdfs/log'+c+'.tex'
			logfile = open( filename, 'w' )
			logfile.write(self.head)
			logfile.write(c)
			logfile.write(self.top)
			for l in range(1,lines+1):
				logfile.write( ' & ' + str(l) + '&  \\\\\n' )
				logfile.write( '\\hline\n' )
			logfile.write( self.foot )
			logfile.close( )

if __name__ == '__main__':
	m = makeLogs()
	m.generate()
