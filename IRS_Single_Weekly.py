###################################################################################################################
# This is the 2017 Single Weekly tax table taken form the IRS Circular E
###################################################################################################################

import IRS_Tax_Brackets
import Calc_Fed_Tax

class Base_Constructor(object):

    def __init__(self, ftc):
        self.ftc = ftc # federal taxable compensation
        self.fit = 0 # federal income tax

class Single_Weekly(Base_Constructor):

    def __init__(self, ftc):
        super(Single_Weekly, self).__init__(ftc)

    def weekly_single_tax_table(self):
        self.fit = Calc_Fed_Tax.Calc_Fed_Tax(self.ftc,
               IRS_Tax_Brackets.IRS_Single_Weekly_Brackets)
        return self.fit
