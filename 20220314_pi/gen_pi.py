try:
    # import version included with old SymPy
    from sympy.mpmath import mp
except ImportError:
    # import newer version
    from mpmath import mp

mp.dps = 1000000  # set number of digits
with open("pi1000000.txt","w") as f:
	f.write(str(mp.pi))
#print(mp.pi)   # print pi to a thousand places
