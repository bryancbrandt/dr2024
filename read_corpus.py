unique_items = set()

with open('WikiQA-train.txt', 'r') as file:
    for line in file:
        # Extract text until the first tab character
        text_until_tab = line.split('\t')[0]

        # Remove leading and trailing whitespaces
        text_until_tab = text_until_tab.strip()

        # Add to the set to ensure uniqueness
        unique_items.add(text_until_tab)

# Convert set to list
unique_items_list = list(unique_items)

# Print or use the unique items list as needed
print(unique_items_list)
print(len(unique_items_list))

# Count the total number of words
total_words = sum(len(item.split()) for item in unique_items_list)
print(f"Total Tokens: {total_words}")

# Write the set to a file formatting each question on a line
with open('train_questions.txt', 'w') as output_file:
    for item in unique_items_list:
        output_file.write(item + '\n')

