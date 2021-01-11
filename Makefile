pkgdirname != basename `git config remote.origin.url` | sed 's/.git$$//'

compile: 
	@echo Nothing to do

install: clean
	mkdir -p ${pkgdir}/opt/aninix/${pkgdirname}/
	rsync -avzp ./*canary* ${pkgdir}/opt/aninix/${pkgdirname}/

test: compile
	python3 -m pytest

clean: 
	cat .gitignore | xargs rm -Rf

diff: 
	@echo Nothing to do.

reverse: 
	@echo Nothing to do.

checkperm:
	@echo Nothing to do.

