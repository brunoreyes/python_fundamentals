import webbrowser # By importing and using webbrowser.open we can open webpages through a computer's default browser

# webbrowser.open("http://www.python.org")

# help(webbrowser)  # opens up documentation of the imported module: webbrowser

# -t opens a new tab while -n opens a new browser

# for i in range(10):
#     print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep=';', end=' ')  #seperating with a '; instead of a default space
#     print()

# chrome = webbrowser.get('/usr/bin/google_chrome %s').open_new_tab("https://www.python.org/")

safari = webbrowser.get(using='safari')
safari.open("https://www.python.org/")