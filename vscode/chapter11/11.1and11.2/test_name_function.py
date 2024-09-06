from name_function import get_formatted_name


def test_first_last_name():
    """被测试的函数能正确处理像Janis Joplin这样的姓名吗？"""
    formatted_name = get_formatted_name('Janis', 'Joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_middle_last_name():
    """被测试的函数能正确处理像Michael Lee Johnson这样的姓名吗？"""
    formatted_name = get_formatted_name('Michael', 'Johnson', 'Lee')
    assert formatted_name == 'Michael Lee Johnson'
