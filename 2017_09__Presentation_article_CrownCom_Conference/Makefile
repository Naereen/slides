# Quick Makefile to easily compile the slides (make pdf) and run the slide (make showtime)
default: all

all:	pandocpdf clean show
all169:	pandocpdf169 clean show169

pandoctex:
	pandoc --variable=aspectratio:43 -N -s --template=../my.beamer -t beamer slides.md -o slides.tex
	./preprocess_tex.sh slides.tex

pandocpdf:	pandoctex
	pdflatex slides.tex
	pdflatex slides.tex
	rm slides.toc slides.snm slides.out slides.nav slides.aux slides.log slides.vrb

open:
	xdg-open slides.pdf &

show:
	pdfpc -d 15 slides.pdf

pandoctex169:
	pandoc --variable=aspectratio:169 -N -s --template=../my.beamer -t beamer slides.md -o slides_169.tex
	./preprocess_tex.sh slides_169.tex

pandocpdf169:	pandoctex169
	pdflatex slides_169.tex
	pdflatex slides_169.tex
	rm slides_169.toc slides_169.snm slides_169.out slides_169.nav slides_169.aux slides_169.log slides_169.vrb

open169:
	xdg-open slides_169.pdf &

show169:
	pdfpc -d 15 slides_169.pdf

clean:
	-mv -vf *.fls *.fdb_latexmk *.ps *.dvi *.htoc *.tms *.tid *.lg *.log *.id[vx] *.vrb *.toc *.snm *.nav *.htmp *.aux *.tmp *.out *.haux *.hidx *.bbl *.blg *.brf *.lof *.ilg *.ind *.meta *.fdb_latexmk *.fls *.gz*busy* /tmp/ 2>/dev/null

Marp:
	Marp slides.md

typora:
	typora slides.md

theme = league

reveal-md:
	reveal-md --theme $(theme) --title "MAB Learning in IoT Networks  |  Date : 20 Sept 2017  |  Lilian Besson  |  CrownCom 2017" slides.md
