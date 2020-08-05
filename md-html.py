######################################################################
# TOOL FOR CONVERTING MARKDOWN (.md) FILES TO HTML for the website
#
# RUNNING:
# SINGLE FILE CONVERSION: python3 md-html.py foo.md html-folder
# ENTIRE FOLDER CONVERSION: python3 md-html.py md-folder html-folder
######################################################################

import markdown2
import sys
import os

md_path = sys.argv[1]
html_path = sys.argv[2]

def convert(md_path):
    md_file = open(md_path)
    md_content = md_file.read()
    md_file.close()
    html_file = open(html_path + '/' + md_path.split('/')[-1].split('.')[0] + '.html', 'w+')
    converted = markdown2.markdown(md_content, extras=["target-blank-links"])
    first_half = f"""
    <!DOCTYPE html>
    <html lang="en-us">
    <head>
        <title>{md_path.split('/')[-1].split('.')[0].replace('-', ' ')}</title>
        <link rel="icon" href="/content/images/favicon_io/favicon.ico" type="image/x-icon">
        <link rel="apple-touch-icon" href="/content/images/favicon_io/apple-touch-icon.png" type="image/png">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" 
        crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="../styles/style.css">
        <script src="https://code.jquery.com/jquery-3.5.1.js" integrity="sha256-QWo7LDvxbWT2tbbQ97B53yJnYU3WhH/C8ycbRAkjPDc=" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" 
        crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" 
        crossorigin="anonymous"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <script type="text/javascript" src="../scripts/script.js"></script>
    </head>
    <body>
        <div id="nav-placeholder"></div>
        <script>
            loadNav();
        </script>
        <div class = 'container' style="width: 600px; margin-top:40px;">
    """
    second_half = """
        </div>
    </body>
    <footer class="footer my-5 pt-5 text-muted text-center text-small" id="footer-placeholder"></footer>
    <script>
        loadFooter();
    </script>
    </html>
    """
    html = first_half + converted + second_half
    html_file.write(html)
    html_file.close()

if os.path.isfile(md_path):
    convert(md_path)
elif os.path.isdir(md_path):
    for md_file in os.listdir(md_path):
        convert(md_path + '/' + md_file)
else:
    print("Can't convert")