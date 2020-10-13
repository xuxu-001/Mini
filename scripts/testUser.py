import logging

from Api.apiFactory import ApiFactory
import app, utils, pytest


@pytest.mark.run(code=0)
class TestUserApi:
    def test_get_token(self):
        # 响应对象
        res = ApiFactory.get_user_api().get_token_api()
        # 打印 请求地址 打印请求参数 打印请求响应数据
        logging.info("请求地址：{}".format(res.url))
        logging.info(f"响应数据：{res.json()}")
        # 断言状态码
        # assert res.status_code == 200
        utils.common_assert_code(res)
        # 断言token存在
        assert len(res.json().get("token")) > 0
        # 保存token
        app.headers['token'] = res.json().get('token')
        print("app.headers:{}".format(app.headers))

    def test_verify_api(self):
        # 响应对象
        res = ApiFactory.get_user_api().verify_token_api()
        # 打印 请求地址 打印请求参数 打印请求响应数据
        logging.info("请求地址：{}".format(res.url))
        logging.info(f"响应数据：{res.json()}")
        # 断言状态码
        # assert res.status_code == 200
        utils.common_assert_code(res)
        # 断言有效
        assert res.json().get('isValid') is True

    def test_user_address_api(self):
        # 响应对象
        res = ApiFactory.get_user_api().user_address_api()
        # 打印 请求地址 打印请求参数 打印请求响应数据
        logging.info("请求地址：{}".format(res.url))
        logging.info(f"响应数据：{res.json()}")
        # 断言状态码
        # assert res.status_code == 200
        utils.common_assert_code(res)
        # 断言信息
        assert False not in [i in res.text for i in ['天天', "13355555555", "上海市", "浦东新区", "110号"]]
