import sys

class Cursor:
    def __init__(self, document):
        self.document = document
        self.position = 0
    def forward(self):
        try:
            self.position += 1
            if len(self.document.characters)==0 or self.position==len(self.document.characters)+1:
                raise IndexError
        except IndexError:
            self.position -= 1
    def back(self):
        try:
            self.position -= 1
            if self.position < 0:
                raise IndexError
        except IndexError:
            self.position += 1
        
    def home(self):
        while self.position > 0 and self.document.characters[self.position-1].character != '\n':
            self.position -= 1
            if self.position == 0:
                break

    def end(self):
        while self.position < len(self.document.characters) and self.document.characters[self.position].character != '\n':
            self.position += 1


class Document:
    def __init__(self, filename=''):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = filename
    @property
    def string(self):
        return "".join((str(c) for c in self.characters))
    def insert(self, character):
        if not hasattr(character, 'character'):      # ексепшн якщо чарактер не стр
            character = Character(character)
        self.characters.insert(self.cursor.position,character)
        self.cursor.forward()
    def delete(self):       # тута модифікуй (якщо хочу ще раз видалити) - назад одну і видалили, експшн якщ опусто
        try:
            del self.characters[self.cursor.position]
        except IndexError:
            print("No characters to delete")

    def save(self):
        try:
            if type(self.filename) != str or self.filename == '':
                raise FileNotFoundError
            with open(self.filename, 'w') as file:
                file.write(''.join((str(c) for c in self.characters)))
        except FileNotFoundError:
            print('file shitt')

class Character:    # if string
    def __init__(self, character, bold=False, italic=False, underline=False):
        try:
            if type(character) != str:
                raise ValueError
            if len(character) != 1:
                raise TypeError
            self.character = character
        except ValueError:
            print("'{}' is invalid. Only str can be used".format(character))
            sys.exit(0)
        except TypeError:
            print("'{}' is invalid. Only single characters".format(character))
            sys.exit(0)
        self.bold = bold
        self.italic = italic
        self.underline = underline
    
    def __str__(self):
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else ''
        return bold + italic + underline + self.character

d = Document()
#d.insert(Character('d', bold=True))
d.insert('l')
d.cursor.back()
# d.delete()
# d.insert('e')
# d.insert('l')
# d.insert('l')
# d.insert('o')
print(d.string)
print(d.cursor.position)
#d.save()




# print(d.cursor.position)
# d.cursor.forward()
# d.cursor.forward()
# print(d.cursor.position)
# d.insert('w')
# d.cursor.forward()
# d.cursor.forward()
# d.cursor.forward()
# d.cursor.forward()
# d.cursor.back()
# print(d.string)


# print(d.cursor.position)

# d.cursor.home()
# d.cursor.end()
# print(d.cursor.position)

#print(d.string)

# d = Document()
# d.insert('h')
# d.insert('e')
# d.insert(Character('l', bold=True))
# d.insert(Character('l', bold=True))
# d.insert('o')
# d.insert('\n')
# d.insert(Character('w', italic=True))
# d.insert(Character('o', italic=True))
# d.insert(Character('r', underline=True))
# d.insert('l')
# d.insert('d')
# #print(d.string)

# d.cursor.home()
# d.delete()
# d.insert('W')
# #print(d.string)

# d.characters[0].underline = True
# print(d.string)




# doc = Document()
# doc.filename = "test_document"
# doc.insert('h')
# doc.insert('e')
# doc.insert('l')
# doc.insert('l')
# doc.insert('o')
# print("".join(doc.characters))

# d = Document()
# d.insert('h')
# d.insert('e')
# d.insert('l')
# d.insert('l')
# d.insert('o')
# d.insert('\n')
# d.insert('w')
# d.insert('o')
# d.insert('r')
# d.insert('l')
# d.insert('d')
# d.cursor.home()
# d.insert("*")
# print(d.string)
# d.cursor.end()
# d.insert("*")
# print(d.string)
# d.cursor.home()
# d.delete()
# print(d.string)