try:
    import pyttsx3
    import speech_recognition as sr
    import pywhatkit
    import yfinance as yf
    import pyjokes
    import webbrowser
    import datetime
    import wikipedia
    
except ImportError as e:
    print(f"Error de importacion: {e}")
    
# Opciones de voz / idioma    
id1 = 'spanish-latin-am'
id2 = 'spanish'
id3 = "en-uk-north"

# escuchar nuestro microfono y devolver el audio como texto
def trasformar_audio_en_texto():
    
    #almacenar recognizer en variable
    r = sr.Recognizer()
    
    #configurar el microfono
    with sr.Microphone() as origen:
        
        #tiempo de espera
        r.pause_threshold = 0.8
        
        #informar que comenzo la grabacion 
        print("Ya puedes hablar")
        
        #guardar lo que escuche en el audio
        audio = r.listen(origen)
        
        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-CO")
            
            # prueba de que pudo ingresar
            print("Dijiste: " + pedido)
            
            #devolver a pedido
            return pedido
        
        #en caso de que no entienda el audio
        except sr.UnknownValueError:
            
            #prueba de que no crompendio el audio
            print("ups, no entendi")
            
            #devolver error
            return "Sigo esperando"
        
        #en caso de no resolver el pedido 
        except sr.RequestError:
            
            #prueba de que no crompendio el audio
            print("ups no hay servicio")
            
            #devolver error
            return "Sigo esperando"
        
        #error inesperado
        except:
            
            #prueba de que no crompendio el audio
            print("ups, algo salio mal")
            
            #devolver error
            return "Sigo esperando"
        
#funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    
    # encender el motor de pytts3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)
    
    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

#Informar el dia de la semana
def pedir_dia():
    
    #crear variable con datos actuales
    dia = datetime.date.today()
    print(dia)
    
    # Crear variable para el dia de la semana 
    dia_semana = dia.weekday()
    print(dia_semana)
    
    # diccionario con nombre de dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}
    
    # decir dia de la semana
    hablar(f"hoy es {calendario[dia_semana]}")

def pedir_hora():
    
    #pedir una variable con datos de la hora
    hora = datetime.datetime.now()
    print(hora)
    hora = f"En este momento son las {hora.hour} horas con {hora.minute} y {hora.second} segundos"
    
    hablar(hora)
    
# funcion saludo inicial
def saludo_inicial():
    
    #crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif hora.hour >= 6 and hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes' 
    
    #decir salido
    hablar(f'Hola, {momento}. Dime en que te puedo colaborar')
    
# funcion central del asistente
def pedir_cosas():

    # activar saludo inicial
    saludo_inicial()

    # variable de corte
    comenzar = True

    # loop central
    while comenzar:

        # activar el micro y guardar el pedido en un string
        pedido = trasformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo youTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir el navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente: ')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya ahora mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Ya mismo lo hago')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar("Perdón pero no la he encontrado")
                continue
        elif 'adiós' in pedido:
            hablar('Adios, que tengas un gran día')
            break
pedir_cosas()