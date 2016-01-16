#! /usr/bin/env python3
import argparse,os,sqlite3,random,gibi,pkg_resources

class Nonce:

    sentence = []
    matrix = gibi.Matrix()
    schema = """
                create table if not exists archive (
                    id integer primary key,
                    word text,
                        unique (word) on conflict replace );
                create table if not exists history (
                    lasttag text,
                    lastid integer,
                        unique (lasttag) on conflict replace);"""
    def __init__(self,**kwds):
        self.__dict__.update(**kwds)
        if not self.matrixfile:
            raise RuntimeError("Supply a valid path to a gibi matrix file.")
        else:
            with open(self.matrixfile,"rb") as f:
                self.matrix.load(f)
        self.archive = sqlite3.connect(self.archivefile)
        self.archive.executescript(self.schema)
        self.archive.commit()
    def bobby(self):
        self.archive.execute("drop table if exists archive")
        self.archive.execute("drop table if exists history")
        self.archive.executescript(self.schema)
        self.archive.commit()
        self.sentence.append("DALEETED")
        return self

    def add_word(self,word=None):
        if not word:
            word = self.matrix.make_word()
        lastid = self.archive.execute(
                "insert into archive (word) values (?)",
                (word,)).lastrowid
        self.archive.execute(
                "insert into history (lasttag,lastid) values ('last',?)",
                (lastid,))
        self.archive.commit()
        return word

    def __str__(self):
        if self.sentence:
            if self.title:
                self.sentence[0] = self.sentence[0].title()
                self.sentence[-1] = self.sentence[-1] + "."
        return " ".join(self.sentence)

    @property
    def lastword(self):
        lastid = None
        lastword = None
        lastidt = self.archive.execute(
                "select lastid from history where lasttag='last'").fetchone()
        if lastidt:
            lastid = lastidt[0]
        if lastid:
            lastwordt = self.archive.execute(
                    "select word from archive where id=?",(lastid,)).fetchone()
            if lastwordt:
                self.sentence.append(lastwordt[0])
        return self

    def dumper(self):
        swrod = [t[0] for t in self.archive.execute("select word from archive")]
        words = []
        while len(swrod):
            pick = random.randint(0,len(swrod)-1)
            words.append(swrod.pop(pick))
        self.sentence.extend(words)
        return self

    def __call__(self):
        if self.drop:
            return self.bobby()
        elif self.dump:
            return self.dumper()
        if self.last:
            return self.lastword
        if self.word:
            self.sentence.append(self.add_word(self.word))
        else:
            numwords = self.words
            self.sentence.extend([self.add_word() for n in range(numwords)])
        return self

def main():
    default_matrixfile = pkg_resources.resource_filename(
            __name__,"data/english.gibi")
    parser = argparse.ArgumentParser(prog="nonce")
    parser.add_argument("--matrixfile",default=default_matrixfile,
            metavar="path",
            help="Path to a gibi matrix file. DEFAULT: " + default_matrixfile)
    parser.add_argument("--archivefile",
            default=os.path.expanduser("~/.nonce.db"),
            metavar="path",
            help="Path to a specific archive. DEFAULT: ~/.nonce.db")
    parser.add_argument("--title",action="store_true",
            help="""Capitalize the first letter of the first word"""
                """ and add a period after the last word.""")
    parser.add_argument("--last",action="store_true",
            help="Show the last word again.")
    parser.add_argument("--dump",action="store_true",
            help="Show the words.")
    parser.add_argument("--drop",action="store_true",
            help="Clear the archived history of words.")
    parser.add_argument("--word",nargs="?",
            help="Add a word and return it.")
    parser.add_argument("--words",nargs="?",type=int,default=1,
            metavar="N",
            help="Make N number of words.")
    parsed = parser.parse_args()
    if os.path.exists(parsed.matrixfile):
        nonce = Nonce(**parsed.__dict__)
        print(nonce())
if __name__ == "__main__":
    main()
