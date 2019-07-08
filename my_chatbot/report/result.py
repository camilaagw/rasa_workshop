import cherrypy
import os

cherrypy.config.update({'server.socket_host': '127.0.0.1',
                         'server.socket_port': 8088,
                        })

class SurveyResult(object):
    @cherrypy.expose
    def index(self, name=None, result=None):
        return open("result.html").read().format(name=name, result=result)
conf={'/result.css':
                    { 'tools.staticfile.on':True,
                      'tools.staticfile.filename': os.path.abspath("./result.css"),
                    }
      }
if __name__ == '__main__':
    cherrypy.quickstart(SurveyResult(), config=conf)