
import time
import csv
from excel import Excel
import os
from reptile import Reptile 

xlsx_path="./DRAM Price Watch List_20220429"

if __name__ == "__main__":
    handle_excel=Excel(xlsx_path)
    print(handle_excel.write())
    # list=[
    #     'https://www.amazon.com/Thermaltake-TOUGHRAM-Motherboard-Syncable-R009D408GX2-3600C18B/dp/B07XVZHHXS/ref=sr_1_2?dchild=1&keywords=Thermaltake%2BTOUGHRAM%2BRGB&qid=1613613259&sr=8-2&th=1',
    #     'https://www.amazon.com/Thermaltake-TOUGHRAM-Motherboard-Syncable-R019D408GX2-3200C16A/dp/B082TJLJX3/ref=sr_1_1?dchild=1&keywords=Thermaltake+TOUGHRAM+RGB+Z-ONE&qid=1613613297&sr=8-1',
    #     'https://www.amazon.com/CORSAIR-Vengeance-3200MHz-Desktop-Memory/dp/B07D1XCKWW/ref=sr_1_1?currency=USD&dchild=1&keywords=Corsair%2BVengeance%2BPro%2BRGB&language=en_US&qid=1613613313&sr=8-1&th=1',
    #     'https://www.newegg.com/g-skill-16gb-288-pin-ddr4-sdram/p/N82E16820232751?Description=GSKILL%20Trident%20Z%20RGB%203200&cm_re=GSKILL_Trident%20Z%20RGB%203200-_-20-232-751-_-Product&quicklink=true',
    #     'https://www.alternate.de/Corsair/DIMM-16-GB-DDR4-3600-Kit-Arbeitsspeicher/html/product/1713319'
    # ]
