import requests
import datetime
import json

class RequestEngine(object):
    def __init__(self,url,method):
        self.url=url
        self.method=method
        with open('request/data','r') as f:
            self.data=f.read().rstrip("\n")

        with open('request/cookie.json','r') as f:
            self.headers=json.load(f)

    def start_request(self):
        if self.method=='GET':
            response=requests.get(self.url,headers=self.headers)
            self.save_response(response.text)
        elif self.method=='POST':
            self.data_coding()
            response=requests.post(self.url,data=self.data,headers=self.headers)
            self.save_response(response.text)
        else:
            pass

    def save_response(self,text):
        time_stamp = '{0:%Y-%m-%d-%H-%M}'.format(datetime.datetime.now())
        file_name='result/'+time_stamp+'.html'
        with open(file_name,'w') as f:
            f.write(text)

    def data_coding(self):
        datas1=self.data.split('&')
        self.data={}
        for data1 in datas1:
            datas2=data1.split('=',1)
            self.data[datas2[0]]=datas2[1]


        print(self.data)
