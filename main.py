#!/usr/bin/python
#-*-coding:UTF-8-*-

from request.engine import RequestEngine

import sys
import getopt

def main(argv):
    url=""
    method=""

    try:
        opts,args=getopt.getopt(argv,"hu:m:",["help","url=","method="])
    except getopt.GetoptError:
        print("Error:main.py -u <url> -m <method:GET/POST>")
        print("or:main.py --url <url> --method <method:GET/POST>")
        sys.exit(2)

    for opt,arg in opts:
        if opt in ("-h","--help"):
            print("main.py -u <url> -m <method:GET/POST>")
            print("or:main.py --url <url> --method <method:GET/POST>")
            sys.exit()
        elif opt in ("-u","--url"):
            url=arg
        elif opt in ("-m","--method"):
            method=arg
            
    if url=="":
        print("ERROR:You should provide me a url")
        sys.exit(2)

    requestengine=RequestEngine(url,method)
    requestengine.start_request()


if __name__=="__main__":
    main(sys.argv[1:])
    
