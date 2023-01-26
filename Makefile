all: real

real:
	./pybrex c.bred <grep.c

small:
	./pybrex c.bred <src.txt

dev:
	./pybrexdev c.bred <src.txt

install: repos npmstuff

repos:
	multigit -r

npmstuff:
	npm install ohm-js yargs atob pako
