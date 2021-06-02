__author__           = "Dilawar Singh"
__email__            = "dilawar.s.rajput@gmail.com"

import nfsim

def test_sanity():
    print(dir(nfsim))
    assert(nfsim.__version__)
    assert(nfsim.__file__)
