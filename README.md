# Dexcom-CodeChallenge
Code Challenge:

This is the readme associated with the coding challenge. I have added notes to each step to better demonstrate understanding of what is being asked

Manual steps
1.	Open browser and go to https://clarity.dexcom.com/
* In this step, we simply navigate to the URL above.  
    
2.	Click "Dexcom CLARITY for Home Users"
* When the click on "Dexcom CLARITY for Home Users", browser will send GET request to https://clarity.dexcom.com/users/auth/dexcom_sts which in responce will give a 302 status code. This is a redirect to the following link: https://uam1.dexcom.com/identity/connect/authorize?client_id=DAEC20AC-9626-4B0E-94B5-B674E298F51E&prompt=&redirect_uri=https%3A%2F%2Fclarity.dexcom.com%2Fusers%2Fauth%2Fdexcom_sts%2Fcallback&response_type=code&scope=openid+offline_access&state=af1b23ba4fdb1d3b7df7a2521c2b490afcdb5767a430ee72&ui_locales=en-US This is also a redirect to link with a "signin" parameter. 
    
3.	Give the username/password: codechallenge / Password123 in the login window
* In this step we enter the username and password parameters that will be used for the POST request.
    
4.	Click Login to access Clarity home page.
* Post request is made and upon further inspection you can see that form data that is needed.
I have listed the form data below: 
      1) idsrv.xsrf
      2) username
      3) password

Test 1. Web Automation:
1.	Successfully automate manual steps by using selenium and page object model.
•	Using pycharm 
•	Pip install selenium 
•	
2.	Code completion in python is mandatory.

Test 2. API Automation:
For this test, Python request library will be used.

Test Steps:
1.	Start with a GET call to https://clarity.dexcom.com
2.	Login with username and password codechallenge / Password123
1.	Do not hardcode access-token, access-token should be retrieved from dynamic server response after login.
3.	Make HTTP POST request call to "/api/subject/1681277794575765504/analysis_session"
4.	Assert analysisSessionId should not be None
![image](https://user-images.githubusercontent.com/89505386/131060017-84250f6d-e345-419b-84a0-2bc9dbbf1956.png)
