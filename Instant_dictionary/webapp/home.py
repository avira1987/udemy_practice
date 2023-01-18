import justpy as jp

class Home:
    path= "/"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a= wp, classes="bg-gray-200 h-screen ")
        jp.Div(a=div, text="this is the Home page", classes ="text-4xl m-2 ")
        jp.Div(a=div, text=""" 
        Shoppers are also interested in a company’s mission. They’ll use the 
        About Us page to determine if they share core values with the business 
        and to decide if they want to shop with the business or not. 
        """, classes ="text-lg ")
        
        return wp

