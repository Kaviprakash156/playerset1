myname = 'kaviprakash'
print(''.join([c[1] + c[0] for c in zip(myname[::2], myname[1::2])]))
