from typing import Optional

from leiaapi.generated import ApiClient, ApplicationApi, Application, LoginToken

import logging
logger = logging.getLogger(__name__)


class SessionManager:

    DEFAULT_SESSION: 'SessionManager' = None

    def __init__(self, api_key: str, client: Optional[ApiClient] = ApiClient()):
        super().__init__()
        self.api_key: str = api_key
        self.client: Optional[ApiClient] = client
        self.token: Optional[str] = None
        self.application_api: ApplicationApi = ApplicationApi(api_client=self.client)
        self.application: Optional[Application] = None

    def set_as_default(self):
        SessionManager.DEFAULT_SESSION = self
        return self

    def login(self):
        login: LoginToken = self.application_api.login_application(self.api_key)
        self.application = login.application
        self.token = login.token
        return self

    def renew(self):
        return self.login()

    def logout(self):
        self.application_api.logout_application(self.token)
        return self


SessionManager(None, "").set_as_default()
