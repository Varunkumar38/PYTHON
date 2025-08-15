def remove_spaces(s):
    result = ""
    for char in s:
        if char != " ":
            result += char
    return result

# Example usage
text = "V a r u n   Kumar"
print(remove_spaces(text))