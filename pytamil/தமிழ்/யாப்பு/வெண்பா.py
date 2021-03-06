# -*- coding: utf-8 -*-

import sys
import antlr4
from antlr4 import *
from antlr4.tree.Trees import Trees
import os

from codegen.வெண்பாLexer import வெண்பாLexer
from codegen.வெண்பாParser import வெண்பாParser
from codecs import open
from nltk import Tree as nltkTree
from nltk.treeprettyprinter import TreePrettyPrinter

 
def main():
    infilename = os.path.join(os.path.dirname(__file__),'வெண்பாinput.txt')
    outfilename = os.path.join(os.path.dirname(__file__),'வெண்பாoutput.txt')
    data = open(infilename).read()   
    input_stream = antlr4.InputStream(data)
    lexer = வெண்பாLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = வெண்பாParser(stream)
    tree = parser.வெண்பா()

    # print(tree.toStringTree())
    strtree = Trees.toStringTree(tree, None, parser)
    print(strtree)
    t = nltkTree.fromstring(strtree)
    # t.pretty_print()
    a = TreePrettyPrinter(t).text()
    print (a)
    # t.pprint(margin=70, indent=0, nodesep=u'', parens=u'()', quotes=False)
    # pprint(Trees.toStringTree(tree, None, parser), width=20, indent=4)
 
    with open(outfilename, 'w', encoding='utf8') as f:
        f.write( a)

if __name__ == '__main__':
    main()
