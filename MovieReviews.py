

class reviews:
    Score = int()
    prose = str()
    def __init__ (rating, textreview):
        reviews.Score = rating
        reviews.prose = str(textreview)

class movie:
    Title = str()
    ReviewsForThisTitle = []
    def __init__ (title, reviews):
        movie.Title = title
        movie.ReviewsForThisTitle.append(reviews)

    def addreview(review):
        movie.ReviewsForThisTitle.append(review)

    def worst_review():
        x= 0
        for i in range(len(movie.ReviewsForThisTitle)):
            if movie.ReviewsForThisTitle[i].Score <= x:
                x=i
        print(movie.ReviewsForThisTitle[x])
            

def main():
    moviereview = reviews(5, "a GOAT movie")
    newMovie = movie("newMovie", moviereview)

    anotherreview = reviews(2, "a garbage movie")

    newMovie.addreview(anotherreview)

    print(movie.Title)
    print(movie.ReviewsForThisTitle)


if __name__ == "__main__":

    main()