__author__           = "Dilawar Singh"
__email__            = "dilawar.s.rajput@gmail.com"

import nfsim

def test_sanity():
    print(dir(nfsim))
    assert(nfsim.__version__)
    assert(nfsim.__file__)
    print(nfsim.System)

if __name__ == "__main__":
    test_sanity()
