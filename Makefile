all: SConstruct 
	scons -Q

help: 
	@echo "Usage: make all"
	@echo "or"
	@echo "Usage: make clean"
	@echo "or"
	@echo "Usage: make scons arg1 arg2 ..."

clean:
	scons -c

#avr-size $(MAIN).out
	