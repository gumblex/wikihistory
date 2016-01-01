#!/bin/bash

# change this
ZHWIKIDUMP=../orig/wiki/zhwiki-20151226-pages-articles.xml.bz2
DUMPVERSION='20151226'

PYTHON=pypy3
BUNZIP=lbunzip2

mkdir build
mkdir dist
$BUNZIP -uc $ZHWIKIDUMP | tee >($PYTHON WikiExtractoryear.py -s > build/wikihistory.xml) | $PYTHON WikiExtractordate.py -s > build/wikicalendar.xml

for book in "history" "calendar"; do
 for lang in cn sg tw hk; do
  $PYTHON sort$book.py -l zh-$lang -i build/wiki$book.xml -d $DUMPVERSION
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
   --authors Wikipedia contributors \
   --language zho \
   --page-breaks-before '/' \
   --no-default-epub-cover
 done
done
#--read-metadata-from-opf wiki$book.opf

#{'asciiize': False,
 #'author-sort': None,
 #'authors': None,
 #'base-font-size': 0.0,
 #'book-producer': None,
 #'breadth-first': False,
 #'change-justification': u'original',
 #'chapter': u'//h:h1',
 #'chapter-mark': u'pagebreak',
 #'comments': None,
 #'cover': None,
 #'debug-pipeline': None,
 #'dehyphenate': True,
 #'delete-blank-paragraphs': True,
 #'disable-font-rescaling': False,
 #'dont-package': False,
 #'dont-split-on-page-breaks': False,
 #'duplicate-links-in-toc': False,
 #'embed-all-fonts': False,
 #'embed-font-family': None,
 #'enable-heuristics': False,
 #'epub-flatten': False,
 #'epub-inline-toc': False,
 #'epub-toc-at-end': False,
 #'expand-css': False,
 #'extra-css': None,
 #'extract-to': None,
 #'filter-css': u'',
 #'fix-indents': True,
 #'flow-size': 320,
 #'font-size-mapping': None,
 #'format-scene-breaks': True,
 #'html-unwrap-factor': 0.4,
 #'input-encoding': None,
 #'input-profile': <calibre.customize.profiles.InputProfile object at 0x7f5abf26ad10>,
 #'insert-blank-line': False,
 #'insert-blank-line-size': 0.5,
 #'insert-metadata': False,
 #'isbn': None,
 #'italicize-common-cases': True,
 #'keep-ligatures': False,
 #'language': None,
 #'level1-toc': u'//h:article[@class="millennium"]/h:h1| //h:article[@class="century"]/h:h1',
 #'level2-toc': u'//h:article[@class="decade"]/h:h1',
 #'level3-toc': None,
 #'line-height': 0.0,
 #'linearize-tables': False,
 #'margin-bottom': 5.0,
 #'margin-left': 5.0,
 #'margin-right': 5.0,
 #'margin-top': 5.0,
 #'markup-chapter-headings': True,
 #'max-levels': 5,
 #'max-toc-links': 100,
 #'minimum-line-height': 120.0,
 #'no-chapters-in-toc': False,
 #'no-default-epub-cover': False,
 #'no-inline-navbars': False,
 #'no-svg-cover': False,
 #'output-profile': <calibre.customize.profiles.GenericEink object at 0x7f5abf285150>,
 #'page-breaks-before': u"//*[name()='h1']",
 #'prefer-metadata-cover': False,
 #'preserve-cover-aspect-ratio': False,
 #'pretty-print': True,
 #'pubdate': None,
 #'publisher': None,
 #'rating': None,
 #'read-metadata-from-opf': u'/tmp/calibre-1.25.0-tmp-qkSkg6/oVS2h1.opf',
 #'remove-fake-margins': True,
 #'remove-first-image': False,
 #'remove-paragraph-spacing': False,
 #'remove-paragraph-spacing-indent-size': 1.5,
 #'renumber-headings': True,
 #'replace-scene-breaks': u'',
 #'search-replace': '[]',
 #'series': None,
 #'series-index': None,
 #'smarten-punctuation': True,
 #'sr1-replace': None,
 #'sr1-search': None,
 #'sr2-replace': None,
 #'sr2-search': None,
 #'sr3-replace': None,
 #'sr3-search': None,
 #'start-reading-at': None,
 #'subset-embedded-fonts': False,
 #'tags': None,
 #'timestamp': None,
 #'title': None,
 #'title-sort': None,
 #'toc-filter': None,
 #'toc-threshold': 6,
 #'toc-title': None,
 #'unsmarten-punctuation': False,
 #'unwrap-lines': True,
 #'use-auto-toc': False,
 #'verbose': 2}
