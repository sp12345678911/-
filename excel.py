from asyncio.windows_events import NULL
import pandas as pd
from reptile import Reptile
from datetime import date



class Excel : 
    def __init__(self):
        self.reptile=Reptile

    def start(self):
        sheets = pd.read_excel("DRAM Price Watch List_20220429.xlsx",sheet_name=None)
        for item in sheets:
            sheet=sheets.get(item)
            if str(sheet.iloc[0][-1]) == str(date.today())+' 00:00:00':
                print('sheet',item,'今天已經更新過了唷')
            else:
                sheet_list=self.to_list(sheet)
                self.read(sheet_list)
    
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
        sheet_list.to_excel('output.xlsx')
    def export_xlsx(self,sheet_list)->None:
        pass
        # with pd.ExcelWriter('output.xlsx') as writer:  
        #     export.to_excel(writer, sheet_name='Sheet_name_1')
        #     export.to_excel(writer, sheet_name='Sheet_name_2')

if __name__ == "__main__":
    excel=Excel()
    excel.start()