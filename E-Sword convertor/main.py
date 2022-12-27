import docx
import re

# Open the Word document
doc = docx.Document('bible.docx')


# Initialize a variable to store the text of the bible
text = ""

# Loop through each paragraph in the document
for paragraph in doc.paragraphs:
    # Add the paragraph text to the overall text variable
    text += paragraph.text + '\n'

# Use a regular expression to find all the verse numbers in the text
verse_numbers = re.findall(r'\d+:\d+', text)

# Loop through each verse number and replace it with the appropriate e-Sword tag
for verse_number in verse_numbers:
    text = text.replace(verse_number, f'<V {verse_number}>')

# Save the text to a file
with open('bible.txt', 'w') as f:
    f.write(text)