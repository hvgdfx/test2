#!coding='utf-8'

from pyhive import hive
import time
host_name = "10.80.25.160"
port = 10000


def hiveconnection(host_name, port, hql):
    conn = hive.Connection(host=host_name, port=port)
    cur = conn.cursor()
    cur.execute(hql)
    result = cur.fetchall()
    return result


for i in range(1, 3):
    date = time.strftime("%Y-%m-%d", time.localtime(time.time() - 86400 * i))
    date_yyyymmdd = time.strftime("%Y%m%d", time.localtime(time.time() - 86400 * i))
    hql = '''select userkey, ua, pub, mos, mos_detail, net, softv, ip from default.client_newuser_other \
    where dt='%(date)s' limit 10'''%{'date': date}
    output = hiveconnection(host_name, port, hql)
    file = open("/home/zhanggx/coldStart/data/output_%s.txt"%(date_yyyymmdd), 'w')
    for userkey, ua, pub, mos, mos_detail, net, softv, ip in output:
        file.write(userkey + '\t' + ua + '\t' + pub + '\t' + mos + '\t' + mos_detail + '\t' + net + '\t' + softv + '\t' + ip)
        file.write('\n')
    file.close()




