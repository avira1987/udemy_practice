import justpy as jp
from webapp import layout
from webapp import page 
class Home(page.Page):
    path= "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay =layout.DefaultLayout(a=wp)
        
        container = jp.QPageContainer(a=lay)
        
        div = jp.Div(a= container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="this is the Home page", classes ="text-4xl m-2 ")
        jp.Div(a=div, text=""" 
        Shoppers are also interested in a company’s mission. They’ll use the 
        About Us page to determine if they share core values with the business 
        and to decide if they want to shop with the business or not. 
        """, classes ="text-lg ")
        
        return wp
