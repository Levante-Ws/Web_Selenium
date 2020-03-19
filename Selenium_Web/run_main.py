# __Author:"Levente Liu"

import unittest
import time
import HTMLTestRunner_jpg

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os
from bs4 import BeautifulSoup


# 加载用例
# 执行用例
# 获取最新测试报告
# 发送邮箱

def add_case(case_path, rule):
    '''加载所有的测试用例'''
    testunit = unittest.TestSuite()

    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)

    testunit.addTests(discover)  # 加载discover
    print(testunit)
    return testunit


def run_case(all_case, report_path):
    '''执行所有用例，并把结果写入测试报告'''
    now = time.strftime("%Y_%m_%d %H_%M_%S")
    report_abspath = os.path.join(report_path, now + "result.html")

    # report_abspath = "\\test_report\\" + now + "result.html"
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner_jpg.HTMLTestRunner(stream=fp,
                                               title=u'PC端直卖网常规功能，测试结果如下，可点开详情查看',
                                               description=u'用例执行情况',
                                               retry=2)
    runner.run(all_case)
    fp.close()


def get_report_file(report_path):
    '''获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getatime(os.path.join(report_path, fn)))
    print("最新测试生成的报告：" + lists[-1])

    # 找到最新生成的测试报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file


def is_result_pass(report_file):
    try:
        with open(report_file, "r", encoding='utf-8') as fp:
            f = fp.read()  # 读报告
        soup = BeautifulSoup(f, "html.parser")

        all_result = soup.find_all(class_="popup_link")
        result_num = 0
        for i in all_result:
            if "通过" in i.text:
                result_num += 1
        if result_num < 7:
            #     print("测试过程有不通过用例：%s" % result)
            return False
        else:
            return True

    except Exception as msg:
        print("判断过程出现异常：%s" % str(msg))
        return False


def send_mail(sender, psw, receiver, smtpserver, report_file, a):
    '''发送最新的测试报告内容'''
    # 读取测试报告的内容
    with open(report_file, "rb") as f:
        mail_body = f.read()

    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype="html", _charset='utf-8')
    if a == True:
        msg['Subject'] = 'PC端直卖网常规功能，测试结果正常（详情可打开附件中HTML文件查看）'
    else:
        msg['Subject'] = 'PC端直卖网常规功能，测试结果存在异常（详情可打开附件中HTML文件查看）'
    # msg['Subject'] = 'PC端直卖网常规功能，测试结果存在异常（详情可打开附件中HTML文件查看）'
    msg['from'] = sender
    msg['to'] = ",".join(receiver)
    msg.attach(body)

    # 添加附件
    att = MIMEText(open(report_file,"rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment;filename="report.html"'
    msg.attach(att)

    # 登录邮箱
    smtp = smtplib.SMTP()
    # 连接邮箱服务器
    smtp.connect(smtpserver)
    # 用户名密码
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('test report email has send out!')


if __name__ == '__main__':
    #  测试用例的路径、规则
    case_path = os.path.join(os.getcwd(), "test_case")
    rule = "test*.py"
    # 加载用例
    all_case = add_case(case_path, rule)

    # 生成测试报告的路径
    report_path = os.path.join(os.getcwd(), "test_report")
    # 执行用例
    run_case(all_case, report_path)

    # 获取最新的测试报告文件
    report_file = get_report_file(report_path)
    # 邮箱配置
    sender = ""
    psw = ""

    # 收件人
    receiver_me = []
    receiver_all = []
    smtp_server = 'imap.exmail.qq.com'

    if not is_result_pass(report_file):
        a = False
        send_mail(sender, psw, receiver_me, smtp_server, report_file, a)
    else:
        a = True
        send_mail(sender, psw, receiver_all, smtp_server, report_file, a)
        print("测试用例全部通过，不向全体发送邮件")


