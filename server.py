from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import csv
from message import tt_email

app = Flask(__name__)
# print(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    data1 = {'Date': datetime.today().strftime('%Y-%m-%d %H:%M:%S')}
    data1.update(data)

    with open('database.txt', mode ='a') as database:
        # email = data['email']
        # subject = data['subject']
        # message = data['message']
        # file = database.write(f'\n{email},{subject},{message}')
        # maintain as dictionary
        file = database.write(f'\n{str(data1)}')

def write_to_csv(data):
    tt_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    with open('database.csv', mode ='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([tt_date,email,subject,message])
        # file = database.write(f'\n{str(data1)}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            tt_estr = 'Email: ' + data['email'] + '<br>' + 'Subject: ' + data['subject'] + '<br>' + 'Message: ' + data['message']
            (tt_email(tt_estr))
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try again!'



# @app.route("favicon.ico")
# def favicon():
#     # return "<p>Hello, Tony Jon Thomas dsgd!</p>"
#     return render_template('about.html')

# main.70a66962.map