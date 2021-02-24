# coding: utf-8
import random
import time
import os
from pathlib import Path

import pandas as pd

from wechatarticles import ArticlesInfo
from wechatarticles.utils import get_history_urls


# 快速获取大量文章urls（利用历史文章获取链接）


def verify_url(article_url):
    """
    简单验证文章url是否符合要求

    Parameters
    ----------
    article_url: str
        文章链接
    """
    verify_lst = ["mp.weixin.qq.com", "__biz", "mid", "sn", "idx"]
    for string in verify_lst:
        if string not in article_url:
            raise Exception("params is error, please check your article_url")

def save_xlsx(fj, lst):
    df = pd.DataFrame(lst, columns=["url", "title", "date", "read_num", "like_num"])
    df.to_excel(fj + ".xlsx", encoding="utf-8")


def demo(lst):
    # 抓取示例，供参考，不保证有效
    fj = "公众号名称"
    item_lst = []
    for i, line in enumerate(lst, 0):
        print("index:", i)
        # item = json.loads('{' + line + '}', strict=False)
        item = line
        timestamp = item["comm_msg_info"]["datetime"]
        ymd = time.localtime(timestamp)
        date = "{}-{}-{}".format(ymd.tm_year, ymd.tm_mon, ymd.tm_mday)

        infos = item["app_msg_ext_info"]
        url_title_lst = [[infos["content_url"], infos["title"]]]
        if "multi_app_msg_item_list" in infos.keys():
            url_title_lst += [
                [info["content_url"], info["title"]]
                for info in infos["multi_app_msg_item_list"]
            ]

        for url, title in url_title_lst:
            try:
                if not verify_url(url):
                    continue
                # 获取文章阅读数在看点赞数
                read_num, like_num, old_like_num = ai.read_like_nums(url)
                print(read_num, like_num)
                item_lst.append([url, title, date, read_num, like_num])
                time.sleep(random.randint(5, 10))
            except Exception as e:
                print(e)
                flag = 1
                break
            finally:
                save_xlsx(fj, item_lst)

        if flag == 1:
            break

    save_xlsx(fj, item_lst)


def convert_list(lst):
    new_list = []
    for item in lst:
        d = {}
        sub_article = None
        for k, v in item["comm_msg_info"].items():
            d[k] = v
        for k, v in item["app_msg_ext_info"].items():
            # 第二篇文章
            if k == "multi_app_msg_item_list" and len(v) > 0:
                sub_article = v
            d[k] = v
        new_list.append(d)

        if sub_article is not None:
            for art in sub_article:
                # a piece of article
                # 必须copy一个新的dict
                sub_d = d.copy()
                # clear this k
                sub_d['multi_app_msg_item_list'] = []
                for k, v in art.items():
                    sub_d[k] = v
                new_list.append(sub_d)

    return new_list


def add_more(df):

    # 个人微信号登陆后获取的token
    appmsg_token = "1102_bUXhScjnSzo2OWEN6qVzJPFLbb0TNhm4Ed2qHQ~~"
    # 个人微信号登陆后获取的cookie
    cookie = "wxuin=2922773620; devicetype=Windows10x64; version=63010043; lang=zh_CN; pass_ticket=XV7+26NN4KzfcszTY5ceEBK/YfdU4P7o8Y3uk6vgwyS+XKxThyqdLJeXKSeaNOo9; wap_sid2=CPT41/EKEooBeV9IQXpkZlIzb2hpSUhZeG5JVUNfMU1GZXpsOUdHSUI4ZlJxWFFhSW9jNkptUlpSTEp1dnFsTDJ6TGpkNW5vWXhadUE2VXVRclVzQzIwd1VzYnIydVB4cUloWHhpTUFOTDNydjY1eG90OVFvek1qVjItQ2VwcVRWLWJpUXA2cXJDMTh5c1NBQUF+ML7H2YEGOA1AlU4="

    # target
    articles_name = "db/articles.csv"
    articles = Path(articles_name)

    if articles.exists():
        df = pd.read_csv(articles_name, encoding='utf-8')
    # if Path('db/articles.xlsx').exists():
    #     df = pd.read_excel('db/articles.xlsx')

    # add columns
    columns = ['read_num', 'reading_num', 'like_num', 'contents', 'comments']
    for column in columns:
        if column not in df:
            df[column] = None
            print('column {} added!'.format(column))

    for index, row in df.iterrows():
        id = row['id']
        title = row['title']
        url = row['content_url']

        if row['read_num'] is not None and row['read_num'] >= 0:
            print('line {}, {} is already ok'.format(index, title))
            continue

        filename = 'db/' + str(id) + "_" + str(index) + '.txt'

        # 获取点赞数、阅读数、评论信息
        ai = ArticlesInfo(appmsg_token, cookie)

        try:
            # url：微信文章链接
            read_num, reading_num, like_num = ai.read_like_nums(url)
            print("{} 阅读：{}; 在看: {}; 点赞: {}".format(title, read_num, reading_num, like_num))
            comments = ai.comments(url)
            print("评论：{}".format(comments))
            # pprint(comment)
            # save content
            content, _, _ = ai.content(url)
            file = open(filename, mode='w', encoding='utf-8')
            file.write(content)
            file.close()

            df.at[index, 'read_num'] = read_num
            df.at[index, 'reading_num'] = reading_num
            df.at[index, 'like_num'] = like_num
            df.at[index, 'contents'] = content
            df.at[index, 'comments'] = comments

            # snapshot
            df.to_csv(articles_name, encoding='utf-8')

            time.sleep(5)
        except Exception as e:
            print('ERROR: {}. article: {}'.format(e, title))
            print(e)


if __name__ == "__main__":
    # 需要抓取公众号的__biz参数
    biz = "MjM5ODk1MTM2Mg=="
    # 个人微信号登陆后获取的uin
    uin = "MjkyMjc3MzYyMA=="
    # 个人微信号登陆后获取的key，隔段时间更新
    key = "241af38c3f8a9ae73c15b7ad6ef153284e82f0b00889fba785b4a95d99021c515b5df09bb04cac12fd631295d35bc0aa74c151caae24b3f5c2a8f2bb180abee449ceb7f386b3bc2fdfe4b1b47fee7c7d8cf90381a53251190244c36571dd23b7614df539ffc5481faa221886f3c6799c6923815c318bccd1a04452898653bc9e"

    urls_name = "db/history_url_info.csv"
    urls = Path(urls_name)

    os.makedirs('db', exist_ok=True)

    df = None
    if not urls.exists():
        lst = get_history_urls(
            biz, uin, key, lst=[], start_timestamp=0, count=0, endcount=1000
        )
        print("总共{}篇文章".format(len(lst)))
        print("抓取到的文章链接")
        print(lst)

        new_list = convert_list(lst)
        df = pd.DataFrame(new_list)
        df.to_csv(urls_name, encoding='utf-8')
    else:
        df = pd.read_csv(urls, encoding='utf-8')

    print(df.describe)

    add_more(df)




    # # 个人微信号登陆后获取的token
    # appmsg_token = "1101_MSL93YEAsVfdfg1HG5DcDoemwMAekiBCW3727fQPo80UenKhGTk4pFYqSshviUKnU2qa3t51TNBme7DG"
    # # 个人微信号登陆后获取的cookie
    # cookie = "wxuin=2922773620; devicetype=Windows10x64; version=63010043; lang=zh_CN; pass_ticket=nM3GuqdPZEWD+8Y/qOQHOtlZof/7i9QVOvrnpXJRaa9F/EzgxeT3JvnRBpQEVkbT; wap_sid2=CPT41/EKEooBeV9IRkFSVExsQ25uQ0ljMW5wV3RNRklYQjNUUHNxLVc3cGVzRzhiWXo0MGNiZUVkMWVwZjJta0kzVFNQMzRGRTVSci1nTkI3Q1VEd0hMMFFUVV9RWnY0eU55LU90VVloS0dETnNfb09UZXNZWmlHOFFnczZYTHV0MWR1c19TNEQ0LXpTc1NBQUF+MNOez4EGOA1AlU4="
    # url = "http://mp.weixin.qq.com/s?__biz=MjM5ODk1MTM2Mg==&amp;mid=2661934345&amp;idx=1&amp;sn=397582833fb933ad430b9b9fafe95546&amp;chksm=bd9fa5a48ae82cb291288ed7d7cfe052ea58a7987fb2e7a9b776c8d0f8417df9e0e36ae6aea5&amp;scene=27"
    # # 获取点赞数、阅读数、评论信息
    # ai = ArticlesInfo(appmsg_token, cookie)
    #
    # # url：微信文章链接
    # read_num, like_num, old_like_num = ai.read_like_nums(url)
    # print("阅读：{}; 在看: {}; 点赞: {}".format(read_num, like_num, old_like_num))
    # print("评论信息")
    # item = ai.comments(url)
    # pprint(item)
