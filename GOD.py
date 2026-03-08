import socket
import requests

def start_recon(url):
    print(f"\n[+] Starting Recon on: {url}")
    target = url.replace("https://", "").replace("http://", "").split('/')[0]
    
    # 1. جلب عنوان الـ IP (الموقع الجغرافي للبيانات)
    try:
        ip = socket.gethostbyname(target)
        print(f"[*] Target IP: {ip}")
    except:
        print("[!] Could not resolve IP.")

    # 2. فحص تقنية السيرفر (Header Analysis)
    try:
        response = requests.get(url)
        server = response.headers.get('Server')
        print(f"[*] Web Server: {server if server else 'Unknown'}")
        
        # التأكد من وجود حماية
        if "cloudflare" in str(server).lower():
            print("[!] Security: Cloudflare detected (Hard to bypass)")
        else:
            print("[+] Security: No Cloudflare detected (Direct access)")
    except:
        print("[!] Could not fetch Headers.")

# جرب السكربت على موقع (لأغراض تعليمية فقط)
target_url = input("Enter target URL (with http/https): ")
start_recon(target_url)
