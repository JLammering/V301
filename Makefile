ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  # Unix
  pwd := $$(pwd)
  translate = $1
else
  # Windows mit MSys2/Cygwin
  pwd := $$(cygpath -m "$$(pwd)")
  translate = $(shell echo '$1' | sed 's/:/;/g')
endif

all: build/main.pdf

# hier Python-Skripte:
build/plot1.pdf: plot1.py matplotlibrc header-matplotlib.tex V301Daten1.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python plot1.py

build/plot2.pdf: plot2.py matplotlibrc header-matplotlib.tex V301Daten2.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python plot2.py

build/plot3a.pdf: plot3a.py matplotlibrc header-matplotlib.tex V301Daten3a.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python plot3a.py

build/plot3b.pdf: plot3b.py matplotlibrc header-matplotlib.tex V301Daten3b.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python plot3b.py

build/plot5.pdf: plot5.py matplotlibrc header-matplotlib.tex V301Daten1.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python plot5.py


# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot1.pdf build/plot2.pdf build/plot3a.pdf build/plot3b.pdf build/plot5.pdf content/Auswertung.tex content/theorie.tex content/durchfuehrung.tex content/diskussion.tex

build/main.pdf: FORCE | build
	  TEXINPUTS="$(call translate,build:)" \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
