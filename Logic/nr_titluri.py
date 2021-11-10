from Domain.book2 import get_gen
from Logic.pret_min import gen_list
from tests.tests import *


def distinct_titles(vanzari):
    genuri = gen_list(vanzari)
    nr_titluri=[]
    g=[]
    for gen in genuri:
        n=0
        for vanzare in vanzari:
            if gen == get_gen(vanzare):
                n+=1
        nr_titluri.append(n)
        g.append(gen)
    return nr_titluri,g