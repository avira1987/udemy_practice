import justpy as jp
from webapp import layout
from webapp import page

class About(page.Page):
    path = "/about"
    
    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a= container, classes="bg-gray-200 h-screen ")
        jp.Div(a=div, text="this about page", classes ="text-4xl m-2 ")
        jp.Div(a=div, text=""" 
        An 'About Us' page is a spot for your founding story, a place to 
        show off your business wins, and a sales page that answers the 
        most pressing question new customers have about your business.
        """, classes ="text-lg ")
        return wp


