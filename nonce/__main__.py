#! /usr/bin/env python3
from nonce import *

main = lambda:Nonce(**NonceMain.parse_args().__dict__)()
if __name__ == "__main__":
    print(main())
