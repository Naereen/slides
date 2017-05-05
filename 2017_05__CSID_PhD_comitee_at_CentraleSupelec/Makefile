# Quick Makefile to easily compile the slides (make pdf) and run the slide (make showtime)
default: pandocpdf

theme = league

reveal-md:
	reveal-md --theme $(theme) --title "CSID  |  Date : 02 May 2017  |  Lilian Besson  |  CentraleSupélec" slides.md

pandocpdf:
	pandoc -N -s --template=../my.beamer -t beamer slides.md -o slides.pdf
	xdg-open slides.pdf &

Marp:
	Marp slides.md

typora:
	typora slides.md
