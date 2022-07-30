import re
from enum import Enum


class TokenType(Enum):
    BLOCK_COMMENT_START = 1
    LINE_COMMENT_START = 2
    QUOTE_START = 3


def get_token_type(token: str):
    block_comment_pos = token.find('/*')
    line_comment_pos = token.find('--')
    quote_pos = token.find("'")


class Divider:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path) as f:
            self.lines = f.readlines()
        self.statements = []
        self.buffer = []
        self.in_comment = False
        self.in_quote = False

    def divide(self):
        for line in self.lines:
            if not line.strip():
                continue

            for token in re.split(r'\s+', line.strip()):
                if self.in_comment:
                    if "*/" in token and "/*" not in re.sub(r'\*/.*', '', token):
                        self.in_comment = False
                        self.buffer.append(re.sub(r'.*\*/', '', token))
                    else:
                        pass
                elif self.in_quote:
                    self.buffer.append(token)
                    if token.count("'") % 2 == 1:
                        self.in_quote = False
                elif "--" in token:
                    self.buffer.append(re.sub(r'--.*', '', token).strip())
                    break
                elif ";" in token:
                    self.buffer.append(re.sub(r';.*', '', token).strip()+';')
                    self.statements.append(' '.join(self.buffer))
                    self.buffer = []
                    self.buffer.append(re.sub(r'.*;', '', token).strip())
                elif "/*" in token and "*/" not in re.sub(r'.*/\*', '', token):
                    self.buffer.append(re.sub(r'/\*.*', '', token).strip())
                    self.in_comment = True
                elif token.count("'") % 2 == 1:
                    self.buffer.append(token)
                    self.in_quote = True
                else:
                    self.buffer.append(token)

            if len(self.buffer) > 0 and self.buffer[-1].endswith(";"):
                self.statements.append(' '.join(self.buffer))
                self.buffer = []

        try:
            self.buffer.remove('')
        except ValueError:
            pass
        if len(self.buffer) > 0 and not self.buffer[-1].endswith(";"):
            self.statements.append(' '.join(self.buffer)+';')


if __name__ == '__main__':
    d = Divider('test.sql')
    d.divide()
    with open('out.sql', 'w') as f:
        for s in d.statements:
            f.write(s)
            f.write('\n')
