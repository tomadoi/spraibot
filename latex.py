from urllib.parse import quote
from slackbot.bot import listen_to, respond_to
import json

@respond_to(r'\$.*\$')
def latex(message):
    # based on https://github.com/nicolewhite/SlackTeX/blob/master/slacktex/views.py
    latex_url = "http://chart.apis.google.com/chart?cht=tx&chl={latex}".format(
        latex=quote(latex))
    message.send_webapi('', json.dumps([{"image_url": latex_url,
        "fallback": "Latex rendering fail?"}]))
