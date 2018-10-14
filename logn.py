from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from .logdata import get_webinfo
from .log_module import Loginfo

def get_ele_times(driver,times,func):
    return WebDriverWait(driver,times).until(func)

def openBrower():
    '''
    :return: webdriver Handle
    '''
    webdriver_handle = webdriver.Firefox()
    return webdriver_handle

def openUrl(handle,url):
    '''load url'''
    handle.get(url)
    handle.maximize_window()

def findElement(d,arg):
    '''
    arg must be dict
    1:text_id
    2:userid
    3:pwdid
    4:loginid
    return useEle,pwdEle,loginEle
    '''
    if 'text_id' in arg:
        ele_login = get_ele_times(d,10,lambda d:d.find_element_by_id('id'))
        ele_login.click()
    useEle = d.find_element_by_id(arg['userid'])
    pwdEle = d.find_element_by_id(arg['pwdid'])
    loginEle = d.find_element_by_id(arg['loginid'])
    return useEle,pwdEle,loginEle

def sendVals(eletuple,arg):
    listkey = ['uname','pwd']
    i = 0
    for key in listkey:
        eletuple[i].send_keys('')
        eletuple[i].clear()
        eletuple[i].send_keys(arg[key])
        i += 1
    eletuple[2].click()

def checkResult(d,err_id,arg,log):
    result = False
    try:
        d.find_element_by_link_text('error')
        print('Account And Pwd Error')
        msg = '%s:error:%s \n'%(arg['uname'],arg['pwd'],arg.err.text)
        log.log_write(msg)
    except:
        msg = '$s:pass \n'%(arg['uname'],arg['pwd'])
        log.log_write(msg)
        print('Account And Pwd Right')
        result = True
    return result

def logout(d,ele_dict):
    d.find_element_by_class_name(ele_dict['usermenu']).click()
    d.find_element_by_link_text(ele_dict['logout']).click()

def login_test(ele_dict,user_list):
    d = openBrower()
    log = Loginfo()
    openUrl(d,ele_dict['url'])
    ele_tuple = findElement(d,ele_dict)
    for arg in user_list:
        sendVals(ele_tuple,arg)
        result = checkResult(d,ele_dict['errorid'],arg,log)
        if result:
            logout(d,ele_dict)
            ele_tuple = findElement(d,ele_dict)
    log.close()

if __name__ == '__main__':
    url = input('url')
    login_text = 'login'
    account = input('id')
    pwd = input('pwd')
    ele_dict = get_webinfo('webinfo.txt')
    user_list = [{'uname':account,'pwd':pwd}]
    login_test(ele_dict,user_list)
