from websites.model import Table
from flask import Blueprint, render_template,redirect,request
from . import db
from .model import Table
# import qrcode
views=Blueprint('views',__name__)

# random string generator
import random
import string
def random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@views.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        in_url=request.form.get('url')
        # print(in_url)
        table=Table.query.filter_by(in_url=in_url).first()
        if table:
            out_url=table.out_url
        else: 
            out_url=random_string()
            table=Table(in_url=in_url,out_url=out_url)
            db.session.add(table)
            db.session.commit()
        out_url= 'https://lordshoray-url-trimmer.herokuapp.com/'+out_url
        return render_template('index2.html',in_url=in_url,out_url=out_url)
    
    return render_template('index2.html')

@views.route('/<string:out_url>')
def redirect_url(out_url):
    table=Table.query.filter_by(out_url=out_url).first()
    if table is None:
        return redirect('/')

    return redirect(table.in_url)