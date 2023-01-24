all: dev

dev:
	./pybred c.bred <src.txt

install: repos npmstuff

repos:
	multigit -r

npmstuff:
	npm install ohm-js yargs atob pako
