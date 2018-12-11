class News:
    def __init__(self, url, title, description, body, create_date='', short_body='', site=''):
        self._url = url
        self._title = title
        self._description = description
        self._body = body
        self._create_date = create_date
        self._short_body = short_body
        self._site = site

    def set_url(self, url):
        self._url = url

    def set_site(self, site):
        self._site = site

    def set_title(self, title):
        self._title = title

    def set_description(self, description):
        self._description = description

    def set_body(self, body):
        self._body = body

    def set_create_date(self, create_date):
        self._create_date = create_date

    def set_short_body(self, short_body):
        self._short_body = short_body

    def get_url(self):
        return self._url

    def get_title(self):
        return self._title

    def get_description(self):
        return self._description

    def get_body(self):
        return self._body

    def get_create_date(self):
        return self._create_date

    def get_short_body(self):
        return self._short_body

    def get_site(self):
        return self._site

    def update_site(self):
        pass

    def __str__(self) -> str:
        return '\n'.join([self._url, self._title, self._description,
                          self._body, self._short_body, self._create_date, self._site])
