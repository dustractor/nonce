sdist:
	python3 setup.py sdist
	cp -R dist ~/Desktop/

code:
	vim Makefile setup.py README.md nonce/__main__.py

