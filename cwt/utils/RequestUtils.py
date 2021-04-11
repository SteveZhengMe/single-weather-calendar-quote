import random
import urllib.request

def get_html_content(url, _as="string"):
    headers = [
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
    ]
    user_agent = random.choice(headers)

    request = urllib.request.Request(url)

    request.add_header('User-Agent', user_agent)
    request.add_header('UserMapper-Agent', user_agent)

    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            if _as.lower() == "list":
                response_line = []
                for line in response:
                    response_line.append(line.rstrip())
                return response_line
            else:
                return response.read()
    except:
        return None
