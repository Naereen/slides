# Quick Makefile to easily compile the slides (make pdf) and run the slide (make showtime)
default: slides.pdf

slides.pdf:	clean pandoctex pandocpdf
pdf:	slides.pdf

pandoctex:
	pandoc --variable=aspectratio:43 -N -s --template=../my.beamer -t beamer slides.md -o slides.tex

pandocpdf:
	latexmk -gg -pdf -pdflatex="xelatex %O %S" slides.tex

open:
	xdg-open slides.pdf &

show:
	pdfpc -d 20 slides.pdf

slides_169.pdf:	clean pandoctex169 pandocpdf169

pandoctex169:
	pandoc --variable=aspectratio:169 -N -s --template=../my.beamer -t beamer slides.md -o slides_169.tex

pandocpdf169:
	latexmk -gg -pdf -pdflatex="xelatex %O %S" slides_169.tex

open169:
	xdg-open slides_169.pdf &

show169:
	pdfpc -d 20 slides_169.pdf

clean:
	-mv -vf *.fls *.fdb_latexmk *.ps *.dvi *.htoc *.tms *.tid *.lg *.log *.id[vx] *.vrb *.toc *.snm *.nav *.htmp *.aux *.tmp *.out *.haux *.hidx *.bbl *.blg *.brf *.lof *.ilg *.ind *.meta *.fdb_latexmk *.fls *.gz*busy* *busy* *.tex /tmp/ 2>/dev/null

Marp:
	Marp slides.md

typora:
	typora slides.md

theme = league
reveal-md:
	reveal-md --theme $(theme) --title "CSID  |  Date : 18 May 2018  |  Lilian Besson  |  CentraleSupélec" slides.md
