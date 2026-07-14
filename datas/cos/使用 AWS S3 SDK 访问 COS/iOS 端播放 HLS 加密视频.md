<!-- source: https://cloud.tencent.com/document/product/436/106774 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:18:10+08:00 -->

# iOS 端播放 HLS 加密视频

最近更新时间：2025-05-30 15:07:12


## 前提条件

创建加密视频，搭建 token 服务，详情请参见 [HLS 视频加密播实践](https://cloud.tencent.com/document/product/460/59291)。

## iOS 端播放指引

**注意：**

配置支持 HTTP 请求，需要在项目的 info.plist 文件中添加 `App Transport Security Settings -> Allow Arbitrary Loads` 并将其设置为 YES。

iOS 端使用 CIPlayerAssistor SDK 中封装好的 CIPlayerAssistor 和 CIMediaConfig 对象来播放 m3u8 文件，用户按照如下规则传入参数，即可实现播放功能。

1. 集成 CIPlayerAssistor SDK

1.1 podfile 文件中新增如下内容并执行`pod install`。

pod 'CIPlayerAssistor'

1.2 导入头文件。

#import <CIPlayerAssistor/CIPlayerAssistor.h>

2. 构造 CIPlayerAssistor 和 CIMediaConfig 对象

CIMediaConfig 参数说明如下：

参数名 说明 是否必填 类型 默认值
fileUrl 请求m3u8接口的文件地址 是 NSString 无

CIPlayerAssistor 参数说明如下：

参数名 说明 是否必填 类型 默认值
config 媒体文件配置信息 是 CIMediaConfig 无
url 调用业务服务返回的带签名的视频链接 是 NSString 无

## iOS 端完整示例代码

@property (strong, nonatomic)AVPlayer *myPlayer;//播放器

@property (strong, nonatomic)AVPlayerItem *item;//播放单元

@property (strong, nonatomic)AVPlayerLayer *playerLayer;//播放界面（layer）

// 创建媒体配置对象

// fileUrl：文件链接。

CIMediaConfig * config = [[CIMediaConfig alloc]initWithFileUrl:@"[https://ci-1251902136.cos.ap-chongqing.myqcloud.com/hls/encrypt/test.m3u8](https://ci-1251902136.cos.ap-chongqing.myqcloud.com/hls/encrypt/test.m3u8)"];

[[CIPlayerAssistor singleAssistor] setDebug:NO];// 关闭日志打印

// CIMediaConfig 类在实例化时 自动生成了公钥 config.publicKey;

[self getToken:config.publicKey fileURL:config.fileUrl protectContentKey:1 callBack:^(NSString * _Nonnull url) {

 dispatch_async(dispatch_get_main_queue(), ^{

 // 设置授权信息，会在 url 上通过&拼接传入的 signature

 // 如果原始 url 是 cdn 的话，不用传 cos 的 signature

 [[CIPlayerAssistor singleAssistor] buildPlayerUrlWithConfig:self.config withUrl:url buildUrlcallBack:^(NSString * _Nullable url, NSError * _Nullable error) {

 AVPlayerItem *item = [[AVPlayerItem alloc] initWithURL:[NSURL URLWithString:url]];

 self.myPlayer = [AVPlayer playerWithPlayerItem:item];

 self.playerLayer = [AVPlayerLayer playerLayerWithPlayer:self.myPlayer];

 self.playerLayer.frame = CGRectMake(0, 100, self.view.bounds.size.width, 300);

 [self.view.layer addSublayer:self.playerLayer];

 [self.myPlayer play];

 }];

 });

}];

- (void)getToken:(NSString *)publickey fileURL:(NSString *)fileURL protectContentKey:(int)protect callBack:(void (^)(NSString * url))callBack{

 // 该 url 仅为示例，请替换成您业务的 url，具体实现请参考 “业务后端示例代码”

 NSMutableURLRequest * mrequest = [[NSMutableURLRequest alloc]initWithURL:[NSURL URLWithString:@"https://cos.cloud.tencent.com/samples/hls/token"]];

 mrequest.HTTPMethod = @"POST";

 [mrequest setValue:@"application/json" forHTTPHeaderField:@"Content-Type"];

 NSData *data = [publickey dataUsingEncoding:NSUTF8StringEncoding];

 publickey = [data base64EncodedStringWithOptions:0];

 NSString * objectKey = [NSURL URLWithString:fileURL].path;

 if ([objectKey hasPrefix:@"/"]) {

 objectKey = [objectKey substringFromIndex:1];

 }

 NSDictionary * body = @{

 @"objectKey":objectKey,

 @"publicKey":publickey,

 @"protectContentKey":@(protect)

 };

 mrequest.HTTPBody = [NSJSONSerialization dataWithJSONObject:body options:NSJSONWritingFragmentsAllowed error:nil];

 [[[NSURLSession sharedSession]dataTaskWithRequest:mrequest completionHandler:^(NSData * _Nullable data, NSURLResponse * _Nullable response, NSError * _Nullable error) {

 NSDictionary * result = [NSJSONSerialization JSONObjectWithData:data options:NSJSONReadingAllowFragments error:nil];

 callBack(result[@"playUrl"]);

 }]resume];

}

## Demo 体验

我们提供了终端播放 HLS 私有加密视频的示例，请参见 [CIPlayerAssistor Demo](https://github.com/tencentyun/CIPlayerAssistor_iOS)。
