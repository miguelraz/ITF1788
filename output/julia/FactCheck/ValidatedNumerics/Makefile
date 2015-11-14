SHELL = /bin/sh
TESTRESULT = $(patsubst %.jl,%.run,$(wildcard *.jl))

.PHONY : all
all : $(TESTRESULT)

%.run : %.jl
	@echo
	@echo "[$<]"
	@julia "$<"
	@touch "$@"
