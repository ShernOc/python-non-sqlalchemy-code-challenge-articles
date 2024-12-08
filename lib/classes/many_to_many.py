
class Article:
    all = []
    def __init__(self, author, magazine, title):
        
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
       
    @property
    def author(self):
        return self._author  
    
    @author.setter 
    def author(self,value):
        if not isinstance(value,Author):
            raise Exception("The author has to be an instance of Author class ")
        self._author = value 
            
    @property
    def magazine(self):
        return self._magazine
    
    @ magazine.setter 
    def magazine(self,value):
        if not isinstance(value, Magazine):
            raise Exception("The magazine has to be on instance of Magazine class ")
        self._magazine = value
    
    @property
    def title(self):
        return self._title 
    
    @title.setter 
    def title(self,value):
       
        if hasattr(self,'_title'):
            raise AttributeError ("The title is cannot be changed")
        
        if not isinstance(value, str):
            raise TypeError("The value has to be a string type")
        
        if  not (5 <= len(value)<= 50):
            raise ValueError(" The characters have  to be between 5 and 50 characters ")
       
        self._title = value

  
class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    #setter 
    @name.setter 
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError("The Value has to be of string type")
        
        if not len(value)>=0:
            raise Exception("The value has to greater than 0 characters long. ")
        
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed after initialization")
        
        self._name = value
            
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        unique = [article.magazine for article in self.articles() if isinstance(article.magazine, Magazine)]
        return unique
    
    def add_article(self, magazine, title):
        #return a new Article object
        return Article(author = self, magazine = magazine, title = title) 

    def topic_areas(self):
        unique_list = self.articles()
        if not unique_list: 
            return None
        category = [article.magazine.category for article in unique_list if isinstance(article.magazine, Magazine)]
        return category
        

class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)
        
    @property 
    def name(self):
        return self._name 
    
    @name.setter
    def name(self,value):
        if hasattr(self, '_name'):
            raise AttributeError("'Magazine' object has no attribute '_name'")
        if not isinstance(value,str):
            raise AttributeError("The name is not of string type")
        if not 2<= len(value)<=16:
            raise Exception("Values has to be of 2,16 characters")
        self._name = self
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self,value):
        if not isinstance(value,str):
            raise TypeError("The name is not of string type")
        
        if not len(value)>=0:
            raise Exception("Category has to have more that 0 characters")
        self._category = value
            
        
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        unique_list = [unique.author for unique in self.articles() if isinstance(unique.author,Author)]
        return unique_list
    
    def article_titles(self):
        titles_list = [article.title for article in Article.all  if article.magazine == self]
        if not titles_list:
            return None  
        return titles_list

    def contributing_authors(self):
        #return authors who have writted more that 2 articles. 
        author_count = {}  #counts the article per author
        # Count the articles by each author for this magazine
        for article in self.articles():
            if isinstance(article.author, Author):
                if article.author not in author_count:
                    author_count[article.author] = 0
                author_count[article.author] += 1
        
        #author with more than two 
        authors_2= [author for author, count in author_count.items() if count > 2
        ]
        
        if authors_2:
            return authors_2
        else:
            return None  
    
    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
    
        top_magazine = max(cls.all, key = lambda magazine: len(magazine.articles()))
        
        if len(top_magazine.articles()) > 0:
            return top_magazine
        else:
            return None  
  
       
        