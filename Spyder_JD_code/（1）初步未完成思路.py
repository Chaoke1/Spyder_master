import requests

for i in range(1,93):
    url = "https://list.jd.com/list.html?cat=9987%2C653%2C655&page="+str(i)+"&s="+str(60*i+1-60)+"&click=0"  #主网站93页，每页60个分网站
    print(url)
    dic = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
    }
    resp = requests.get(url, headers=dic)
    resp.encoding = 'UTF-8'
    file_master = open('master_html.txt', 'w', encoding='UTF-8')  #保存每页60个分网站的txt文本

    file_master.writelines(resp.text)
    """
    a = re.findall(r'<a href=\"(.*\.html)\" target=\"_blank\">',request)
    此处是对主站网页源代码进行正则，过滤出每页60个分网站的网址（即60个产品的网址）
    """
    resp.close()
    for j in ()
