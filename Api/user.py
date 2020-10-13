import requests
import app,logging


class UserApi:
    def __init__(self):
        # 获取token
        self.get_token_url = app.base_url + '/token/user'
        # token验证
        self.token_verify_url = app.base_url + '/token/verify'
        # 用户地址信息
        self.user_address_url = app.base_url + '/address'

    def get_token_api(self):
        # 请求体
        data = {'code': app.code}
        logging.info("用户-获取token")
        return requests.post(self.get_token_url, json=data, headers=app.headers)

    def verify_token_api(self):
        # 请求参数
        data = {"token": app.headers.get("token")}
        logging.info("用户-token验证")
        # 返回响应对象
        return requests.post(self.token_verify_url, json=data, headers=app.headers)

    def user_address_api(self):
        """用户地址信息"""
        logging.info("用户-用户地址信息")
        # 返回响应对象
        return requests.get(self.user_address_url, headers=app.headers)
