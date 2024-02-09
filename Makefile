install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

lint:
	black . --line-length 79
	isort . --profile black
	ruff . 

clean:
	pyclean .
	rm -rf *.mp3

