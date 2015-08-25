SHELL = /bin/sh
OBJ = $(patsubst %.cpp,%,$(wildcard *.cpp))
TESTRESULT = $(patsubst %.cpp,%.log,$(wildcard *.cpp))
CXSC_HOME=${HOME}/cxsc

.PHONY : all
all : $(OBJ) $(TESTRESULT)

% : %.cpp
	g++ -I${CXSC_HOME}/include -L${CXSC_HOME}/lib -lcxsc -lboost_unit_test_framework -o "$@" "$<"

%.log : %
	@echo
	@echo "[$<]"
	@LD_LIBRARY_PATH=${CXSC_HOME}/lib "./$<" > "$@" || true
