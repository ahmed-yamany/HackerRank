from html.parser import HTMLParser


class myHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        for i in attrs:
            print('->', str(i[0]).strip(), '>', str(i[1]).strip())

    def handle_endtag(self, tag):
        print('End   :', tag)

    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        for i in attrs:
            print('->', str(i[0]).strip(), '>', str(i[1]).strip())


N = int(input())
parser = myHTMLParser()
for i in range(N):
    S = input()
    parser.feed(S)

