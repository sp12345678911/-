from asyncio.windows_events import NULL
import pandas as pd
from reptile import Reptile
from datetime import date



class Excel : 
    def __init__(self):
        self.reptile=Reptile
        self.export={}

    def start(self) -> NULL:
        sheets = pd.read_excel("DRAM Price Watch List_20220429.xlsx",sheet_name=None)
        for item in sheets:
            sheet=sheets.get(item)
            if str(sheet.iloc[0][-1]) == str(date.today())+' 00:00:00':
                print('sheet',item,'今天已經更新過了唷')
            else:
                sheet_list=self.to_list(sheet)
                self.export[item]=self.read(sheet_list)
        self.export_xlsx()

    def to_list(self,sheet)->list:
        return pd.DataFrame(sheet.values.tolist())

    def read(self,sheet_list)->None:
        sheet_max_row,sheet_max_column=sheet_list.shape
        price_list=[]
        for i in range(sheet_max_row):
            url=sheet_list[1][i]
            if str(url) == 'nan':
                price_list.append("此為空值")
            else:
                reptile=self.reptile(sheet_list[1][i])
                price_list.append(reptile.get_price())
        sheet_list.insert(sheet_max_column,str(date.today()),price_list)
        return(sheet_list)

    def export_xlsx(self)->None:
        with pd.ExcelWriter('output.xlsx') as writer:  
            self.export["3200 3600 2x8GB"].to_excel(writer, sheet_name='3200 3600 2x8GB')
            self.export["4000 4400 4600 2x8GB"].to_excel(writer, sheet_name='4000 4400 4600 2x8GB')
            self.export["3200 3600 2x16GB"].to_excel(writer, sheet_name='3200 3600 2x16GB')
            self.export["3200 3600 2x32GB"].to_excel(writer, sheet_name='3200 3600 2x32GB')
            self.export["DDR5 4800 5200 5600 2x16GB"].to_excel(writer, sheet_name='DDR5 4800 5200 5600 2x16GB')
            
            
            

if __name__ == "__main__":
    excel=Excel()
    excel.start()