LoggerCalls
===========

A python script to create logs for analogue contests

---
This program has been tested under Kubuntu and requires Python and pdflatex installed in order to work.

In your clone directory please provide a directory called "pdfs" for the program to put the pdfs into.

The program will generate 50 unique call signs, in order to change this number, edit the line in makeLogs.py to read

m = makeLogs(x)

where x is the number of logs you want.

The script is designed to only generate simple callsigns, such as OZ for Denmark and not 5P, 5Q etc.
If simple call signs are not wanted please edit the line in makeLogs.py to read

self.calls = mc.makeCalls( False )

Enjoy!
