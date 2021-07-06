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