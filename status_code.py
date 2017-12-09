import requests
import json
# headers = {
# 	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
# 	 "Accept-Encoding":"gzip, deflate",
# 	 "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8",
# 	 "Cache-Control":"no-cache",
# 	 "Connection":"keep-alive",
# 	 "Content-Length":"2207",
# 	"Content-Type":"application/x-www-form-urlencoded",
# 	 "Cookie":"_privy_BEFC766EA2C2ED7B4D2D2340=%7B%22uuid%22%3A%22b72744d3-003f-4308-bd36-49fcd4d44a63%22%2C%22variations%22%3A%7B%7D%2C%22country_code%22%3A%22IN%22%7D; ASP.NET_SessionId=zmghqudpmsbn0zirtavbm3wn; _privy_match_session=1; _privy_lr=1; __utmt=1; _privy_a=%7B%22referring_domain%22%3Anull%2C%22referring_url%22%3A%22%22%2C%22utm_medium%22%3A%22unknown%22%2C%22utm_source%22%3Anull%2C%22search_term%22%3Anull%2C%22initial_url%22%3A%22http%3A%2F%2Fkit19.com%2F%22%2C%22sessions_count%22%3A3%2C%22pages_viewed%22%3A22%7D; _privy_b=%7B%22referring_domain%22%3Anull%2C%22referring_url%22%3A%22%22%2C%22utm_medium%22%3A%22unknown%22%2C%22utm_source%22%3Anull%2C%22search_term%22%3Anull%2C%22initial_url%22%3A%22http%3A%2F%2Fkit19.com%2F%22%2C%22pages_viewed%22%3A12%7D; __utma=168107323.530769249.1505381229.1505383928.1510221054.3; __utmb=168107323.11.10.1510221054; __utmc=168107323; __utmz=168107323.1505381229.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __unam=7639673-15e7fb6b353-2cb4591b-21",
# 	 "Host":"kit19.com",
# 	 "Origin":"http://kit19.com",
# 	 "Pragma":"no-cache",
# 	 "Referer":"http://kit19.com/",
# 	 "Upgrade-Insecure-Requests":"1",
# 	 "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"
# }

# body={
#  	"txtcountrycode":"+91",
#  	"txtMobile":"",
# 	"txtUserName":"designco716292",
# 	"txtPassword":"4855",
# 	"chktc":"on",
#  	"btnLoginFor":"login",
# 	"txtcountrycode1":"+91",
# 	"txttrydemomobileno":"",
#  	"__EVENTTARGET":"",
# 	"__EVENTARGUMENT":"",
#  	"__VIEWSTATE":"/wEPDwULLTE3NzgyOTI4MTEPFgIeBnVwZGF0ZQUcMTElMmY5JTJmMjAxNyszJTNhNDclM2EzMCtQTRYCAgMPZBYMAgMPDxYCHghJbWFnZVVybAUdfi91cGxvYWRfbG9nby8xMzY2OF9LaXQxOS5wbmdkZAIFDxYCHgVzdHlsZQUNZGlzcGxheTpibG9ja2QCCA8PFgIfAQUdfi91cGxvYWRfbG9nby8xMzY2OF9LaXQxOS5wbmdkZAIcD2QWBmYPZBYGAgMPFgIeB1Zpc2libGVoFgICAQ8PFgIfAQUUfi9pbWcvYmFja19zbGlkZS5qcGdkZAIpDxYCHwIFe3dpZHRoOjJweCAhaW1wb3J0YW50O2JhY2tncm91bmQtcG9zaXRpb246cmlnaHQ7YmFja2dyb3VuZC1yZXBlYXQ6bm8tcmVwZWF0O21hcmdpbjo1cHggMHB4IDBweCAwcHg7aGVpZ2h0OjFweDtkaXNwbGF5OmJsb2NrO2QCLQ8WAh8CBQ1kaXNwbGF5OmJsb2NrZAICD2QWBAIRDzwrABECARAWABYAFgAMFCsAAGQCEw88KwARAwAPFgQeC18hRGF0YUJvdW5kZx4LXyFJdGVtQ291bnRmZAEQFgAWABYADBQrAABkAgQPZBYCAgEPZBYGAgcPFgIfA2hkAgoPZBYEAgsPEA8WBh4NRGF0YVRleHRGaWVsZAUKU3RhdGVfTmFtZR4ORGF0YVZhbHVlRmllbGQFCFN0YXRlX0lEHwRnZBAVIAxTZWxlY3QgU3RhdGUPQW5kaHJhIFByYWRlc2ggEUFydW5hY2hhbCBQcmFkZXNoBUFzc2FtBUJpaGFyDENoaGF0dGlzZ2FyaAVEZWxoaQNHb2EHR3VqYXJhdAdIYXJ5YW5hEEhpbWFjaGFsIFByYWRlc2gRSmFtbXUgYW5kIEthc2htaXIJSmhhcmtoYW5kCUthcm5hdGFrYQZLZXJhbGEOTWFkaHlhIFByYWRlc2gLTWFoYXJhc2h0cmEHTWFuaXB1cglNZWdoYWxheWEHTWl6b3JhbQhOYWdhbGFuZAZPcmlzc2EFb3RoZXIKUHVkdWNoZXJyeQZQdW5qYWIJUmFqYXN0aGFuBlNpa2tpbQpUYW1pbCBOYWR1B1RyaXB1cmENVXR0YXIgUHJhZGVzaAtVdHRhcmFraGFuZAtXZXN0IEJlbmdhbBUgDFNlbGVjdCBTdGF0ZQExATIBMwE0ATUBNgE3ATgBOQIxMAIxMQIxMgIxMwIxNAIxNQIxNgIxNwIxOAIxOQIyMAIyMQIzMQIyMgIyMwIyNAIyNQIyNgIyNwIyOQIyOAIzMBQrAyBnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBZmQCDQ8QZBAVAQtTZWxlY3QgQ2l0eRUBC1NlbGVjdCBDaXR5FCsDAWcWAWZkAgwPFgIfA2hkAh4PZBYKAgEPDxYCHgRUZXh0BQZEZWxoaS1kZAIDDw8WAh8IBQwwMTEtNDU3Mjg5MDBkZAIFDw8WAh8IBQw5MTk5MTAwMjUwNDJkZAIHDw8WAh8IBRNjb250YWN0dXNAa2l0MTkuY29tZGQCCQ8PFgIfCAUQaHR0cDovL2tpdDE5LmNvbWRkAiAPFgIfA2gWCAIDDw8WAh8IBQZEZWxoaS1kZAIFDw8WAh8IBRNjb250YWN0dXNAa2l0MTkuY29tZGQCBw8PFgIfCAUMOTE5OTEwMDI1MDQyZGQCCQ8PFgIfCAUQaHR0cDovL2tpdDE5LmNvbWRkGAQFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYCBQdpbWdIb21lBQVjaGt0YwUQTXVsdGlWaWV3RGlzcGxheQ8PZGZkBQhncmRQcm9tbw88KwAMAQhmZAUMZGF0YWdyaWR2aWV3D2dkAbUPupbAl82pladZXhPrfAiJ86NTQFwvSq4u7E2t5T4=",
#  	"__VIEWSTATEGENERATOR": "90059987"

#  }

response = requests.get("https://admin.jeruk-emas.org/login")

# Check status code for lottery admin.
print(response.status_code)

if response.status_code ==100:
    print("server is working fine")


else:
	response2=requests.get("http://www.kit19.com/ComposeSMS.aspx?username=designco716292&password=4855&sender=DSGNCO&to=9532991671&message=Their%20is%20some%20technical%20issue%20in%20lottery%20admin%20pannel%20please%20check%20it%20immediately&priority=1&dnd=1&unicode=0")

	
# Check status code for lottery "cmd36.com".	
response3 = requests.get("https://cmd36.com/")

print(response3.status_code)

if response3.status_code ==100:
    print("server is working fine")


else:
	response3=requests.get("http://www.kit19.com/ComposeSMS.aspx?username=designco716292&password=4855&sender=DSGNCO&to=9532991671&message=Their%20is%20some%20technical%20issue%20in%20lottery%20cmd36.com%20pannel%20please%20check%20it%20immediately&priority=1&dnd=1&unicode=0")

# Check status code for lottery "csovegas.com/".	
response4 = requests.get("https://csovegas.com/")

print(response4.status_code)

if response4.status_code ==100:
    print("server is working fine")


else:
	response4=requests.get("http://www.kit19.com/ComposeSMS.aspx?username=designco716292&password=4855&sender=DSGNCO&to=9532991671&message=Their%20is%20some%20technical%20issue%20in%20lottery%20csovegas.com%20pannel%20please%20check%20it%20immediately&priority=1&dnd=1&unicode=0")	
	
	
# Check status code for lottery "ibet36.net/".	
response5 = requests.get("https://ibet36.net/")

print(response5.status_code)

if response5.status_code ==100:
    print("server is working fine")


else:
	response5=requests.get("http://www.kit19.com/ComposeSMS.aspx?username=designco716292&password=4855&sender=DSGNCO&to=9532991671&message=Their%20is%20some%20technical%20issue%20in%20lottery%20ibet36.net%20pannel%20please%20check%20it%20immediately&priority=1&dnd=1&unicode=0")	

# Check status code for lottery "ibet36.com/".	
response6 = requests.get("https://ibet36.com")

print(response6.status_code)

if response6.status_code ==100:
    print("server is working fine")


else:
	response6=requests.get("http://www.kit19.com/ComposeSMS.aspx?username=designco716292&password=4855&sender=DSGNCO&to=9532991671&message=Their%20is%20some%20technical%20issue%20in%20lottery%20ibet36.com%20pannel%20please%20check%20it%20immediately&priority=1&dnd=1&unicode=0")		
	
	
# response1 =requests.get("http://kit19.com/",data=json.dumps(body), headers=headers)

    # print(response1.status_code)
    # akanksha461%20

    # http://www.kit19.com/ComposeSMS.aspx?username=designco716292&password=4855&sender=DCOMBD&to=8591771290&message=Message&priority=1&dnd=1&unicode=0


    # http://www.kit19.com/AddSenderId.aspx?username=designco716292&password=4855&SenderId=DCOMBD&SenderIdType=GSM 

