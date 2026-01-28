

class reviews:
    Score = int()
    prose = str()
    def __init__ (self, rating, textreview):
        self.Score = rating
        self.prose = str(textreview)
    def printreview(self):
        print("Score:", self.Score)
        print("Review:", self.prose)

class movie:
    Title = str()
    ReviewsForThisTitle = []
    def __init__ (self, title, reviews):
        self.Title = title
        self.ReviewsForThisTitle.append(reviews)

    def addreview(self,review):
        self.ReviewsForThisTitle.append(review)
    def worst_review(self):
        x= 0
        for i in range(len(self.ReviewsForThisTitle)):
            if self.ReviewsForThisTitle[i].Score <= x:
                x=i
        self.ReviewsForThisTitle[x].printreview()
    def best_review(self):
        x= 0
        for i in range(len(self.ReviewsForThisTitle)):
            if self.ReviewsForThisTitle[i].Score >= x:
                x=i
        self.ReviewsForThisTitle[x].printreview()
    def average_review(self):
        total = 0
        for i in range(len(self.ReviewsForThisTitle)):
            total = total + self.ReviewsForThisTitle[i].Score
        average = total / len(self.ReviewsForThisTitle)
        print("Average score:", average)


def main():
    moviereview = reviews(5, "a GOAT movie")
    newMovie = movie("newMovie", moviereview)

    anotherreview = reviews(2, "a garbage movie")

    newMovie.addreview(moviereview)
    newMovie.addreview(anotherreview)

    print(newMovie.Title)
    newMovie.worst_review()
    newMovie.best_review()
    newMovie.average_review()

if __name__ == "__main__":

    main()