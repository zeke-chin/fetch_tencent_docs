<!-- source: https://cloud.tencent.com/document/product/436/68285 -->
<!-- fetcher: jina -->
<!-- fetched_at: 2026-07-13T17:05:38+08:00 -->

# 匿名访问 COS

最近更新时间：2023-09-21 20:29:25


## 开放存储桶为公有读

将存储桶开放为公有读私有写，存储桶中所有对象都可被匿名访问。配置方式可参考 [设置存储桶访问权限](https://cloud.tencent.com/document/product/436/13315)。

## 开放对象为公有读

将指定对象开放为公有读私有写，该对象可直接通过对象 URL 访问。配置方式可参考 [设置对象的访问权限](https://cloud.tencent.com/document/product/436/13327)。

## 开放文件夹为公有读

将文件夹开放为公有读私有写，该文件夹下所有文件可被匿名访问。配置方式可参考 [设置文件夹权限](https://cloud.tencent.com/document/product/436/39298)。

## 公有读权限评估机制

COS 权限的评估机制可参考 [访问策略评估流程](https://cloud.tencent.com/document/product/436/41516)，针对存储桶、文件夹、对象级别的公有读权限设置出现冲突时，优先级排序为：

针对某个对象的 ACL，对象 ACL 优先级最高，若对象 ACL 为继承权限，以文件夹 ACL 为准，若文件夹 ACL 为继承权限，以存储桶 ACL 为准。
