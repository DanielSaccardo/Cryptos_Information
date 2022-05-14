import os

try:
    import requests
except ImportError:
    print("\n\n")
    os.system("pip install requests")
    import requests
    print("\n\n")

try:
    from bs4 import BeautifulSoup as Bs
except ImportError:
    print("\n\n")
    os.system("pip install beautifulsoup4")
    try:
        from bs4 import BeautifulSoup as Bs
    except ImportError:
        from bs4 import BeautifulSoup as Bs
    print("\n\n")


def extract_page(url):
    """
    This function scraps the html of a web page

    :param url: URL of the site
    :type url: str

    :return: HTML
    """

    page = requests.get(url)  # Scrap HTML
    html = Bs(page.text, features="html.parser")  # Beautify HTML

    return html


def extract_json(api_url):
    """
    This function scraps the json of a API

    :param api_url: API URL of the JSON
    :type api_url: str

    :return: JSON
    """

    content = requests.get(api_url)

    return content.json()


def get_class_text(page, tag, class_name):
    """
    This function isolate the text into an HTML class

    :param page: HTML of the page
    :type page: bs4.BeautifulSoup

    :param tag: HTML tag that refers to the class
    :type tag: str

    :param class_name: Name of the class
    :type class_name: str

    :return: String contained on the selected class
    """

    html_class = page.findAll(tag, {"class": class_name})

    values = []
    for value in html_class:
        values.append(value.text)

    return values


def get_href_str(page, tag, class_name):
    """
    This funtion isolate the HTML href path

    :param page: HTML of the page
    :type page: bs4.BeautifulSoup

    :param tag: HTML tag referring to the class
    :type tag: str

    :param class_name: Class in which is contained the href
    :type class_name: str

    :return: Array of paths
    """

    all_paths = [i['href'] for i in page.findAll('a', href=True)]

    html_class = page.findAll(tag, {"class": class_name})

    paths = []
    for i in range(len(all_paths)):
        if all_paths[i] in str(html_class) and all_paths[i] not in paths:
            paths.append(all_paths[i])

    return paths
