#!/usr/bin/env python
#coding: utf-8


import login_verify
import select_menu
import modify_passwd
import Operating_funds
import check_account
import View_messages_accounts
import sys

if __name__ == '__main__':
    
    check_account.zc()
    login_verify.login_account()
    while True:
        select_menu.menu_options()
        service = int(raw_input('请选择服务类型：'))
        if service == 1:
            modify_passwd.change_passwd()
        elif service == 2:
            Operating_funds.rmb_operation()
        elif service == 3:
            View_messages_accounts.zhxixi()
        elif service == 4:
            print 'Bye'
            sys.exit()
        else: 
            print '你输入的选项不存在,请重新输入' 
            print
        