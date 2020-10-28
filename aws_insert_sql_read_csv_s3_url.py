
#read the given query of mysql in csv or excel

from flask import Flask,jsonify,request
#pip install openpyxl module
import pymysql
import pandas as pd
import botocore

import boto3
import csv
from botocore.client import Config

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
    name='bha1.csv'

    df=pd.read_sql_query("select * from student where id='" + str(value) + "'",con=z)
    df.to_csv(name,index=False)

    print(df)
    #query = "select * from student where id='" + str(number) + "'"

    #y.execute(query)
    #bha = y.fetchall()


    #for i in bha:
    #    k={"id":i[0],"studentname":i[1]," phone":i[2],"email":i[3],"city":i[4]}

    ACCESS_KEY_ID = "AKIAZNN5NBT72GR3NKP7"
    ACCESS_SECRET_KEY = "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"
    BUCKET_NAME = "flask121"

    data = open(name, "rb")

    s3 = boto3.resource(
        "s3",
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version="s3v4")
    )
    s3.Bucket(BUCKET_NAME).put_object(Key=name, Body=data)

    print("Done")

    #bucket = "flask121"
    #my_bucket = s3.Bucket(bucket)

    my_config = Config(
        signature_version=botocore.UNSIGNED)  # instead of botocore.UNSIGNED use 's3v4' for better url
    s3_client = boto3.client('s3', config=my_config)

    params = {"Bucket": 'flask121', "Key": name}
    url = s3_client.generate_presigned_url('get_object', params, ExpiresIn=3600)
    # print({value: url})





    return jsonify({name: url})

if __name__=="__main__":
    aws_insert_sql_read_csv.run(debug=True)



