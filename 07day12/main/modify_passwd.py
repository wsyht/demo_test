#!/usr/bin/env Python
#coding:utf-8

def change_passwd():
    
    #导入常用模块
    import os
    import sys
    
    #旧密码本次新循环变量
    last_count = 3
    Change_count = 3
    ChangeError_conunt = 0
    
    #新密码三次循环变量
    last_new_count = 3
    Change_new_count = 3
    ChangeError_new_conunt = 0
    
    #账户文件变量
    accounts_file = 'f:/accounts_file.txt'
    login_file = 'f:/login_file.txt'
    new_accounts_file = 'f:/new_accounts_file.txt'
    accounts_lock = 'f:/accounts_lock.txt'
    
    #三次输入正确旧密码机会
    while ChangeError_conunt <  Change_count:
        
        old_passwd = raw_input('请输入你的旧密码：')
        Match_flag = False
        with open(login_file) as f:
            for li in f.readlines():
                username,password=li.split()
                if old_passwd == password:
                    Match_flag = True
                    
                    #三次输入正确新密码机会
                    while ChangeError_new_conunt < last_new_count:
                        new1_passwd = raw_input('请输入你的新密码：')
                        new2_passwd = raw_input('请再次输入你的新密码：')
                        if new1_passwd == new2_passwd:
                            last_count = 3
                            ChangeError_conunt = 0
                            with open(accounts_file) as f:
                                for line in f.readlines():
                                    new_file = file(new_accounts_file,'ab')
                                    new_file.write(line.replace(password,new2_passwd))
                                new_file.close()
                            os.remove(accounts_file) 
                            os.rename(new_accounts_file, accounts_file)
                            with open(login_file,'w') as f:
                                f.write(username+'\t')
                                f.write(new2_passwd)
                            print 'passwd： 所有的身份验证令牌已经成功更新。'                            
                            break 
                                                    
                        else:
                            #新密码输错警告信息输出
                            last_new_count -= 1
                            ChangeError_new_conunt += 1
                            print "抱歉，两次输入的新密码不匹配："
                            print '你还有%s次机会' % last_new_count
                            if last_count == 0:
                                print "passwd: 已经超出服务重试的最多次数"
                                sys.exit()
                                
        #旧密码输错警告信息输出                        
        if Match_flag == False:        
            last_count -= 1
            ChangeError_conunt += 1
            print "你输入的旧密码有误，请重新输入："
            print '你还有%s次机会' % last_count
        else:
            break

    else:
        #三次输入旧密码机会用完锁账号
        print "你输入的次数过多，账号已锁定"       
        f=file(accounts_lock,'ab')
        f.write(username+'\n')
        f.close()

        




                
                
                