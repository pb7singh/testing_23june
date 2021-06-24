from flask import Flask, render_template,url_for, request,redirect
import datetime
import csv
app = Flask(__name__)
@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def works(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
            try:
                data=request.form.to_dict()
                write_to_csv(data)
                return render_template('/thank_you.html')
            except:
                return "unable to save it to database"
    else:
        return "something went wrong"

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        file=database.write(f'\nEmail:-{email}, Subject:-{subject}, Message:-{message} Time={datetime.time()}\n')

def write_to_csv(data):
    with open('database.csv',newline='',mode='a') as database2:
        email=data['email']
        subject=data['subject']
        message=data['message']
        csv_writer=csv.writer(database2, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])