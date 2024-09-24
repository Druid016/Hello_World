import webbrowser

# Specify the URL
url = 'https://www.youtube.com/watch?v=p3sHjReqPFE'

# Specify the path to Firefox (ensure this path is correct)
firefox_path = 'C:/Program Files/Mozilla Firefox/firefox.exe'

# Register Firefox browser
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))

# Open the URL using Firefox
webbrowser.get('firefox').open(url)
