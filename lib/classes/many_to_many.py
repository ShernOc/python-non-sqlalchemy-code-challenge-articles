
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
       
        if hasattr(self,"title"):
            AttributeError ("The title is cannot be changed")
        else:
            if isinstance(value, str):
               if 5 <= len(value)<= 50: 
                    self._title = value
               else:
                   ValueError(" The characters have  to be between 5 and 50 characters ")
                   
            else: TypeError("The value has to be a string type")
       
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
        if hasattr(self, "name"):
            AttributeError("Name cannot be changed after initialization")
        else: 
            if isinstance(value,str):
                if len(value)>=0:
                    self._name = value
                else: 
                    ValueError("The Name value must be longer than 0 character")
            else: 
                TypeError("The Value has to be of string type")
        
 
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list ({article.magazine for article in self.articles()})
    
    
    def add_article(self, magazine, title):
        #return a new Article object
        return Article(author = self, magazine = magazine, title = title) 

    def topic_areas(self):
        topic_areas = list({magazine.category for magazine in self.magazines()})
        if topic_areas:
            return topic_areas
        else:
            return None
        
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
        
        if isinstance(value,str):
            if 2<= len(value)<=16:
                self._name = value
            else:  
                ValueError("Values has to be of 2 and 16 characters")
        else: 
            TypeError("Name must be a string")
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self,value):
        if isinstance(value,str):
            if len(value):
               self._category = value  
            else: 
             TypeError("The name is not of string type")
        else: 
            Exception("Category has to have more that 0 characters")
       
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        unique_list = list ({unique.author for unique in self.articles()})
        return unique_list
    
    def article_titles(self):
        titles_list = [article.title for article in self.articles()]
        if titles_list:
            return titles_list
        return None

    def contributing_authors(self):
        authors = {}
        list_of_authors = []
        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1  
        
        for author in authors:
            if authors[author] >= 2:
                list_of_authors.append(author) 
                  
        if (list_of_authors):
            return list_of_authors
        else:
            return None
    

# instances 
author_1 = Author("Carry Bradshaw")
author_2 = Author("Nathaniel Hawthorne")

magazine1 = Magazine("Vogue", "Fashion")
magazine2 = Magazine("How to Kill a Mocking Bird", "Lifestyle")

article_1 = Article(author_1, magazine1, "How to wear a tutu with style")
article_2 = Article(author_2, magazine2, "Dating life in NYC")

#calling the functions 
#Show case the article 
print([article.title for article in author_1.articles()])
print([article.title for article in author_2.articles()])

#adding the articles
new_article = author_1.add_article(magazine1, "Top 10 fashion tips")
print(new_article.title)



#getting the magazine
print([mag.name for mag in author_1.magazines()])

#showing the topic areas 
print(author_2.topic_areas())

#magazine title
print([article.title for article in magazine1.articles()])

#showing the contributors based on the author. 
print([author.name for author in magazine1.contributors()])

#showcase the magazine titles
print(magazine1.article_titles())

#contributing authors 
print([author.name for author in magazine1.contributing_authors()])

#showcasing all the articles
print([article.title for article in Article.all])