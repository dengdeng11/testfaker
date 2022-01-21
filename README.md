# testfaker
django and get identity

1、先安装python
下载tgz的python包
解压后进入python目录，进行编译
./configure
make && make install
编译成功后，使用命令python3 -V查看

2、安装django和faker
可联网环境下：
pip install Django==3.2.11
pip install faker==11.3.0
不可联网环境下怎么操作：
第一步：先在可联网环境下执行pip install进行安装
第二步：再将下载下来的包打包
pip download /test/downpackages(自己指定下载的目录) -r pkgversion.txt
pkgversion.txt 中为Django==3.2.11  faker==11.3.0
第三步：将downpackages 和 pkgversion.txt拷贝到不可联网的服务器
第四步：在不联网服务器安装
pip install --no-index --find-index=文件路径\downpackages -r pkgversion.txt

4、提供脚手架创建django项目
django-admin startproject testdjango


5、运行时提示sqlite版本过低，进行升级
https://blog.csdn.net/line_on_database/article/details/116058659
更新后仍提示版本过低，重新解压编译python

6、运行命令：python3 manage.py runserver 0.0.0.0:8000
