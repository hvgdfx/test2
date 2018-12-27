import pyhs2

sql = "select * from v$version;"
file_path = ''

def connect()
    import cx_Oracle
    con = cx_Oracle.connect('web', 'adm2017in09g08web', '10.90.19.2:1521/orcl')
    # con1 = cx_Oracle.connect('app', 'zqppa2017y08g07m', '10.90.19.1:1521/orcl')
    cur = con.cursor()
    return cur


def exe(sql, file):
    cur = connect()
    cur.execute(sql)
    return cur.fetchall()


def read_file(file_path):
    with open(file_path) as file:
        file.read()

if __name__ == '__main__':
    exe(sql, file)



