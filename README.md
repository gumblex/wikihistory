维基编年史 / 维基日历
==================

## 制作过程
可使用 `make.sh` 自动生成。更改 ZHWIKIDUMP 和 DUMPVERSION 变量为实际文件位置和版本。

1. 下载[维基百科 XML 数据](http://dumps.wikimedia.org/zhwiki/latest/)：选择 zhwiki-latest-pages-articles.xml.bz2。注意你的硬盘。
2. 更改 `make.sh` 中 ZHWIKIDUMP 和 DUMPVERSION 变量为实际文件位置和版本。
3. `./make.sh`

生成的文件在 dist 文件夹。

## 文件说明
* __README.md__ 本说明。
* __make.sh__ 自动制作脚本：使用前请按实际修改。
* __WikiExtractoryear.py__、__WikiExtractordate.py__ 筛选原存档XML中所需部分。
* __sorthistory.py__、__sortcalendar.py__ 整理筛选出的XML文件并生成HTML。
* __style.css__ HTML样式。

## 授权协议

    Copyright (C) 2014-2016 Dingyuan Wang

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
