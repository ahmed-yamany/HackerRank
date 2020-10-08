from html.parser import HTMLParser


class myHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print('>>> Multi-line Comment')
            print(data)
        else:
            print('>>> Single-line Comment')
            print(data)

    def handle_data(self, name):
        if str(name).strip():
            print('>>> Data')
            print(name)


N = int(input())
html_string = ''
for i in range(N):
    html_string += input().rstrip() + '\n'

parser = myHTMLParser()
parser.feed(html_string.strip())
parser.close()
