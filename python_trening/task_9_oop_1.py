class Input:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

search = Input('input#search', '/file/text.txt')

print(search.text + '\n' + search.loc, '\n')


class Button:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

connect = Button('Сonnection', 'Enter')

print(connect.text + '\n' + connect.loc, '\n')

class Title:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

s_name = Title('File server', '/root')

print(s_name.text + '\n' + s_name.loc, '\n')

class Link:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

ip_adr = Link('IP', '192.168.0.115')

print(ip_adr.text + '\n' + ip_adr.loc, '\n')