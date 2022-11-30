import wikipedia


def main():
    try:
        page_search = input("Please Enter a Page title or Search phrase: ")
        while page_search != "":
            print(f"Title: {page_search}")
            print("Summary:")
            print(wikipedia.summary(f"{page_search}"))
            page_search = input("Please Enter a Page title or Search phrase:  ")
        else:
            print("Thank you.")
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)


if __name__ == '__main__':
    main()
