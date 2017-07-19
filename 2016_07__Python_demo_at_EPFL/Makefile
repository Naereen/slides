reveal-md:
	# reveal-md --theme sky --title "Python tutorial for Deep Learning @ BIG (EPFL)" slides_reveal.md
	reveal-md --theme league --title "Python tutorial for Deep Learning @ BIG (EPFL)" slides_reveal.md

pandocpdf:
	pandoc --variable=aspectratio:43 -N -s --template=../my.beamer -t beamer slides_pandoc.md -o slides_pandoc.pdf
	xdg-open slides_pandoc.pdf &

pandocpdf169:
	pandoc --variable=aspectratio:169 -N -s --template=../my.beamer -t beamer slides_pandoc.md -o slides_pandoc_169.pdf
	xdg-open slides_pandoc_169.pdf &
