from unittest.mock import patch
import project

def test_add_new_book():
    project.library = []
    project.add_new_book("Test Book", "Test Author", "2024")
    assert len(project.library) == 1
    assert project.library[0]['title'] == "Test Book"
    assert project.library[0]['author'] == "Test Author"
    assert project.library[0]['year'] == "2024"
    assert project.library[0]['status'] == "available"

def test_return_book():
    project.library = []
    project.add_new_book("Test Book", "Test Author", "2024")

    project.library[0]['status'] = "borrowed"

    with patch('builtins.input', return_value="Test Book"):
        project.return_book()

    assert project.library[0]['status'] == "available"

def test_borrow_book():
    project.library = []
    project.add_new_book("Test Book", "Test Author", "2024")

    with patch('builtins.input', return_value="Test Book"):
        project.borrow_book()

    assert project.library[0]['status'] == "borrowed"
