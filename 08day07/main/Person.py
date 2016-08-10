#!/usr/bin/env Python
#coding:utf-8
#本节定义了三个人物对像，以及他们的一些个人信息
#所使用到的技术有：面向对像，静态字段，动态字段
import sys,time
class Person(object):
    
    gsks = "-------------故事开始-------------"  #如下两行都是静态字段
    rwjs = '故事里有三个人物角色,如下是他们三个人的资料：' 
    gx = '其中张三和王丽是情侣关系'  
     
    def __init__(self,name,sex,age,zuji,nation,job):
        self.Name = name                      #如下六行都是动态字段
        self.Sex = sex
        self.Age = age
        self.Zuji = zuji
        self.Nation = nation
        self.Job = job
    
    def loadgu(self):
        print '正在加载故事，请稍候',
        for i in xrange(3):  
            time.sleep(1)
            print '.',
            
    def wait(self,seconds):
        time.sleep(seconds)

zs = Person('张三','男','20','广东','汉族','学生')
wl = Person('王丽','女','20','广东','汉族','学生')
ls = Person('李四','男','23','北京','满族','销售经理')

zs.loadgu()
print
print
zs.wait(1.5)
print Person.gsks
zs.wait(1.5)
print Person.rwjs
zs.wait(1.5)
print Person.gx
zs.wait(1.5)
print zs.Name,'    ',zs.Sex,'    ',zs.Age,'',zs.Zuji,'   ',zs.Nation,'    ',zs.Job
print wl.Name,'    ',wl.Sex,'    ',wl.Age,'',wl.Zuji,'   ',wl.Nation,'    ',wl.Job
print ls.Name,'    ',ls.Sex,'    ',ls.Age,'',ls.Zuji,'   ',ls.Nation,'    ',ls.Job

