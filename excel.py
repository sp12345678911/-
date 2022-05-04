from asyncore import read
import pandas as pd
from reptile import Reptile


reptile=Reptile()
class Excel : 
    def __init__(self):
        pass
    
    
    def start(self):
        dfs = pd.read_excel("DRAM Price Watch List_20220429.xlsx",sheet_name=None)
        for df in dfs:
            self.read(dfs.get(df))
            
    def read(self,sheet):
        sheet_max_row,sheet_max_column=sheet.shape
        for i in range(sheet_max_row):
            if str(sheet.iloc[i][1]) == "nan":
                pass
            else:
                print(reptile.get_price(sheet.iloc[i][1]))
            # print(sheet.iloc[i][1]) # get URL
    
    async def write(self) -> None:
        test=reptile.get_price('https://www.alternate.de/Corsair/DIMM-16-GB-DDR4-3600-Kit-Arbeitsspeicher/html/product/1713319')
        await print("test",test)

if __name__ == "__main__":
    excel=Excel()
    excel.start()
    # print(df.items())
    # print(df.get('3200 3600 2x8GB'))
    # for df in dfs:
    #     print(dfs.get(df))
    # df=dfs.get('DDR5 4800 5200 5600 2x16GB')
    # sheet_row,sheet_column=df.shape
    # print(sheet_row)
    # for i in range(sheet_row):
    #     for n in range(sheet_column):
    #         print(df.iloc[i][n])
    # df_dict=df.get('3200 3600 2x8GB')
    # print(df_dict.shape)
    # print(df.index(value))