import os
from flask import Flask, request, jsonify, send_file
import pydicom

app = Flask(__name__)

def anonimize_dicom_file(input_path, output_directory):
    ds = pydicom.dcmread(input_path)
    # Aqui, você pode acessar os metadados do DICOM (por exemplo, ds.PatientName)
    # e modificar ou remover informações sensíveis.
    ds.PatientName = "Paciente Anônimo"
    # Outras ações de anonimização, se necessário...

    output_path = os.path.join(output_directory, os.path.basename(input_path))
    ds.save_as(output_path)

@app.route('/anonimize', methods=['POST'])
def anonimize_dicom():
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo fornecido"})

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Nome de arquivo vazio"})

    # Configure o caminho para a pasta onde você deseja salvar as imagens anonimizadas
    output_directory = 'C:/Users/202303183445/Desktop/API_backend'

    input_path = os.path.join(output_directory, file.filename)

    file.save(input_path)

    anonimize_dicom_file(input_path, output_directory)

    # Envie o arquivo anonimizado como resposta
    return send_file(input_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)





