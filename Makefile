install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

lint:
	black .
	isort .
	ruff check .

clean:
	pyclean .
	rm -rf *.mp3

