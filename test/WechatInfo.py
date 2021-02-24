# coding: utf-8
import os
from pprint import pprint
from wechatarticles import ArticlesInfo

if __name__ == "__main__":

    # print('dddd\ndddd'.replace('\n', '_'))

    # 登录微信PC端获取文章信息
    appmsg_token = "1101_MSL93YEAsVfdfg1HG5DcDoemwMAekiBCW3727fQPo80UenKhGTk4pFYqSshviUKnU2qa3t51TNBme7DG"
    cookie = "wxuin=2922773620; devicetype=Windows10x64; version=63010043; lang=zh_CN; pass_ticket=nM3GuqdPZEWD+8Y/qOQHOtlZof/7i9QVOvrnpXJRaa9F/EzgxeT3JvnRBpQEVkbT; wap_sid2=CPT41/EKEooBeV9IRkFSVExsQ25uQ0ljMW5wV3RNRklYQjNUUHNxLVc3cGVzRzhiWXo0MGNiZUVkMWVwZjJta0kzVFNQMzRGRTVSci1nTkI3Q1VEd0hMMFFUVV9RWnY0eU55LU90VVloS0dETnNfb09UZXNZWmlHOFFnczZYTHV0MWR1c19TNEQ0LXpTc1NBQUF+MNOez4EGOA1AlU4="
    article_url = "http://mp.weixin.qq.com/s?__biz=MjM5ODk1MTM2Mg==&amp;mid=2661934345&amp;idx=1&amp;sn=397582833fb933ad430b9b9fafe95546&amp;chksm=bd9fa5a48ae82cb291288ed7d7cfe052ea58a7987fb2e7a9b776c8d0f8417df9e0e36ae6aea5&amp;scene=27"
    test = ArticlesInfo(appmsg_token, cookie)
    content = test.content(article_url)
    comments = test.comments(article_url)
    read_num, like_num, old_like_num = test.read_like_nums(article_url)
    print("content: {}".format(content))
    print("comments: {}".format(comments))
    print("read_like_num: ", read_num, like_num, old_like_num)
