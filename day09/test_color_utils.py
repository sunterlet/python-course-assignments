import pytest
import color_utils as cu

def test_load_colors(tmp_path):
    # Create a temporary color file
    color_file = tmp_path / "colors.txt"
    color_file.write_text("Red\nBlue\nGreen")
    
    colors = cu.load_colors(str(color_file))
    assert len(colors) == 3
    assert "Red" in colors
    assert "Blue" in colors
    assert "Green" in colors

def test_load_colors_empty_file(tmp_path):
    # Create an empty file
    color_file = tmp_path / "empty.txt"
    color_file.write_text("")
    
    with pytest.raises(ValueError):
        cu.load_colors(str(color_file))

def test_load_colors_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        cu.load_colors("nonexistent.txt")

def test_get_color_mapping():
    colors = ["Red", "Blue", "Green"]
    mapping = cu.get_color_mapping(colors)
    
    assert mapping["red"] == "Red"
    assert mapping["blue"] == "Blue"
    assert mapping["green"] == "Green"
    assert len(mapping) == 3

def test_validate_color_choice():
    mapping = {"red": "Red", "blue": "Blue"}
    
    # Test valid color
    is_valid, color = cu.validate_color_choice("red", mapping)
    assert is_valid
    assert color == "Red"
    
    # Test case insensitivity
    is_valid, color = cu.validate_color_choice("RED", mapping)
    assert is_valid
    assert color == "Red"
    
    # Test invalid color
    is_valid, color = cu.validate_color_choice("green", mapping)
    assert not is_valid
    assert color is None 