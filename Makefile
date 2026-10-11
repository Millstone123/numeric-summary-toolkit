.PHONY: setup summary test

summary:
	python3 summarize.py

setup: test

test:
	python3 summarize.py
	python3 -m unittest discover -s tests -v
