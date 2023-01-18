import justpy as jp

class About:
    path = "/about"
    
    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a= wp, classes="bg-gray-200 h-screen ")
        jp.Div(a=div, text="this about page", classes ="text-4xl m-2 ")
        jp.Div(a=div, text=""" 
        An 'About Us' page is a spot for your founding story, a place to 
        show off your business wins, and a sales page that answers the 
        most pressing question new customers have about your business.
        """, classes ="text-lg ")
        return wp


jp.Route(About.path, About.serve)
jp.justpy(port=8001)
