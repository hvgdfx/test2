
### centos7 install python
1. wget https://www.python.org/ftp/python/3.5.6/Python-3.5.6.tar.xz
2. tar xvJf *.tar.xz
3. ./configure --prefix=/opt/python3.5 --enable-shared
4. make
5. make install
6. ln -s /usr/python3.5/bin/python3 /usr/bin/python3  #创建软链接
7. Reference: https://www.cnblogs.com/longxiang92/p/5829206.html

