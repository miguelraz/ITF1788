SHELL = /bin/sh
TESTRESULT = $(patsubst %.tst,%.run,$(wildcard *.tst))
OCTAVE ?= octave

.PHONY : all
all : $(TESTRESULT)

%.run : %.tst
	@echo
	@echo "[$<]"
	@$(OCTAVE) -q --no-gui --eval "pkg load interval; test $<" || true
	@touch "$@"
