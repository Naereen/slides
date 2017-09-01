# Quick Makefile to easily compile the slides (make pdf) and run the slide (make showtime)
default: pandocpdf

theme = league

reveal-md:
	reveal-md --theme $(theme) --title "MAB Learning in IoT Networks  |  Date : 20 Sept 2017  |  Lilian Besson  |  CrownCom 2017" slides.md

show:
	pdfpc -d 15 slides.pdf

show169:
	pdfpc -d 15 slides_169.pdf

pandocpdf:
	pandoc --variable=aspectratio:43 -N -s --template=../my.beamer -t beamer slides.md -o slides.tex
	./preprocess_tex.sh slides.tex
	pdflatex slides.tex
	pdflatex slides.tex
	xdg-open slides.pdf &

pandocpdf169:
	pandoc --variable=aspectratio:169 -N -s --template=../my.beamer -t beamer slides.md -o slides_169.tex
	./preprocess_tex.sh slides_169.tex
	pdflatex slides_169.tex
	pdflatex slides_169.tex
	xdg-open slides_169.pdf &

Marp:
	Marp slides.md

typora:
	typora slides.md
