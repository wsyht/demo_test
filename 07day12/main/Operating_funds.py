#!/usr/bin/env Python
#coding:utf-8


def rmb_operation():
    while True:
        zijin="f:/ye.txt"
        dk='f:/dk.txt'
        yb = 100
        sb = 300
        wb = 500 
        yq = 1000
        lq = 2000
        print '''
                1、查看余额                            2、存款
                3、提现                                    4、贷款
                5、还款                                    6、返回首页
        '''
        xuan1 = input('请选择你要执行的操作：')
        def menu():
                print '''
                    1、100元                                 2、300元
                    3、500元                                 4、1000元
                    5、2000元                               6、手动输入其它金额
                    7、返回上一页
                '''      
        def dk_menu():
            print '''
                    1、查看已贷款资金                           2、手动输入贷款金额
                    3、返回上一页
            '''   
        def xye():                     
            with open(zijin,'wb') as f:
                f.write(ye)
            print '存款完成，你现在的余额为%s元' %   ye  
        if xuan1 == 1:
            try:
                f=open(zijin)
            except:
                with open(zijin,'w') as f:
                    f.write('0')
                    print '你的账户余额为%d元'
            else:
                f.close()
                with open(zijin) as f:
                    ye=int(f.readline())              
                    print '你的账户余额为%d元' % ye
                    
        elif xuan1 == 2:
            while True:
                menu()
                chun = input('请选择你要存款的额度：')
                with open(zijin) as f:
                    ye = int(f.readline()) 
                    if chun == 1:  
                        ye = ye + yb 
                    elif chun == 2:
                        ye = ye + sb 
                    elif chun == 3:
                        ye = ye + wb 
                    elif chun == 4:
                        ye = ye + yq 
                    elif chun == 5:
                        ye = ye + lq              
                    elif chun == 6:
                        sczj = input('请输入你要存款的金额：')                       
                        ye = ye + sczj
                    else:
                        break
                    ye=str(ye)
                    xye()
        elif xuan1 == 3:
            while True:
                menu()
                chun = input('请选择你要存款的额度：')
                with open(zijin) as f:
                    ye = int(f.readline()) 
                    if chun == 1:  
                        ye = ye - yb 
                    elif chun == 2:
                        ye = ye - sb 
                    elif chun == 3:
                        ye = ye - wb 
                    elif chun == 4:
                        ye = ye - yq 
                    elif chun == 5:
                        ye = ye - lq              
                    elif chun == 6:
                        sczj = input('请输入你要存款的金额：')                       
                        ye = ye - sczj
                    else:
                        break
                    ye=str(ye)
                    xye()
                  
        elif xuan1 == 4:
            while True:
                dk_menu()
                dai = input('请选择选项：')
                if dai == 1:
                    try:
                        f = open(dk)  
                    except:
                        with open(dk) as f:
                            f.write('0')
                            print '你现在的余额为0元'
                    else:
                        f.close()
                        with open(dk) as f:
                            f = f.readline()
                            print '你现在的余额为%s元' %    f
                            
                elif dai == 2:
                    daikuan = input('请选择你要贷款的额度：')
                    
                    try:
                        f=open(dk)
                    except:
                        with open(dk,'w') as f:
                            daikuan=str(daikuan)
                            f=f.write(daikuan)
                            
                            print '你现在的余额为%s元'  %    f
                    else:
                        f.close()
                        with open(dk) as f:     
                            dlk = int(f.readline())
                            daikuan=int(daikuan)
                            dlk = dlk + daikuan
                            dlk = str(dlk)
                        with open(dk,'wb') as f:
                            f.write(dlk)                        
                            print '你现在的余额为%s元'  % dlk
                else:
                    break
        elif xuan1 == 5:
            while True:
                try:
                    f=open(dk)
                except:
                    print '你没有欠款'
                    break           
                else:
                    with open(dk) as f:
                        ye=int(f.readline())  
                        if ye == 0:
                            print "你的欠款额度为0"
                        else:
                            with open(dk) as f:
                                ye=int(f.readline())
                                print '你现在的欠款金额为%s元'  %    ye
                                qk=int(raw_input("请输入你要还款的金额："))
                                qk = ye - qk
                                if qk < 0:
                                    print "你输入的还款金额多于你欠的金额请输新输入"
                                    break
                                qk = str(qk)
                                with open(dk,'w') as f:
                                    f.write(qk)
                                print '你现在的欠款金额为%s元'  %    qk
                                fanhui=raw_input('请输入1返回上一页：')
                                if fanhui == 1:
                                    break 
                    break            
        elif xuan1 == 6:
              break            
    
    
        
        
    