from flask import Blueprint,render_template,make_response,send_from_directory,jsonify,session,redirect,url_for,json,request
import connection
page2=Blueprint("page2",__name__)

@page2.route('/name_search',methods=['GET','POST'])
def name_search():
    data = json.loads(request.form.get('name'))
    print(data)
    return "ok"