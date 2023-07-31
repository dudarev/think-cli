 test:
	pytest --cov --cov-report html --cov-report term

show-coverage:
	open htmlcov/index.html

 clean:
	rm -rf *.pyc

 run:
	t

 .PHONY: test clean run
