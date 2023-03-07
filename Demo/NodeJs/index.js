const tencentcloud = require("tencentcloud-sdk-nodejs")
const fs = require("fs");
const util = require("util");

const OCRClient = tencentcloud.ocr.v20181119.Client

const client = new OCRClient({
    credential: {
        secretId: "AKIDW1V1SkriMxJQTXVGmGVWHn7C1qhOq8E8",
        secretKey: "yMix3wcFfsraBkElPLAtUuJg4RjsulMp",
    },
    // 产品地域
    region: "ap-guangzhou",
})

const sample_img = fs.readFileSync('sample.jpg', {encoding: 'base64'});

client.RecognizeTableAccurateOCR(
    {
        ImageBase64: sample_img.toString(),
    },
).then(
    (data) => {
        console.log(util.inspect(data, {depth: null}))
    },
    (err) => {
        console.error(err)
    }
)