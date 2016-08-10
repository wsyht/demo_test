#!/usr/bin/env Python
#coding:utf-8

login_file = 'f:/login_file.txt'

def zhxixi():
    with open(login_file) as f:
        for line in f.readlines():
            user,passwd = line.strip('\n').split()
            print '用户名：%s ' % user
            print '密码：%s ' % passwd
 
    with open('f:/' + user + '_xi.txt') as f:
        for line in f.readlines():   
            print line.strip('\n')
    fh=int(raw_input('按1返回上一层：'))
    if fh == 1:
        print 
                    