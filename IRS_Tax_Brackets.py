###################################################################################################################
# This is the 2017 tax tables taken form the IRS Circular E
###################################################################################################################


# brackets are assumed to be in increasing order
IRS_Single_Weekly_Brackets = [
  { 'threshold':    0,  'baseTax':    0.00, 'incrementalRate': 0.00 },
  { 'threshold':   44,  'baseTax':    0.00, 'incrementalRate':  .10 },
  { 'threshold':  224,  'baseTax':   18.00, 'incrementalRate':  .15 },
  { 'threshold':  774,  'baseTax':  100.50, 'incrementalRate':  .25 },
  { 'threshold': 1812,  'baseTax':  360.00, 'incrementalRate':  .28 },
  { 'threshold': 3730,  'baseTax':  897.04, 'incrementalRate':  .33 },
  { 'threshold': 8058,  'baseTax': 2325.28, 'incrementalRate':  .35 },
  { 'threshold': 8090,  'baseTax': 2336.48, 'incrementalRate':  .396 }
]


IRS_Married_Weekly_Brackets = [
  { 'threshold':    0,  'baseTax':    0.00, 'incrementalRate': 0.00 },
  { 'threshold':  166,  'baseTax':    0.00, 'incrementalRate':  .10 },
  { 'threshold':  525,  'baseTax':   35.90, 'incrementalRate':  .15 },
  { 'threshold': 1626,  'baseTax':  201.05, 'incrementalRate':  .25 },
  { 'threshold': 3111,  'baseTax':  572.30, 'incrementalRate':  .28 },
  { 'threshold': 4654,  'baseTax': 1004.34, 'incrementalRate':  .33 },
  { 'threshold': 8180,  'baseTax': 2167.92, 'incrementalRate':  .35 },
  { 'threshold': 9218,  'baseTax': 2531.22, 'incrementalRate':  .396 }
]


IRS_Single_Biweekly_Brackets = [
  { 'threshold':     0,  'baseTax':    0.00, 'incrementalRate': 0.00 },
  { 'threshold':    88,  'baseTax':    0.00, 'incrementalRate':  .10 },
  { 'threshold':   447,  'baseTax':   35.90, 'incrementalRate':  .15 },
  { 'threshold':  1548,  'baseTax':  201.05, 'incrementalRate':  .25 },
  { 'threshold':  3623,  'baseTax':  719.80, 'incrementalRate':  .28 },
  { 'threshold':  7460,  'baseTax': 1794.16, 'incrementalRate':  .33 },
  { 'threshold': 16115,  'baseTax': 4650.31, 'incrementalRate':  .35 },
  { 'threshold': 16181,  'baseTax': 4673.41, 'incrementalRate':  .396 }
]


IRS_Married_Biweekly_Brackets = [
  { 'threshold':     0,  'baseTax':    0.00, 'incrementalRate': 0.00 },
  { 'threshold':   333,  'baseTax':    0.00, 'incrementalRate':  .10 },
  { 'threshold':  1050,  'baseTax':   71.70, 'incrementalRate':  .15 },
  { 'threshold':  3252,  'baseTax':  402.00, 'incrementalRate':  .25 },
  { 'threshold':  6221,  'baseTax': 1144.25, 'incrementalRate':  .28 },
  { 'threshold':  9308,  'baseTax': 2008.61, 'incrementalRate':  .33 },
  { 'threshold': 16360,  'baseTax': 4335.77, 'incrementalRate':  .35 },
  { 'threshold': 18437,  'baseTax': 5062.72, 'incrementalRate':  .396 }
]


IRS_Single_Semi_Monthly_Brackets = [
  { 'threshold':     0,  'baseTax':    0.00, 'incrementalRate': 0.00 },
  { 'threshold':    96,  'baseTax':    0.00, 'incrementalRate':  .10 },
  { 'threshold':   484,  'baseTax':   38.80, 'incrementalRate':  .15 },
  { 'threshold':  1677,  'baseTax':  217.75, 'incrementalRate':  .25 },
  { 'threshold':  3925,  'baseTax':  779.75, 'incrementalRate':  .28 },
  { 'threshold':  8081,  'baseTax': 1943.43, 'incrementalRate':  .33 },
  { 'threshold': 17458,  'baseTax': 5037.84, 'incrementalRate':  .35 },
  { 'threshold': 17529,  'baseTax': 5062.69, 'incrementalRate':  .396 }
]


IRS_Married_Semi_Monthly_Brackets = [
  { 'threshold':     0,  'baseTax':    0.00, 'incrementalRate': 0.00 },
  { 'threshold':   360,  'baseTax':    0.00, 'incrementalRate':  .10 },
  { 'threshold':  1138,  'baseTax':   77.80, 'incrementalRate':  .15 },
  { 'threshold':  3523,  'baseTax':  435.55, 'incrementalRate':  .25 },
  { 'threshold':  6740,  'baseTax': 1239.80, 'incrementalRate':  .28 },
  { 'threshold': 10083,  'baseTax': 2139.80, 'incrementalRate':  .33 },
  { 'threshold': 17723,  'baseTax': 4697.04, 'incrementalRate':  .35 },
  { 'threshold': 19973,  'baseTax': 5484.54, 'incrementalRate':  .396 }
]


IRS_Single_Monthly_Brackets = [
  { 'threshold':     0,  'baseTax':     0.00, 'incrementalRate': 0.00 },
  { 'threshold':   192,  'baseTax':     0.00, 'incrementalRate':  .10 },
  { 'threshold':   969,  'baseTax':    77.70, 'incrementalRate':  .15 },
  { 'threshold':  3354,  'baseTax':   435.45, 'incrementalRate':  .25 },
  { 'threshold':  7850,  'baseTax':  1559.45, 'incrementalRate':  .28 },
  { 'threshold': 16163,  'baseTax':  3887.09, 'incrementalRate':  .33 },
  { 'threshold': 34917,  'baseTax': 10075.91, 'incrementalRate':  .35 },
  { 'threshold': 35058,  'baseTax': 10125.26, 'incrementalRate':  .396 }
]


IRS_Married_Monthly_Brackets = [
  { 'threshold':     0,  'baseTax':     0.00, 'incrementalRate': 0.00 },
  { 'threshold':   721,  'baseTax':     0.00, 'incrementalRate':  .10 },
  { 'threshold':  2275,  'baseTax':   155.40, 'incrementalRate':  .15 },
  { 'threshold':  7046,  'baseTax':   871.05, 'incrementalRate':  .25 },
  { 'threshold': 13479,  'baseTax':  2479.30, 'incrementalRate':  .28 },
  { 'threshold': 20167,  'baseTax':  4351.94, 'incrementalRate':  .33 },
  { 'threshold': 35446,  'baseTax':  9294.01, 'incrementalRate':  .35 },
  { 'threshold': 39946,  'baseTax': 10969.01, 'incrementalRate':  .396 }
]
