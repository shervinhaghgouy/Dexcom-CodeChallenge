import requests

from config import USERNAME, PASSWORD

with requests.session() as session:

    #Step 1: Start with a GET call
    get_url = 'https://clarity.dexcom.com'
    step_one = session.get(get_url)
    print(step_one)

    #Step2: 2.	Login with username and password
    #This is the URL called when 'Dexcom CLARITY for Home User' is clicked
    getidsrv_url = 'https://clarity.dexcom.com/users/auth/dexcom_sts'
    getidsrv = session.get(getidsrv_url)

    #Get url with signin parameter ex: https://uam1.dexcom.com/identity/login?signin=3fb176b0d9e556b5cab1a007f4c4f3d2
    post_url = getidsrv.url

    #Parameters needed for post: Username / Password / idsrv.xsrf
    idsrv_xsrf = getidsrv.cookies["idsrv.xsrf"]
    login_data = {
                'idsrv.xsrf' : idsrv_xsrf,
                'username' : USERNAME,
                'password' : PASSWORD
    }
    step_two = session.post(post_url, data=login_data)
    print(step_two.content)

    #Step 3: make HTTP POST request call to "/api/subject/1681277794575765504/analysis_session"
    base_url = 'https://clarity.dexcom.com/api/subject/1681277794575765504/analysis_session'
    # need acces token -> could not find this token. Used POSTMAN to verify by manually obtaining the access token. Please refer to README page for POSTMAN results. 
    api_request = session.post(base_url, data=login_data)
    print(api_request.content)
