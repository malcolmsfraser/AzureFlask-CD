install:
	pip install --upgrade pip&&\
		pip install -r requirements.txt

test:

	
lint:
	pylint --disable=R,C app.py

deploy:

	
all: install lint deploy