# Quick Makefile to easily compile the slides (make pdf) and run the slide (make show)
SHELL=/usr/bin/env /bin/bash

default: send

send:	send_zamok
send_zamok:
	CP --exclude=.git ./*.md ./*.pdf ${Szam}teach/info1_algo1_2019/slides/
	cd .. ; make send_zamok


talk:
	clear ; pokemonsay "Good luck Lilian :-)" ; make show_pandoc ; clear ; pokemonsay 'You rock!'

all:	pandoctex pandocpdf clean show
all169:	pandoctex169 pandocpdf169 clean show169

pandoctex:
	pandoc -N -s --template=../common/my.beamer -t beamer slides.md -o slides.tex
	./preprocess_tex.sh slides.tex

pandocpdf:
	latexmk -xelatex -gg -pdf slides.tex
	rm slides.toc slides.snm slides.out slides.nav slides.aux slides.log slides.vrb

open:
	xdg-open slides.pdf &

show:
	pdfpc -d 20 slides.pdf

show_pandoc:
	pdfpc -d 20 slides.pdf

pandoctex169:
	pandoc --variable=aspectratio:169 -N -s --template=../common/my.beamer -t beamer slides.md -o slides_169.tex
	./preprocess_tex.sh slides_169.tex

pandocpdf169:
	latexmk -xelatex -gg -pdf slides_169.tex
	rm slides_169.toc slides_169.snm slides_169.out slides_169.nav slides_169.aux slides_169.log slides_169.vrb

open169:
	xdg-open slides_169.pdf &

show169:
	pdfpc -d 20 slides_169.pdf

clean:
	-mv -vf *.fls *.fdb_latexmk *.ps *.dvi *.htoc *.tms *.tid *.lg *.log *.id[vx] *.vrb *.toc *.snm *.nav *.htmp *.aux *.tmp *.out *.haux *.hidx *.bbl *.blg *.brf *.lof *.ilg *.ind *.meta *.fdb_latexmk *.fls *.gz*busy* /tmp/ 2>/dev/null

Marp:
	Marp slides.md

typora:
	typora slides.md

theme = league

reveal-md:
	reveal-md --theme $(theme) --title "Cours ALGO1  |  Date : 10 septembre 2019  |  Lilian Besson" slides.md
