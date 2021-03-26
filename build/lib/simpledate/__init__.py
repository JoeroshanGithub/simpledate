"""
Author: Roshan Joe

Combine commonly used functionality of today and now.
Also added an integer add or subtract to the date ,
to mimic sql getdate() + num


"""


import datetime


class SimpleDate(datetime.datetime):
    @classmethod
    def today(cls):
        dt=super().today() 
        return cls(dt.year,dt.month,dt.day)

    def add(self,days=None):
        if not(days ):
            raise KeyError("Number of days is mandatory")
        return self+datetime.timedelta(days=days )

    def __add__(self , other) :     
        if type(other)==int:
            return self.add(other)
        return super().__add__(other)
    
    def __sub__(self , other) :     
        if type(other)==int:
            return self.add(-1*other)
        return super().__sub__(other)

def today():
    return SimpleDate.today()
def now():
    return SimpleDate.now()
     
        


 