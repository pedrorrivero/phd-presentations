## ----------------------------------------------------------------------------
##    _____  _____
##   |  __ \|  __ \    AUTHOR: Pedro Rivero
##   | |__) | |__) |   ---------------------------------
##   |  ___/|  _  /    DATE: February 27, 2021
##   | |    | | \ \    ---------------------------------
##   |_|    |_|  \_\   https://github.com/pedrorrivero
##
## ----------------------------------------------------------------------------
## MIT License
##
## Copyright (c) 2021 Pedro Rivero Ramírez
##
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
##
## The above copyright notice and this permission notice shall be included in
## all copies or substantial portions of the Software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.
## ----------------------------------------------------------------------------
## Command line interface (CLI) → make <cmd> (* = requires templates repo)
##  • (auto): build document; running `make` defaults to this
##  • all: bib + auto + clean + version + zip
##  • bib: bibtool pass to .bib files
##  • clean: delete intermediate build files
##  • cleanall: clean + delete output files
##  • debug: debugger for auto command
##  • debib: debuger for bib command
##  • init: (*) initializes project, copying necessary files from templates repo
##  • uninit: (*) undoes init
##  • pull: (*) updates local files from templates repo
##  • push: (*) updates templates repo from local files
##  • publish: version + bib2bbl + zip + bbl2bib + extract in versions directory
##  • version: builds version-titled document and saves it to versions directory
##  • zip: zips all relevant files and saves it to versions directory
## ----------------------------------------------------------------------------
## User parameter choices
##  • MAINFILE: { Thesis, Paper, Article, Presentation, Poster, Coverletter }
##  • INSTANCE: Specific name of document for versions.
## 							Default := $(shell pwd | xargs basename | sed -E 's/^[0-9]+_//')
##  • OTHERS: Other files such as listings. Default := $(shell echo '')
##  • MAKE_DIR: Name of build directoy. Default := _make
##  • VERS_DIR: Name of versions directoy. Default := _versions
##  • TEMPLATES_REPO: Path to your own repo for pull/push or blank to skip.
##  • ENGINE: { pdflatex, xelatex }
##  • GIT: Creates .gitignore file. Default := TRUE
##  • VERBOSE: Default := TRUE
## ----------------------------------------------------------------------------
## ${TEMPLATES_REPO} - Internal structure (* = no pull)(+ = no push)
## ├── BIB
## ├── CLS
## ├── Content (*)(+)
## │   └── [01_Introduction.tex]
## ├── Figures
## │	 ├── _design (*)(+)
## │	 ├── _plot
## │	 │   ├── data (*)(+)
## │	 │   │   └── [example.json]
## │	 │   ├── plotters
## │	 │   └── [plot_*.py] (*)(+)
## │   └── [placeholders] (*)(+)
## ├── FONTS
## ├── LOGOS
## ├── MAKE
## ├── STY
## ├── TEX (*)
## ├── [LICENSE] (*)(+)
## └── [README.md] (*)(+)
## ----------------------------------------------------------------------------

## User parameters (To expand each time use '=': e.g. INSTANCE = $(DIR_NAME))
MAINFILE := Presentation
INSTANCE = $(shell echo $(DIR_NAME) | sed -E 's/^[0-9]+_//')

OTHERS := $(shell echo '')

MAKE_DIR := _make
VERS_DIR := _versions
TEMPLATES_REPO := ~/Documents/01_Academic/99_TEMPLATES/01_LATEX/

ENGINE := pdflatex
GIT := TRUE
VERBOSE := TRUE


## ----------------------------------------------------------------------------
## Definitions
## ----------------------------------------------------------------------------

## Commands (To expand each time use '=': e.g. for changing ${ENGINE} later)
COMPILE_BIB := "bibtex ./$(MAKE_DIR)/$(MAINFILE)"
COMPILE_TEX = "$(ENGINE) -output-directory='./$(MAKE_DIR)/' $(MAINFILE)"
GREP_DEBUG := grep --color -A 10 -B 25 -i -E 'Undefined|Info:|Warning:|Error:'

## Messages (To expand each time use '=': e.g. for using $@)
SUCCESSFUL_BIB = "\'$@\' successfully labeled and sorted"
SUCCESSFUL_BST := "bibtex pass completed..."
SUCCESSFUL_BUILD = "\'$@\' successfully built"
SUCCESSFUL_INIT := "\'$(MAINFILE)\' successfully initialized"
SUCCESSFUL_TEX = "$(ENGINE) pass completed..."
SUCCESSFUL_PULL := "successfully updated"
SUCCESSFUL_PUSH := "successfully copied to templates repository"

## Filesystem
DIR_NAME := $(shell basename ${PWD})
SERIAL_NAME := $(shell date +%y%m%d)_$(INSTANCE)
ZIP_NAME := $(SERIAL_NAME).zip
VERS_NAME := $(SERIAL_NAME).pdf
PUB_NAME := $(shell date +%y%m%d)P_$(INSTANCE)

CONTENT_DIR := Content
FIGURES_DIR := Figures
PLOTTERS_DIR := $(FIGURES_DIR)/_plot/plotters
LOGOS_DIR := LOGOS
FONTS_DIR := FONTS

FIGURES_REGEX = -name "[^.]*.*" -not -path "*/_*"
FIGURES := $(shell find $(FIGURES_DIR)/* $(FIGURES_REGEX) 2>/dev/null)
PLOTTERS_REGEX = -name "[^.]*.*" -not -path "*__pycache__*"
PLOTTERS := $(shell find $(PLOTTERS_DIR)/* $(PLOTTERS_REGEX) 2>/dev/null)
LOGOS := $(shell find $(LOGOS_DIR)/* -name "[^.]*.*" 2>/dev/null)
FONTS := $(shell find $(FONTS_DIR)/* -name "[^.]*.*" 2>/dev/null)
TEX := $(shell find . -name "*.tex")	# Regular (La)TeX files
CLS := $(shell find . -name "*.cls")	# Class files (in theory only one)
STY := $(shell find . -name "*.sty")	# Style files
BIB := $(shell find . -name "*.bib")	# Bibliography files
BST := $(shell find . -name "*.bst")	# Bibliography style files

IMAGES := $(shell echo $(FIGURES) $(LOGOS))
LATEX := $(shell echo $(TEX) $(CLS) $(STY) $(BIB) $(BST))
EXTRA := $(shell echo $(FONTS) $(OTHERS))

# Use double $ to escape variable expansion (i.e. $ → $$)
OUTPUT_REGEX := ^\./$(MAINFILE)\.((pdf)|(ps)|(dvi))$$
OUTPUT := $(shell find -E . -regex "$(OUTPUT_REGEX)" 2> /dev/null)

ZIP_REGEX := ^\.((.*/\..*)|(.*/_.*)|(.*/Makefile$$)|(.*\.zip$$)|
ZIP_REGEX += (/$(MAKE_DIR))|(/$(VERS_DIR)))
ZIPABLES = $(shell find . | grep -Ev "$(ZIP_REGEX)" | sort 2> /dev/null)

## Settings and default
ifeq ($(GIT),TRUE)
GITIGNORE := "echo '**.DS_Store\n**.venv*\n**__pycache__\n**$(MAKE_DIR)'"
GITIGNORE += " > .gitignore"
endif

ifeq ($(VERBOSE),FALSE)
# @command || true : avoids Make’s confusing warning that an error was ignored
.SILENT:
endif

ifeq ($(MAINFILE),Coverletter) # Force xelatex engine
ENGINE := xelatex
endif

.DEFAULT:
	@if [ $@ != 'Makefile' ]; then echo "[ ERROR ]  No rule found for '$@'..."; fi


## ----------------------------------------------------------------------------
## Document specific build
## ----------------------------------------------------------------------------

.PHONY: auto
auto: $(MAINFILE).pdf

Thesis.pdf: $(LATEX) $(IMAGES) $(EXTRA)
	@make clean 1> /dev/null	# Prevents non-zero return value issues with bibtex
	@-mkdir ${MAKE_DIR} 2>/dev/null || true
	@echo '------------ $(MAINFILE) ------------' | tr [:lower:] [:upper:]
	@eval $(COMPILE_TEX) &> /dev/null
	@mv -f ./${MAKE_DIR}/${MAINFILE}.idx ./
	@echo "[  TEX  ]  ${SUCCESSFUL_TEX}"
	@eval $(COMPILE_BIB) &> /dev/null
	@echo "[  BST  ]  ${SUCCESSFUL_BST}"
	@eval $(COMPILE_TEX) &> /dev/null
	@mv -f ./${MAKE_DIR}/${MAINFILE}.idx ./
	@echo "[  TEX  ]  ${SUCCESSFUL_TEX}"
	@eval $(COMPILE_TEX) &> /dev/null
	@mv -f ./${MAKE_DIR}/${MAINFILE}.idx ./
	@echo "[  TEX  ]  ${SUCCESSFUL_TEX}"
	@mv -f ./${MAINFILE}.i* ./${MAKE_DIR}/
	@mv -f ./${MAKE_DIR}/${MAINFILE}.pdf ./
	@echo "[  FILE ]  ${SUCCESSFUL_BUILD}"

Paper.pdf: $(LATEX) $(IMAGES) $(EXTRA)
	@make clean 1> /dev/null	# Prevents non-zero return value issues with bibtex
	@-mkdir ${MAKE_DIR} 2>/dev/null || true
	@echo '------------ $(MAINFILE) ------------' | tr [:lower:] [:upper:]
	@eval $(COMPILE_TEX) &> /dev/null
	@echo "[  TEX  ]  ${SUCCESSFUL_TEX}"
	@eval $(COMPILE_BIB) &> /dev/null
	@echo "[  BST  ]  ${SUCCESSFUL_BST}"
	@eval $(COMPILE_TEX) &> /dev/null
	@echo "[  TEX  ]  ${SUCCESSFUL_TEX}"
	@eval $(COMPILE_TEX) &> /dev/null
	@echo "[  TEX  ]  ${SUCCESSFUL_TEX}"
	@mv -f ./${MAKE_DIR}/${MAINFILE}.pdf ./
	@echo "[  FILE ]  ${SUCCESSFUL_BUILD}"

Article.pdf: $(LATEX) $(IMAGES) $(EXTRA)
	@make clean 1> /dev/null	# Prevents non-zero return value issues with bibtex
	@-mkdir ${MAKE_DIR} 2>/dev/null || true
	@echo '------------ $(MAINFILE) ------------' | tr [:lower:] [:upper:]
	@eval $(COMPILE_TEX) &> /dev/null
	@echo "[  TEX  ]  ${SUCCESSFUL_TEX}"
	@eval $(COMPILE_BIB) &> /dev/null
	@echo "[  BST  ]  ${SUCCESSFUL_BST}"
	@eval $(COMPILE_TEX) &> /dev/null
	@echo "[  TEX  ]  ${SUCCESSFUL_TEX}"
	@eval $(COMPILE_TEX) &> /dev/null
	@echo "[  TEX  ]  ${SUCCESSFUL_TEX}"
	@mv -f ./${MAKE_DIR}/${MAINFILE}.pdf ./
	@echo "[  FILE ]  ${SUCCESSFUL_BUILD}"

Presentation.pdf: $(LATEX) $(IMAGES) $(EXTRA)
	@make clean 1> /dev/null	# Prevents non-zero return value issues with bibtex
	@-mkdir ${MAKE_DIR} 2>/dev/null || true
	@echo '------------ $(MAINFILE) ------------' | tr [:lower:] [:upper:]
	@eval $(COMPILE_TEX) &> /dev/null
	@echo "[  TEX  ]  ${SUCCESSFUL_TEX}"
	@eval $(COMPILE_TEX) &> /dev/null
	@echo "[  TEX  ]  ${SUCCESSFUL_TEX}"
	@mv -f ./${MAKE_DIR}/${MAINFILE}.pdf ./
	@echo "[  FILE ]  ${SUCCESSFUL_BUILD}"

Poster.pdf: $(LATEX) $(IMAGES) $(EXTRA)
	@make clean 1> /dev/null	# Prevents non-zero return value issues with bibtex
	@-mkdir ${MAKE_DIR} 2>/dev/null || true
	@echo '------------ $(MAINFILE) ------------' | tr [:lower:] [:upper:]
	@eval $(COMPILE_TEX) &> /dev/null
	@echo "[  TEX  ]  ${SUCCESSFUL_TEX}"
	@eval $(COMPILE_BIB) &> /dev/null
	@echo "[  BST  ]  ${SUCCESSFUL_BST}"
	@eval $(COMPILE_TEX) &> /dev/null
	@echo "[  TEX  ]  ${SUCCESSFUL_TEX}"
	@eval $(COMPILE_TEX) &> /dev/null
	@echo "[  TEX  ]  ${SUCCESSFUL_TEX}"
	@mv -f ./${MAKE_DIR}/${MAINFILE}.pdf ./
	@echo "[  FILE ]  ${SUCCESSFUL_BUILD}"

Coverletter.pdf: $(LATEX) $(IMAGES) $(EXTRA)
	@make clean 1> /dev/null	# Prevents non-zero return value issues with bibtex
	@-mkdir ${MAKE_DIR} 2>/dev/null || true
	@echo '------------ $(MAINFILE) ------------' | tr [:lower:] [:upper:]
	@eval $(COMPILE_TEX) &> /dev/null
	@echo "[  TEX  ]  ${SUCCESSFUL_TEX}"
	@eval $(COMPILE_TEX) &> /dev/null
	@echo "[  TEX  ]  ${SUCCESSFUL_TEX}"
	@mv -f ./${MAKE_DIR}/${MAINFILE}.pdf ./
	@echo "[  FILE ]  ${SUCCESSFUL_BUILD}"


## ----------------------------------------------------------------------------
## Phony formulae → can be set to trigger as an order-only prerequisite
## ----------------------------------------------------------------------------

.PHONY: all
all: bib auto clean version zip

.PHONY: bib
bib:
	@echo '------------ BIBTEX ------------'
	@make -B $(BIB)	# Unconditionally make all targets (always make)

.PHONY: clean
clean:
	@echo '------------ CLEAN ------------'
	@-rm -rf ./${MAKE_DIR}/
	@echo "[  DIR  ]  Build directory successfully cleaned"

.PHONY: cleanall
cleanall: clean
	@-rm -f $(OUTPUT)
	@echo "[ FILES ]  Output successfully removed"

.PHONY: debug
debug:
	@echo '------------ DEBUG ------------'
	@echo "Type  R <return>  for running."
	@echo "Type  H <return>  for immediate help."
	@echo "Type  X <return>  for exiting."
	@echo '-------------------------------'
	@sleep 2
	@-eval $(COMPILE_TEX) | $(GREP_DEBUG)

.PHONY: debib	# Debug bib
debib:
	@echo '------------ DEBIB ------------'
	@echo "Type  R <return>  for running."
	@echo "Type  H <return>  for immediate help."
	@echo "Type  X <return>  for exiting."
	@echo '-------------------------------'
	@sleep 2
	@-eval $(COMPILE_BIB) | $(GREP_DEBUG)

.PHONY: publish
publish: $(VERS_DIR)/$(PUB_NAME)

${VERS_DIR}/${PUB_NAME}.pdf: $(MAINFILE).pdf
	@make version
	@mv ${VERS_DIR}/${VERS_NAME} ${VERS_DIR}/${PUB_NAME}.pdf
	@echo "[  FILE ]  '${VERS_DIR}/${PUB_NAME}.pdf' succesfully renamed"

${VERS_DIR}/${PUB_NAME}.zip: $(ZIPABLES)
	@make bib2bbl
	@make zip
	@mv ${VERS_DIR}/${ZIP_NAME} ${VERS_DIR}/${PUB_NAME}.zip
	@echo "[  FILE ]  '${VERS_DIR}/${PUB_NAME}.zip' succesfully renamed"
	@make bbl2bib

${VERS_DIR}/${PUB_NAME}: $(VERS_DIR)/$(PUB_NAME).pdf $(VERS_DIR)/$(PUB_NAME).zip
	@echo '------------ PUBLISH ------------'
	@-rm -rf $@ 2> /dev/null
	@-mkdir -p $@ 2>/dev/null || true
	@unzip -q ${VERS_DIR}/${PUB_NAME}.zip -d $@ 2>/dev/null
	@echo "[  DIR  ]  ${SUCCESSFUL_BUILD}"

.PHONY: bib2bbl
bib2bbl: $(MAINFILE).pdf
	@cp ${MAKE_DIR}/*.bbl ./ 2>/dev/null
	@mv ./*.bib ${MAKE_DIR}

.PHONY: bbl2bib
bbl2bib:
	@-rm -f ./*.bbl 2>/dev/null
	@mv ${MAKE_DIR}/*.bib ./

.PHONY: version
version: $(VERS_DIR)/$(VERS_NAME)

${VERS_DIR}/${VERS_NAME}: $(MAINFILE).pdf
	@-mkdir ${VERS_DIR} 2>/dev/null || true
	@-cp -f ${MAINFILE}.pdf ./$@
	@echo '------------ VERSION ------------'
	@echo "[  FILE ]  ${SUCCESSFUL_BUILD}"

.PHONY: zip
zip: $(VERS_DIR)/$(ZIP_NAME)

${VERS_DIR}/${ZIP_NAME}: $(ZIPABLES)
	@echo '------------ ZIP ------------'
	@-rm -f $@ 2> /dev/null
	@zip $@ $(ZIPABLES)
	@echo "[  FILE ]  ${SUCCESSFUL_BUILD}"


## ----------------------------------------------------------------------------
## Init, uninit, pull (update), and push (save) functionality
## ----------------------------------------------------------------------------

ifdef TEMPLATES_REPO

.PHONY: init
ifeq ($(MAINFILE),Thesis)
init:
	@-cp ${TEMPLATES_REPO}/TEX/Thesis.tex ./
	@-mkdir ./${CONTENT_DIR} 2>/dev/null || true
	@-cp -r ${TEMPLATES_REPO}/${CONTENT_DIR} ./
	@-mkdir ./${FIGURES_DIR} 2>/dev/null || true
	@-cp -r ${TEMPLATES_REPO}/${FIGURES_DIR} ./
	@-mkdir ./${LOGOS_DIR} 2>/dev/null || true
	@-cp -r ${TEMPLATES_REPO}/${LOGOS_DIR} ./
	@-cp ${TEMPLATES_REPO}/CLS/ThesisPR.cls ./
	@-cp ${TEMPLATES_REPO}/STY/PRMath.sty ./
	@-cp ${TEMPLATES_REPO}/STY/PRTools.sty ./
	@-cp ${TEMPLATES_REPO}/BIB/PR.bib ./
	@-cp ${TEMPLATES_REPO}/BIB/PRbib.bst ./
	@-cp ${TEMPLATES_REPO}/LICENSE ./
	@-cp ${TEMPLATES_REPO}/README.md ./
	@-eval $(GITIGNORE)
	@echo "[  INIT ]  $(SUCCESSFUL_INIT)"

else ifeq ($(MAINFILE),Paper)
init:
	@-cp ${TEMPLATES_REPO}/TEX/Paper.tex ./
	@-mkdir ./${CONTENT_DIR} 2>/dev/null || true
	@-cp -r ${TEMPLATES_REPO}/${CONTENT_DIR} ./
	@-mkdir ./${FIGURES_DIR} 2>/dev/null || true
	@-cp -r ${TEMPLATES_REPO}/${FIGURES_DIR} ./
	@-cp ${TEMPLATES_REPO}/STY/PRMath.sty ./
	@-cp ${TEMPLATES_REPO}/STY/PRTools.sty ./
	@-cp ${TEMPLATES_REPO}/BIB/PR.bib ./
	@-cp ${TEMPLATES_REPO}/LICENSE ./
	@-cp ${TEMPLATES_REPO}/README.md ./
	@-eval $(GITIGNORE)
	@echo "[  INIT ]  $(SUCCESSFUL_INIT)"

else ifeq ($(MAINFILE),Article)
init:
	@-cp ${TEMPLATES_REPO}/TEX/Article.tex ./
	@-mkdir ./${CONTENT_DIR} 2>/dev/null || true
	@-cp -r ${TEMPLATES_REPO}/${CONTENT_DIR} ./
	@-mkdir ./${FIGURES_DIR} 2>/dev/null || true
	@-cp -r ${TEMPLATES_REPO}/${FIGURES_DIR} ./
	@-mkdir ./${LOGOS_DIR} 2>/dev/null || true
	@-cp -r ${TEMPLATES_REPO}/${LOGOS_DIR} ./
	@-cp ${TEMPLATES_REPO}/CLS/ArticlePR.cls ./
	@-cp ${TEMPLATES_REPO}/STY/PRMath.sty ./
	@-cp ${TEMPLATES_REPO}/STY/PRTools.sty ./
	@-cp ${TEMPLATES_REPO}/BIB/PR.bib ./
	@-cp ${TEMPLATES_REPO}/BIB/PRbib-seq.bst ./
	@-cp ${TEMPLATES_REPO}/LICENSE ./
	@-cp ${TEMPLATES_REPO}/README.md ./
	@-eval $(GITIGNORE)
	@echo "[  INIT ]  $(SUCCESSFUL_INIT)"

else ifeq ($(MAINFILE),Presentation)
init:
	@-cp ${TEMPLATES_REPO}/TEX/Presentation.tex ./
	@-mkdir ./${CONTENT_DIR} 2>/dev/null || true
	@-cp -r ${TEMPLATES_REPO}/${CONTENT_DIR} ./
	@-mkdir ./${FIGURES_DIR} 2>/dev/null || true
	@-cp -r ${TEMPLATES_REPO}/${FIGURES_DIR} ./
	@-mkdir ./${LOGOS_DIR} 2>/dev/null || true
	@-cp -r ${TEMPLATES_REPO}/${LOGOS_DIR} ./
	@-cp ${TEMPLATES_REPO}/STY/beamerthemePRwide.sty ./
	@-cp ${TEMPLATES_REPO}/STY/PRMath.sty ./
	@-cp ${TEMPLATES_REPO}/STY/PRTools.sty ./
	@-cp ${TEMPLATES_REPO}/LICENSE ./
	@-cp ${TEMPLATES_REPO}/README.md ./
	@-eval $(GITIGNORE)
	@echo "[  INIT ]  $(SUCCESSFUL_INIT)"

else ifeq ($(MAINFILE),Poster)
init:
	@-cp ${TEMPLATES_REPO}/TEX/Poster.tex ./
	@-mkdir ./${FIGURES_DIR} 2>/dev/null || true
	@-cp -r ${TEMPLATES_REPO}/${FIGURES_DIR} ./
	@-mkdir ./${LOGOS_DIR} 2>/dev/null || true
	@-cp -r ${TEMPLATES_REPO}/${LOGOS_DIR} ./
	@-cp ${TEMPLATES_REPO}/STY/beamerposter.sty ./
	@-cp ${TEMPLATES_REPO}/STY/beamerthemeconfposter.sty ./
	@-cp ${TEMPLATES_REPO}/STY/PRMath.sty ./
	@-cp ${TEMPLATES_REPO}/STY/PRTools.sty ./
	@-cp ${TEMPLATES_REPO}/LICENSE ./
	@-cp ${TEMPLATES_REPO}/README.md ./
	@-eval $(GITIGNORE)
	@echo "[  INIT ]  $(SUCCESSFUL_INIT)"


else ifeq ($(MAINFILE),Coverletter)
init:
	@-cp ${TEMPLATES_REPO}/TEX/Coverletter.tex ./
	@-mkdir ./${CONTENT_DIR} 2>/dev/null || true
	@-cp -r ${TEMPLATES_REPO}/${CONTENT_DIR} ./
	@-mkdir ./${FIGURES_DIR} 2>/dev/null || true
	@-cp -r ${TEMPLATES_REPO}/${FIGURES_DIR} ./
	@-mkdir ./${LOGOS_DIR} 2>/dev/null || true
	@-cp -r ${TEMPLATES_REPO}/${LOGOS_DIR} ./
	@-mkdir ./${FONTS_DIR} 2>/dev/null || true
	@-cp -r ${TEMPLATES_REPO}/${FONTS_DIR} ./
	@-cp ${TEMPLATES_REPO}/CLS/awesome-cv.cls ./
	@-cp ${TEMPLATES_REPO}/STY/fontawesome.sty ./
	@-cp ${TEMPLATES_REPO}/LICENSE ./
	@-cp ${TEMPLATES_REPO}/README.md ./
	@-eval $(GITIGNORE)
	@echo "[  INIT ]  $(SUCCESSFUL_INIT)"

else
init:
	@echo "[ ERROR ]  INIT not defined for '$(MAINFILE)'..."

endif

## ----------------------------------------------------------------------------

.PHONY: uninit
uninit:
	@find . -not -name 'Makefile' -delete
	@echo "[  INIT ]  Directory successfully un-initialized"

## ----------------------------------------------------------------------------

.PHONY: pull
pull:
	@echo '------------ PULL ------------'
	@cp ${TEMPLATES_REPO}/MAKE/Makefile ./
	@echo "[  FILE ]  'Makefile' ${SUCCESSFUL_PULL}"
	@-if [ ! -z "${LOGOS}" ];\
		then cp -r ${TEMPLATES_REPO}/${LOGOS_DIR} ./ 2>/dev/null;\
		echo "[  DIR  ]  '${LOGOS_DIR}' ${SUCCESSFUL_PULL}"; fi
	@-if [ ! -z "${FONTS}" ];\
		then cp -r ${TEMPLATES_REPO}/${FONTS_DIR} ./ 2>/dev/null;\
		echo "[  DIR  ]  '${FONTS_DIR}' ${SUCCESSFUL_PULL}"; fi
	@for file in ${CLS}; do cp ${TEMPLATES_REPO}/CLS/$${file} ./$${file} \
		2>/dev/null; echo "[  FILE ]  '$${file}' ${SUCCESSFUL_PULL}"; done
	@for file in $(STY); do cp ${TEMPLATES_REPO}/STY/$${file} ./$${file} \
		2>/dev/null; echo "[  FILE ]  '$${file}' ${SUCCESSFUL_PULL}"; done
	@for file in $(BIB); do cp ${TEMPLATES_REPO}/BIB/$${file} ./$${file} \
		2>/dev/null; echo "[  FILE ]  '$${file}' ${SUCCESSFUL_PULL}"; done
	@for file in $(BST); do cp ${TEMPLATES_REPO}/BIB/$${file} ./$${file} \
		2>/dev/null; echo "[  FILE ]  '$${file}' ${SUCCESSFUL_PULL}"; done
	@for file in ${PLOTTERS}; do cp ${TEMPLATES_REPO}/$${file} ./$${file} \
		2>/dev/null; echo "[  FILE ]  '$${file}' ${SUCCESSFUL_PULL}"; done

## ----------------------------------------------------------------------------

.PHONY: push
push:
	@echo '------------ PUSH ------------'
	@-mkdir ${TEMPLATES_REPO}/MAKE 2>/dev/null || true
	@cp Makefile ${TEMPLATES_REPO}/MAKE
	@echo "[  FILE ]  'Makefile' ${SUCCESSFUL_PUSH}"
	@-if [ ! -z "${LOGOS}" ];\
		then mkdir ${TEMPLATES_REPO}/${LOGOS_DIR} 2>/dev/null;\
		cp -r ./${LOGOS_DIR} ${TEMPLATES_REPO}/;\
		echo "[  DIR  ]  '${LOGOS_DIR}' ${SUCCESSFUL_PUSH}";\
		fi
	@-if [ ! -z "${FONTS}" ];\
		then mkdir ${TEMPLATES_REPO}/${FONTS_DIR} 2>/dev/null;\
		cp -r ./${FONTS_DIR} ${TEMPLATES_REPO}/;\
		echo "[  DIR  ]  '${FONTS_DIR}' ${SUCCESSFUL_PUSH}";\
		fi
	@-mkdir ${TEMPLATES_REPO}/TEX 2>/dev/null || true
	@cp ${MAINFILE}.tex ${TEMPLATES_REPO}/TEX
	@echo "[  FILE ]  '${MAINFILE}.tex' ${SUCCESSFUL_PUSH}"
	@make -B $(CLS) $(STY) $(BIB) $(BST) $(PLOTTERS) # Unconditionally make

# ${LOGOS}:
# 	@-mkdir ${TEMPLATES_REPO}/${LOGOS_DIR} 2>/dev/null
# 	@cp $@ ${TEMPLATES_REPO}/$@
# 	@echo "[FILE]:\t '$@' ${SUCCESSFUL_PUSH}"
#
# ${FONTS}:
# 	@-mkdir ${TEMPLATES_REPO}/${FONTS_DIR} 2>/dev/null
# 	@cp $@ ${TEMPLATES_REPO}/$@
# 	@echo "[FILE]:\t '$@' ${SUCCESSFUL_PUSH}"

${CLS}:
	@-mkdir ${TEMPLATES_REPO}/CLS 2>/dev/null || true
	@cp $@ ${TEMPLATES_REPO}/CLS
	@echo "[  FILE ]  '$@' ${SUCCESSFUL_PUSH}"

${STY}:
	@-mkdir ${TEMPLATES_REPO}/STY 2>/dev/null || true
	@cp $@ ${TEMPLATES_REPO}/STY
	@echo "[  FILE ]  '$@' ${SUCCESSFUL_PUSH}"

${BIB}:
	@bibtool --ignored.word{and} --ignored.word{or} --ignored.word{of} \
		--ignored.word{to} --ignored.word{for} --ignored.word{in} \
		--ignored.word{on} --ignored.word{at} --ignored.word{from} \
		--ignored.word{y} --ignored.word{o} --ignored.word{de} \
		--ignored.word{a} --ignored.word{para} --ignored.word{por} \
		--ignored.word{en} --ignored.word{sobre} --ignored.word{desde} \
		-f "%+n(author):%4D(year):%-4T(title)" -s $@ -o $@
	@echo "[  BIB  ]  ${SUCCESSFUL_BIB}"
	@-mkdir ${TEMPLATES_REPO}/BIB 2>/dev/null || true
	@cp $@ ${TEMPLATES_REPO}/BIB
	@echo "[  FILE ]  '$@' ${SUCCESSFUL_PUSH}"

${BST}:
	@-mkdir ${TEMPLATES_REPO}/BIB 2>/dev/null || true
	@cp $@ ${TEMPLATES_REPO}/BIB
	@echo "[  FILE ]  '$@' ${SUCCESSFUL_PUSH}"

${PLOTTERS}:
	@-mkdir -p ${TEMPLATES_REPO}/${PLOTTERS_DIR} 2>/dev/null || true
	@cp $@ ${TEMPLATES_REPO}/$@
	@echo "[  FILE ]  '$@' ${SUCCESSFUL_PUSH}"

else

${BIB}:
	@bibtool --ignored.word{and} --ignored.word{or} --ignored.word{of} \
		--ignored.word{to} --ignored.word{for} --ignored.word{in} \
		--ignored.word{on} --ignored.word{at} --ignored.word{from} \
		--ignored.word{y} --ignored.word{o} --ignored.word{de} \
		--ignored.word{a} --ignored.word{para} --ignored.word{por} \
		--ignored.word{en} --ignored.word{sobre} --ignored.word{desde} \
		-f "%+n(author):%4D(year):%-4T(title)" -s $@ -o $@
	@echo "[  BIB  ]  ${SUCCESSFUL_BIB}"

endif
