SHELL = /bin/sh
TESTRESULT = $(patsubst %.tst,%.run,$(wildcard *.tst))
OCTAVE ?= octave

.PHONY : all $(TESTRESULT)
all : $(TESTRESULT)

$(TESTRESULT) :  %.run : %.tst
	@echo
	@echo "[$<]"
	@$(OCTAVE) -q --no-gui "$<"
