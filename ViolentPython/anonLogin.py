import ftplib


def anonLogin(hostname):
    try:
        ftp = ftplib.FTP()
        ftp.connect(hostname, 2121)
        ftp.login('anonymous', 'me@your.com')
        print('\n[*] %s FTP Anonymous Login Succeeded!' % hostname)
        ftp.quit()
        return True
    except Exception as e:
        print('\n[-] %s FTP Anonymous Login Failed!' % hostname)
        return False


def main():
    host = '192.168.137.195'
    anonLogin(host)


if __name__ == '__main__':
    main()
