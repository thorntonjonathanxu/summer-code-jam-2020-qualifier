"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import typing
import textwrap
import re
# from itertools import count



class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:
    """The `Article` class you need to write for the qualifier."""

    # _ids = count(0)
    _ids = -1
    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
      # self.id = next(self._ids)
      Article._ids += 1
      self.id = Article._ids
      self.title = title
      self.author = author
      self.publication_date = publication_date
      self.content = content
      self.last_edited = None
      pass

    # @property
    # def content(self):
    #   return self._content

    # @content.setter
    # def content(self,x):
    #   if (self.content == x):
    #     return self._content
    #   else:
    #     self.last_edited = datetime.datetime.now()
    #     self.content = x
    #     return self._content

    def __repr__(self):
      self.publication_date = datetime.datetime.isoformat(self.publication_date)
      return '<{self.__class__.__name__} title="{self.title}" author=\'{self.author}\' publication_date=\'{self.publication_date}\'>'.format(self=self)

    def __len__(self):
      return len(self.content)

    def short_introduction(self, n_characters):
      # spaces = [n for n in range(n_characters+1) if self.content.find(' ',n) == n]
      # return self.content[:spaces[-1]]
      return textwrap.wrap(self.content, n_characters, break_long_words=False)[0]

    def most_common_words(self,n_words):
      words_dict = {}
      temp = self.content.strip().lower()
      temp = re.sub('[^0-9a-zA-Z]+', ' ', temp) #Replace non alphanumeric characters
      temp =temp.strip()
      word_list = temp.split(' ')
      for word in word_list:
        if word in words_dict:
          words_dict[word] += 1
        else:
          words_dict[word] = 1
      return {k: v for k, v in sorted(words_dict.items(), key=lambda item: item[1],reverse=True)[:n_words]}

#Beginner Level Test Cases----------------------------------------------------------
# fairytale = Article(title="The emperor's new clothes",author="Hans Christian Andersen",content="'But he has nothing at all on!' at last cried out all the people. The Emperor was vexed, for he knew that the people were right.",publication_date=datetime.datetime(1837, 4, 7, 12, 15, 0))
# print(fairytale)


#Intermediate Level Test Cases-------------------------------------------------------
# article_one = Article(title="PEP-8", author="Guide van Rossum", content="Use snake_case", publication_date=datetime.datetime(2001, 7, 5))
# print(article_one.id)
# article_two = Article(title="Fluent Python", author="Luciano Ramalho", content="Effective Programming", publication_date=datetime.datetime(2015, 8, 20))
# print(article_two.id)

# print(fairytale.last_edited)
# fairytale.content = "I'm making a change to the content of this article"
# print(fairytale.last_edited)
# print(fairytale.__dict__)