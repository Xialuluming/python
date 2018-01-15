进入CMD回车执行pip install PyMySQL，然后import pymysql
c = pymysql.Connect(
    host=
    port=
    user=
    passwd=
    db=
    charset='utf8'
)

cursor = c.cursor()
sql="select * from table1"
ex=cursor.execute(sql)
results = cursor.fetchall()
l=list(results)
d=pd.DataFrame(l)