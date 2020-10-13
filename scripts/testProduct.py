from Api.apiFactory import ApiFactory
import logging
class TestProductApi:
    def test_product_classify_api(self):
        res = ApiFactory.get_product_api().product_classify_api()
        # 打印 请求地址 打印请求参数 打印请求响应数据
        logging.info("请求地址：{}".format(res.url))
        logging.info(f"响应数据：{res.json()}")
        # 断言状态码
        assert res.status_code == 200
        # 断言id、name、topic_img_id、description、img
        assert "id" in res.text and "name" in res.text and "topic_img_id" in res.text and "description" in res.text and "img" in res.text

        # 断言列表长度大于0
        assert len(res.json()) > 0

    def test_classify_product_api(self):
        res = ApiFactory.get_product_api().classify_product_api()
        # 打印 请求地址 打印请求参数 打印请求响应数据
        logging.info("请求地址：{}".format(res.url))
        logging.info(f"响应数据：{res.json()}")
        # 断言状态码
        assert res.status_code == 200
        # 断言列表长度大于0
        assert len(res.json()) > 0
        # 断言关键字段
        assert False not in [i in res.text for i in ["id", "name", "price", "stock"]]

    def test_product_detail_api(self):
        res = ApiFactory.get_product_api().product_detail_api()
        # 打印 请求地址 打印请求参数 打印请求响应数据
        logging.info("请求地址：{}".format(res.url))
        logging.info(f"响应数据：{res.json()}")
        # 断言状态码
        assert res.status_code == 200
        # 断言id
        assert res.json().get('id') == 2
        # 断言price
        assert res.json().get('price') == '0.01'
        # 断言name
        assert res.json().get('name') == '梨花带雨 3个'