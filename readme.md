## centos7
### install python
1. wget https://www.python.org/ftp/python/3.5.6/Python-3.5.6.tar.xz
2. tar xvJf *.tar.xz
3. ./configure --prefix=/opt/python3.5 --enable-shared
4. make
5. make install
6. ln -s /usr/python3.5/bin/python3 /usr/bin/python3  #创建软链接
7. Reference: https://www.cnblogs.com/longxiang92/p/5829206.html

### install pip3
1. yum install openssl-devel -y #安装依赖
2. yum install zlib-devel -y    #安装依赖
3. wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-19.6.tar.gz#md5=c607dd118eae682c44ed146367a17e26 
4. tar -zxvf setuptools-19.6.tar.gz 
5. cd setuptools-19.6
6. 

### vim
#### 增加行号
1. vim ./.vimrc
2. :set nu

