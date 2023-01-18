import justpy as jp

@jp.SetRoute("/home")
def home():
    wp = jp.WebPage()
    jp.Div(a=wp, text = 'Hello2 world', 
           classes ='text-red-900 bg-gray-500 '
                        'font-serif	text-lg	',)
    jp.Div(a= wp, text= 'hello3 again')
    return wp

@jp.SetRoute("/about")
def about():
    wp = jp.WebPage()
    jp.Div(a=wp, text = 'Hello1 world')
    jp.Div(a= wp, text= 'hello 1again')
    return wp


# jp.Route("/home",home)

jp.justpy()