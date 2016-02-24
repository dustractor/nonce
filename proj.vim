call argloco#TabArgs([
            \	["make","Makefile"],
            \	["proj","proj.vim"],
            \	["help","README.md"],
            \	["init","nonce/__init__.py"],
            \	["main","nonce/__main__.py"]
            \	])

set makeprg=tell\ noncemaker\ make

nnoremap <F12> :silent! make<bar>redraw!<CR>
