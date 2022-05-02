import string
from turtle import st
import pandas as pd
from reptile import Reptile


reptile=Reptile()
class Excel : 
    def __init__(self,path: str):
        self.excel_path=path

    async def write(self) -> None:
        test=reptile.get_price('https://www.alternate.de/Corsair/DIMM-16-GB-DDR4-3600-Kit-Arbeitsspeicher/html/product/1713319')
        await print("test",test)
    def read(self):
        pass