# this function isn't useful just shows me
# why the parameter types have to be in a certain order

def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:......{}, {}".format(p1, p2))
    print("var-positional (*args):.....{}".format(args))
    print("keyword (k):................{}".format(k))
    print("var-keyword (kwargs):.....{}".format(kwargs))

# p1 and p2 are positional or keyword arguements
# *args is a var positional parameter that accepts a variable (like x) amount of arguements
# k is a keyword parameter, the arg has to be passed with a keyword with the name given(k)
# **kargs is a var keyword argument that accepts a variable amount of keywords

func(1, 2, 3, 4, 5, 9, 10, k=6, k1=7, k2=8)
# positional-or-keyword:......1, 2
# var-positional (*args):.....(3, 4, 5, 9, 10)
# keyword (k):................6 we called the parameter k, so needs to be named k
# var-keyword (kwargs):.....{'k1': 7, 'k2': 8}