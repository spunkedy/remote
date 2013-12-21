To install on your cent os 6 box you need:

python
easy_install flask
easy_install onkyo-eiscp
easy_install pyroku
easy_install requests

The init script that is included is just to have a quick way to set it up. There is nothing locked down for security, this means that it is highly insecure. Consider putting it into a separate container like apache wsgi and having a separate user run it.

