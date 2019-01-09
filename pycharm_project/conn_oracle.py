import pyhs2

sql = "select * from v$version;"
file_path = ''

def upload(file_path):
    import cx_Oracle
    # con = cx_Oracle.connect('web', 'adm2017in09g08web', '10.90.19.2:1521/orcl')
    # con = cx_Oracle.connect('app', 'zqppa2017y08g07m', '10.90.19.1:1521/orcl')
    con = cx_Oracle.connect('compass', 'tjfh2018luop1527', '10.90.19.1:1521/orcl')
    cur = con.cursor()
    with open(file_path) as file:
        lines = file.readlines()
        for line in lines:
            value = line.replace('\n', '').split('\t')
            sql = "insert into compass.F_NEWSAPP_COLDSTART_RETAIN (dt, dtdiff, new_users, hb_users, retain_users, inpv, infopv, clickpv, dur, stayuv, direct_users, direct_num, push_users, push_num, outside_users, outside_num, desktop_users, desktop_num) values (to_date('%s', 'yyyy-mm-dd'), '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d')"  % (value[0], int(value[1]), int(value[2]), int(value[3]), int(float(value[4])), int(value[5]), int(value[6]), int(value[7]), int(value[8]), int(value[9]), int(value[10]), int(value[11]), int(value[12]), int(value[13]), int(value[14]), int(value[15]), int(value[16]), int(value[17]))
            cur.execute(sql)
            con.commit()



if __name__ == '__main__':
    upload('coldDaily_2018-11-24.txt')


#
# import cx_Oracle
# con = cx_Oracle.connect('compass', 'tjfh2018luop1527', '10.90.19.1:1521/orcl')
# cur = con.cursor()
#
#
#
# sql = "insert into compass.F_NEWSAPP_COLDSTART_RETAIN (dt, dtdiff, new_users, hb_users, retain_users, inpv, infopv, clickpv, dur, stayuv, direct_users, direct_num, push_users, push_num, outside_users, outside_num, desktop_users, desktop_num) values (to_date('%s', 'yyyy-mm-dd'), '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d')" \
#       % ('2018-12-12', 1,2,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0)
#
#
#
# cur.execute(sql)
# sql2 = "select * from compass.F_NEWSAPP_COLDSTART_RETAIN"
# cur.execute(sql2)
#
# file = open('test.txt', 'r')
# lines = file.readlines()
# value = line.replace('\n', '').split('\t')
# sql = "insert into compass.F_NEWSAPP_COLDSTART_RETAIN (dt, dtdiff, new_users, hb_users, retain_users, inpv, infopv, clickpv, dur, stayuv, direct_users, direct_num, push_users, push_num, outside_users, outside_num, desktop_users, desktop_num) values (to_date('%s', 'yyyy-mm-dd'), '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d')" % (value[0], int(value[1]), int(value[2]), int(value[3]), int(float(value[4])), int(value[5]), int(value[6]),int(value[7]), int(value[8]), int(value[9]), int(value[10]), int(value[11]), int(value[12]), int(value[13]),int(value[14]), int(value[15]), int(value[16]), int(value[17]))
# cur.execute(sql)
# sql2 = "select * from compass.F_NEWSAPP_COLDSTART_RETAIN"
# cur.execute(sql2)
# cur.fetchall()

# sql_delete = 'truncate compass.F_NEWSAPP_COLDSTART_RETAIN'


F_NEWSAPP_COLDSTART_RETAIN