from test_9_checks import Checks


# class Input:
#
#     def __init__(self, text, loc):
#         self.text = text
#         self.loc = loc
#
# search = Input('input#search', '/file/text.txt')
#
# print(search.text + '\n' + search.loc, '\n')
#
#
# class Button:
#
#     def __init__(self, text, loc):
#         self.text = text
#         self.loc = loc
#
# connect = Button('Сonnection', 'Enter')
#
# print(connect.text + '\n' + connect.loc, '\n')
#
# class Title:
#
#     def __init__(self, text, loc):
#         self.text = text
#         self.loc = loc
#
# s_name = Title('File server', '/root')
#
# print(s_name.text + '\n' + s_name.loc, '\n')
#
# class Link:
#
#     def __init__(self, text, loc):
#         self.text = text
#         self.loc = loc
#
# ip_adr = Link('IP', '192.168.0.115')
#
# print(ip_adr.text + '\n' + ip_adr.loc, '\n')


class TextBox(Checks):
    def __init__(self, loc):
        super().__init__(loc)

    def fill_field(self, text):
        return f"Заполняем поле {self.loc} текстом: {text}"


class CheckBox(Checks):
    def __init__(self, loc):
        super().__init__(loc)

    def click_check_box(self):
        return f"Кликаем по чекбоксу {self.loc}"


class RadioButton(Checks):
    def __init__(self, loc):
        super().__init__(loc)

    def click_radio_button(self):
        return f"Кликаем по радио баттону {self.loc}"


class WebTable(Checks):
    def __init__(self, loc):
        super().__init__(loc)

    def get_cell_text(self, row, column):
        return f"Получаем текст из ячейки {self.loc}: Строка {row}, Колонка {column}"


text_box = TextBox("TextBox_Locator")
check_box = CheckBox("CheckBox_Locator")
radio_button = RadioButton("RadioButton_Locator")
web_table = WebTable("WebTable_Locator")

print(f"TextBox locator: {text_box.check_text()}")
print(f"CheckBox locator: {check_box.check_text()}")
print(f"RadioButton locator: {radio_button.check_text()}")
print(f"WebTable locator: {web_table.check_text()}")