class BrowserHistory:
    class link:
        def __init__(self,url):
            self.url=url
            self.next=None
            self.prev=None

    def __init__(self, homepage: str):
        self.curr=self.link(homepage) ### points to current link
        self.links=self.curr ### points to the head of the browser hisotry (LL)

    def visit(self, url: str) -> None:
        new_link=self.link(url)
        prev_link=self.curr ### when new link is visited current link becomes previous compared to the new curr so we are storing
        self.curr.next=new_link
        self.curr=self.curr.next
        self.curr.prev=prev_link

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.prev==None:
                break
            self.curr=self.curr.prev
        return self.curr.url

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.next==None:
                break
            self.curr=self.curr.next
        return self.curr.url

        
