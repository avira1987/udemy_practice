import justpy as jp
from definition import Definition
import requests
from webapp import layout
from webapp import page

class Dictionary(page.Page):
    path= "/dictionary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a= container, classes="bg-gray-100 h-screen ")
        jp.Div(a=div, text="Instant English Dictionary", classes ="text-4xl m-2 ")
        jp.Div(a=div, text="Get the definition of any English word as you type.",
                classes = "text-lg")
        input_div = jp.Div(a=div, classes ="grid grid-cols-2")
        output_div = jp.Div(a=div, classes ="m-2 p-2 text-lg border-2 h-40 ")

        input_box =jp.Input(a=input_div , placeholder = "type in a word here.",
                outputdiv = output_div,
                classes ="m-2 bg-gray-100 border-2 border-gray-200 "
                    "rounded w-64 focus:bg-white focus:outline-none "
                    "focus:border-purple-500 py-2 px-4")
        input_box.on('input', cls.get_definition)

        # jp.Button(a=input_div, click=cls.get_definition , text="Get Definition", 
        #         outputdiv=output_div ,classes = "border-2 text-gray-500",
        #         inputbox= input_box)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        defined = Definition(widget.value).get()
        widget.outputdiv.text = " ".join(defined)
#vaghti bekhaim az tarigh api mani kalamaro peyda konim    
    # @staticmethod
    # def get_definition(widget, msg):
    #     req = requests.get(f"http://127.0.0.1:8000/api?w={widget.value}")
    #     data = req.json()
    #     widget.outputdiv.text = " ".join(data['definition'])