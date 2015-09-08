SHELL = /bin/sh
TESTRESULT = $(patsubst %.jl,%.log,$(wildcard *.jl))

.PHONY : all
all : $(TESTRESULT)

%.log : %.jl
	julia "$<" > "$@"
