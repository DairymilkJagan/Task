def sort_sorted():
    # Using sorted() on a list of names
    names = ["Jagan", "Bharani", "Vijay", "Virat"]
    sorted_names = sorted(names)
    print("original:",names)
    print("Sorted names using sorted():", sorted_names)

    # Using sort() on a list of words
    words = ["Geeks", "For", "Geeks"]
    words.sort()
    print("original list:",words)
    print("Sort words using sort():", words)

if __name__ == "__main__":
    sort_sorted()
