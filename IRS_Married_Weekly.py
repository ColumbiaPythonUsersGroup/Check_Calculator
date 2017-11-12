import IRS_Tax_Brackets
import Calc_Fed_Tax

class Base_Constructor(object):

    def __init__(self, ftc):
        self.ftc = ftc
        self.fit = 0

class Married_Weekly(Base_Constructor):

    def __init__(self, ftc):
        super(Married_Weekly, self).__init__(ftc)

    def weekly_married_tax_table(self):
        self.fit = Calc_Fed_Tax.Calc_Fed_Tax(self.ftc,
               IRS_Tax_Brackets.IRS_Married_Weekly_Brackets)
        return self.fit
