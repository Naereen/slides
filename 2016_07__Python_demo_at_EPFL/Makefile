reveal-md:
	# reveal-md --theme sky --title "Python tutorial for Deep Learning @ BIG (EPFL)" slides_reveal.md
	reveal-md --theme league --title "Python tutorial for Deep Learning @ BIG (EPFL)" slides_reveal.md

pandocpdf:
	pandoc -s --template=my.beamer -t beamer slides_pandoc.md -o slides_pandoc.pdf
	xdg-open slides_pandoc.pdf &
