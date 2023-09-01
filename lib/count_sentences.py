class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        sentences = self.value.split('.')
        sentences = [s.strip() for s in sentences if s.strip()]

        question_sentences = self.value.split('?')
        question_sentences = [s.strip() for s in question_sentences if s.strip()]

        exclamation_sentences = self.value.split('!')
        exclamation_sentences = [s.strip() for s in exclamation_sentences if s.strip()]

        total_sentences = len(sentences) + len(question_sentences) + len(exclamation_sentences)
        return total_sentences

if __name__ == "__main__":
    string = MyString("Hello World.")
    print(string.is_sentence())  # True
    print(string.is_question())  # False
    print(string.is_exclamation())  # False
    print(string.count_sentences())  # 1
