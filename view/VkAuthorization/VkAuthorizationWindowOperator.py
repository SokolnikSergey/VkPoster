from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage

from PyQt5.QtCore import QUrl,QObject,pyqtSignal
import re
class VkAuthorizationWindowOperator(QObject):

    vk_auth_window_closed  = pyqtSignal()
    token_recieved = pyqtSignal(str)

    def __init__(self,view,app_id):
        super(VkAuthorizationWindowOperator, self).__init__()
        self.__view = view
        self.__app_id = app_id
        self.snapping_internal_signals()

    def snapping_internal_signals(self):
        self.__view.loadFinished.connect(self.get_token)
        self.__view.window_closed.connect(self.vk_auth_window_closed)



    def clear_page(self):
        self.__view.setPage(QWebPage(self))

    def setStartUrl(self):
        req = 'https://oauth.vk.com/authorize?client_id={app_id}&display=mobile&redirect_uri=http://vk.com&scope=groups,messages,wall,offline,photos,friends&response_type=code&v=5.60'.format(app_id = str(self.__app_id))
        self.__view.load(QUrl(req))

    def processPageHTML(self, html):
        if 'access_token' in html:
            access_token = re.search(r'"access_token":"(?P<token>\w+)?"', html).group('token')
            print("has token emited " + access_token)
            self.token_recieved.emit(str(access_token))

    def get_token(self):
        self.__view.page().toHtml(self.processPageHTML)

        current_url = self.__view.url().toString()
        if 'user_denied' in current_url: # the user has clicked 'cancel' during vk-authorization
            self.vk_auth_window_closed.emit()
        elif '#code=' in current_url:
            code = self.__view.url().toString()[self.__view.url().toString().index("code=") + 5:]
            req = 'https://oauth.vk.com/access_token?client_id={app_id}&client_secret=GqQfpAYszfmlLsG1Vvjb&redirect_uri=http://vk.com&code='.format(app_id = str(self.__app_id)) + str(code)
            self.__view.setUrl(QUrl(req))


    def show(self):
        self.__view.show()

    def hide(self):
        self.__view.hide()

