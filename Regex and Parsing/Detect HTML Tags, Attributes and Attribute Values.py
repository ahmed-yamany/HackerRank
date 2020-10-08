from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print('->', i[0], '>', i[1])


N = int(input())
html = ''
for i in range(N):
    S = input()
    html += S + '\n'

parser = MyHTMLParser()
parser.feed(html)
