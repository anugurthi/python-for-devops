import re  # Import the 're' module for Regular Expressions

text = "The quick brown fox"
pattern = r"brown"  # The pattern we want to find

# re.search() looks for the pattern in the text
search = re.search(pattern, text)

if search:
    print("Pattern found:", search.group())  # .group() gives us the matching text
else:
    print("Pattern not found")
