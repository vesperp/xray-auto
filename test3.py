import os
import re
import multiprocessing
from datetime import datetime
import uuid
import subprocess

def get_url():
    # f = open("ys.txt")
    # lines = f.readlines()
    with open('ys.txt') as f:
        lines = f.read().splitlines()
        print(lines) #返回list
        #用f.read().splitlines()不要用f.readlines() 有\n命令行会报错
        with multiprocessing.Pool(4) as p:
            pool = p.map(do_scan,lines)
            print(pool)
    # f.close()
    print("Xray Scan End~")
    return

# 报告
def do_scan(targeturl,outputfilename=uuid.uuid4().hex):
#    scan_date = datetime.now().date().strftime('%Y%m%d_%H%M%S') 加时间戳
 #   _name = uuid.uuid4().hex 加唯一字符串
 #   _url = re.sub( r'(http://)|(https://)' , '' , targeturl) 正则匹配
#    _url = _url.replace('.','_').strip() if '/' not in  _url  else _url.split('/')[0].replace('.','_').strip() 切切切加转换
  #  scan_command="xray webscan --basic-crawler {} --html-output {}{}.html".format(targeturl, _url , scan_date)
    scan_command="xray webscan --basic-crawler {} --html-output {}.html".format(targeturl, outputfilename)
    os.system(scan_command)
#    subprocess.call(scan_command)
    return

if __name__ == '__main__':
    get_url()