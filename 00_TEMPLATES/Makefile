#    _____  _____
#   |  __ \|  __ \    AUTHOR: Pedro Rivero
#   | |__) | |__) |   ---------------------------------
#   |  ___/|  _  /    DATE: February 27, 2020
#   | |    | | \ \    ---------------------------------
#   |_|    |_|  \_\   https://github.com/pedrorrivero
#

## User interface, just set the main filename and it will do everything for you.
# You can choose the engine for compilation. Default: pdflatex/xelatex
# If you have any extra code or images included list them in EXTRA_FILES.
# This should work as long as you have all the .tex, .sty, .cls and .bib files
# in the same folder.

ENGINE = pdflatex
# ENGINE = xelatex

MAINFILE = main
EXTRA_FILES := $(shell echo Figures/*)
MAKE_DIR = make
TEMP := $(shell mkdir ${MAKE_DIR} 2>/dev/null)

## Inner workings
TEX = $(shell echo *.tex)
STY = $(shell echo *.sty)
# CLS = $(shell echo *.cls)
BIB = $(shell echo *.bib)

TRACKERS = $(shell echo $(TEX) $(STY) $(CLS))

# .PHONY: all
# all: $(MAINFILE).pdf

$(MAINFILE).pdf: $(TRACKERS) $(EXTRA_FILES)
	@echo '----------- BUILD -----------'
	@eval ${ENGINE} -output-directory='./${MAKE_DIR}/' ${MAINFILE} 1> /dev/null
		@echo "Initial ${ENGINE} pass completed..."
	@eval bibtex ./${MAKE_DIR}/${MAINFILE}.aux 1> /dev/null
		@echo "Bibtex pass completed..."
	@eval ${ENGINE} -output-directory='./${MAKE_DIR}/' ${MAINFILE} 1> /dev/null
	@eval ${ENGINE} -output-directory='./${MAKE_DIR}/' ${MAINFILE} 1> /dev/null
		@echo "Final ${ENGINE} passes (x2) completed..."
	@mv -f ./${MAKE_DIR}/*.pdf ./
		@echo "SUCCES! $@ moved to parent directory"

# .PHONY: push
# push: $(MAINFILE).pdf
# 	@echo '----------------------'
# 	git push origin master

.PHONY: debug
debug:
	@echo '----------- DEBUG -----------'
	@echo "Type  R <return>  for running."
	@echo "Type  H <return>  for immediate help."
	@echo "Type  X <return>  for exiting."
	@echo '-----------------------------'
	@sleep 2
	@-eval ${ENGINE} -output-directory='./${MAKE_DIR}/' ${MAINFILE} | \
		grep -A 25 -B 5 -i -E 'Info:|Warning:|Error:'

.PHONY: clean
clean:
	@echo '----------- CLEAN -----------'
	-rm -rf ./${MAKE_DIR}/

.PHONY: cleanall
cleanall: clean
	-rm -f *.pdf
	-rm -f *.ps
	-rm -f *.dvi
