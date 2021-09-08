 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import smtplib


with open('mail.txt', 'r') as f:
    alicilar = [line.strip() for line in f]


eposta = 'mailadres'
sifre = 'mailsifre'

baslik = "Selam!"
icerik = " Bu mail python smtplib ile gonderilmistir. "
message = 'Subject: {}\n\n{}'.format(baslik, icerik)


mail = smtplib.SMTP("mailsunucusu",587)
mail.ehlo()
mail.starttls()
mail.login(eposta,sifre)

try:
    
    mail.sendmail(eposta,alicilar,message)
    print ("Mail gönderimi başarılı")
except:
    print("Mail Gönderimi başarısız")    