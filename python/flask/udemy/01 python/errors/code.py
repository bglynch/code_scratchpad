def divide(divided, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return divided / divisor


grades = []
print("Welcome to the average grade program.")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print(e)
    print("There are no grades in the list")
else:
    print(f"The average grade is {average}.")
finally:
    print("Thank you")


# =============================================================================
# Custon error classes
# =============================================================================
class TooManyPagesReadError(ValueError):
    pass


class Book:
    def __init__(self, name:str, page_count:int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return(
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
            )
    
    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages"
            )
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}")

python101 = Book("Python101", 60)
try:
    python101.read(35)
    python101.read(50)
except TooManyPagesReadError as e:
    print(e)
