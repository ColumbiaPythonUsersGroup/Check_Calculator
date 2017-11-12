###################################################################################################################
# This is the tax calculation functions
###################################################################################################################

from math import floor

def Calc_Fed_Tax (Taxable_Income, brackets):
    Taxable_Income = floor( Taxable_Income)
    # find the appropriate tax bracket
    for bracket in brackets:
         if Taxable_Income < bracket['threshold']:
             break
         Threshold = bracket['threshold']
         Base_Tax = bracket['baseTax']
         Incremental_Rate = bracket['incrementalRate']

    # calculate the tax
    return Base_Tax + (Taxable_Income - Threshold) * Incremental_Rate
