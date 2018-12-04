## centos7
### install python
1. wget https://www.python.org/ftp/python/3.5.6/Python-3.5.6.tar.xz
2. tar xvJf *.tar.xz
3. ./configure --prefix= <font color=#FF0000>/opt/python3.5</font> --enable-shared  #这个路径很关键，是bin的调用路径 
4. make
5. make install
6. ln -s /usr/python3.5/bin/python3 /usr/bin/python3  #创建软链接
7. Reference: https://www.cnblogs.com/longxiang92/p/5829206.html

### install pip3
1. 关键是bin的路径得选好
2. Reference:https://www.cnblogs.com/dongml/p/8719421.html

### vim
##### 增加行号
1. vim ./.vimrc
2. :set nu
<font color=#0099ff>xx</font>
<font face="黑体">我是黑体字</font>
<font face="微软雅黑">我是微软雅黑</font>
<font face="STCAIYUN">我是华文彩云</font>
<font color=#0099ff size=7 face="黑体">color=#0099ff size=72 face="黑体"</font>
<font color=#00ffff size=72>color=#00ffff</font>
<font color=gray size=72>color=gray</font>
