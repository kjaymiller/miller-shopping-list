from render_engine import Site, Page, Collection, Blog


site = Site()
site.SITE_TITLE = 'The Miller Wishlist'

@site.register_route
class Index(Page):
    template = "index.html" # page.html is the default template but you can make a custom template
    slug = "index"


@site.register_collection
class Pages(Collection):
    routes = [""] # routes will appear at '/page' and '/pages/page'
    content_path = "content" # collections must have their paths assigned
    template = "page.html"


site.render(strict=True) # build out the tools
