# Quick Makefile to easily compile the slides (make pdf) and run the slide (make showtime)
default: pandocpdf

theme = sky
theme = league

reveal-md:
	reveal-md --theme $(theme) --title "CSID  |  Date: 02 May 2017  |  Lilian Besson  |  CentraleSupélec" slides.md

pandocpdf:
	pandoc -i -N -s --template=../my.beamer -t beamer slides.md -o slides.pdf
	xdg-open slides.pdf &

Marp:
	Marp slides.md

typora:
	typora slides.md

showtime:	slides
slides:
	#-gmusicbrowser -cmd Pause  # Just to make sure your music player is NOT playing when you start your talk
	@echo "Using Impressive.py (from http://impressive.sourceforge.net/)"
	impressive.py --fullscreen --page-progress --mousedelay 500 --tracking --transtime 0 --duration 25m slides.pdf | tee timestats`date +"__%d-%m__%H:%M"`.txt
	# http://impressive.sourceforge.net/manual.php
