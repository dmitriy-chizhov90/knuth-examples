
def printExp(e, er, gs=None, ls=None):
    r = eval(e, gs, ls)
    print('{0} = {1}, {2}'.format(
        e,
        r,
        ('pass' if (r == er) else '!!! fail - {0} expected'.format(er))))

