import time
import openai #IMPORTAMOS LA LIBRERIA DE OPEN AI
              #INSTALAR LA LIBRERIA MEDIANTE TERMINAL(PIP INSTALL OPENAI)

#INSERTAMOS LA CLAVE DE ACCESO PARA EL USO DEL API KEY
key = "CLAVE DE ACCESO"
openai.api_key = key

#GUARDAMOS LAS PREGUNTAS, RESPUESTAS Y MENSAJES EN UNA LISTA
question = list()
answer_gpt = list()
message = list()

#CREAMOS EL CONTEXTO DE LAS PREGUNTAS
context = input("Sistema: Escribte un contexto: ")
#SI EL CONTEXTO NO ES AGREGADO LAS RESPUESTAS SERAN MAS CONCISAS
if context == "":
    context = "responde lo mas conciso posible"

message.append({'role': 'system', 'content':context})

#INICIAMOS EL CHAT
while True:
    question_update = input("Yo: ")
    #PARA SALIR DEL CHAT ESCRIBIMOS LAS PALABRAS GUARDADAS EN LA LISTA PARA ROMPER EL CICLO
    if question_update.lower() in ['exit', 'quit', 'salir', 'finalizar','terminar']:
        print("Chatbot: Fue un palcer ayudarte")
        time.sleep(3)
        break
    #SI NO ESCRIBIMOS NADA EL CHAT SIMPLEMENTE CONTINUARA SIN CERRAR EL CICLO
    if question_update == "":
        continue
    
    #DEFINIMOS EL MODELO DE RESPUESTA DEL CHAT
    message.append({'role': 'system', 'content':question_update})
    answers = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= message,
        temperature= 0,
        max_tokens = 500
    )
    #MOSTRAMOS LA RESPUESTA DADA POR EL MODELO QUE DEFINIMOS
    answer_update = answers.choices[0]['message']['content']
    print(f'\nchatbot: {answer_update}')