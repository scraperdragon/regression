import sys
import pickle

stub = sys.argv
stub.append(None)
filename = stub[1]
test = stub[2]

with open(filename, "rb") as fobj:
    tests = pickle.load(fobj)

for item in tests:
    if item==test or test is None:
        print '>>>', repr(item)
        print repr(tests[item])

