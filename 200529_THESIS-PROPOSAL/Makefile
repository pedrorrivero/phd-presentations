#    _____  _____
#   |  __ \|  __ \    AUTHOR: Pedro Rivero
#   | |__) | |__) |   ---------------------------------
#   |  ___/|  _  /    DATE: April 26, 2020
#   | |    | | \ \    ---------------------------------
#   |_|    |_|  \_\   https://github.com/pedrorrivero
#

## User interface, just set the main filename and it will do everything for you.
# You can choose the engine for compilation. Default: pdflatex/xelatex.
# Figures/logos must be placed in the Figures/Logos direrctories. These are
# searched excluding any hidden files.
# If you have any extra files such as listings include them in EXTRA.

ENGINE = pdflatex
# ENGINE = xelatex

MAINFILE = Presentation
IMAGES := $(shell find Figures/* LOGOS/* -name "[^/.]*.*")
EXTRA := $(shell echo '')
MAKE_DIR = make

## Commands
COMPILE_TEX = "${ENGINE} -output-directory='./${MAKE_DIR}/' ${MAINFILE}"
COMPILE_BIB = "bibtex ./${MAKE_DIR}/${MAINFILE}"


## Filesystem
TEX = $(shell find . -name "*.tex")	# Regular (La)TeX files
STY = $(shell find . -name "*.sty")	# Style files
CLS = $(shell find . -name "*.cls")	# Class files (in theory only one)
BIB = $(shell find . -name "*.bib")	# Bibliography files
BST = $(shell find . -name "*.bst")	# Bib. style files

LATEX = $(shell echo $(TEX) $(STY) $(CLS) $(BIB) $(BST))

## Formulae
$(MAINFILE).pdf: $(LATEX) $(IMAGES) $(EXTRA)
	@mkdir ${MAKE_DIR} 2>/dev/null
	@echo '----------- BUILD -----------'
	@eval $(COMPILE_TEX) &> /dev/null
	@echo "Initial ${ENGINE} pass completed..."
	@eval $(COMPILE_TEX) &> /dev/null
	@echo "Final ${ENGINE} pass completed..."
	@mv -f ./${MAKE_DIR}/*.pdf ./
	@echo "SUCCES! File '$@' moved to parent directory"

$(BIB):
	@bibtool --ignored.word{and} --ignored.word{or} --ignored.word{of} \
		--ignored.word{to} --ignored.word{for} --ignored.word{in} \
		--ignored.word{on} --ignored.word{at} --ignored.word{from} \
		--ignored.word{y} --ignored.word{o} --ignored.word{de} \
		--ignored.word{a} --ignored.word{para} --ignored.word{por} \
		--ignored.word{en} --ignored.word{sobre} --ignored.word{desde} \
		-f "%+n(author):%4D(year):%-4T(title)" -s $@ -o $@
	@echo "Bibtex file '$@' correctly labeled and sorted"

.PHONY: all
all: bib $(MAINFILE).pdf clean

.PHONY: bib
bib:
	@echo '----------- BIBTEX -----------'
	@make -B $(BIB)	# Unconditionally make all targets

.PHONY: clean
clean:
	@echo '----------- CLEAN -----------'
	-rm -rf ./${MAKE_DIR}/

.PHONY: cleanall
cleanall: clean
	-rm -f *.pdf
	-rm -f *.ps
	-rm -f *.dvi

.PHONY: debug
debug:
	@echo '----------- DEBUG -----------'
	@echo "Type  R <return>  for running."
	@echo "Type  H <return>  for immediate help."
	@echo "Type  X <return>  for exiting."
	@echo '-----------------------------'
	@sleep 2
	@-eval $(COMPILE_TEX) | grep -A 25 -B 5 -i -E 'Info:|Warning:|Error:'

.PHONY: debib	# Debug bib
debib:
	@echo '----------- DEBIB -----------'
	@echo "Type  R <return>  for running."
	@echo "Type  H <return>  for immediate help."
	@echo "Type  X <return>  for exiting."
	@echo '-----------------------------'
	@sleep 2
	@-eval $(COMPILE_BIB) | grep -A 25 -B 5 -i -E 'Info:|Warning:|Error:'
