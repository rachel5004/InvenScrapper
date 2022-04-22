class NewsData:
    def __init__(self) -> None:
        self.link = ""
        self.date = ""
        self.title = ""
        self.writer = ""
        self.content = ""

    def __init__(self, dict):
        self.link = dict["link"]
        self.date = dict["date"]
        self.title = dict["title"]
        self.writer = dict["writer"]
        self.content = dict["content"]

    def print_data(self):
        print(self.title)