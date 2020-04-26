# Author: Pedro Rivero
# Date:		October 22, 2019

## User interface, just set the main filename and it will do everything for you
# If you have any extra code or images included list them in EXTRA_FILES
# This should work as long as you have all the .tex, .sty and .bib files in
# the same folder.

TEMP2 := $(shell mkdir make 2>/dev/null)

MAINFILE = presentation
EXTRA_FILES := $(shell echo LOGOS/* Figures/*)
# EXTRA_FILES := $(shell echo LOGOS/*)
MAKE_DIR = make

## Inner workings
TEX = $(shell echo *.tex)
STY = $(shell echo *.sty)

TRACKERS = $(shell echo $(TEX) $(STY))

# .PHONY: all
# all: $(MAINFILE).pdf

$(MAINFILE).pdf: $(TRACKERS) $(EXTRA_FILES)
	@echo '----------------------'
	@pdflatex -output-directory='./${MAKE_DIR}/' $(MAINFILE) 1> /dev/null
		@echo 'First pdflatex pass completed...'
	@pdflatex -output-directory='./${MAKE_DIR}/' $(MAINFILE) 1> /dev/null
		@echo 'Second pdflatex pass completed...'
	@mv -f ./${MAKE_DIR}/*.pdf ./
		@echo 'SUCCES! $@ moved to parent directory'
	@echo '----------------------'

# .PHONY: push
# push: $(MAINFILE).pdf
# 	@echo '----------------------'
# 	git push origin master
# 	@echo '----------------------'

.PHONY: clean
clean:
	@echo '----------------------'
	-rm -f ${MAKE_DIR}/*
	@echo '----------------------'

.PHONY: cleanall
cleanall: clean
	-rm -f *.pdf
	-rm -f *.ps
	-rm -f *.dvi
	-rm -rf ./${MAKE_DIR}/
	@echo '----------------------'
