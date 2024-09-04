
"""
CREATE TABLE households (PRODUCT_NUM int,DEPARTMENT varchar(255),COMMODITY varchar(255),BRAND_TY varchar(255),
NATURAL_ORGANIC_FLAG varchar(255),PRIMARY KEY (PRODUCT_NUM));
"""
import mysql.connector
import pandas as pd
from mysql.connector import errorcode

config = {
    'host': 'cloud-compuring.mysql.database.azure.com',
    'user': 'cloud_group',
    'password':'Sreeja@123' ,
    'database':'cloudfinal'
    }
try:
    conn = mysql.connector.connect(**config)
    print("Connection established")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

cursor = conn.cursor()

df = pd.read_csv("C:/Users/monis/Desktop/MS/Cincinnati/Courses/Cloudcomputing/Assignment-7/Others/8451_The_Complete_Journey_2_Sample/400_households.csv")
df.columns = df.columns.str.replace(' ', '')
df=df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
dftotuple=list(df.to_records(index=False))
loopctrl=1;
progressbar=0;
for eachtuple in dftotuple:
    try:
        cursor.execute(
        # '''INSERT INTO transactions (BASKET_NUM,HSHD_NUM,PURCHASE_,PRODUCT_NUM,SPEND,UNITS,STORE_R,WEEK_NUM,YEAR_NUM) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
        #     (int(eachtuple.BASKET_NUM),int(eachtuple.HSHD_NUM),str(eachtuple.PURCHASE_),int(eachtuple.PRODUCT_NUM),int(eachtuple.SPEND),int(eachtuple.UNITS),str(eachtuple.STORE_R),int(eachtuple.WEEK_NUM),int(eachtuple.YEAR_NUM)));
    #    '''INSERT INTO products (PRODUCT_NUM,DEPARTMENT,COMMODITY,BRAND_TY,NATURAL_ORGANIC_FLAG) VALUES (%s,%s,%s,%s,%s)''',
    #     (int(eachtuple.PRODUCT_NUM),(eachtuple.DEPARTMENT),(eachtuple.COMMODITY),(eachtuple.BRAND_TY),(eachtuple.NATURAL_ORGANIC_FLAG)));
    # ''' INSERT INTO products()'''
    #    '''
    '''INSERT INTO households (HSHD_NUM,L,AGE_RANGE,MARITAL,INCOME_RANGE,HOMEOWNER,HSHD_COMPOSITION,HH_SIZE,CHILDREN) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
             (int(eachtuple.HSHD_NUM),(eachtuple.L),(eachtuple.AGE_RANGE),eachtuple.MARITAL,eachtuple.INCOME_RANGE,eachtuple.HOMEOWNER,eachtuple.HSHD_COMPOSITION,int(eachtuple.HH_SIZE),eachtuple.CHILDREN));
        conn.commit()
        loopctrl=loopctrl+1;
        if(loopctrl>20000):
            break;
        progressbar=progressbar+(loopctrl/20000);
        print(progressbar);
    except Exception as e:  # work on python 3.x
            print('Failed to upload to ftp: ' + str(e))

conn.commit()
cursor.close()
conn.close()