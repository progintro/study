# Build the downloadable artifacts from chapters/*/README.md and questions/:
#
#   build/NN-slug.pdf        one PDF per chapter (mermaid diagrams rendered by
#                            tools/mermaid.py into build/mermaid/, cached by hash)
#   build/study.pdf          the whole book: cover, contents, parts, question bank
#   build/study-md.zip       the Markdown sources
#   build/questions.json     the question bank, for tools and agents
#   build/llms.txt           index for agents; build/llms-full.txt the whole guide as
#                            one Markdown file
#
# pandoc and xelatex run in the same pinned image as notes and lab-material, so the
# course sites typeset identically. `make PANDOC="pandoc"` runs a local pandoc
# instead (needs xelatex and the fonts below).
#
# `make fetch` downloads the lecture slides and homework PDFs the chapters and the
# question bank were written from (sources/slides/, sources/hw/; not committed).

BUILD ?= build
IMAGE ?= ghcr.io/ethan42/pandoctex:20260825
PANDOC ?= docker run --rm --tmpfs /tmp:size=2g -u $(shell id -u):$(shell id -g) -v $(CURDIR):/data -w /data \
	-e LANG=C.UTF-8 -e HOME=/tmp $(IMAGE) pandoc
REPO ?= progintro/progintro.github.io

CHAPTERS := $(sort $(wildcard chapters/*/README.md))
QUESTIONS := $(sort $(wildcard questions/*/*.md))
SLUGS := $(patsubst chapters/%/README.md,%,$(CHAPTERS))
CHAPTER_PDFS := $(SLUGS:%=$(BUILD)/%.pdf)
FIGURES := $(wildcard figures/*.pdf)
DEPS := tex/header.tex tex/table-widths.lua tools/pdf-prep.py tools/mermaid.py $(FIGURES)

# The same typesetting flags for every PDF. -V babel-lang= and the \babelprovide in
# tex/header.tex work around pandoc 3.7's babel wiring; see lab-material/CLAUDE.md.
# tex/table-widths.lua makes table columns wrap instead of running off the page.
PDF_FLAGS = -f gfm+tex_math_dollars+raw_attribute -s --toc --lua-filter=tex/table-widths.lua \
	--pdf-engine=xelatex -H tex/header.tex \
	-V mainfont="Linux Libertine O" -V monofont="Noto Mono" -V fontsize=12pt \
	-V lang=el -V babel-lang= \
	-V colorlinks=true -V linkcolor=ditcharcoal -V urlcolor=ditcyan -V toccolor=ditcharcoal

all: $(CHAPTER_PDFS) $(BUILD)/study.pdf $(BUILD)/study-md.zip $(BUILD)/llms.txt

$(BUILD):
	mkdir -p $(BUILD)

# The running header carries the chapter title, without its "Κεφάλαιο N:" prefix and
# with LaTeX's special characters escaped ("Ροή Ελέγχου #2").
$(BUILD)/%.pdf: chapters/%/README.md $(DEPS) | $(BUILD)
	python3 tools/mermaid.py
	python3 tools/pdf-prep.py $< > $(BUILD)/$*.md
	$(PANDOC) $(BUILD)/$*.md $(PDF_FLAGS) --toc-depth=2 \
		-V header-includes='\def\chaptitle{$(shell grep -m1 '^# ' $< | sed -e 's/^# //' -e 's/^[^:]*: //' -e 's/[#&%$$_]/\\&/g')}' \
		-o $@

$(BUILD)/questions.json $(BUILD)/questions.md: $(QUESTIONS) sources/manifest.yaml tools/gen-exercises.py | $(BUILD)
	python3 tools/gen-exercises.py --check --build $(BUILD)

$(BUILD)/study.pdf: $(CHAPTERS) $(DEPS) tex/book.tex glossary.md $(BUILD)/questions.md | $(BUILD)
	python3 tools/mermaid.py
	python3 tools/pdf-prep.py --all > $(BUILD)/study.md
	$(PANDOC) $(BUILD)/study.md $(PDF_FLAGS) --toc-depth=1 --top-level-division=chapter \
		-V documentclass=report -H tex/book.tex \
		-V header-includes='\def\chaptitle{Οδηγός Μελέτης}' \
		-o $@

$(BUILD)/study-md.zip: $(CHAPTERS) $(QUESTIONS) | $(BUILD)
	rm -f $@
	zip -q -r $@ README.md glossary.md chapters questions $(wildcard figures)

$(BUILD)/llms.txt: $(CHAPTERS) glossary.md $(BUILD)/questions.md tools/llms.py tools/pdf-prep.py | $(BUILD)
	python3 tools/pdf-prep.py --all --plain > $(BUILD)/llms-full.txt
	python3 tools/llms.py > $@

.PHONY: all fetch lint check-code exercises check clean
fetch:
	mkdir -p sources/slides sources/hw/2023 sources/hw/2024 sources/hw/2025
	gh release download 2025 -R $(REPO) -D sources/slides -p 'lec*.pdf' -p make.pdf --skip-existing
	gh release download 2025 -R $(REPO) -D sources/hw/2025 -p 'hw*.pdf' -p stergios.pdf --skip-existing
	gh release download 2024 -R $(REPO) -D sources/hw/2024 -p 'hw*.pdf' --skip-existing
	gh release download 2023 -R $(REPO) -D sources/hw/2023 -p 'hw*.pdf' --skip-existing

lint:
	python3 tools/lint.py --strict
	python3 tools/gen-exercises.py --lint

check-code:
	python3 tools/check-code.py

exercises:
	python3 tools/gen-exercises.py
	python3 tools/gen-glossary.py

check: lint check-code
	python3 tools/gen-exercises.py --check
	python3 tools/gen-glossary.py --check

clean:
	rm -rf $(BUILD) _site
