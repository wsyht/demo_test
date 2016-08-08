#!/usr/bin/env Python
#coding:utf-8

account_file = 'f:/accounts_file.txt'

def zc():
    try:
        f=open(account_file)       
    except:
        
        print '检测到你的电脑还没有注册账号，请先注册账号再使用柜员机系统，感谢你对本系统的支持！'
        
        #注册账号
        while True:
            try:
                zh=raw_input('请输入你要注册的账号(必须是纯数字，长度为3位)：')
                a=int(zh)
            except:
                print '抱歉，你只能输入数字'
            else:
                lenzh=len(zh)
                if lenzh!= 3:
                    print '你输入的账号长度不对，请重新输入'
                else:
                        break
                    
        #注册密码            
        while True:
            try:
                mm1=raw_input('请输入你要设置的密码,必须是纯数字，长度为六位:')
                mm2=raw_input('请再次输入你要设置的，必须是纯数字，长度为六位:')
                a=int(mm1)
                a=int(mm2)
            except:
                print '抱歉，你只能输入数字'        
            else:
                lenmm1=len(mm1)
                lenmm2=len(mm2)
                if lenmm1 != 6 and lenmm2 != 6:
                    print '你输入的账号长度不对，请重新输入'
                else:
                    if mm1 != mm2:
                        print '你两次输入的新密码不匹配，请重新输入'
                    else:
                        gj=raw_input('请输入你的国籍：')
                        age=raw_input('请输入你的年龄：')
                        sex=raw_input('请输入你的性别：')
                        with open('f:/' + zh + '_xi.txt','a') as f:
                            f.write('国籍：' + gj + '\n')
                            f.write('年龄：' + age + '\n')
                            f.write('性别：' + sex + '\n')
                        with open(account_file,'a') as f:
                            f.write(zh + '\t')
                            f.write(mm2 +'\n')
                        #with open('f:/' + zh + '_ye.txt','w') as f:
                            #f.write('0')
                            print '恭喜你账号注册成功 '
                            break
                              
    else:
        f.close()