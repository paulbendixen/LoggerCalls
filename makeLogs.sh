#!/bin/bash

python makeLogs.py
cd pdfs
for f in log*.tex
do
	pdflatex $f
done
pdfunite log*.pdf allLogs.pdf
