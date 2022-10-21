# create a function that will wrap the text
def wrap_text(text, font, max_width):
    # create a list of words from the text
    words = text.split(' ')
    # create a list of lines
    lines = []
    # create a variable that will hold the current line
    current_line = ''
    # loop through the words
    for word in words:
        # check if the current line + the word is too long
        if font.size(current_line + word)[0] < max_width:
            # if it is not too long, add the word to the current line
            current_line += word + ' '
        else:
            # if it is too long, add the current line to the list of lines
            lines.append(current_line)
            # set the current line to the word
            current_line = word + ' '
    # add the last line to the list of lines
    lines.append(current_line)
    # return the list of lines
    return lines