def load_colors(filename):
    """
    Load colors from a file.
    
    Args:
        filename (str): Path to the file containing colors
        
    Returns:
        list: List of color strings
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If the file is empty or contains no valid colors
    """
    # Open the file
    try:
        file = open(filename, 'r', encoding='utf-8')
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")
    
    # Read all lines
    colors = []
    for line in file:
        # Remove spaces and newlines
        color = line.strip()
        # Only add non-empty lines
        if color != "":
            colors.append(color)
    
    # Close the file
    file.close()
    
    # Check if we found any colors
    if len(colors) == 0:
        raise ValueError("No colors found in file.")
    
    return colors

def get_color_mapping(colors):
    """
    Create a case-insensitive mapping of colors.
    
    Args:
        colors (list): List of color strings
        
    Returns:
        dict: Dictionary mapping lowercase colors to original case
        
    Examples:
        >>> mapping = get_color_mapping(['Red', 'Blue'])
        >>> mapping['red'] == 'Red'
        True
        >>> mapping['blue'] == 'Blue'
        True
        >>> len(mapping)
        2
        >>> 'RED' in mapping
        False
        >>> 'red' in mapping
        True
    """
    # Create empty dictionary
    mapping = {}
    
    # Add each color to dictionary
    for color in colors:
        # Convert to lowercase for the key
        key = color.lower()
        # Keep original case for the value
        mapping[key] = color
    
    return mapping

def validate_color_choice(choice, color_mapping):
    """
    Validate if a color choice exists in the mapping.
    
    Args:
        choice (str): User's color choice
        color_mapping (dict): Dictionary of valid colors
        
    Returns:
        tuple: (bool, str) - (is_valid, selected_color)
        
    Examples:
        >>> mapping = {'red': 'Red', 'blue': 'Blue'}
        >>> is_valid, color = validate_color_choice('red', mapping)
        >>> is_valid
        True
        >>> color
        'Red'
        >>> is_valid, color = validate_color_choice('RED', mapping)
        >>> is_valid
        True
        >>> color
        'Red'
        >>> is_valid, color = validate_color_choice('green', mapping)
        >>> is_valid
        False
        >>> color is None
        True
    """
    # Remove spaces and convert to lowercase
    choice = choice.strip()
    choice = choice.lower()
    
    # Check if choice is in mapping
    if choice in color_mapping:
        return True, color_mapping[choice]
    else:
        return False, None

if __name__ == "__main__":
    import doctest
    doctest.testmod() 
