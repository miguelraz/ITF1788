SHELL = /bin/sh
OBJ = $(patsubst %.cpp,%,$(wildcard *.cpp))
TESTRESULT = $(patsubst %.cpp,%.log,$(wildcard *.cpp))

.PHONY : all
all : $(OBJ) $(TESTRESULT)

% : %.cpp
	g++ -lgaol -lgdtoa -lcrlibm -lboost_unit_test_framework -o "$@" "$<"

%.log : %
	@echo
	@echo "[$<]"
	@"./$<" > "$@" || true
