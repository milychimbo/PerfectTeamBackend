from flask import Flask, request, jsonify
import fitz
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola, bienvenido al backend de Perfect Team!"

@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    # Obtener el contenido del archivo PDF desde la solicitud HTTP
    pdf_content = request.data

    # Procesar el contenido del archivo PDF
    pdf_document = fitz.open(stream=pdf_content)
    pdf_text = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pdf_text += page.get_text()

    # Procesar pdf_text para obtener el nombre del consultor y sus habilidades
    # Aquí asumimos que el nombre del consultor está en la primera línea y las habilidades en las siguientes líneas
    lines = pdf_text.split("\n")
    consultor_name = lines[0].strip()
    skills = lines[1:]

    # Estructurar la información en un diccionario
    data = {
        "consultor_name": consultor_name,
        "skills": skills
    }

    # Convertir el diccionario a JSON y devolverlo en la respuesta HTTP
    json_data = json.dumps(data, indent=4)
    return jsonify(json_data)
    

if __name__ == '__main__':
    app.run()