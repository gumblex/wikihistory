维基编年史 / 维基日历
==================

## 制作过程
可参见`make.sh`自动生成。

1. 下载[维基百科XML数据](http://dumps.wikimedia.org/zhwiki/latest/)：选择 zhwiki-latest-pages-articles.xml.bz2。注意你的硬盘。
2. `bzcat zhwiki-latest-pages-articles.xml.bz2 | python3 WikiExtractoryear.py`
3. `python3 sorthistory.py -l <语言> -i <XML文件名>` -l 选项可以为：
   * __zh-cn__ 大陆简体
   * __zh-hk__ 香港繁體
   * __zh-sg__ 马新简体
   * __zh-tw__ 台灣正體

维基日历制作过程相同，脚本文件名为`WikiExtractordate.py`、`sortdate.py`。

## 文件说明
* __README.md__ 本说明。
* __make.sh__ 自动制作脚本：使用前请按实际修改。
* __WikiExtractoryear.py__、__WikiExtractordate.py__ 筛选原存档XML中所需部分。
* __sorthistory.py__、__sortdate.py__ 整理筛选出的XML文件并生成HTML。
* __wikihistory.opf__、__wikidate.opf__ EPub元数据。
* __style.css__ HTML样式。
本次生成：
* __wikihistory.xml__、__wikidate.xml__ 筛选出的XML文件
* __wikihistory_*.html__ 《维基编年史》
* __wikidate_*.html__ 《维基日历》
* __wikihistory_*.book.html__ 《维基编年史》EPub版HTML
* __wikidate_*.book.html__ 《维基日历》EPub版HTML

