#  Imported Tax Libraries/Modules
import IRS_Single_Weekly
import IRS_Married_Weekly

#  Function that calls the appropriate library/module
def status(payfreq, filing_status, ftc):
    if payfreq == 'w' and filing_status == 's':
        x = IRS_Single_Weekly.Single_Weekly(ftc)
        return x.weekly_single_tax_table()
    if payfreq == 'w' and filing_status == 'm':
        x = IRS_Married_Weekly.Married_Weekly(ftc)
        return x.weekly_married_tax_table()

#  Questions that will eventually be asked through the GUI or web App
#payfreq = str(raw_input("What is your pay frequency? "))
#payfreq = payfreq.lower()

#filing_status = str(raw_input("What is your filing status? "))
#filing_status = filing_status.lower()

#ftc = int(raw_input("What is the taxable comp? "))

#  Sends results to function to call the tax table
#status(payfreq, filing_status, ftc)

#  Preliminary printing of results until GUI has been built
#print(type(payfreq))
#print(type(filing_status))
#print(status(payfreq, filing_status, ftc))

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/netcheck", methods=['POST'])
def netcheck():
    if request.method == 'POST':
        gross = int(request.form['gross_wages'])
        print(gross)

        pre_tax = int(request.form['pretax_ded'])
        print(pre_tax)

        ftc = gross - pre_tax

        payfreq = str(request.form['pay_freq'])
        print(payfreq)

        filing_status = str(request.form['marital_status'])
        print(filing_status)

        print(status(payfreq, filing_status, ftc))

    return render_template("netcheck.html")


if __name__ == '__main__':
    app.debug = True
    app.run()