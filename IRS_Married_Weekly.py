class Base_Constructor(object):

    def __init__(self, ftc):
        self.ftc = ftc
        self.fit = 0

class Married_Weekly(Base_Constructor):

    def __init__(self, ftc):
        super(Married_Weekly, self).__init__(ftc)

    def weekly_married_tax_table(self):
        if self.ftc <= 166:
            return self.fit
        elif self.ftc >= 166 and self.ftc <= 525:
            self.ftc = (self.ftc - 44) * .10
            irs_tax = 0
            self.fit = irs_tax + self.ftc
            return self.fit
        elif self.ftc >= 526 and self.ftc <= 1626:
            self.ftc = (self.ftc - 224) * .15
            irs_tax = 18
            self.fit = irs_tax + self.ftc
            return self.fit
        elif self.ftc >= 1627 and self.ftc <= 3111:
            self.ftc = (self.ftc - 774) * .25
            irs_tax = 100.50
            self.fit = irs_tax + self.ftc
            return self.fit
        elif self.ftc >= 3112 and self.ftc <= 4654:
            self.ftc = (self.ftc - 1812) * .28
            irs_tax = 360
            self.fit = irs_tax + self.ftc
            return self.fit
        elif self.ftc >= 4655 and self.ftc <= 8180:
            self.ftc = (self.ftc - 3730) * .33
            irs_tax = 897.04
            self.fit = irs_tax + self.ftc
            return self.fit
        elif self.ftc >= 8181 and self.ftc <= 9218:
            self.ftc = (self.ftc - 8058) * .35
            irs_tax = 2325.28
            self.fit = irs_tax + self.ftc
            return self.fit
        else:
            self.ftc = (self.ftc - 9218) * .396
            irs_tax = 2531.22
            self.fit = irs_tax + self.ftc
            return self.fit