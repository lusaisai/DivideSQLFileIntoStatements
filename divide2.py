class Divider:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path) as f:
            self.content = f.read().strip()
            if len(self.content) > 0 and self.content[-1] != ';':
                self.content += ';'
        self.statements = []
        self.buffer = []
        self.in_quote = False
        self.in_block_comment = False
        self.in_line_comment = False

    def divide(self):
        px = ''
        for x in self.content:
            if not self.in_quote and not self.in_block_comment and not self.in_line_comment and x == ';':
                self.statements.append(''.join(self.buffer))
                self.buffer = []
                px = ''
                continue
            else:
                self.buffer.append(x)

            if not self.in_block_comment and not self.in_quote and not self.in_line_comment:
                if (px, x) == ("/", "*"):
                    self.in_block_comment = True
                elif (px, x) == ("-", "-"):
                    self.in_line_comment = True
                elif x == "'":
                    self.in_quote = True
            else:
                if self.in_block_comment and (px, x) == ("*", "/"):
                    self.in_block_comment = False
                elif self.in_line_comment and x == "\n":
                    self.in_line_comment = False
                elif self.in_quote and x == "'":
                    self.in_quote = False

            px = x


if __name__ == '__main__':
    d = Divider('test.sql')
    d.divide()
    with open('out2.sql', 'w') as f:
        for s in d.statements:
            f.write(s)
            f.write('\n;\n')
