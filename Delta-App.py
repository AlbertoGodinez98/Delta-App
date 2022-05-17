from Lib import *


# logging.info("info")

x = Inv("DL-05", 20)
# x.info()
#print("Initial quantity", x.current_quantity)
x.operation(15, "remove")
x.operation(50, "+")
#print("Current quantity", x.current_quantity)
