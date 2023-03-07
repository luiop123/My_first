import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.common.profile.HttpProfile;
import java.util.Base64;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;
import com.tencentcloudapi.ocr.v20181119.OcrClient;
import com.tencentcloudapi.ocr.v20181119.models.*;
import java.io.*;
public class RecognizeTableAccurateOCR
{
    public static void main(String [] args) {
        try{
            // 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
            // 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
            // 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
            Credential cred = new Credential("AKIDW1V1SkriMxJQTXVGmGVWHn7C1qhOq8E8", "yMix3wcFfsraBkElPLAtUuJg4RjsulMp");
            // 实例化一个http选项，可选的，没有特殊需求可以跳过
            HttpProfile httpProfile = new HttpProfile();
            httpProfile.setEndpoint("ocr.tencentcloudapi.com");
            String imagePath = "D:\\demo\\MyProject02\\images\\R-C (1).jpg";
            InputStream inputStream = null;
            byte[] buffer = null;
            //读取图片字节数组
            try {
                inputStream = new FileInputStream(imagePath);
                int count = 0;
                while (count == 0) {
                    count = inputStream.available();
                }
                buffer = new byte[count];
                inputStream.read(buffer);
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                if (inputStream != null) {
                    try {
                        // 关闭inputStream流
                        inputStream.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }
            String imageBase64 = Base64.getEncoder().encodeToString(buffer);

            // 实例化一个client选项，可选的，没有特殊需求可以跳过
            ClientProfile clientProfile = new ClientProfile();
            clientProfile.setHttpProfile(httpProfile);
            // 实例化要请求产品的client对象,clientProfile是可选的
            OcrClient client = new OcrClient(cred, "ap-shanghai", clientProfile);
            // 实例化一个请求对象,每个接口都会对应一个request对象
            RecognizeTableAccurateOCRRequest req = new RecognizeTableAccurateOCRRequest();
//            req.setImageUrl("fgb");
            req.setImageBase64(imageBase64);
            // 返回的resp是一个RecognizeTableAccurateOCRResponse的实例，与请求对象对应
            RecognizeTableAccurateOCRResponse resp = client.RecognizeTableAccurateOCR(req);
            // 输出json格式的字符串回包
            System.out.println(RecognizeTableAccurateOCRResponse.toJsonString(resp));
        } catch (TencentCloudSDKException e) {
            System.out.println(e.toString());
        }
    }
}
    /**
     * imgFile 图片本地存储路径
     */
