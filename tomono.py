def replace_text(input_string):
    # Create a dictionary mapping Latin characters to Mathematical Monospace characters
    latin_to_monospace = {}
    start_char = ord('A')  # Start with Latin uppercase A
    start_monospace_char = 0x1D670  # Start with U+1D670 (Mathematical Monospace Capital A)
    
    # Map uppercase letters
    for i in range(26):
        latin_to_monospace[chr(start_char + i)] = chr(start_monospace_char + i)
    
    # Map lowercase letters
    start_char = ord('a')  # Start with Latin lowercase a
    start_monospace_char = 0x1D68A  # Start with U+1D68A (Mathematical Monospace Lowercase A)
    for i in range(26):
        latin_to_monospace[chr(start_char + i)] = chr(start_monospace_char + i)

    # Replace text
    result = []
    for char in input_string:
        if char == ' ':  # Replace spaces with em spaces
            result.append('\u2003')
        elif char in latin_to_monospace:  # Replace Latin characters with monospace characters
            result.append(latin_to_monospace[char])
        else:  # Leave other characters unchanged
            result.append(char)
    
    return ''.join(result)

# Example usage
input_string: str = input(str("Provide the string to transform:"))
output_string: str = replace_text(input_string)
print(output_string)
