import cx_Oracle
import os

os.environ["NLS_LANG"] = ".UTF8"

connection = cx_Oracle.connect("c##java01/java01@402-oracle:1521/orcl")
cur = connection.cursor()

sql = "select * from member"
#sql2 = "insert into member values ('dkdldl222222ldl', 'qlalfqjsgh', '이름', '2020-01-02', '남자', '010-0000-0000', 'dlapdlf@naver.com', '구로', 1, 1, 0)"

#cur.execute(sql2)
#connection.commit()

cur.execute(sql)

for x in cur:
    print(x)

connection.close()