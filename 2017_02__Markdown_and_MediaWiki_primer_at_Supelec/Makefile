# Quick Makefile to easily compile the slides (make pdf) and run the slide (make showtime)
default: showtime


theme = sky
theme = league

reveal-md:
	reveal-md --theme $(theme) --title "GouTP @ SCEE |  Date: 23 Feb 2017  |  By: Lilian Besson  | About: Markdown & MediaWiki" slides_reveal.md

pandocpdf:
	pandoc -N -s --template=../my.beamer -t beamer slides_pandoc.md -o slides_pandoc.pdf
	xdg-open slides_pandoc.pdf &

Marp:
	Marp slides_marp.md

typora:
	typora document_typora.md

showtime:	slides
slides:
	#-gmusicbrowser -cmd Pause  # Just to make sure your music player is NOT playing when you start your talk
	@echo "Using Impressive.py (from http://impressive.sourceforge.net/)"
	impressive.py --fullscreen --page-progress --mousedelay 500 --tracking --transtime 0 --duration 25m slides_pandoc.pdf | tee timestats`date +"__%d-%m__%H:%M"`.txt
	# http://impressive.sourceforge.net/manual.php
