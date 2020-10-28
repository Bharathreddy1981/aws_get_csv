
#read the given query of mysql in csv or excel

from flask import Flask,jsonify,request
#pip install openpyxl module
import pymysql
import pandas as pd


aws_insert_sql_read_csv = Flask(__name__)
@aws_insert_sql_read_csv.route("/csv/<value>", methods=["GET"])
def read(value):

    #jsondata=request.get_json()
    #image=jsondata["image"]
    #value=jsondata["image"].split('/')[-1]
    #print(value)

    z = pymysql.connect(
                host="database-1.cfmudpl0e2d7.ap-south-1.rds.amazonaws.com",
                user="admin",
                passwd="bharath**",
                db="transction_prod"
    )
    #y = z.cursor()

    df=pd.read_sql_query("select * from student where studentname='" + str(value) + "'",con=z)
    df.to_csv("anil.csv",index=False)

    print(df)
    #query = "select * from student where id='" + str(number) + "'"

    #y.execute(query)
    #bha = y.fetchall()


    #for i in bha:
    #    k={"id":i[0],"studentname":i[1]," phone":i[2],"email":i[3],"city":i[4]}

    return {"url":df}

if __name__=="__main__":
    aws_insert_sql_read_csv.run(host='0.0.0.0')



