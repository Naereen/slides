theme = sky
theme = league

reveal-md:
	reveal-md --theme $(theme) --title "GouTP @ SCEE |  Date: 23 Feb 2017  |  By: Lilian Besson  | About: Markdown & MediaWiki" slides_reveal.md

pandocpdf:
	pandoc -N -s --template=../my.beamer -t beamer slides_pandoc.md -o slides_pandoc.pdf
	xdg-open slides_pandoc.pdf &
