
import requests
import json

capmonster_apikey = "ENTER YOUR APIKEY HERE"

while True: 


#########################################
 taskId = requests.post('https://api.capmonster.cloud/createTask', json={
  "clientKey":capmonster_apikey,
  "task":
  {
      "type":"HCaptchaTaskProxyless",
      "websiteURL":"http://piggyawesome.com/captcha/hcaptcha.html",
      "websiteKey":"be45eabf-9b3c-47da-9355-a8826037e630",
  }
  })

 print("Doing captcha be45eabf-9b3c-47da-9355-a8826037e630:   " + str(taskId.status_code))
 print(taskId.text)
 '''
 taskId = json.loads(taskId.text)['taskId']
 response = requests.post('https://api.capmonster.cloud/getTaskResult', json={
    "clientKey":capmonster_apikey,
    "taskId": taskId
 })




 data={'captcha_key': response}
 reply = requests.post("http://piggyawesome.com/captcha/hcaptcha.html", data=data)
 print("Awnser:"+ response.text)
 print("Submitting captcha: " + str(reply.status_code))
 '''
################################
 taskId2 = requests.post('https://api.capmonster.cloud/createTask', json={
  "clientKey":capmonster_apikey,
  "task":
  {
      "type":"HCaptchaTaskProxyless",
      "websiteURL":"http://piggyawesome.com/captcha/hcaptcha.html",
      "websiteKey":"25ce5b61-92a3-4c8e-9971-a53ff887e829",
  }
  })

 print("Doing captcha 25ce5b61-92a3-4c8e-9971-a53ff887e829:   " + str(taskId2.status_code))
 print(taskId2.text)
 
'''
 taskId2 = json.loads(taskId2.text)['taskId']

  response2 = requests.post('https://api.capmonster.cloud/getTaskResult', json={
    "clientKey":capmonster_apikey,
    "taskId": taskId2
 })




 data={'captcha_key': response2}
 reply2 = requests.post("http://piggyawesome.com/captcha/hcaptcha.html", data=data)
 print("Awnser:"+ response2.text)
 print("Submitting captcha: " + str(reply2.status_code))

'''


 






 
