
import time
import csv
from excel import Excel
import os
from reptile import Reptile 

xlsx_path="./DRAM Price Watch List_20220429"

if __name__ == "__main__":
    handle_excel=Excel()
    handle_excel.start()