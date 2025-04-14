"""
Este script permite al usuario ingresar consultas desde la 
terminal, que luego son enviadas a la API de OpenAI
para obtener respuestas. Incluye manejo de historial de 
comandos con flechas (usando readline), validación de entrada,
y captura de errores comunes durante la interacción con la API.
"""

import os
import openai
from openai import OpenAI

try:
    # Habilitar historial con flecha arriba
    import readline

    LAST_INPUT = ""

    while True:
        try:
            # Nivel 1: Aceptación de consulta del usuario
            consulta = input("Escribí tu consulta para chatGPT (Enter para salir): ").strip()

            if consulta == "":
                print("Saliendo del programa.")
                break

            # Guardar en historial (habilita flecha ↑)
            readline.add_history(consulta)
            LAST_INPUT = consulta

            try:
                # Nivel 2: Tratamiento de la consulta
                if not consulta:
                    raise ValueError("No se ingresó ninguna consulta.")
                print(f"You: {consulta}")

                try:
                    # Nivel 3: Llamado a la API
                    client = OpenAI(api_key=os.getenv("sk-proj-hzBfDLz-wQE-1yjLZl7P-glq" \
                    "Wo2Tq975s3umkoBUIWUU85XtDfUe962aVgNbzssTqwaj-" \
                    "tyK6VT3BlbkFJ8jCpdlgypoqTqxPeoGgrO96SJ_ppFiLvH63" \
                    "jgRNnTvpQ8Y8pPg5iyryrrdrSPFVLklAViNJQsA"))

                    response = client.chat.completions.create(
                        model="gpt-4.0",  # gpt-4.1 puede no estar disponible públicamente aún
                        messages=[
                            {"role": "user", "content": consulta}
                        ]
                    )

                    print("chatGPT:", response.choices[0].message.content.strip())

                except openai.OpenAIError as e:
                    print("Error de OpenAI:", str(e))
                except Exception as e:
                    print("Error inesperado al invocar la API:", str(e))

            except ValueError as ve:
                print("Error en la consulta:", ve)
            except Exception as e:
                print("Error inesperado en el tratamiento de la consulta:", str(e))

        except (KeyboardInterrupt, EOFError):
            print("\nEntrada cancelada por el usuario.")
            break
        except Exception as e:
            print("Error inesperado al leer la entrada del usuario:", str(e))

except ImportError:
    print("No se pudo importar readline. En Windows, instalá pyreadline3 con:")
    print("   pip install pyreadline3")


    #lksadjalksdjlaskdjlsakjdalksdjlaksjdlkasjdl
    #asdkjashdjkashdkjashdkjsahdkjahsdkjhaskjdhd
    #askdjaskldjlksajdlkajslkdjdalkjsdklajsdlkas
    #jsaddjsakdjakshdjakshdkjsahdkjsahdjksadhkad
    #aksdjlksajdlkasjdlkasjdlkasjlkdjsalkdjsaldj
    #salkdjlksadjlkasdjlkasjdlkasjdlkasjdlkasjdl
    #salkjdlsakjdlkasjdlkasjdlkajslkdjlasdjsakjl
    #askljdlkasjdlkajslkdjaslkdjlaksjdlksajdlkas
    #lksadjlkasjdlkasjdlkasjdlkajsdlkajslkdjasdl
    #aksjdlkasjdlkasjdlkasjdlksajdlksajdlksadljs
    #salkdjlkasjdlkasjdlkasjdlkajslkdajslkdjsalk
    #saldjlksajdlkasjdlkasjdlkajdlkasjdlkasjdkjl
    #asljdlkasjdlkasjdlkajslkdajslkdjaslkdjalksj
    #lksadjlkasjdlkasjdlkasjdlkajsdlkajslkdjasdl
    #aksjdlkasjdlkasjdlkasjdlksajdlksajdlksadljs
    #salkdjlkasjdlkasjdlkasjdlkajslkdajslkdjsalk
    #saldjlksajdlkasjdlkasjdlkajdlkasjdlkasjdkjl
    #asljdlkasjdlkasjdlkajslkdajslkdjaslkdjalksj
    #asljdlkasjdlkasjdlkajslkdajslkdjaslkdjalksj
    #lksadjlkasjdlkasjdlkasjdlkajsdlkajslkdjasdl
    #aksjdlkasjdlkasjdlkasjdlksajdlksajdlksadljs
    #salkdjlkasjdlkasjdlkasjdlkajslkdajslkdjsalk
    #saldjlksajdlkasjdlkasjdlkajdlkasjdlkasjdkjl
    #asljdlkasjdlkasjdlkajslkdajslkdjaslkdjalksj
