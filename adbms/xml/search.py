import xml.etree.cElementTree as ET

tree = ET.parse('./data.xml')
books = tree.findall('./Books/Book')


for book in books:
    print("Book ID:", book.get('id'))
    print("Price:", book.get('price'))
    print("Title:", book.find('title').text)
    print("Author:", book.find('author').text)
    print("\n")
    
#search for a specific book
booktitle = tree.find(".//Book[title='hello3']")
if booktitle:
    print("Book ID:", book.get('id'))
    print("Price:", book.get('price'))
    print("Title:", book.find('title').text)
    print("Author:", book.find('author').text)
else:
    print("nhi mila")
    
#finding book with id = 3 and changing the title
# Find the book with the specified ID
book_id = "3"
book = tree.find(".//Book[@id='" + book_id + "']")

# Check if the book is found
if book is not None:
    # Update the title
    title_element = book.find('title')
    if title_element is not None:
        new_title = "the secret"
        title_element.text = new_title

        # Save the changes back to the XML file
        tree.write('./data.xml')
        print(f'Title of Book with ID {book_id} changed to "{new_title}".')
    else:
        print(f'Title element not found for Book with ID {book_id}.')
else:
    print(f'Book with ID {book_id} not found.')

