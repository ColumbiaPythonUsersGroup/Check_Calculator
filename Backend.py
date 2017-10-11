import IRS_Tables

payfreq = str(raw_input("What is your pay frequency? "))
payfreq = payfreq.lower()

filing_status = str(raw_input("What is your filing status? "))
filing_status = filing_status.lower()

ftc = int(raw_input("What is the taxable comp? "))

if payfreq == "w" and filing_status == "s":
    f = IRS_Tables.Single_Weekly(ftc)
    print(f.weekly_single_tax_table())