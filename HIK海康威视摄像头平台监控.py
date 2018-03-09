# -*- coding: UTF-8 -*-  
import smtplib
import os
from email.mime.text import MIMEText  
a='10.210.5.3'
b=os.system('ping '+a)
if(b==1):
    mailto_list=['fangjiacheng@northcom.cn']           #收件人(列表)  
    mail_host="smtp.163.com"            #使用的邮箱的smtp服务器地址，这里是163的smtp地址  
    mail_user="kangpeili2010"                           #用户名  
    mail_pass="1qa2ws"                             #密码  
    mail_postfix="163.com"                     #邮箱的后缀，网易就是163.com  
    def send_mail(to_list,sub,content):  
        me="告警信息"+"<"+mail_user+"@"+mail_postfix+">"  
        msg = MIMEText(content,_subtype='plain')  
        msg['Subject'] = sub  
        msg['From'] = me  
        msg['To'] = ";".join(to_list)                #将收件人列表以‘；’分隔  
        try:  
            server = smtplib.SMTP() 
            server.connect(mail_host)                            #连接服务器  
            server.login(mail_user,mail_pass)               #登录操作  
            server.sendmail(me, to_list, msg.as_string())  
            server.close()  
            return True  
        except Exception as e:  
             print(str(e))  
             return False  
    for i in range(1):                             #发送1封，上面的列表是几个人，这个就填几  
        if send_mail(mailto_list,"告警信息","致管理员：\n   HIK视频监控设备ip"+a+'暂时无法连通，请前往控制面板进行检查。\n\n\n\n\n\n\n\n\n\n\n*此为系统自动生成，无需回复\n*All Right By Fang Jia Cheng@2017.1_Python'):  #邮件主题和邮件内容  
           #这是最好写点中文，如果随便写，可能会被网易当做垃圾邮件退信  
           print("发送成功")
        else:   
           print("发送失败") 
