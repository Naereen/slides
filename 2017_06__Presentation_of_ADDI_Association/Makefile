# Quick Makefile to easily compile the slides (make pdf) and run the slide (make showtime)
default: pandocpdf

theme = league

reveal-md:
	reveal-md --theme $(theme) --title "Association des Docteurs et Doctorants de l'IETR  |  Présentation  |  Juin 2017" slides.md

pandocpdf:
	pandoc --variable=aspectratio:43 -N -s --template=../my.beamer -t beamer slides.md -o slides.pdf
	xdg-open slides.pdf &

pandocpdf169:
	pandoc --variable=aspectratio:169 -N -s --template=../my.beamer -t beamer slides.md -o slides_169.pdf
	xdg-open slides_169.pdf &

Marp:
	Marp slides.md

typora:
	typora slides.md
