class Article:
    
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        author._articles.append(self)
        if self.magazine not in author._magazines:
            author._magazines.append(self.magazine)
        if magazine:
            magazine._articles.append(self)
        if author not in magazine._contributors:
            magazine._contributors.append(author)
        if title: 
            magazine._titles.append(title)
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise TypeError("author must be an instance of Author")
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if (not hasattr(self, 'title')):
            self._title = value
        
class Author:
        
    def __init__(self, name):
        self.name = name
        self._articles = []
        self._magazines = []
        self._topics = []
        
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if (not hasattr(self, 'name')) and type(value) == str and len(value) > 0:
            self._name = value
        

    def articles(self):
        return self._articles

    def magazines(self):
        return self._magazines

    def add_article(self, magazine, title):
        if magazine.category not in self._topics:
            self._topics.append(magazine.category)
            magazine._contributors.append(self)
        return Article(self, magazine, f"{title}" )

    def topic_areas(self):
        return self._topics if len(self._topics) > 0 else None



class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        self._contributors = []
        self._titles = []
        
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if type(value) == str and len(value) > 0:
            self._category = value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) == str and  1 < len(value) < 17:
            self._name = value 

    def articles(self):
        return self._articles

    def contributors(self):
        return self._contributors

    def article_titles(self):
        return self._titles if len(self._titles) > 0 else None

    def contributing_authors(self):
        # count = 0
        # double_contributors = []
        # sorted_contributors = sorted(self._contributors)
        # for i in range(1, len(sorted_contributors)):
        #     if sorted_contributors[i] == sorted_contributors[i - 1]:
        #         double_contributors.append(sorted_contributors[i])
                
        # # for author in sorted(self._contributors):
        # #     if author
        # # return [contributor for contributor in set(self._contributors) if  author for author in self._contributors ]
        # return list(set(double_contributors))
        
        result = [author for author in set(self._contributors) if sum(1 for article in self._articles if article.author == author) > 2]
        return result if len(result) > 0 else None
