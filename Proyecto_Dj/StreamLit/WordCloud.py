############################################################################################
# Paqueterías
############################################################################################
import numpy as np
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import nltk
from IPython.display import display
import streamlit as st
from nltk.corpus import stopwords
from PIL import Image
import collections
import base64
from pathlib import Path
import re
import json
#nltk.download('wordnet')
###########################################################################################################################
# Formato en Letex para encabezado del app
###########################################################################################################################
st.latex(r'''{\Huge{\textbf{WordCloud}}\space}_{v0.X}''')
st.latex(r'''\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space
\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space
\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space
\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space
\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space
\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space
\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space
{by}^{\large{\space\mathbf{\mu\epsilon\tau\rho\iota\mathfrak{c}\zeta}}}''')
###########################################################################################
# Funciones-Herramientas
###########################################################################################
# Formato sidebar imagen

def GetFileJson(path,name,encode :str ="utf8"):
    configuration = None
    try:
        with open("./"+path+"/"+name+".json", "r", encoding=encode) as f:
            configuration = json.loads(f.read())
            return configuration
    except  Exception as e:
        print(e)

configuration = GetFileJson("Config","config")
# print(configuration)
if configuration['wordcloud'][0]['location_produccion']:
    st.set_option('deprecation.showfileUploaderEncoding', False)

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
# Lectura de archivo
def lectura():
    st.sidebar.title("Menú principal")
    try:
        # Las columnas leidas no son todas las columnas existentes en el csv original
        a = st.sidebar.file_uploader("Busca tu archivo csv",encoding="ISO-8859-1",type="csv",key="box1")
        b = pd.read_csv(a, usecols=["Hit Sentence","Date","Reach","Influencer","Sentiment"],encoding="utf-8", sep=",")
        if b is not None:    
            return b
    except:
        pass
# Paleta de colores disponibles al WordCloud
def coloreando(self):
    paleta = []
    if self == "WordCloud letras color Xpectus":
        paleta = [0,47,1]
    if self == "WordCloud letras color blanco":
        paleta = [255,255,255]
    elif self == "WordCloud letras color Positivo":
        paleta = [52,140,131]
    elif self == "WordCloud letras color Negativo":
        paleta = [140,20,26]
    return paleta
# Opciones de formas para WordCloud
def formando(self):
    topologia = []
    if self == "Rectangular(tradiconal)":
        topologia = None
    elif self == "Circular":
        topologia = np.array(Image.open(r"circulo.jpg"))
    elif self == "Nube":
        topologia = np.array(Image.open(r"nube1.jpg"))
    elif self == "Nube de habla":
        topologia = np.array(Image.open(r"nube2.png"))
    elif self == "Twitter":
        topologia = np.array(Image.open(r"twitter.png"))
    return topologia
# Resta de listas
def resta_listas(a,b):
    for o in range(len(b)):
        for i in range(len(a)):
            try:
                if a[i]==b[o]:
                    a.remove(b[o])
                else:
                    pass
            except:
                pass
    return a
# Creación y grafico WordCloud
def comun_wordcloud(self1,self2,self3,self4):
    stoppalabras = stopwords.words("spanish")
    stoppalabrass = stopwords.words("english")
    lista = convertidor_columna_a_lista(self4)
    inicios = [lista[l] for l in range(len(lista)) if lista[l].startswith(("//","http","?http","?","¿",".","(",")","rt","\\","/","¡","!","'",'"',";",":","-","_","*","+","[","]",">","<","%","$","="))]
    lista_base = GetFileJson("file","exeption")
    stoppalabras.extend(inicios)
    stoppalabras.extend(lista_base)
    stoppalabras.extend(stoppalabrass)
    lista = resta_listas(lista,stoppalabras)
    unique_string= (" ").join(lista)
    unique_string = unique_string.lower()
    wordcloud = WordCloud(font_path=('Roboto-Medium.ttf'),width=1024,height=768,background_color=None,mask=self1,mode="RGBA",
        stopwords=stoppalabras,max_words=self2,collocations=False,color_func=lambda *args,**kwargs:(self3[0],self3[1],
            self3[2])).generate(unique_string)
    plt.figure(facecolor="None")
    plt.imshow(wordcloud)
    plt.axis("off")
    st.pyplot() #Linea necesaria para tener plot en Streamlit
    st.title("Contador por Palabra")
    lista2 = WordCloud(stopwords=stoppalabras,collocations=False).process_text(unique_string)
    data = contar(lista2,p)
    st.dataframe(data)
    fig, ax = plt.subplots(figsize=(15,8))
    data.sort_values(by="Repeticiones").plot.barh(x="Palabras",y="Repeticiones",ax=ax)
    ax.set_title("Principales palabras y sus repeticiones")
    plt.show()
    st.pyplot()
# WordCloud simple
def simple_wordcloud(self1,self2,self3,self4):
    lista = convertidor_string_a_lista(self4)
    stoppalabras = stopwords.words("spanish")
    stoppalabras = stopwords.words("english")
    inicios = [lista[l] for l in range(len(lista))  if lista[l].startswith(("//","http","?http","?","¿",".","(",")","rt","\\","/","¡","!","'",'"',";",":","-","_","*","+","[","]",">","<","%","$","="))]
    lista_base = GetFileJson("file","exeption1")
    stoppalabras.extend(inicios)
    stoppalabras.extend(lista_base)
    lista = resta_listas(lista,stoppalabras)
    unique_string= (" ").join(lista)
    unique_string = unique_string.lower()
    wordcloud = WordCloud(font_path=('Roboto-Medium.ttf'),width=1024,height=768,background_color=None,mask=self1,mode="RGBA",
                            stopwords=stoppalabras,max_words=self2,collocations=False,color_func=lambda *args,**kwargs:(self3[0],self3[1],
                            self3[2])).generate(unique_string)
    plt.figure(facecolor="None")
    plt.imshow(wordcloud)
    plt.axis("off")
    st.pyplot() #Linea necesaria para tener plot en Streamlit
def quitar_urls(txt):
    return "  ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)","",txt).split())
def stop_words(s,n):
    #Quitará las palabras más repetidas
    from collections import Counter
    l = cuerpo_texto(s)
    l = [x for x in Counter(l).most_common(n)]
    return l
# Cuerpo de texto por lista de frases
def cuerpo_texto(dataframe):
    l = []
    s = dataframe.iloc[0]
    s.map(lambda x: l.extend(x))
    #Regresa una lista del texto
    return l 
# Lista a texto
def convertidor_lista_a_string(list):
    return (" ").join(list)
# Conteo de palabras
def contar(self,numero):
    cuentas = collections.Counter(self)
    return pd.DataFrame(cuentas.most_common(numero),columns=["Palabras","Repeticiones"])
# Columna de DataFrame a lista
def convertidor_columna_a_lista(df):
    """
    Recibe una columna del DataFrame y convierte cada entrada
    en una sola lista
    """
    lista_final = []
    for i in range(len(df["Hit Sentence"])):
        lista_parcial = df["Hit Sentence"][i].split()
        lista_final.extend(lista_parcial)
    return lista_final
#Convertidor de string a lista
def convertidor_string_a_lista(string):
    li = list(string.split(" ")) 
    return li 
# Agrupacion para WordClouds-Sentimientos
def agrupacion_y_plot(self):
    df_sent = self[["Hit Sentence","Sentiment"]]
    for i in range(len(df_sent)):
        if df_sent["Sentiment"][i] == "Neutral":
            neutrales = ("").join(str(df_sent["Hit Sentence"][i]))
        elif df_sent["Sentiment"][i] == "Positive":
            positivos = ("").join(str(df_sent["Hit Sentence"][i]))
        elif df_sent["Sentiment"][i] == "Negative":
            negativos = ("").join(str(df_sent["Hit Sentence"][i]))
        else:
            pass
    if neutrales is not None:
        formass =formando(forma)
        coloress = [255,255,8]
        pp = int(p+30)
        st.write("**WordCloud Neutral**")
        simple_wordcloud(formass,pp,coloress,neutrales)
    else:
        st.write("**No hay tweets neutrales**")
    if positivos is not None:
        formass =formando(forma)
        coloress = [22,247,5]
        pp = int(p+30)
        st.write("**WordCloud Positivo**")
        simple_wordcloud(formass,pp,coloress,positivos)
    else:
        st.write("**No hay tweets positivos**")
    if negativos is not None:
        formass =formando(forma)
        coloress = [247,5,5]
        pp = int(p+30)
        st.write("**WordCloud Negativo**")
        simple_wordcloud(formass,pp,coloress,negativos)
    else:
        st.write("**No hay tweets negativos**")
    return 
# Formato sobre Streamlit
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        st.sidebar.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("styles3.css")
# Montando la imagen-sidebar
header_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
                img_to_bytes("metrics.png"))
st.sidebar.markdown(header_html, unsafe_allow_html=True)
##############################################################################################################
# Inicio de programa
##############################################################################################################
df1 = lectura()
df = df1
p = int(st.sidebar.number_input("¿Cúantas palabras significativas extras deseas?",min_value=0, max_value=2000,value=0,key="box2"))    # Llamado de WordCloud y dentro está el conteo de palabras
color = st.sidebar.selectbox("Seleciona tu tipo de WordCloud", ["WordCloud letras color blanco","WordCloud letras color Xpectus","WordCloud letras color Positivo","WordCloud letras color Negativo"], key="box5")
forma = st.sidebar.selectbox("Seleciona la forma de tu WordCloud", ["Rectangular(tradiconal)","Circular","Nube","Nube de habla","Twitter"], key="box6")
st.sidebar.title("Acerca de")
st.sidebar.info("Este es un proyecto del Laboratorio de Ciencia de Datos... " 
                "comentarios, preguntas y demás retroalimentaciones, comunicarse con: "
                "[Diego Trejo](https://t.me/Piocolo)")
try:
    if st.button("Procesa wordcloud"):
        formas =formando(forma)
        colores = coloreando(color)
        p = int(p+30)
        comun_wordcloud(formas,p,colores,df)
    else:
        pass
except Exception as e :
    st.write("**Antes de procesar, carga tu archivo 1**"+e)
try:
    if st.button("Procesa series de tiempo"):
        # Construcción de series de tiempo
        # Columna nueva para conteo de palabras
        df1["numero_palabras"] = 0
        for i in range(len(df1["Hit Sentence"])):
            df1["numero_palabras"][i] = len(df1["Hit Sentence"][i].split(" "))
        # Creación de columnas hora, fecha y minutos
        df1["hora"] = pd.DatetimeIndex(df1["Date"]).hour
        df1["fecha"] = pd.DatetimeIndex(df1["Date"]).month
        df1["minutos"] = pd.DatetimeIndex(df1["Date"]).minute
        # Haciendo sumas de horas, minutos, longitud de texto, etc...
        hora_tweets = df1.groupby(["hora"])["Reach"].sum()
        minutos_tweets = df1.groupby(["minutos"])["Reach"].sum()
        fecha_tweets = df1.groupby(["fecha"])["Reach"].sum()
        df1["longitud_texto"] = df1["Hit Sentence"].str.len()
        prom_texto_hora = df1.groupby(["hora"])["longitud_texto"].mean()
        prom_palabras_hora = df1.groupby(["hora"])["numero_palabras"].mean()
        #####################################################################################################
        # Plot de series de tiempo
        #####################################################################################################
        # Plot serie de tiempo por fecha
        st.title("Series de Tiempo")
        fecha_tweets.transpose().plot(kind="line",figsize=(15,4))
        plt.title("Número tentativo de retweets por mes", bbox={"facecolor":"0.8","pad":0})
        plt.grid(True)
        st.pyplot()
        # Plot serie de tiempo por hora
        hora_tweets.transpose().plot(kind="line",figsize=(15,4))
        plt.title("Número de tentativo de retweets por hora", bbox={"facecolor":"0.8","pad":0})
        plt.grid(True)
        st.pyplot()
        # Plot serie de tiempo por minuto
        minutos_tweets.transpose().plot(kind="line",figsize=(15,4))
        plt.title("Número tentativo de retweets por minuto", bbox={"facecolor":"0.8","pad":0})
        plt.grid(True)
        st.pyplot()
        # Plot serie de tiempo por horas promedio en longitud de texto
        prom_texto_hora.transpose().plot(kind="line",figsize=(15,4))
        plt.title("Longitud promedio en Tweets por hora", bbox={"facecolor":"0.8","pad":0})
        plt.grid(True)
        st.pyplot()
        # Plot serie de tiempo por hora promedio de número de palabras
        prom_palabras_hora.transpose().plot(kind="line",figsize=(15,4))
        plt.title("Palabras promedio por cada hora", bbox={"facecolor":"0.8","pad":0})
        plt.grid(True)
        st.pyplot()
        # Fuente de los tweets
        df1["fuente"] = ""
        # Filtrado de los usuarios fuente
        for i in range(len(df1["Influencer"])):
            m = re.search("(?<=>)(.*)",df1["Influencer"][i])
            try:
                df1["fuente"][i] = m.group(0)
            except AttributeError:
                df1["fuente"][i] = df1["Influencer"][i]
        # Ver qué hace el relpace
        df1["fuente"] = df1["fuente"].str.replace("</a>"," ",case=False)
        # Agrupando por usuario y alcance, para sumar
        tweets_por_fuente = df1.head(30).groupby(["fuente"])["Reach"].sum()
        # Plot de usuarios y alcance
        tweets_por_fuente.transpose().plot(kind="bar",figsize=(10,12))
        plt.title("Alcance por usuario/fuente",bbox={"facecolor":"0.8","pad":0})
        st.pyplot()
    else:
        pass
except Exception as e :
    st.write("**Antes de procesar, carga tu archivo**"+e)
try: 
    if st.button("Procesa tweets por sentimientos"):
        # Usando segregación de sentiminetos de origen(los raw en el archivo original)
        #st.write(len(df1["Sentiment"]),df1["Sentiment"][1],type(df1["Sentiment"][1]))
        pos = 0
        neg = 0
        neu = 0
        for i in range(len(df1["Sentiment"])):
            if df1["Sentiment"][i] == "Positive":
                pos = pos + 1
            elif df1["Sentiment"][i] == "Neutral":
                neu = neu + 1
            elif df1["Sentiment"][i] == "Negative":
                neg = neg + 1
        df2 = pd.DataFrame({
            "Sentimiento": ["Positivo", "Neutral", "Negativo"],
            "Recurrencia": [pos, neu, neg]})
        df2.plot.barh("Sentimiento", "Recurrencia")
        st.pyplot()
    else:
        pass
except Exception as e :
    st.write("**Antes de procesar, carga tu archivo**"+e)
try:
    if st.button("Procesa wordclouds por grupo"):
        #########################################################################################
        # Agrupación de WordClouds
        #########################################################################################
        agrupacion_y_plot(df1)
    else:
        pass
except Exception as e :
    st.write("**Antes de procesar, carga tu archivo**"+e)