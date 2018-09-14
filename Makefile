all: frames timesheet

frames:
	@python frames.py > ./watson_dir/frames

timesheet:
	python timesheet.py

lint:
	pylint timesheet.py frames.py

.PHONY: all frames timesheet lint
