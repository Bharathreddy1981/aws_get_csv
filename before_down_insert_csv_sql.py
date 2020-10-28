#reading the csv file of present in the post man body and retriving information and inserting into the RDS

from flask import Flask,jsonify,request
import boto3
import csv
from botocore.client import Config
import pymysql
import pandas as pd

copying = Flask(__name__)
@copying.route("/last", methods=["POST"])
def read():
    jsondata=request.get_json()
    value=jsondata["image"]
    print(value)

    ACCESS_KEY_ID = "AKIAZNN5NBT72GR3NKP7"
    ACCESS_SECRET_KEY = "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"
    AWS_DEFAULT_REGION = 'ap-south-1'
    s3_client = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        region_name=AWS_DEFAULT_REGION,
        #config=Config(signature_version='s3v4')
    )
    my_bucket = s3_client.Bucket('flask121')

 #   bucket = s3_client.Bucket('flask121')
    obj = my_bucket.Object(key=value)
    response = obj.get()
    lines = response['Body'].read().split()
    lines.pop(0)

    for line in lines:

        z = pymysql.connect(
            host="database-1.cfmudpl0e2d7.ap-south-1.rds.amazonaws.com",
            user="admin",
            passwd="bharath**",
            db="transction_prod"
        )
        y = z.cursor()
        encoding = 'utf-8'
        k = line.decode(encoding)

        #
        # print(k)

        w = k.split(",")

        # print(w)
        st = []
        dict = {}
        dict["id"] = w[0]
        dict["employee_name"] = w[1]
        dict["phone_number"] = w[2]
        dict["email_id"] = w[3]
        dict["city"] = w[4]
        st.append(dict)

        # print(st)

        for k in st:
            id = k["id"]
            employeename = k["employee_name"]
            phonenumber = k["phone_number"]
            email = k["email_id"]
            city = k["city"]

        #print(k)

            #query = "insert into hotel values('" + str(id) + "','" + str(employeename) + "','" + str(phonenumber) + "','" + str(email) + "','" + str(city) + "')"


            #y.execute(query)

        z.commit()

    return jsonify({'url': value})



if __name__=="__main__":
    copying.run(host='0.0.0.0')

