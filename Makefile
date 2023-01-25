all: real

real:
	./pybred c.bred <grep.c

small:
	./pybred c.bred <src.txt

dev:
	./pybreddev c.bred <src.txt

comby1:
	./pybred comby1.bred <main.go

install: repos npmstuff

repos:
	multigit -r

npmstuff:
	npm install ohm-js yargs atob pako
