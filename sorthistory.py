#!/usr/bin/env python3
import sys, os
import re
import operator
from zhconv import convert_for_mw as zhconv
getint = lambda instr: int(re.findall('\\d+', instr)[0])
catclass = ('millennium','century','decade','year')
locale = 'zh-cn'
filename = 'wikihistory.xml'
#outfile = 'wikihistory.html'
outfile = os.path.splitext(filename)[0] + '_' + locale + '.html'
bookmode = False
dumpversion = '20151226'
for i,a in enumerate(sys.argv):
	if a == '-l':
		# locale
		locale = sys.argv[i+1]
		outfile = os.path.splitext(filename)[0] + '_' + locale + '.html'
	elif a == '-i':
		# input
		filename = sys.argv[i+1]
		outfile = os.path.splitext(filename)[0] + '_' + locale + '.html'
	elif a == '-o':
		# output
		outfile = sys.argv[i+1]
	elif a == '-b':
		bookmode = True
	elif a == '-d':
		dumpversion = sys.argv[i+1]

bookhtmlheader = zhconv('''<!DOCTYPE html>
<html lang="%s" dir="ltr">
<head>
<title>维基编年史</title>
<link href="style.css" rel="stylesheet"/>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
</head>
<body>
<h1 id="pagetitle">维基编年史</h1>
____年到底发生了什么？
\n''' % locale, locale)
htmlheader = zhconv('''<!DOCTYPE html>
<html lang="%s" dir="ltr">
<head>
<meta charset="UTF-8" />
<title>维基编年史</title>
<link rel="stylesheet" href="style.css" />
<script>
function gotoyear(){
var y = document.getElementById("toyear").value;
if (y!="") {
window.location.hash = '#3-'+y;}
}
</script>
</head>
<body>
<h1 id="pagetitle">维基编年史</h1>
<form id="searchform" onsubmit="gotoyear();return false;">公元
<input name="year" placeholder="" id="toyear">年到底发生了什么？<input name="go" type="submit" value="→" onclick="gotoyear()">
</form>
<script>
document.getElementById("toyear").value = Math.floor(Math.random() * 2014) + 1
</script>
\n''' % locale, locale)

if bookmode:
	htmlheader = bookhtmlheader

htmlfooter = zhconv(r'''<footer><a hrerf="http://zh.wikipedia.org">中文维基百科</a>存档版本：'''+dumpversion+r'''。自动提取程序：<a href="https://github.com/gumblex/wikihistory">gumblex</a>。<br>授权协议：<a rel="license" href="http://zh.wikipedia.org/wiki/Wikipedia%3ACC-BY-SA-3.0%E5%8D%8F%E8%AE%AE%E6%96%87%E6%9C%AC" title="Wikipedia:CC-BY-SA-3.0协议文本">知识共享 署名-相同方式共享 3.0协议</a><a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.zh" style="display:none;"></a></footer>
</body></html>
''', locale)

with open(filename, 'r') as f:
	allhis = []
	cat = 0
	year = 0
	title = ''
	content = []
	for ln in f:
		l = ln.strip()
		if not l:
			pass
		elif l[:5]=='<doc ':
			title = zhconv(l.split()[3].split('"')[1], locale)
			if title[0] == '前':
				year = -getint(title)
			else:
				year = getint(title)
			if title[-2:] == '千年':
				cat = 0
				if year>0:
					year -= 1
				year *= 1000
			elif title[-2] == '世': #紀
				cat = 1
				if year>0:
					year -= 1
				year *= 100
			elif title[-2:] == '年代':
				if year<0:
					year -= 9
				cat = 2
			else:
				cat = 3
			print(cat,year,title)
		elif l=='</doc>':
			allhis.append((cat,year,title,tuple(content)))
			cat,year,title,content = 0,0,'',[]
		else:
			content.append(zhconv(l, locale))
historylist = sorted(allhis, key=operator.itemgetter(1, 0))
del allhis
ldict = {'': '', '*': 'ul', '#': 'ol', ':': 'dl', ';': 'dl'}
idict = {'': '', '*': 'li', '#': 'li', ':': 'dt', ';': 'dd'}
print('Writing HTML...')
if bookmode:
	articleheader = '<article class="%s"><h1 id="%s-%s">%s</h1>\n'
else:
	articleheader = '<article class="%s"><h1 id="%s-%s"><a class="top" href="#pagetitle">↑</a>%s</h1>\n'
with open(outfile, 'w') as w:
	w.write(htmlheader)
	w.write('<nav role="navigation" class="toc">\n<h2>%s</h2>\n<ul>\n' % zhconv('目录',locale))
	for item in historylist:
		if item[0]<2:
			w.write('<li><a href="#%s-%s">%s</a></li>\n' % (item[0],item[1],item[2]))
	w.write('</ul></nav>\n')
	for item in historylist:
		w.write(articleheader % (catclass[item[0]],item[0],item[1],item[2]))
		listack = []
		for key,ln in enumerate(item[3]):
			if ln[:4] == '<h2>':
				while listack:
					w.write('</%s>' % listack.pop())
				if key == len(item[3])-1:
					continue
				elif item[3][key+1][:4] == '<h2>':
					continue
				title = ln[4:-5]
				if title[:2] == '大事':
					w.write('<h2 class="events">%s</h2>\n' % title)
				elif title == '出生':
					w.write('<h2 class="births">%s</h2>\n' % title)
				elif title == '逝世':
					w.write('<h2 class="deaths">%s</h2>\n' % title)
				else:
					w.write(ln + '\n')
			elif ln[:4] == '<h3>':
				while listack:
					w.write('</%s>' % listack.pop())
				if key == len(item[3])-1:
					continue
				elif item[3][key+1][:4] == '<h3>':
					continue
				title = ln[4:-5]
				if title[-1] == '月':
					w.write('<h3 class="month">%s</h3>\n' % title)
				else:
					w.write(ln + '\n')
			elif ln[:4] == '<li>':
				title = ln[4:-5].strip()
				splitpoint = re.match(r'^[\*#:;]+', title).end()
				thisstep = title[:splitpoint].strip()
				text = title[splitpoint:].strip()
				for k,i in enumerate(thisstep):
					if k+1 > len(listack):
						while k+1 > len(listack):
							listack.append(ldict[i])
							w.write('<%s>' % ldict[i])
							lasti = idict[i]
					elif listack[k][0] != ldict[i]:
						while len(listack)-1 > k:
							w.write('</%s>' % listack.pop())
						while k+1 > len(listack):
							listack.append(ldict[i])
							w.write('<%s>' % ldict[i])
							lasti = idict[i]
				while len(listack)-1 > k:
					w.write('</%s>' % listack.pop())
				w.write('<%s>%s</%s>' % (idict[i], text, idict[i]))
			else:
				while listack:
					w.write('</%s>' % listack.pop())
				if key == 0 and ln == item[2]:
					pass
				elif ln[0]=='<':
					if ln[1] in ('b','i','u','s'):
						w.write('<p>' + ln + '</p>\n')
					else:
						w.write(ln + '\n')
				else:
					w.write('<p>' + ln + '</p>\n')
		while listack:
			w.write('</%s>' % listack.pop())
		w.write('</article>\n')
	w.write(htmlfooter)
print('Done.')
