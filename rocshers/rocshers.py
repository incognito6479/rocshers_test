import http.client
import datetime
from urllib.parse import urlparse

# 9 commonly used HTTP Methods
HTTP_METHODS = ['POST', 'GET', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'TRACE', 'CONNECT', 'OPTIONS']
ERRORS = []
ANSWERS = {}


def url_validator(x):
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc])
    except:
        return False


def url_sort(file_path):
    valid_urls = []
    counter = 0
    with open(file_path) as urls:
        for url in urls:
            counter += 1
            url = url.strip()
            if url_validator(url):
                if url.startswith('https'):
                    url = url[8:]
                else:
                    url = url[7:]
                valid_urls.append(url)
            else:
                ERRORS.append(counter)
    return valid_urls


def find_url_available_methods():
    start_time = datetime.datetime.now()
    valid_urls = url_sort("rocshers/urls.txt")
    for url in valid_urls:
        connection = http.client.HTTPConnection(url)
        for method in HTTP_METHODS:
            connection.request(method, '/')
            resp = connection.getresponse()
            if resp.status != 405:
                if url in ANSWERS:
                    ANSWERS[url][method] = resp.status
                else:
                    ANSWERS[url] = {method: resp.status}
            connection.close()
    print(f"\n{ANSWERS}")
    if ERRORS:
        print("\nErrors: ")
        for i in ERRORS:
            print(f"    Line {i} is not a valid url")
    print(f"\nПотраченное время: {datetime.datetime.now() - start_time}")
    return ANSWERS


if __name__ == '__main__':
    find_url_available_methods()
