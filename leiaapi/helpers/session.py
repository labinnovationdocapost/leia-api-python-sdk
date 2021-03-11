from typing import Optional

from leiaapi.generated import ApiClient, ApplicationApi

import logging
logger = logging.getLogger(__name__)


class SessionManager:

    DEFAULT_SESSION: 'SessionManager' = None

    def __init__(self, api_key: str, client: Optional[ApiClient] = ApiClient()):
        super().__init__()
        self.api_key = api_key
        self.client = client
        self.token = None
        self.application_api = ApplicationApi(api_client=self.client)

    def set_as_default(self):
        SessionManager.DEFAULT_SESSION = self
        return self

    def login(self):
        login = self.application_api.login_application(self.api_key)
        self.token = login.token
        return self

    def renew(self):
        return self.login()

    def logout(self):
        self.application_api.logout_application(self.token)
        return self


SessionManager(None, "").set_as_default()
