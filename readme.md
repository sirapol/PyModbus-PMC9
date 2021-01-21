# This is example and Modbus address of Power Meter Schneider PM9C.

# -----Software-----
1. Python 3.7.3 (windows10)
2. pymodbus library version 2.4.0

# -----Hardware-----
1. Laptop or PC windows10 OS.
2. [USB to RS485](https://www.aliexpress.com/item/4000677447909.html?spm=a2g0o.productlist.0.0.43bc33257WVEWW&algo_pvid=a0eae799-171a-4136-b0ac-549083598147&algo_expid=a0eae799-171a-4136-b0ac-549083598147-18&btsid=0b0a555a16112162049042313ed0e3&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_)
3. Power Meter Schneider PM9C

# -----Wiring-----\
Laptop|USB----GND-------------|PowerMeter\
or------|to-----A---<---> RS485+|Schneider\
PC-----|RS485--B---<---> RS485-|PM9C\