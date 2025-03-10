class movie_recommendation_system:

    def __init__(self, name, rating, release_date, genres):
        self.name = name
        self.rating = rating
        self.release_date = release_date
        self.genres = genres

    def movie_makers(self, dir, prod):
        self.director = dir
        self.production = prod
        print(f"Director: {self.director},\nProduction of: {self.production}")

    def get_details(self):
        print(f"Movie Name: {self.name},\nRating: {self.rating},\nRelease date: {self.release_date},\nGenres: {self.genres}")

# movie1 = movie_recommendation_system("DDLJ", 8.5, "23/04/2000", "Rom-Com")
# movie1.get_details()
# movie1.movie_makers("Ptta nahi....!", "Dharma Production")


# learn about called method and calling method
class Mother:
    def setName(self, name):
        self.name = name

class Kid(Mother):
    def setMarks(self, marks):
        self.marks = marks

class Father:
    def __init__(self, name, age):
        self.property = 78000
        self.name = name
        self.age = age

    def display_property(self):
        print("father's property:", self.property)

class Son(Father):
    def __init__(self, age):
        self.age = age


kid1 = Kid()
print(kid1.setName("Dyuti"))
print(kid1.setMarks(45))
print(kid1.name)
print(kid1.marks)

s = Son()
s.display_property()
    
    