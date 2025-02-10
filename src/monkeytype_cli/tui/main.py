from textual.app import App, ComposeResult
from textual.widgets import Label

class Page(App):
    def compose(self) -> ComposeResult:
        yield Label("Monkeytype CLI is under development...")
        yield Label("Press `CTRL + q` to exit")

page = Page()