# This program checks the presence of
# targeted string in web pages content
# whose URLs are inputted.
import requests


def url_check_function(string, web_page_url):
    """This function tests if target string exist in inputted URL's
    Web Page content.  This function needs 2 parameters:
        "string" - your target string;
        "web_page_url" - your Web Page's URL.
    """
    try:
        content = requests.get(web_page_url)  # Python requests.Response Object
    except Exception as e:
        print(f'Inputted URL " {web_page_url} " isn\'t match'
              f' any URL in the WEB.' + '\n' + str(e))
        return False
    detected: bool = string in content.text
    content.close()  # Closes the connection to the server.
    return detected


# This loop allows to check more then one target string.
check_target_string = 'Y'
while check_target_string == 'Y' or check_target_string == 'y':
    target_string = input('Please input your target string: ')
    print(f'Your target string is: {target_string}')

    # This loop tests inputted Web Pages for target string existence.
    yes_or_no = 'Y'
    while yes_or_no == 'Y' or yes_or_no == 'y':
        url = input('Please input URL you going to check: ')
        result = url_check_function(target_string, url)
        if result:
            print(f'The string "{target_string}" is there in this content')
        else:
            print(f'The string "{target_string}" isn\'t there in this content')
        yes_or_no = input('Would you like to check another URL (Y/N)? ')

    check_target_string = input(
        'Would you like to check another target string (Y/N)? ')

input('Push "Enter" to finish: ')
