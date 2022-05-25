from Lib import *


DL_05 = Inv("DL-05", 20)
DL_06 = Inv("DL-06", 100)
DL_05.operation(15, "remove")
DL_05.operation(50, "+")
DL_06.operation(30, "-")
DL_06.show()
