import requests
from .exceptions import *
import time

class FCaptcha:
    def __init__(self, api_key : str) -> None:
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": self.api_key
        })

    def _create_task(self, data):
        r = self.session.post("https://api.fcaptcha.lol/api/createTask", json=data)
        if task := r.json().get("task"):
            if task_id := task.get("task_id"):
                return task_id
        raise parse_exception(r.json().get("error"))
    
    def _get_task_result(self, task_id : str):
        r = self.session.post("https://api.fcaptcha.lol/api/getTaskData", json={
            "task_id": task_id
        })
        try:
            data = r.json()
        except:
            raise FCaptchaDownException()
        return data


    def get_balance(self) -> float:
        r = self.session.get(f"https://api.fcaptcha.lol/get_balance/{self.api_key}")
        try:
            data = r.json()
        except:
            raise FCaptchaDownException()
        if balance := data.get("balance"):
            return balance
        
        raise parse_exception(data.get("message"))
    
    def solve_hcaptcha(
            self,
            sitekey : str,
            host : str,
            proxy : str,
            rqdata : str = None,
            user_agent : str = None,
    ):
        payload = {
            "sitekey": sitekey,
            "host": host,
            "proxy": proxy,   
        }
        if rqdata:
            payload["rqdata"] = rqdata
        if user_agent:
            payload["user_agent"] = user_agent
        task_id = self._create_task(payload)
        while True:
            time.sleep(3)
            result = self._get_task_result(task_id)
            if result["task"]["state"] == "processing":
                continue
            if result["task"]["state"] == "completed":
                return result["task"]["captcha_key"]
            
            raise FcaptchaTaskFailedException()
        
        

    