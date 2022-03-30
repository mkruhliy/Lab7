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
        while self.position > 0 and \
            self.document.characters[self.position-1].character != '\n':
            self.position -= 1
            if self.position == 0:
                break

    def end(self):
        while self.position < len(self.document.characters) \
            and self.document.characters[self.position].character != '\n':
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
        if not hasattr(character, 'character'):
            character = Character(character)
        self.characters.insert(self.cursor.position,character)
        self.cursor.forward()

    def delete(self):
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
            print('check your file name')


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
            print("'{}' is invalid. Only single characters can be used".format(character))
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
d.insert('h')
d.insert('e')
d.insert(Character('l', bold=True))
d.insert(Character('l', bold=True))
d.insert('o')
d.insert('\n')
d.insert(Character('w', italic=True))
d.insert(Character('o', italic=True))
d.insert(Character('r', underline=True))
d.insert('l')
d.insert('d')
print(d.string)
# he*l*lo
# /w/o_rld




# Improvements:

print(d.cursor.position)
# 11
d.cursor.forward()             # forward() improved: can't go forward in cursor position while being on the last position
print(d.cursor.position)
# 11


d1 = Document()
d1.insert('W')
d1.cursor.home()
print(d1.cursor.position)
# 0
d1.cursor.back()               # back() improved: can't go backwards in cursor position while being in the start position
print(d1.cursor.position)
# 0


d1.cursor.home()               # home() improved: now works while being in the start position
print(d1.cursor.position)
# 0


d1.cursor.end()
d1.delete()                    # delete() improved: doesn't crash but informs us if we try to delete character while cursor being on the last position


d1.save()                      # save() improved: now can't save if file name is not specified(Document(filename)) or file name is not str type
# check your file name


ch1 = Character(5)             # __init__ improved: now checks if character is a str type and if it is a single letter
# '5' is invalid. Only str can be used
ch2 = Character('lmao')
# 'lmao' is invalid. Only single characters can be used
