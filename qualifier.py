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
from collections import Counter

class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:
    """The `Article` class you need to write for the qualifier."""

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
      self.title = title
      self.author = author
      self.publication_date = datetime.datetime.isoformat(publication_date)
      self.content = content
      pass

    def __repr__(self):
      return '{self.__class__.__name__} title="{self.title}" author="{self.author}" publication_date="{self.publication_date}"'.format(self=self)

    def len(self):
      return len(self.content)

    def short_introduction(self, n_characters):
      # spaces = [n for n in range(n_characters+1) if self.content.find(' ',n) == n]
      # return self.content[:spaces[-1]]
      return textwrap.wrap(self.content, n_characters, break_long_words=False)[0]

    def most_common_words(self,n_words):
      words_dict = {}
      for word in self.content:
        if word in words_dict:
          words_dict[word] += 1
        else:
          words_dict[word] = 1
      return sorted(words_dict,key = words_dict.gets, reverse=True)[:n_words]





fairytale = Article(title="The emperor's new clothes",author="Hans Christian Andersen",content="'But he has nothing at all on!' at last cried out all the people. The Emperor was vexed, for he knew that the people were right.",publication_date=datetime.datetime(1837, 4, 7, 12, 15, 0))
print(fairytale)
print(fairytale.len())
print(fairytale.short_introduction(60))
fairytale.most_common_words(5)