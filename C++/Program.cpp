#include <tencentcloud/core/Credential.h>
#include <tencentcloud/core/profile/ClientProfile.h>
#include <tencentcloud/core/profile/HttpProfile.h>
#include <tencentcloud/ocr/v20181119/OcrClient.h>
#include <tencentcloud/ocr/v20181119/model/RecognizeTableAccurateOCRRequest.h>
#include <tencentcloud/ocr/v20181119/model/RecognizeTableAccurateOCRResponse.h>
#include <iostream>
#include <string>
#include <vector>

using namespace TencentCloud;
using namespace TencentCloud::Ocr::V20181119;
using namespace TencentCloud::Ocr::V20181119::Model;
using namespace std;

int main() {
        // 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        Credential cred = Credential("AKIDW1V1SkriMxJQTXVGmGVWHn7C1qhOq8E8", "yMix3wcFfsraBkElPLAtUuJg4RjsulMp");

        // 实例化一个http选项，可选的，没有特殊需求可以跳过
        HttpProfile httpProfile = HttpProfile();
        httpProfile.SetEndpoint("ocr.tencentcloudapi.com");

        // 实例化一个client选项，可选的，没有特殊需求可以跳过
        ClientProfile clientProfile = ClientProfile();
        clientProfile.SetHttpProfile(httpProfile);
        // 实例化要请求产品的client对象,clientProfile是可选的
        OcrClient client = OcrClient(cred, "ap-shanghai", clientProfile);

        // 实例化一个请求对象,每个接口都会对应一个request对象
        RecognizeTableAccurateOCRRequest req = RecognizeTableAccurateOCRRequest();
        
        //req.SetImageBase64("vdfvdv");
        req.SetImageUrl("https://th.bing.com/th/id/R.b8b0d750540eaeaab04163678ed55641?rik=RLtB%2bwS%2bjAwG0A&riu=http%3a%2f%2fimg95.699pic.com%2fexcel%2f40015%2f8976.jpg!%2fcrop%2f0x1400a0a1400%2ffw%2f850%2fquality%2f90&ehk=WKUs1auwe8JkIEJl6l4r0K4XxmEvb2%2fKTF36Ve9PxLo%3d&risl=&pid=ImgRaw&r=0");

        // 返回的resp是一个RecognizeTableAccurateOCRResponse的实例，与请求对象对应
        auto outcome = client.RecognizeTableAccurateOCR(req);
        if (!outcome.IsSuccess())
        {
            cout << outcome.GetError().PrintAll() << endl;
            return -1;
        }
        RecognizeTableAccurateOCRResponse resp = outcome.GetResult();
        // 输出json格式的字符串回包
        cout << resp.ToJsonString() << endl;
    
    return 0;
}