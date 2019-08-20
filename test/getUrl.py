import requests

def geturl(url):
	try:
		r=requests.get(url, timeout=100)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		return "异常"

if __name__ =="__main__":
	url = "http://jwweb.scujcc.cn/"
	print(geturl(url))