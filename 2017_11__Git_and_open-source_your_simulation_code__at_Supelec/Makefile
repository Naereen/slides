# Quick Makefile to easily compile the slides (make pdf) and run the slide (make showtime)
default: pandocpdf

theme = league

reveal-md:
	reveal-md --theme $(theme) --title "2nd GouTP  |  Date : 09 Nov 2017  |  Lilian Besson  |  CentraleSupélec" slides.md

pandocpdf:
	pandoc --variable=aspectratio:43 -N -s --template=../common/my.beamer -t beamer slides-pandoc.md -o slides.pdf
	xdg-open slides.pdf &

pandocpdf169:
	pandoc --variable=aspectratio:169 -N -s --template=../common/my.beamer -t beamer slides-pandoc.md -o slides_169.pdf
	xdg-open slides_169.pdf &

Marp:
	Marp slides.md

typora:
	typora slides.md
