import api
import documentations
import justpy as jp

jp.Route("/api", api.API.serve)
jp.Route("/",documentations.Doc.serve)
jp.justpy()
