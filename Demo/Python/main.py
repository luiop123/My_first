# #以下代码是将【本地图片】进行文字识别
# -*- coding: utf-8 -*-
#pip install tencentcloud-sdk-python
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models
import base64
import json
import jsonpath
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models
try:
    # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
    # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
    # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
    cred = credential.Credential("AKIDW1V1SkriMxJQTXVGmGVWHn7C1qhOq8E8", "yMix3wcFfsraBkElPLAtUuJg4RjsulMp")
    # 实例化一个http选项，可选的，没有特殊需求可以跳过
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"

    # 实例化一个client选项，可选的，没有特殊需求可以跳过
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    # 实例化要请求产品的client对象,clientProfile是可选的

    client = ocr_client.OcrClient(cred, "ap-shanghai", clientProfile)
    # 实例化一个请求对象,每个接口都会对应一个request对象
    req = models.RecognizeTableAccurateOCRRequest()
    params = {
        "ImageUrl": "https://th.bing.com/th/id/R.b8b0d750540eaeaab04163678ed55641?rik=RLtB%2bwS%2bjAwG0A&riu=http%3a%2f%2fimg95.699pic.com%2fexcel%2f40015%2f8976.jpg!%2fcrop%2f0x1400a0a1400%2ffw%2f850%2fquality%2f90&ehk=WKUs1auwe8JkIEJl6l4r0K4XxmEvb2%2fKTF36Ve9PxLo%3d&risl=&pid=ImgRaw&r=0"
    }

    image_path = 'D:\\PycharmProject\\pythonProject2\\R-C (1).jpg'

    with open(image_path, 'rb') as f:  # 以二进制读取本地图片
        data = f.read()
        encodestr = str(base64.b64encode(data), 'utf-8')  # base64编码图片
    req.from_json_string(json.dumps(params))
    # req.ImageBase64 = encodestr

    # 返回的resp是一个RecognizeTableAccurateOCRResponse的实例，与请求对象对应
    resp = client.RecognizeTableAccurateOCR(req)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)