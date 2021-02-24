**原工程不知道加了啥，clone太慢了，直接push一个不带git信息的。加入了自己修改的一些爬公众号的东西。**

# 微信公众号文章爬虫（微信文章阅读点赞的获取）

![](https://img.shields.io/pypi/v/wechatarticles)![](https://img.shields.io/pypi/l/wechatarticles)[![](https://img.shields.io/badge/docs-building-blue)](https://wnma3mz.github.io/wechat_articles_spider/build/html/index.html)
安装

`pip install wechatarticles`

展示地址：

[日更，获取公众号的最新文章链接](https://data.wnma3mz.cn/demo.html)，支持日更阅读点赞评论正文

技术交流可以直接联系，微信二维码见末尾（微信；wnma3mz)。烦请进行备注，如wechat_spider

统一回复，项目可正常运行。若不能正常运行，该行会删除。

联系前请注意：

1. 不（能）做自动登录微信公众号、微信

2. 不（能）做实时获取参数

3. 参数过期需要手动更新

4. 换一个公众号需要手动更新

注：本项目仅供学习交流，严禁用于商业用途（该项目也没法直接使用），不能达到开箱即用的水平。使用本项目需要读文档+源码+动手实践，参考示例代码（`test`文件夹下）进行改写。

提示：另外，已经有很多朋友（大佬）通过直接看源码，已经基于这套项目，或者重写，用于各自的需求。

实现思路一:

1. 从微信公众号平台获取微信公众所有文章的url
2. 登录微信PC端或移动端获取文章的阅读数、点赞数、评论信息

完整思路可以参考我的博客: [记一次微信公众号爬虫的经历（微信文章阅读点赞的获取）](https://wnma3mz.github.io/hexo_blog/2017/11/18/记一次微信公众号爬虫的经历（微信文章阅读点赞的获取）/)

实现思路二：

1. 登陆微信PC端或移动端获取公众号所有文章的url，这种获取到的url数量大于500，具体数量每个微信号不完全一致
2. 同上种方法，获取文章阅读数、点赞数、评论信息

公开已爬取的公众号历史文章的永久链接，日期均截止commit时间，仅供测试与学习，欢迎各位关注这些优质公众号。

<details>
  <summary>公众号列表</summary>
    <li>科技美学</li>
    <li>共青团中央</li>
    <li>南方周末</li>
    <li>AppSo</li>
</details>


## Notes

项目始于2017年，当前更新于2021年2月

项目代码进行调整，调用以前的接口请使用`pip install wechatarticles==0.5.8`。

1. 爬取失败的时候，可能有以下原因
   1. **运行的时候需要关闭网络代理（抓包软件），或者添加相关参数**
   2. 参数是否最新，获取微信相关参数（cookie、token）时，一定要保证是**对应公众号**的任意文章
   3. 检查代码
   4. 需要关注对应公众号（Maybe）
2. 思路一获取url时，每页间隔可以设定久一点，比如3分钟，持续时间几小时（来自网友测试）
3. 获取文章阅读点赞时，每篇文章可以设定在5-10s左右，过期时间为4小时；若被封，大约5-10分钟就可继续抓取。
4. 思路二获取url时，如果被封，需要24小时整之后才能重新抓取

参数文件说明见[README](https://github.com/wnma3mz/wechat_articles_spider/blob/master/docs)

## python版本

- `python`: 3.6.2、3.7.3

## 功能实现

<details>
  <summary>功能</summary>
    公众号相关
    <li>公众号信息</li>
    <li>公众号biz。获取方式：清博、公众号网页</li>
    <li>公众号发表文章数量（不完全准确）</li>
    文章相关
    <li>某公众号文章的url。获取方式：公众号网页、PC端微信、移动端微信、微信读书</li>
    <li>某公众号所有文章信息（包含点赞数、阅读数、评论信息），需要手动更改循环</li>
    <li>某公众号指定文章的信息</li>
    <li>支持微信文章下载至本地转为html（图片可选是否保存）</li>
</details>

## API实例

#### 利用公众号网页版获取微信文章url
此处有次数限制，不可一次获取太多url。解决方案多个账号同时爬取
[test_WechatUrls.py](https://github.com/wnma3mz/wechat_articles_spider/blob/master/test/test_WechatUrls.py)

#### 登录微信PC端获取文章信息
[test_WechatInfo.py](https://github.com/wnma3mz/wechat_articles_spider/blob/master/test/test_WechatInfo.py)

#### 快速获取大量文章urls（利用历史文章获取链接）
[test_GetUrls.py](https://github.com/wnma3mz/wechat_articles_spider/blob/master/test/test_GetUrls.py)

#### 利用公众号获取链接，并获取阅读点赞
[test_ArticlesAPI.py](https://github.com/wnma3mz/wechat_articles_spider/blob/master/test/test_ArticlesAPI.py)

#### 微信文章下载为离线HTML（含图片）
[test_Url2Html.py](https://github.com/wnma3mz/wechat_articles_spider/blob/master/test/test_Url2Html.py)


### 相关文档

见博客与下方文档

official_cookie和token手动获取方式见[这篇文档](https://github.com/wnma3mz/wechat_articles_spider/blob/master/docs/get_cookie_token.md)

wechat_cookie和appmsg_token手动获取的介绍，可以参考[这篇文档](https://github.com/wnma3mz/wechat_articles_spider/blob/master/docs/get_appmsg_token.md)

wechat_cookie和appmsg_token自动获取的介绍（需要安装`mitmproxy`，已放弃），仅供参考[这篇文档](https://github.com/wnma3mz/wechat_articles_spider/blob/master/docs/关于自动获取微信参数.md)。默认开放端口为8080。

# 关于一些爬微信所需要的参数的获取
用来根据url爬文章：
- *appmsg_token*： 个人微信号登陆后获取的token
- *cookie*

用来爬公众号的历史url：
- biz： 需要抓取公众号的__biz参数
- uin： 个人微信号登陆后获取的uin
- *key*： 个人微信号登陆后获取的key，隔段时间更新

只有biz和uin是不变的，前者代表公众号，后者代表用户。

以上参数使用fiddler获取：
1. 安装打开fiddler，可以参考[使用教程](https://www.cnblogs.com/yyhh/p/5140852.html)；
1. 使用fiddler的filter功能，对host进行过滤，只显示：mp.weixin.qq.com；
1. 使用微信pc客户端打开公众号的历史，此时fiddler应该截获了一堆关于微信的请求；
1. 找到action=urlcheck的post请求，里面除了biz参数都能找到。cookie自然也能在header里找到；
1. 随便找个带biz的请求即可，比如action=home（应该是查看公众号历史文章所触发的请求）的；

action=urlcheck的请求示例：
```
POST /mp/profile_ext?action=urlcheck&uin=MjkyMjc3MzYyMA==&key=241af38c3f8a9ae73c15b7ad6ef153284e82f0b00889fba785b4a95d99021c515b5df09bb04cac12fd631295d35bc0aa74c151caae24b3f5c2a8f2bb180abee449ceb7f386b3bc2fdfe4b1b47fee7c7d8cf90381a53251190244c36571dd23b7614df539ffc5481faa221886f3c6799c6923815c318bccd1a04452898653bc9e&pass_ticket=XV7+26NN4KzfcszTY5ceEBK/YfdU4P7o8Y3uk6vgwyS+XKxThyqdLJeXKSeaNOo9&appmsg_token=1102_bUXhScjnSzo2OWEN6qVzJPFLbb0TNhm4Ed2qHQ~~&a8scene=7&session_us= HTTP/1.1
```

action=home的请求示例：
```
GET /mp/profile_ext?action=home&__biz=MjM5ODk1MTM2Mg==&scene=124&uin=MjkyMjc3MzYyMA%3D%3D&key=241af38c3f8a9ae73c15b7ad6ef153284e82f0b00889fba785b4a95d99021c515b5df09bb04cac12fd631295d35bc0aa74c151caae24b3f5c2a8f2bb180abee449ceb7f386b3bc2fdfe4b1b47fee7c7d8cf90381a53251190244c36571dd23b7614df539ffc5481faa221886f3c6799c6923815c318bccd1a04452898653bc9e&devicetype=Windows+10+x64&version=63010043&lang=zh_CN&a8scene=7&pass_ticket=XV7%2B26NN4KzfcszTY5ceEBK%2FYfdU4P7o8Y3uk6vgwyS%2BXKxThyqdLJeXKSeaNOo9&fontgear=2 HTTP/1.1
```

test/GetUrls.py执行即可。

