from rocshers.rocshers import url_validator, find_url_available_methods, url_sort


# no idea how to test my own code

def test_url():
    assert url_validator("https://google.com")


def test_sort_url():
    assert url_sort("rocshers/urls.txt")


def test_main_func():
    assert find_url_available_methods
