#!/usr/bin/python
import sys
import time
import os
import socket
from platform import system
class colors:

    ENDC     = '\33[0m'
    BOLD     = '\33[1m'
    ITALIC   = '\33[3m'
    URL      = '\33[4m'
    BLINK    = '\33[5m'
    BLINK2   = '\33[6m'
    SELECTED = '\33[7m'

    BLACK  = '\33[30m'
    RED    = '\33[31m'
    GREEN  = '\33[32m'
    YELLOW = '\33[33m'
    BLUE   = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE  = '\33[36m'
    WHITE  = '\33[37m'

    BLACKBG  = '\33[40m'
    REDBG    = '\33[41m'
    GREENBG  = '\33[42m'
    YELLOWBG = '\33[43m'
    BLUEBG   = '\33[44m'
    VIOLETBG = '\33[45m'
    BEIGEBG  = '\33[46m'
    WHITEBG  = '\33[47m'

    GREY    = '\33[90m'
    RED2    = '\33[91m'
    GREEN2  = '\33[92m'
    YELLOW2 = '\33[93m'
    BLUE2   = '\33[94m'
    VIOLET2 = '\33[95m'
    BEIGE2  = '\33[96m'
    WHITE2  = '\33[97m'

    GREYBG    = '\33[100m'
    REDBG2    = '\33[101m'
    GREENBG2  = '\33[102m'
    YELLOWBG2 = '\33[103m'
    BLUEBG2   = '\33[104m'
    VIOLETBG2 = '\33[105m'
    BEIGEBG2  = '\33[106m'
    WHITEBG2  = '\33[107m'
 
print
print
print
os.system("clear")
print
print

def ping():
	print
	print
	time.sleep(1)
	print
	
	os.system("curl https://api.hackertarget.com/nping/?q=" + ip)
	print(" ")
	
def http():
	print
	print
	print
	os.system("curl https://api.hackertarget.com/httpheaders/?q=" + ip)
	print(" ")



def whois():
	print
	print

	print
	os.system("curl http://api.hackertarget.com/whois/?q=" + ip)
	print(" ")


def trace():
	print
	print
	print
	os.system("curl https://api.hackertarget.com/mtr/?q=" + ip)
	print(" ")



def dns():
	print
	print
	print
	os.system("curl https://api.hackertarget.com/dnslookup/?q=" + ip)
	print(" ")


def reversedns():
	print
	print
	print
	os.system("curl https://api.hackertarget.com/reversedns/?q=" + ip)
	print(" ")


def geoip():
	print
	print
	print
	os.system("curl https://api.hackertarget.com/geoip/?q=" + ip)
	print(" ")


def reverseip():
	print
	print
	print
	os.system("curl https://api.hackertarget.com/reverseiplookup/?q=" + ip)
	print(" ")
	

def nmap():
	print
	print
	print
	os.system("curl https://api.hackertarget.com/nmap/?q=" + ip)
	print(" ")



def plink():
	print
	print
	print
	os.system("curl https://api.hackertarget.com/pagelinks/?q=" + ip)
	print(" ")


	print
	print
	time.sleep(3)
	print
os.system("clear")
class colors:

    ENDC     = '\33[0m'
    BOLD     = '\33[1m'
    ITALIC   = '\33[3m'
    URL      = '\33[4m'
    BLINK    = '\33[5m'
    BLINK2   = '\33[6m'
    SELECTED = '\33[7m'

    BLACK  = '\33[30m'
    RED    = '\33[31m'
    GREEN  = '\33[32m'
    YELLOW = '\33[33m'
    BLUE   = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE  = '\33[36m'
    WHITE  = '\33[37m'

    BLACKBG  = '\33[40m'
    REDBG    = '\33[41m'
    GREENBG  = '\33[42m'
    YELLOWBG = '\33[43m'
    BLUEBG   = '\33[44m'
    VIOLETBG = '\33[45m'
    BEIGEBG  = '\33[46m'
    WHITEBG  = '\33[47m'

    GREY    = '\33[90m'
    RED2    = '\33[91m'
    GREEN2  = '\33[92m'
    YELLOW2 = '\33[93m'
    BLUE2   = '\33[94m'
    VIOLET2 = '\33[95m'
    BEIGE2  = '\33[96m'
    WHITE2  = '\33[97m'

    GREYBG    = '\33[100m'
    REDBG2    = '\33[101m'
    GREENBG2  = '\33[102m'
    YELLOWBG2 = '\33[103m'
    BLUEBG2   = '\33[104m'
    VIOLETBG2 = '\33[105m'
    BEIGEBG2  = '\33[106m'
    WHITEBG2  = '\33[107m'

print("\33[91m████████╗\33[95m██████╗\33[91m ██████╗\33[95m ██████╗ ")
print("\33[91m╚══██╔══╝\33[95m██╔══██╗\33[91m╚════██╗\33[95m╚════██╗")
print("\33[91m   ██║   \33[95m██████╔╝\33[91m █████╔╝\33[95m █████╔╝")
print("\33[91m   ██║   \33[95m██╔══██\33[91m╗ ╚═══██╗\33[95m ╚═══██╗")
print("\33[91m   ██║   \33[95m██║  ██║\33[91m██████╔╝\33[95m██████╔╝")
print("\33[91m   ╚═╝   \33[95m╚═╝  ╚═╝\33[91m╚═════╝ \33[95m╚═════╝ ")
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("\33[91m[\33[95m+\33[91m]\33[91mCOMPUTER HOST \33[95m" +hostname)    
print("\33[91m[\33[95m+\33[91m]\33[91mCOMPUTER IP \33[95m" + IPAddr)   

print ("\33[91m[\33[95m+\33[91m] \33[95mWhois lookup")
print ("\33[91m[\33[95m+\33[91m] \33[95mDNS lookup")
print ("\33[91m[\33[95m+\33[91m] \33[95mReverse DNS lookup")
print ("\33[91m[\33[95m+\33[91m] \33[95mGeoIP lookup")
print ("\33[91m[\33[95m+\33[91m] \33[95mReverse IP lookup")
print ("\33[91m[\33[95m+\33[91m] \33[95mHttp Response")
print ("\33[91m[\33[95m+\33[91m] \33[95mPing")
print ("\33[91m[\33[95m+\33[91m] \33[95mPage Link")
print ("\33[91m[\33[95m+\33[91m] \33[95mNmap")
print ("\33[91m[\33[95m+\33[91m] \33[95mTraceroute")
	
print
print
print
ip = input("\33[91m[\33[95m+\33[91m] \33[95mEnter IP or Domain:\33[91m")
os.system ('clear')
print("\33[95m██╗██████╗     ██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗") 
print("\33[91m██║██╔══██╗    ██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗")
print("\33[95m██║██████╔╝    ██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██║  ██║")
print("\33[91m██║██╔═══╝     ██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██║  ██║")
print("\33[95m██║██║         ███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██████╔╝")
print("\33[91m╚═╝╚═╝         ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═════╝ ")
                                                                  

time.sleep(0.1)
print("\33[91m{\033[32m!\33[91m}\33[95mwhois")
whois()
print("\33[91m{\033[32m!\33[91m}\33[95mdns")
dns()
print("\33[91m{\033[32m!\33[91m}\33[95mreversedns")
reversedns()
print("\33[91m{\033[32m!\33[91m}\33[95mgeoip")
geoip()
print("\33[91m{\033[32m!\33[91m}\33[95mreverseip")
reverseip()
print("\33[91m{\033[32m!\33[91m}\33[95mhttps")
http()
print("\33[91m{\033[32m!\33[91m}\33[95mping")
ping()
print("\33[91m{\033[32m!\33[91m}\33[95mplink")
plink()
print("\33[91m{\033[32m!\33[91m}\33[95mnmap")
nmap()
print("\33[91m{\033[32m!\33[91m}\33[95mtrace")
trace()
print("bye.....")
time.sleep(3)
sys.exit()
