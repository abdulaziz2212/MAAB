import string
from collections import Counter

# File path for the input text file
file_path = 'sample.txt'

# File path for the output report
report_path = 'word_count_report.txt'

# Function to create the file if it does not exist
def create_sample_file():
    print("sample.txt not found.")
    print("Please type in a paragraph to create the file.")
    text = input("Enter your paragraph: ")
    with open(file_path, 'w') as file:
        file.write(text)
    print("sample.txt has been created with your input.")

# Function to clean and count word frequencies
def count_word_frequencies(text):
    # Convert text to lowercase and remove punctuation
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Split the text into words
    words = text.split()
    
    # Count the frequency of each word
    word_count = Counter(words)
    
    return word_count, len(words)

# Function to generate the report and save to the file
def generate_report(word_count, total_words):
    # Sort the word counts by frequency (most common first)
    sorted_word_count = word_count.most_common(5)
    
    # Prepare the report content
    report_content = "Word Count Report\n"
    report_content += f"Total Words: {total_words}\n"
    report_content += "Top 5 Words:\n"
    
    for word, count in sorted_word_count:
        time_str = "times" if count > 1 else "time"
        report_content += f"{word} - {count} {time_str}\n"
    
    # Write the report to the file
    with open(report_path, 'w') as file:
        file.write(report_content)
    print(f"Word count report saved to {report_path}")

# Main function to process the word frequency count
def main():
    # Check if the file exists
    try:
        with open(file_path, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        create_sample_file()
        with open(file_path, 'r') as file:
            text = file.read()
    
    # Count word frequencies
    word_count, total_words = count_word_frequencies(text)
    
    # Display total word count and top 5 most common words
    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in word_count.most_common(5):
        time_str = "times" if count > 1 else "time"
        print(f"{word} - {count} {time_str}")
    
    # Generate and save the report
    generate_report(word_count, total_words)

# Run the program
if __name__ == "__main__":
    main()
