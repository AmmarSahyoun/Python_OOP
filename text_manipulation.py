source_file = 'my_doc.txt'
answer_file = 'result.txt'


class Substitute:
    def __init__(self, source_file, answer_file):
        self.source_file = source_file
        self.answer_file = answer_file
        self.words = None

    def string_to_list(self):
        '''Read text file, turn it into a
        2D list of words for each line'''
        words = []
        with open(self.source_file, 'r') as file_object:
            lines = file_object.read().split('\n')
            for line in lines:
                words.append(line.split())
        self.words = words

    def list_to_string(self):
        '''Convert 2D list back into a
        string with newline characters'''
        lines = []
        for line in self.words:
            lines.append(' '.join(line))
        string = '\n'.join(lines)
        self.words = string

    def swap_words(self):
        self.string_to_list()
        for line in self.words:
            for i in range(len(line)):
                if (i + 1) % 5 == 0:
                    word = line[i]
                    line[i] = 'HELLO'
        self.list_to_string()
        file = open(self.answer_file, 'w')
        file.writelines(self.words)
        file.close()

'''The class Stars which is a child class of Substitute, will replace every third word 
      by a series of *  '''
class Stars(Substitute):
    def swap_words(self):
        self.string_to_list()
        for line in self.words:
            for i in range(len(line)):
                if (i + 1) % 3 == 0:
                    word = line[i]
                    line[i] = '*' * len(word)
        self.list_to_string()
        file = open(self.answer_file, 'w')
        file.writelines(self.words)
        file.close()

# h = Substitute(source_file, answer_file)
# h.swap_words()

s = Stars(source_file, answer_file)
s.swap_words()