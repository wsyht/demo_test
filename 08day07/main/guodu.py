#!/usr/bin/env Python
#coding:utf-8

import Person
import time

class gzjd(object):
    
    gzsq = '-------------高中时期-------------'
    dxsq = '-------------大学时期-------------'
    shsq = '-------------社会时期-------------'
    
    def __init__(self):
        pass
        
    def gzdh(self):
        Person.zs.wait(1.5)
        print Person.zs.Name,('：高考成绩出来了,王丽你考的怎么样')
        Person.zs.wait(1.5)
        print Person.wl.Name,('：我考上了北京师范大学了，你呢？')
        Person.zs.wait(1.5)
        print Person.zs.Name,('：我落弟了，不过我觉定上北京做网管，供你读大学')
        Person.zs.wait(1.5)
        print Person.wl.Name,('：真的吗？张三，你真好.')
        Person.zs.wait(1.5)
        print Person.zs.Name,('：为了你，我觉得值得')
        Person.zs.wait(1.5)
        print Person.wl.Name,('：张三...')
        Person.zs.wait(1.5)
        
    def dxdh(self):
        Person.zs.wait(1.5)
        print ('王丽顺利入学了，而此时张三还正走在去面试网管的路上')
        Person.zs.wait(1.5)
        print ('叮叮叮')
        Person.zs.wait(1.5)
        print Person.zs.Name,('：喂，你好！')
        Person.zs.wait(1.5)
        print ('人事：你好！我是北京网络时代有限公司的人事，请问你是张三先生吗？')
        Person.zs.wait(1.5)
        print Person.zs.Name,('：是的')
        Person.zs.wait(1.5)
        print ('人事：是这样的，我们看了你投递过来我们公司的简历，觉得你很适合我们公司的岗位，想手邀请你明天下午三点过来面试，请问您方便吗？')
        Person.zs.wait(1.5)
        print Person.zs.Name,('：好的，没有问题')
        Person.zs.wait(1.5)
        print ('人事：嗯嗯，好的，稍候我会发一封面试邀请到你的邮箱，请注意扫收')
        Person.zs.wait(1.5)
        print Person.zs.Name,('：好的，谢谢！')
        
    def ms(self):
        print '到了第二天',
        for i in xrange(3):  
            time.sleep(1)
            print '.',
        print
        print ('IT主管：王先生，经过面试，我们觉得你很适合我们的网管的岗位，工资可以给你五K，请问你什么时候可以来上班呢？')
        Person.zs.wait(1.5)
        print Person.zs.Name,('：我明天就可以来上班')
        Person.zs.wait(1.5)
        print ('IT主管：那好，稍候我们人事会发录取通知书给你，今天的面试就先到这样')
        Person.zs.wait(1.5)
        print Person.zs.Name,('：好的，非常感谢')

    def society(self):
        Person.zs.wait(1.5)
        print '王丽毕业了，在一家网络公司工作，并且认识了一位高富帅'
        Person.zs.wait(1.5)
        print Person.wl.Name,('：张三，我们分手吧！我觉得我们的差距太大了')
        Person.zs.wait(1.5)
        print Person.zs.Name,('：为什么？你不想一下你能读完大学还是我供你的，你现在说这种话')
        Person.zs.wait(1.5)
        print Person.wl.Name,('：你的钱我以后会还给你的，我们以后就这样吧')
        Person.zs.wait(1.5)
        print Person.zs.Name,('：好，既然你这么觉情我也不说什么了')
        Person.zs.wait(1.5)
        
    def fs(self):    
        print('张三很心痛...')
        Person.zs.wait(3)
        print ('张三在家冷静了几天，想了想，我觉定要奋发图强，让你后悔，于是自学了三个月Linux')
        Person.zs.wait(1.5)
        print ('不久张三做上了运维总监，月新五万，并且买了车买房')
        Person.zs.wait(1.5) 
        print ('不久张三又碰到了李丽')
        Person.zs.wait(1.5)
        print Person.zs.Name,('：你还过得好吗')
        Person.zs.wait(1.5)
        print Person.wl.Name,('：他已经和他分手了，我知道我以前我的过去做错了，你能再给我一次机会吗？我们重新开始')
        Person.zs.wait(1.5)
        print Person.zs.Name,('：好，我们重新开始')
    
print 
print gzjd.gzsq
gz = gzjd()    
gz.gzdh()
print
print gzjd.dxsq
gz.dxdh()
print
gz.ms()
print
print gzjd.shsq
print
gz.society()
print
gz.fs()


    