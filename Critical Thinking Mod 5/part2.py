def calculate_points(books_purchased):
    if books_purchased < 2:
        return 0
    elif books_purchased < 4:
        return 5
    elif books_purchased < 6:
        return 15
    elif books_purchased < 8:
        return 30
    else:
        return 60

def main():
    try:
        books = int(input("Enter the number of books purchased this month: "))
        if books < 0:
            print("Number of books cannot be negative.")
            return
        points = calculate_points(books)
        print(f"Points awarded: {points}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()