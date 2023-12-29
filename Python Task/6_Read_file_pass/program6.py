# 6.Read a file and pass it to a function which checks for the given input string 
# ( case insensitive check).
# If the given string is found, the function should return True. 
# Create another function which will read the input file s and scan it to 
# get the count of each word in it. 
# After the process is completed print each word  along with the number of times 
# it occurred in the file.


class FileReader:
    @staticmethod
    def check_word(word):
        with open("file.txt", "r") as file:
            for line in file:
                if word in line:
                    return True
        return False

    @staticmethod
    def count_word(filename):
        count_words = {}
        with open(filename, 'r') as file:
            for line in file:
                for word in line.split():
                    count_words[word] = count_words.get(word, 0) + 1
        return count_words


# Check if a word is present in the file
word_to_check = "Hello"
if FileReader.check_word(word_to_check):
    print(f"The word '{word_to_check}' is present in the file.")
else:
    print(f"The word '{word_to_check}' is not present in the file.")

# Count occurrences of each word in the file
filename_to_count = "file.txt"
word_counts = FileReader.count_word(filename_to_count)
print("Word counts:", word_counts)
