
class TextEditor:
    def __init__(self):
        self.text = [[]]
        self.cursor = [0,0]

    def type_in(self, char):
        line, col = self.cursor
        self.text[line].insert(col, char)
        self.cursor[1] += 1
    
    def newline(self):
        line, col = self.cursor
        new_line = self.text[line][col:]
        self.text[line] = self.text[line][:col]
        self.text.insert(line+1, new_line)
        self.cursor = [line+1, 0]

    def backspace(self):
        line, col = self.cursor
        if col > 0:
            # decrement normally
            self.text[line].pop(col - 1)
            self.cursor[1] -= 1
        elif line > 0:
            lengthOfFirstLine = len(self.text[line-1])
            self.text[line-1].extend(self.text[line])
            self.text.pop(line)
            self.cursor = [line -1, lengthOfFirstLine]

    def move_cursor(self, direction):
        line, col = self.cursor
        if direction == "left":
            if col > 0:
                self.cursor = [line, col-1]
            elif line > 0:
                self.cursor[0] -= 1
                currLineIndex = self.cursor[0]
                self.cursor[1] = len(self.text[currLineIndex])
        elif direction == "right":
            if col < len(self.text[line]):
                self.cursor[1] += 1
            elif line < len(self.text) - 1:
                self.cursor[0] += 1
                self.cursor[1] = 0
        elif direction == "up" and line > 0:
            self.cursor[0] -= 1
            newlineindex = self.cursor[0]
            self.cursor[1] = min(self.cursor[1], len(self.text[newlineindex]))
        elif direction == "down" and line < len(self.text) - 1:
            self.cursor[0] += 1
            newlineindex = self.cursor[0]
            self.cursor[1] = min(self.cursor[1], len(self.text[newlineindex]))


    



    

    # def type_in(self, char):
    #     self.text.insert(self.cursor, char)
    #     self.cursor += 1
    
    # def backspace(self):
        
    #     if self.cursor > 0:
    #         self.text.pop(self.cursor - 1)
    #         self.cursor -= 1

    # def move_cursor(self, direction):
    #     if direction == "left" and self.cursor > 0:
    #         self.cursor -= 1
    #     if direction == "right" and self.cursor < len(self.text):
    #         self.cursor += 1


    # def __str__(self):
    #     firstString = ''.join(self.text[:self.cursor])
    #     firstStringPlusCursor = firstString + "|"
    #     completeString = firstStringPlusCursor + ''.join(self.text[self.cursor:])
    #     return completeString





editor = TextEditor()
print(str(editor))
assert str(editor) == "|"
editor.type_in("a")
print('curr editor', str(editor))
assert str(editor) == "a|"

editor.type_in("b")
assert str(editor) == "ab|"

editor.move_cursor("left")
assert str(editor) == "a|b"



editor.backspace()

assert str(editor) == "|b"


editor.backspace()
assert str(editor) == "|b"

editor.move_cursor("right")
assert str(editor) == "b|"

editor.backspace()
assert str(editor) == "|"








"""
Part 1 - basic text editor

Part 2 - introduce a cursor
    type_in(character) - insert the character to be before the cursor
    backspace() - delete the character that is before the cursor
    __str__() - return the contents as a string, with a `|` inserted where the cursor is.

    move_cursor(direction) - move the cursor one character either left or right

Part 3 - multiple lines
    move_cursor(direction) - up and down, left, right
    newline() - insert a line break before the cursor

    backspace() - merges lines when cursor is at the beginning of a line

"""


