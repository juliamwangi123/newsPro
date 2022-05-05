class Headlines:
    '''
    News class to define headlines object
    '''

    def __init__(self,  title, description, content, url, url_to_image, published_at):
        self.title = title
        self.description = description
        self.url = url
        self.url_to_image = url_to_image
        self.published_at = published_at
        self.content=content


class Bbc:
    def __init__(self,  title, description, content, url, url_to_image, published_at):
        self.title = title
        self.description = description
        self.url = url
        self.url_to_image = url_to_image
        self.published_at = published_at
        self.content=content
