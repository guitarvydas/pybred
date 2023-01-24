all: dev

dev:
	rm -f pattern*
	./pybred c.bred <src.txt
	ls -l pattern*

install: repos npmstuff

repos:
	multigit -r

npmstuff:
	npm install ohm-js yargs atob pako
