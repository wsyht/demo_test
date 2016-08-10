#!/usr/bin/env Python
#coding:utf-8

def login_account():
    
    #导入需要用的模块
    import time
    import sys
    import random
    
    #定义循环次数变量
    last_count = 3
    login_count = 3
    LoginError_conunt = 0
    
    #定义账户文件变量
    accounts_file = 'f:/accounts_file.txt'
    accounts_lock = 'f:/accounts_lock.txt'
    login_file = 'f:/login_file.txt'
    
    #三次输入正确密码的机会
    while LoginError_conunt <  login_count:
        
        #输入账号
        username = raw_input('请输入你的账号登陆：')
        
        #登陆账号已所告警
        try:
            f=open(accounts_lock)
        except:
            
            #输入密码            
            password = raw_input('请输入你的密码：')
            
            #账号密码输入成功
            with open(accounts_file) as f:
                Match_flag = False
                for line in f.readlines():
                    user,passwd = line.strip('\n').split()           
                    if username == user and password == passwd:
                        
                        #输入验证码
                        while True:
                            code=[]
                            for i in xrange(5):
                                if i == random.randint(0,5):
                                    code.append(str(random.randint(0,5)))
                                else:
                                    temp = random.randint(65,90)
                                    code.append(chr(temp))
                            Codes = ''.join(code)
                            print Codes
                            User_Codes = raw_input('请输入验证码：')
                            if User_Codes == Codes: 
                                print '正在登陆,请稍候',
                                for i in xrange(5):  # @UnusedVariable
                                    time.sleep(1)
                                    print '.',
                                print 
                                print "login success..."
                                print "Welcome %s login Teller system" % user
                                with open(login_file,'w') as f:
                                    f.write(username+'\t')
                                    f.write(password)
                                Match_flag = True
                                time.sleep(1)
                                print
                                break
                            else:
                                print "你输入的验证码有误，请重新输入"
        else:
            with open(accounts_lock) as f:
                for line in f.readlines(): 
                    user = line.strip('\n')
                    if username == user:
                        print "对不起，你的账户已锁定，无法登陆"
                        sys.exit()
                        

        
        #输错密码告警            
        if Match_flag == False:
            last_count -= 1
            LoginError_conunt += 1
            print "你输入账号或密码不正确，请重新输入"
            print '你还有%s次机会' % last_count
        else:
            break
        
    else:
        #三次输入密码机会用完锁账号
        print "Your account is locked "       
        f=file(accounts_lock,'ab')
        f.write(username+'\n')
        f.close()
        sys.exit()

    
