class Date:
    def __init__(self,month,day,year):
        if day > 31 or day<1:
            print('Wrong input, day should be in the range 1 to 31')
            return
        elif month>12 or month<1:
                print('Wrong input, month should be in the range 1 to 12')
                return
        self.month = month
        self.day = day
        self.year =year
    months = {1:'January',2:"February",3:'March', 4:'April',5:'May',6:'June',7:"Jule",8:'August',9:"September", 10:"October",11:"November", 12:"December"}

    def __str__(self):
        return f"{self.month}/{self.day}/{self.year}\n{self.months[self.month]} {self.day}, {self.year}\n{self.day} {self.months[self.month]} {self.year}" 
        

today = Date(2,8,2025)
print(today)