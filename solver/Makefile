PLATFORM = macos_universal2
INC      = /Library/gurobi1001/macos_universal2/include/
CC       = gcc
CPP      = g++
CARGS    = -m64 -g
CLIB     = -L/Library/gurobi1001/macos_universal2/lib -lgurobi100
CPPLIB   = -L/Library/gurobi1001/macos_universal2/lib -lgurobi_c++ -lgurobi100

bilinear: bilinear.cpp
	$(CPP) $(CARGS) -o $@ $< -I$(INC) $(CPPLIB) -lm