timesheet:
	python ./timesheet.py

lint:
	pylint ./timesheet.py

.PHONY: timesheet lint
