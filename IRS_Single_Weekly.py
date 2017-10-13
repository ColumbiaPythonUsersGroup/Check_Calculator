###################################################################################################################
# This is the 2017 Single Weekly tax table taken form the IRS Circular E
###################################################################################################################

class Base_Constructor(object):

    def __init__(self, ftc):
        self.ftc = ftc
        self.fit = 0

class Single_Weekly(Base_Constructor):

    def __init__(self, ftc):
        super(Single_Weekly, self).__init__(ftc)

    def weekly_single_tax_table(self):
        if self.ftc <= 44:
            return self.fit
        elif self.ftc >= 45 and self.ftc <= 224:
            self.ftc = (self.ftc - 44) * .10
            irs_tax = 0
            self.fit = irs_tax + self.ftc
            return self.fit
        elif self.ftc >= 225 and self.ftc <= 774:
            self.ftc = (self.ftc - 224) * .15
            irs_tax = 18
            self.fit = irs_tax + self.ftc
            return self.fit
        elif self.ftc >= 775 and self.ftc <= 1812:
            self.ftc = (self.ftc - 774) * .25
            irs_tax = 100.50
            self.fit = irs_tax + self.ftc
            return self.fit
        elif self.ftc >= 1813 and self.ftc <= 3730:
            self.ftc = (self.ftc - 1812) * .28
            irs_tax = 360
            self.fit = irs_tax + self.ftc
            return self.fit
        elif self.ftc >= 3731 and self.ftc <= 8058:
            self.ftc = (self.ftc - 3730) * .33
            irs_tax = 897.04
            self.fit = irs_tax + self.ftc
            return self.fit
        elif self.ftc >= 8059 and self.ftc <= 8090:
            self.ftc = (self.ftc - 8058) * .35
            irs_tax = 2325.28
            self.fit = irs_tax + self.ftc
            return self.fit
        else:
            self.ftc = (self.ftc - 8090) * .396
            irs_tax = 2336.48
            self.fit = irs_tax + self.ftc
            return self.fit