import pandas as pd
from reptile import Reptile
import asyncio



class Excel : 
    def __init__(self):
        self.reptile=Reptile
    
    def start(self):
        dfs = pd.read_excel("DRAM Price Watch List_20220429.xlsx",sheet_name=None)
        for df in dfs:
            self.read(dfs.get(df))
            
    def read(self,sheet)->None:
        sheet_max_row,sheet_max_column=sheet.shape
        for i in range(sheet_max_row):
            target = sheet.iloc[i][1]
            if str(target) == "nan":
                pass
            else:
                reptile=self.reptile(target)
                reptile.get_price()
    
    async def write(self) -> None:
        test=self.reptile.get_price('https://www.alternate.de/Corsair/DIMM-16-GB-DDR4-3600-Kit-Arbeitsspeicher/html/product/1713319')
        await print("test",test)

if __name__ == "__main__":
    excel=Excel()
    excel.start()