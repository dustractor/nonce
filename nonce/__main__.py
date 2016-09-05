from gibi import Matrix
from pkg_resources import resource_stream
from argparse import ArgumentParser
args = ArgumentParser(prog=__name__)

args.add_argument("wordcount",type=int,nargs="?",default=1)


ns = args.parse_args()
globals().update(**ns.__dict__)

matrix = Matrix()

matrixfile = resource_stream(__name__, "en.gibi")

matrix.load(matrixfile)

words = (matrix.make_word() for i in range(wordcount))


print(" ".join(words))



