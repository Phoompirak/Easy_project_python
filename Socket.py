from socket import*

def ip_connect(x, y):
    ip = gethostbyname(y)
    print(f"IP of {y} is :{ip}")

web = input("Website :")
ip_connect(web, web)