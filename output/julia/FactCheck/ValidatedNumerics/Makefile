SHELL = /bin/sh
TESTRESULT = $(patsubst %.jl,%.run,$(wildcard *.jl))

.PHONY : all $(TESTRESULT)
all : $(TESTRESULT)
	echo $(TESTRESULT)

$(TESTRESULT) : %.run : %.jl
	@echo
	@echo "[$<]"
	@julia "$<" || true
