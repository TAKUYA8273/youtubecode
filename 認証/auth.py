import requests
import json

def authorization():
    content_type = "application/x-www-form-urlencoded"
    client = "MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE="
    code = input(f"https://www.epicgames.com/id/api/redirect?clientId=3446cd72694c4a4485d81b77adbb2141&responseType=code にアクセスして、fnauth/?code= の後の文字列をコピーし、貼り付けてください ")
    authorization_code = requests.post("https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token",
        headers={"Content-Type":content_type,"Authorization":f"basic {client}"},
        data={"grant_type":"authorization_code","code":f"{code}"}
    ).json()
    create_device_auth = requests.post(f"https://account-public-service-prod.ol.epicgames.com/account/api/public/account/{authorization_code['account_id']}/deviceAuth",
        headers={"Authorization":f"Bearer {authorization_code['access_token']}"}
    ).json()
    device_auth = {
        "device_id":f"{create_device_auth['deviceId']}","account_id":f"{create_device_auth['accountId']}","secret":f"{create_device_auth['secret']}"
    }
    with open("device_auths.json","w") as f:
        json.dump(device_auth,f)

if __name__ == "__main__":
    authorization()
