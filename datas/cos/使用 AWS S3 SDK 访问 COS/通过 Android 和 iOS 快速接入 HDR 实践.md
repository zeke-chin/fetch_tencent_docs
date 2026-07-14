<!-- source: https://cloud.tencent.com/document/product/436/125143 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:17:12+08:00 -->

# 通过 Android 和 iOS 快速接入 HDR 实践

最近更新时间：2025-12-30 10:10:52


## HDR 简介

HDR（High Dynamic Range Imaging），高动态范围成像，是一种能够显示更大曝光动态范围的图像，它能保留图像中的更多细节和色彩信息，使图像的明暗差别更明显、色彩更丰富，从而提供更真实和丰富的视觉体验。

数据万象支持在处理 HDR 图片时保留原有的 HDR 信息，使处理后的图片依然能展示出 HDR 效果，详见 [HDR 图片处理](https://cloud.tencent.com/document/product/460/118040)。

## HDR 类型介绍

支持在处理时保留的 HDR 类型 支持的图片格式
Ultra HDR：ISO 标准的 GainMap HDR（安卓生态）JPEG
Apple Adaptive HDR：符合 ISO 标准的苹果定制 GainMap HDR（苹果生态）HEIF
10 bit 色深 HDR：非增益图实现的原生 HDR HEIF、AVIF

**说明：**

HDR 图片为付费服务，与基础图片处理搭配使用时，将产生 HDR 图片处理费用，如果处理结果图为 HEIF/HEIC 或 AVIF，将产生图片高级压缩和 HDR 图片处理两项费用，详细计费说明可参见 [图片处理费用](https://cloud.tencent.com/document/product/460/58117)。

## 兼容性

安卓从 Android 14（API 级别34）开始提供对 Ultra HDR 图片的原生支持，如果小于 Android 14或者硬件不支持 HDR，图片会自动降级显示为标准的 SDR（标准动态范围）版本。

安卓从 Android 13（API 级别33）开始支持10 bit 色深的 HDR 图片，对于早期硬件不支持 HDR 的设备，系统默认会通过量化降级的方式以8 bit 形态进行展示，不存在兼容性问题。

苹果从 iOS 18开始支持对 Ultra HDR 图片的原生支持，如果 iOS 系统版本小于18，则设备仅能显示遵循苹果协议的 HDR 图片（Apple Adaptive HDR）。此外如果设备硬件不支持 HDR，图片会自动降级显示为 SDR（标准动态范围）版本。

苹果从 iOS 13开始支持10 bit 色深的 HDR 图片，对于早期硬件不支持 HDR 的设备，系统默认会通过动态范围映射的方式以8 bit 形态进行展示，不存在兼容性问题。

## 显示 HDR 图片代码示例

以当前市场中占比最广泛的 Ultra HDR 为例，完整示例请参见 [Android HDR Demo](https://github.com/tencentyun/cloud-Infinite-sdk-android/tree/main/QCloudInfiniteHdrSample)、[iOS HDR Demo](https://github.com/tencentyun/cloud-Infinite-sdk-ios.git)。

Android

iOS

1. 调用 `Bitmap.hasGainMap()`（自 Android 14起可用）检查其是否具有增益映射。

2. 如需以完整动态范围显示 Ultra HDR 图片，请将窗口的颜色模式设置为 `ActivityInfo.COLOR_MODE_HDR`。

更多代码示例，请参考 [显示 Ultra HDR 图片](https://developer.android.com/media/grow/ultra-hdr/display)。

val bitmap = BitmapFactory.decodeFile("HDR.jpg")

imageView.setImageBitmap(bitmap)

// Set color mode of the activity to the correct color mode.

window.colorMode =

 if (bitmap.hasGainmap()) ActivityInfo.COLOR_MODE_HDR else ActivityInfo.COLOR_MODE_DEFAULT

更多关于 HDR 的用法，请参考 [显示 HDR 图片](https://developer.apple.com/documentation/uikit/supporting-hdr-images-in-your-app?language=objc)。

Swift UI

UIKit

// 要在 SwiftUI 图像视图中启用 HDR，使用 View 中的 allowedDynamicRange 修饰符即可。

Image(systemName: "photo")

 .resizable()

 .allowedDynamicRange(.constrainedHigh)

// 要在 UIKit 图像视图中启用HDR，仅需要在UIImageView对象中设置preferredImageDynamicRange属性即可。

// Swift

let view = UIImageView()

view.preferredImageDynamicRange = .high

// Objc

UIImageView *imageView = [[UIImageView alloc] init];

imageView.preferredImageDynamicRange = UIImageDynamicRangeHigh;

**注意：**

HDR 图像在应用中展示时仅支持iOS 17.0及以上的系统版本。

开发和调试时要避免使用模拟器，需要在真机上运行。
