all: tests typecheck

typecheck: force
	python \
		-m mypy \
		--python-version 3.4 \
		--ignore-missing-imports \
		--strict \
		rdg/*.py

tests: force
	nose2

sdist:
	python setup.py sdist

bdist:
	python setup.py bdist

force: