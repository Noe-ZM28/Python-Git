from django.http import HttpResponse
import datetime
#TExto
Saludo = """<HTML>
                <HEAD><TITLE> SAludo </TITLE></HEAD>
                <BODY>
                        <CENTER> Bienvenido:D </CENTER>
                </BODY>
            </HTML>"""

Despedida = """<HTML>
                <HEAD><TITLE> SAludo </TITLE></HEAD>
                <BODY>
                        <CENTER> Hasta la prixima :D </CENTER>
                </BODY>
            </HTML>"""



def bienvenida(request):#Primera vista
    return HttpResponse(Saludo)
def despedida(request):#despedida
    return HttpResponse(Despedida)
def fecha(request):
    fecha_actual = datetime.datetime.now()
    HorayFecha =  """<HTML>
                    <HEAD><TITLE> SAludo </TITLE></HEAD>
                    <BODY>
                            <CENTER> La fechay hora de ahora es:  %s </CENTER>
                    </BODY>
                </HTML>""" % fecha_actual
    return HttpResponse(HorayFecha)








