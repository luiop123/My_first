package main

import (
	"fmt"
	// "io/ioutil"

	v20181119 "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/ocr/v20181119"
)

func main() {
	cli, err := v20181119.NewClientWithSecretId("AKIDW1V1SkriMxJQTXVGmGVWHn7C1qhOq8E8",
		"yMix3wcFfsraBkElPLAtUuJg4RjsulMp",
		"ap-guangzhou")
	if err != nil {
		panic(err)
	}

	// srcByte, err := ioutil.ReadFile(`sample.jpg`)
	// if err != nil {
	// 	panic(err)
	// }
	// srcByte1=srcByte
	//imageBase64 := base64.StdEncoding.EncodeToString(srcByte)

	imageUrl := "https://ts1.cn.mm.bing.net/th/id/R-C.074dcd4c5cb219bde88b368af0153dd3?rik=eKTBmnMuXA9zEQ&riu=http%3a%2f%2fimg02.tuke88.com%2fpreview%2f1535477%2f00%2f00%2f72%2f5b0bc75e52cb3.jpg-0.jpg!%2ffw%2f800%2fquality%2f90%2funsharp%2ftrue%2fcompress%2ftrue&ehk=3nA900m1LbUNEKdE%2fDBFgWzQwQI%2bj1OXoqHnYpZUyDc%3d&risl=&pid=ImgRaw&r=0"
	req := v20181119.NewRecognizeTableAccurateOCRRequest()
	req.ImageUrl = &imageUrl
	//req.ImageBase64 = &imageBase64
	res, err := cli.RecognizeTableAccurateOCR(req)
	if err != nil {
		panic(err)
	}
	fmt.Println(res.ToJsonString())
}
