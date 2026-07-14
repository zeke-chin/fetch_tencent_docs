<!-- source: https://cloud.tencent.com/document/product/436/63683 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T18:03:52+08:00 -->

# 媒体 bucket 接口

最近更新时间：2023-09-21 20:29:45


## 简介

本文档提供关于媒体 bucket 接口的 API 概览和 SDK 示例代码。

API 操作名 操作描述
[DescribeMediaBuckets](https://cloud.tencent.com/document/product/436/48988)查询媒体处理开通情况 用于查询已经开通媒体处理功能的存储桶

## SDK API 参考

SDK 所有接口的具体参数与方法说明，请参见 [SDK API](https://cos-ios-sdk-doc-1253960454.file.myqcloud.com/)。

## 查询媒体处理开通情况

#### 功能说明

用于查询已经开通媒体处理功能的存储桶。

**注意**

 COS iOS SDK 版本需要大于等于 v5.9.6。

#### 请求示例

**Objective-C**

QCloudGetDescribeMediaBucketsRequest * request = [[QCloudGetDescribeMediaBucketsRequest alloc]init];

// 地域信息，例如 ap-shanghai、ap-beijing，若查询多个地域以“,”分隔字符串，支持中国大陆地域

request.regions = @[@"ap-shanghai"];

// 存储桶名称，以“,”分隔，支持多个存储桶，精确搜索

request.bucketNames = @[@"examplebucket-1250000000"];

// 存储桶名称前缀，前缀搜索

request.bucketName = @"examplebucket-1250000000";

// 第几页

request.pageNumber = 0;

// 每页个数

request.pageSize = 100;

request.finishBlock = ^(QCloudDescribeMediaInfo * outputObject, NSError *error) {

 // outputObject 请求到的媒体信息，详细字段请查看api文档或者SDK源码

 // QCloudDescribeMediaInfo 类；

};

[[QCloudCOSXMLService defaultCOSXML] CIGetDescribeMediaBuckets:request];

**说明**

更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/iOS/Objc/Examples/cases/GetSnapshot.m) 查看。

**Swift**

let request : QCloudGetDescribeMediaBucketsRequest = QCloudGetDescribeMediaBucketsRequest();

// 地域信息，例如 ap-shanghai、ap-beijing，若查询多个地域以“,”分隔字符串，支持中国大陆地域

request.regions = ["ap-shanghai"];

// 存储桶名称，以“,”分隔，支持多个存储桶，精确搜索

request.bucketNames = ["bucketNames"];

// 存储桶名称前缀，前缀搜索

request.bucketName = "bucketName";

// 第几页

request.pageNumber = 0;

// 每页个数

request.pageSize = 100;

request.finishBlock = { (result, error) in

 // result 请求到的媒体信息，详细字段请查看api文档或者SDK源码

 // QCloudMediaInfo 类；

}

QCloudCOSXMLService.defaultCOSXML().ciGetDescribeMediaBuckets(request);

**说明**

更多完整示例，请前往 [GitHub](https://github.com/tencentyun/cos-snippets/tree/master/iOS/Swift/Examples/cases/GetSnapshot.swift) 查看。
