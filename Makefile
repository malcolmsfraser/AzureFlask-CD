install:
	pip install --upgrade pip&&\
		pip install -r requirements.txt
			pip install awsebcli --upgrade

test:

	
lint:
	pylint --disable=R,C application.py

deploy:
	eb deploy
	
all: install lint deploy