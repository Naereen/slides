# Quick Makefile to easily compile the slides (make pdf) and run the slide (make showtime)
SHELL=/usr/bin/env /bin/bash

default: pandocpdf

theme = league

reveal-md:
	reveal-md --theme $(theme) --title "Julia introduction  |  Date : 14 June 2018  |  Lilian Besson  |  CentraleSupélec" slides.md

pandocpdf:
	# pandoc --variable=aspectratio:43 -N -s --template=../my.beamer -t beamer slides-pandoc.md -o slides.pdf
	pandoc --variable=aspectratio:43 -N -s --template=../my.beamer -t beamer slides-pandoc.md -o slides.tex
	latexmk -xelatex -gg -pdf slides.tex
	xdg-open slides.pdf &

show:
	pdfpc -d 30 slides.pdf

pandocpdf169:
	# pandoc --variable=aspectratio:169 -N -s --template=../my.beamer -t beamer slides-pandoc.md -o slides_169.pdf
	pandoc --variable=aspectratio:169 -N -s --template=../my.beamer -t beamer slides-pandoc.md -o slides_169.tex
	latexmk -xelatex -gg -pdf slides_169.tex
	xdg-open slides_169.pdf &

show169:
	pdfpc -d 30 slides_169.pdf

Marp:
	Marp slides.md

typora:
	typora slides.md
