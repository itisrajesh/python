# >: Right-justify the text
# ^: Center the text
# (space): Pad with spaces
# 0 (zero): Pad with zeros
# … (ellipsis): Truncate with an ellipsis

def text_format(text):
    """
    Description: Function to display formatted text (width=50) as output.
    Input: {text :str}
    Output: None
    """
    print(f'{text:^50}')
    

if __name__ == '__main__':
    text_format("Python is a programming language")