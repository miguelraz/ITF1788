SHELL = /bin/sh
TESTRESULT = $(patsubst %.py,%.run,$(wildcard *.py))

.PHONY : all
all : $(TESTRESULT)

%.run : %.py
	@echo
	@echo "[$<]"
	@python3 "$<" || true
	@touch "$@"
