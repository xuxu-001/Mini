from Api.apiFactory import ApiFactory

# 实例化HomeApi

# # 调用轮播图
# print("轮播图:{}".format(ApiFactory.get_home_api().banner_api().json()))
# # 调用主题
# print("主题：{}".format(ApiFactory.get_home_api().theme_api().json()))
# # 调用最近新品
# print("最近新品：{}".format(ApiFactory.get_home_api().recent_product_api().json()))
# 调用商品分类
# print("分类：{}".format(ApiFactory.get_product_api().product_classify_api().json()))
# # 调用分类下商品
# print("分类下商品：{}".format(ApiFactory.get_product_api().classify_product_api().json()))
# # 调用商品信息
# print("商品信息：{}".format(ApiFactory.get_product_api().product_detail_api(26).json()))
# 获取token
# print("返回值：{}".format(ApiFactory.get_user_api().get_token_api().json()))
# print("用户名{}".format(ApiFactory.get_user_api().user_address_api().json()))

print("查看订单：{}".format(ApiFactory.get_order_api().order_list_api().json()))
print("创建订单：{}".format(ApiFactory.get_order_api().create_order_api(12,7).json()))
print("查看订单：{}".format(ApiFactory.get_order_api().query_order_api(71).json()))