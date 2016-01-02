#!/bin/bash

# change this
ZHWIKIDUMP=../orig/wiki/zhwiki-20151226-pages-articles.xml.bz2
DUMPVERSION='20151226'

PYTHON=pypy3
BUNZIP=lbunzip2

mkdir build
mkdir dist
cp style.css dist/
$BUNZIP -uc $ZHWIKIDUMP | tee >($PYTHON WikiExtractoryear.py -s > build/wikihistory.xml) | $PYTHON WikiExtractordate.py -s > build/wikicalendar.xml

for book in "history" "calendar"; do
 for lang in cn sg tw hk; do
  $PYTHON sort$book.py -l zh-$lang -i build/wiki$book.xml -d $DUMPVERSION -o dist/wiki${book}_zh-$lang.html
  $PYTHON sort$book.py -l zh-$lang -i build/wiki$book.xml -d $DUMPVERSION -b -o build/wiki${book}_zh-$lang.book.html
 done
done

for book in "history" "calendar"; do
 for lang in cn sg tw hk; do
  ebook-convert build/wiki${book}_zh-$lang.book.html dist/wiki${book}_zh-$lang.epub \
   --level1-toc '//h:article[@class="millennium"]/h:h1|//h:article[@class="century"]/h:h1|//h:article[@class="month"]/h:h1' \
   --level2-toc '//h:article[@class="decade"]/h:h1' \
   --chapter '//h:article[@class="century"]/h:h1|//h:article[@class="month"]/h:h1' \
   --chapter-mark 'pagebreak' \
   --authors 'Wikipedia contributors' \
   --language zho \
   --page-breaks-before '/' \
   --no-default-epub-cover
 done
done

rm -rf build/
