all: real

real:
	./pybred c.bred <src.txt

dev:
	./pybreddev c.bred <src.txt

install: repos npmstuff

repos:
	multigit -r

npmstuff:
	npm install ohm-js yargs atob pako
