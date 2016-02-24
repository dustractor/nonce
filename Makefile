sdist:
	python3 setup.py sdist
	cp dist/*.tar.gz ~/Desktop/
	tell noncetester 'upjack'

clean:
	rm -rf dist nonce.egg-info

code:
	vim -c 'so proj.vim'

