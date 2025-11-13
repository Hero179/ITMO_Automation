class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sbox(self):
        return self.x * self.y

    def pbox(self):
        return (self.x + self.y) * 2

box1 = Box(5, 8)
print(box1.sbox())
print(box1.pbox())

print('\n')

box2 = Box(10, 20)
print(box2.sbox())
print(box2.pbox())

print('\n')

box3 = Box(15, 20)
print(box3.sbox())
print(box3.pbox())

print('\n')

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b

obj = Math(10, 5)
print(obj.addition())
print(obj.multiplication())
print(obj.division())
print(obj.subtraction())

print('\n')

class Elements:

    def __init__(self, text, type, loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return "Клик по кнопке - {}".format(self.text)

text_box = Elements('Text Box', 'Кнопка', '')
check_box = Elements('Check Box', 'Кнопка', '')
radio_button = Elements('Radio Button', 'Кнопка', '')
web_tables = Elements('Web Tables', 'Кнопка', '')
buttons = Elements('Buttons', 'Кнопка', '')
links = Elements('Links', 'Кнопка', '')
broken_links_images = Elements('Broken Links - Images', 'Кнопка', '')
upload_and_download = Elements('Upload and Download', 'Кнопка', '')
dynamic_properties = Elements('Dynamic Properties', 'Кнопка', '')

print(text_box.click())
print(check_box.click())
print(radio_button.click())
print(web_tables.click())
print(buttons.click())
print(links.click())
print(broken_links_images.click())
print(upload_and_download.click())
print(dynamic_properties.click())

print('\n')

class Forms:

    def __init__(self, text, type, loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return "Клик по кнопке - {}".format(self.text)

practice_form = Forms('Practice Form', 'Кнопка', '')

print(practice_form.click())

print('\n')

class Alerts_Frame_Windows:

    def __init__(self, text, type, loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return "Клик по кнопке - {}".format(self.text)

browser_windows = Alerts_Frame_Windows('Browser Windows', 'Кнопка', '')
alerts = Alerts_Frame_Windows('Alerts', 'Кнопка', '')
frames = Alerts_Frame_Windows('Frames', 'Кнопка', '')
nested_frames = Alerts_Frame_Windows('Nested Frames', 'Кнопка', '')
modal_dialogs = Alerts_Frame_Windows('Modal Dialogs', 'Кнопка', '')

print(browser_windows.click())
print(alerts.click())
print(frames.click())
print(nested_frames.click())
print(modal_dialogs.click())

print('\n')

class Widgets:

    def __init__(self, text, type, loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return "Клик по кнопке - {}".format(self.text)

accordian = Widgets('Accordian', 'Кнопка', '')
auto_complete = Widgets('Auto Complete', 'Кнопка', '')
date_picker = Widgets('Date Picker', 'Кнопка', '')
slider = Widgets('Slider', 'Кнопка', '')
progress_bar = Widgets('Progress Bar', 'Кнопка', '')
tabs = Widgets('Tabs', 'Кнопка', '')
tool_tips = Widgets('Tool Tips', 'Кнопка', '')
menu = Widgets('Menu', 'Кнопка', '')
select_menu = Widgets('Select Menu', 'Кнопка', '')

print(accordian.click())
print(auto_complete.click())
print(date_picker.click())
print(slider.click())
print(progress_bar.click())
print(tabs.click())
print(tool_tips.click())
print(menu.click())
print(select_menu.click())

print('\n')

class Interactions:

    def __init__(self, text, type, loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return "Клик по кнопке - {}".format(self.text)

sortable = Interactions('Sortable', 'Кнопка', '')
selectable = Interactions('Selectable', 'Кнопка', '')
resizable = Interactions('Resizable', 'Кнопка', '')
droppable = Interactions('Droppable', 'Кнопка', '')
dragabble = Interactions('Dragabble', 'Кнопка', '')

print(sortable.click())
print(selectable.click())
print(resizable.click())
print(droppable.click())
print(dragabble.click())

print('\n')

class Book_Store_Application:

    def __init__(self, text, type, loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return "Клик по кнопке - {}".format(self.text)

login = Interactions('Login', 'Кнопка', '')
book_store = Interactions('Book Store', 'Кнопка', '')
profile = Interactions('Profile ', 'Кнопка', '')
book_store_api = Interactions('Book Store API', 'Кнопка', '')

print(login.click())
print(book_store.click())
print(profile.click())
print(book_store_api.click())

print('\n')