import feedparser, redis
from flask import Flask, render_template
from flask_caching import Cache

config = {
    "DEBUG": False,          # some Flask specific configs
    "CACHE_TYPE": "redis", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

@app.route("/")
@cache.cached(timeout=50)
def home():
    return render_template("home.html")

@app.route("/funny")
@cache.cached(timeout=50)
def funny():
    funnyurl = "https://9gag-rss.com/api/rss/get?code=9GAGFunny&format=2"
    funnyfeed = feedparser.parse(funnyurl)
    funnyname = funnyfeed.feed.title
    funnytitles = []
    funnylinks = []
    for item in funnyfeed.entries:
        funnytitles.append(item.title)
        funnylinks.append(item.link)
    return render_template("9gagfunny.html", funnyname=funnyname, funnytitles=funnytitles, funnylinks=funnylinks, len=len(funnyfeed.entries))

@app.route("/awesome")
@cache.cached(timeout=50)
def awesome():
    awesomeurl = "https://9gag-rss.com/api/rss/get?code=9GAGAwesome&format=2"
    awesomefeed = feedparser.parse(awesomeurl)
    awesomename = awesomefeed.feed.title
    awesometitles = []
    awesomelinks = []
    for item in awesomefeed.entries:
        awesometitles.append(item.title)
        awesomelinks.append(item.link)
    return render_template("9gagawesome.html", awesomename=awesomename, awesometitles=awesometitles, awesomelinks=awesomelinks, len=len(awesomefeed.entries))

@app.route("/comic")
@cache.cached(timeout=50)
def comic():
    comicurl = "https://9gag-rss.com/api/rss/get?code=9GAGComic&format=2"
    comicfeed = feedparser.parse(comicurl)
    comicname = comicfeed.feed.title
    comictitles = []
    comiclinks = []
    for item in comicfeed.entries:
        comictitles.append(item.title)
        comiclinks.append(item.link)
    return render_template("9gagcomic.html", comicname=comicname, comictitles=comictitles, comiclinks=comiclinks, len=len(comicfeed.entries))

@app.route("/fresh")
@cache.cached(timeout=50)
def fresh():
    freshurl = "https://9gag-rss.com/api/rss/get?code=9GAGFresh&format=2"
    freshfeed = feedparser.parse(freshurl)
    freshname = freshfeed.feed.title
    freshtitles = []
    freshlinks = []
    for item in freshfeed.entries:
        freshtitles.append(item.title)
        freshlinks.append(item.link)
    return render_template("9gagfresh.html", freshname=freshname, freshtitles=freshtitles, freshlinks=freshlinks, len=len(freshfeed.entries))

if __name__ == '__main__':
    app.run(debug=False)
