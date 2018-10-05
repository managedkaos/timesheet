PYLINT = $(HOME)/Envs/Timesheet/bin/pylint
PYCODESTYLE = $(HOME)/Envs/Timesheet/bin/pycodestyle --statistics
FILES = timesheet.py frames.py

all: frames timesheet

frames:
	@python frames.py > ./watson_dir/frames

timesheet:
	python timesheet.py

lint: $(FILES)
	$(PYLINT) $(FILES)
	$(PYCODESTYLE) $(FILES)

.PHONY: all frames timesheet lint
