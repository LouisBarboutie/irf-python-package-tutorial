from example_package_louis.listutils import listutils

def interleave(s1: str, s2: str):
    s = ''
    for c1, c2 in zip(listutils.reverse(s1), s2):
        s += c1 + c2

    return s

if __name__ == '__main__' :
    STR1 = 'VOG!lo olH'
    STR2 = 'el,Wrd ROY' 
    res = interleave(STR1, STR2)
    print(f'Interleaved string: {res=}')
