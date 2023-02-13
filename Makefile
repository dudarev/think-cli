 test:
	pytest --cov --cov-report html --cov-report term

 clean:
	rm -rf *.pyc

 run:
	t

 .PHONY: test clean run
