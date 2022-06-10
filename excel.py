import pandas as pd
from reptile import Reptile
from datetime import date



class Excel : 
    def __init__(self):
        self.reptile=Reptile
    
    def start(self):
        dfs = pd.read_excel("DRAM Price Watch List_20220429.xlsx",sheet_name=None)
        for df in dfs:
            self.read(dfs.get(df))
            
    def read(self,sheet)->None:
        sheet_max_row,sheet_max_column=sheet.shape
        if sheet.iloc[0][sheet_max_column-1] == date.today():
            for i in range(sheet_max_row):
                target_url = sheet.iloc[i][1]
                if str(target_url) == "nan":
                    pass
                else:
                    reptile=self.reptile(target_url)
                    reptile.get_price()
        else:
          print('今天已經更新過了唷')

    
    async def write(self) -> None:
        pass

if __name__ == "__main__":
    excel=Excel()
    excel.start()