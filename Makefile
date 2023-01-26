all: comby1

comby1:
	./pybred comby1.bred <main.go

install: repos npmstuff

repos:
	multigit -r

npmstuff:
	npm install ohm-js yargs atob pako
