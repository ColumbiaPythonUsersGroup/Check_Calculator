

class Single_Weekly(object):

    def __init__(self, ftc):
        self.ftc = ftc
        self.fit = 0

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


class Married_Weekly(object):

    def __init__(self):
        pass

    def weekly_married_tax_table(self):
        pass

class Single_Biweekly(object):

    def __init__(self):
        pass

    def biweekly_single_tax_table(self):
        pass

class Married_Biweekly(object):

    def __init__(self):
        pass

    def biweekly_married_tax_table(self):
        pass


payfreq = str(raw_input("What is your pay frequency? "))
payfreq = payfreq.lower()

filing_status = str(raw_input("What is your filing status? "))
filing_status = filing_status.lower()

ftc = int(raw_input("What is the taxable comp? "))

if payfreq == "w" and filing_status == "s":
    f = Single_Weekly(ftc)
    print(f.weekly_single_tax_table())
