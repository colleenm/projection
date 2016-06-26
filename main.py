import os

import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'content': 'hello world',
        }

        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))


class PlayerPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'player_name': self.request.get('name'),
        }
        
        template = JINJA_ENVIRONMENT.get_template('templates/player-page.html')
        self.response.write(template.render(template_values))


class ExchangePage(webapp2.RequestHandler):
    def get(self):
        template_values = {
        }

        template = JINJA_ENVIRONMENT.get_template('templates/exchange.html')
        self.response.write(template.render(template_values))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/exchange', ExchangePage),
    ('/player', PlayerPage),
], debug=True)
