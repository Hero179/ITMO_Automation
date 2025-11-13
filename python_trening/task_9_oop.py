# class Button:
#
#     def __init__(self, text, link):
#         self.text = text
#         self.link = link
#
#
# # Создаем экземпляры класса
# home = Button('Домой', '/home')
# catalog_msk = Button('Каталог', '/msk/catalog')
#
# # Получаем доступ к атрибутам
# print(home.text)
# print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)
#
# print('\n')
#
# print(catalog_msk.text)
# print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)

class ButtonTwo:

    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)

home_two = ButtonTwo('Домой', '/home', 'button#home')

print(home_two.click())

print('\n')

class Input:

    def __init__(self, text, loc):
        self.loc = loc
        self.text = text

search = Input('Поиск', 'input#search')
products = Input('Товары', 'input#products')

print(search.loc)
print(search.text)
print(products.loc)
print(products.text)

print('\n')

class Button:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

pictures = Button('Картинки', 'button#pictures')

print(pictures.text)
print(pictures.loc)

print('\n')

class Title:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

video = Title('Видео', 'title#video')

print(video.text)
print(video.loc)

print('\n')

class Link:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

balance = Link('Баланс', 'link#balance')

print(balance.text)
print(balance.loc)