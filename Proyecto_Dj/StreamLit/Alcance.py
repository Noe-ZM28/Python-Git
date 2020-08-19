import streamlit  as st
import math
import pandas as pd
import json

def cargaConfig():
    configuration = None
    try:
        with open("./Config/config.json", "r") as f:
            configuration = json.loads(f.read())
            return configuration
    except  Exception as e:
        print(e)

configuration = cargaConfig()
#st.title("Alcance de Twitter --» Facebook")
st.markdown("<h1 style='text-align: center; color: blue;'>Alcance de Twitter --» Facebook</h1>", unsafe_allow_html=True)
Tema=st.text_input('Dar un tema')
Imp=st.number_input('Da un número de impresiones',min_value=1)
NMsn=st.number_input('Da un número de publicaciones', min_value=1)
NUser=st.number_input('Da un número de usuarios', min_value=1)


#####################Constantes###############################################
Total=7.4e6 #Usuarios de Twitter en México
Total2=90.0e6#Usuarios de Facebook en México
Total3= 3.4e8#Usuarios totales de Twitter en el Mundo
Total4= 2.4e9#Usuarios totales de Facebook en el Mundo 
####################Funciones#################################################
def Impresiones(x,y,z):
    if y<=z:
        return x+z
    else:
        return math.nan, st.write('El número de Publicaciones debe ser mayor al de Usuarios')   
    
def Factor(x):
    if x<1:
        st.write("Las Impresiones deben ser un entero positivo")
    elif 1<=x and x<1000:
        return 1/(1+math.log10(x))
    elif 1000<=x and x<1e4:
        return 1/((1+math.log10(x/1e3))*(1+math.log10(x)))
    elif 1e4<=x and x<1e6:
        return 1/(2*(1+math.log10(x)))
    elif 1e6<=x and x<1e7:
        return 1/((2+math.log10(x/1e6))*(1+math.log10(x)))
    elif 1e7<=x and x<1e8:
        return 1/((3+5*math.log10(x/1e7))*(1+math.log10(x)))
    elif 1e8<=x and x<1e9:
        return 1/((8+15*math.log10(x/1e8))*(1+math.log10(x)))
    elif 1e9<=x and x<1e10:
        return 1/((23+53*math.log10(x/1e9))*(1+math.log10(x)))
    elif 1e10<=x and x<1e11:
        return 1/((76+258*math.log10(x/1e10))*(1+math.log10(x)))
    elif 1e11<=x and x<1e12:
        return 1/((334+767*math.log10(x/1e11))*(1+math.log10(x)))
    elif 1e12<=x and x<1e13:
        return 1/((1101+4390*math.log10(x/1e12))*(1+math.log10(x)))
    elif 1e13<=x and x<1e14:
        return 1/((5491+14100*math.log10(x/1e13))*(1+math.log10(x)))
    else:
        return 3.4e-6
    
def Alc(x):
    return x*Factor(x)
  

def Nivel(x):
    if x<=7.4e6:
        st.write("El Alcance de ", Tema, " es Nacional")
    else:
        st.write("El Alcance de ", Tema, " es Internacional")
    return
    
def AlcF(x):
    if  x<=0.1*Total:
        return 0.7*Total2*(math.exp((100*x/Total-50)/10)-math.exp(-4.999998649)) 
    elif  0.1*Total<x and x<=0.4*Total:
        return 0.7*Total2*(math.exp((100*(x/Total)-50)/10)) 
    elif 0.4*Total<x and x<=Total:
        return Total2*(0.3*math.exp((100*x/Total-100)/10))+0.7*Total2 
    elif Total<x and x<0.4*Total3:
        return 0.3*Total4*(1-math.exp((-100*(x-Total)/Total3)/10))+Total2 
    elif 0.4*Total3<=x and x<Total3:
        return Total4*(1-0.60*math.exp((40-100*x/Total3)/10)+0.60*math.exp((-60)/10))
    else:
        st.write("Se ha superado el número de usuarios en el Mundo",2.4e9)

def PubF(x,y,z,u):
    if  z/u<=3:
        return (z/u)*UserF(x,u,z)
    else:
        return (z/(2*u))*UserF(x,u,z)
    
        
def UserF(x,y,z):
    if  x<=0.4*Total2:
        return x*(math.exp(-3.5-(z/y)/10))+y 
    elif 0.4*Total2<x and x<=Total2:
        return x*(math.exp(-3.5-(z/y)/10))+y
    elif Total2<x and x<0.4*Total4:
        return x*(math.exp((-4.-(z/y)/10)))+y 
    elif 0.4*Total4<=x and x<Total4:
        return x*(math.exp((-4.5-(z/y)/10)))+y 
    else:
        st.write("Se ha superado el número de usuarios en el Mundo",2.4e9)
        
        
def AlcTotal(x):
    if AlcF(x)<=x:
        return  0.5*x+AlcF(x) 
    elif  x<AlcF(x) and x<=0.95*Total:
        return  AlcF(x)+(1-(x/Total))*x 
    else:
        return AlcF(x)+0.05*x 
    
def UyPTotal(x,y,z):
   if AlcF(x)<=x:
       return  0.5*y+z 
   elif  x<AlcF(x) and x<=0.95*Total:
       return  z+(1-(x/Total))*y 
   else:
       return z+0.05*y 
          
################Boton de Activación################## 
if st.button("Calcular"):
    ImpEf=Impresiones(Imp,NUser,NMsn)
    a1=Alc(ImpEf)   
    a2=AlcF(a1)    
    a3=AlcTotal(a1)
    a4=PubF(a2,a1,NMsn,NUser)
    a5=UserF(a2,NUser,NMsn)
    a6=UyPTotal(a1,NUser,a5)
    a7=UyPTotal(a1,NMsn,a4)
    Nivel(a1)
    df=pd.DataFrame(data= {Tema:["Publicaciones","Usuarios","Alcance"],'Twitter':["{:6,}".format(round(NMsn)),"{:6,}".format(round(NUser)),"{:6,}".format(round(a1))], 'Facebook':["{:6,}".format(round(a4)),"{:6,}".format(round(a5)),"{:6,}".format(round(a2))],'Totales':["{:6,}".format(round(a7)),"{:6,}".format(round(a6)),"{:6,}".format(round(a3))]}) 
    df.set_index(Tema, inplace=True)
    st.table(df)
else:
    st.write('**Presionar el botón Calcular**') 
#########Calificar y guardar información################################
ruta=configuration['alcance'][0]['path']
#ruta='/home/ernesto/Documentos/python/Log/datos.json'
Calf=st.number_input('Da una calificación de estos resultados del 1 al 10', min_value=1,max_value=10) 
if st.button("Calificar"):
    ImpEf=Impresiones(Imp,NUser,NMsn)
    a1=Alc(ImpEf)   
    a2=AlcF(a1)    
    a3=AlcTotal(a1)
    a4=PubF(a2,a1,NMsn,NUser)
    a5=UserF(a2,NUser,NMsn)
    a6=UyPTotal(a1,NUser,a5)
    a7=UyPTotal(a1,NMsn,a4)
    f=open(ruta,"a")
    df=pd.DataFrame(data= {Tema:["Publicaciones","Usuarios","Alcance"],'Twitter':[round(NMsn),round(NUser),round(a1)], 'Facebook':[round(a4),round(a5),round(a2)],'Totales':[round(a7),round(a6),round(a3)]}) 
    df.set_index(Tema, inplace=True)
    f.write("%s\n" % df  )
    f.write("Calificacion\t" "%s\n" % Calf)
    st.markdown("<h4 style='text-align: center; color: green;'>Gracias, Se ha calificado</h4>", unsafe_allow_html=True)
    f.close()
else:
    st.markdown("<h4 style='text-align: center; color: red;'>No olvides dar una calificación</h4>", unsafe_allow_html=True)

