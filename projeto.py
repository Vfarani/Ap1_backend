import pydicom

from flask import Flask, request, jsonify, send_file


app = Flask(__name__)


@app.route('/anonimize', methods=['POST'])
def anonimize_dicom():
    # Seu código de anonimização aqui
    return jsonify({"message": "Imagem DICOM anonimizada com sucesso"})

if __name__ == '__main__':
    app.run(debug=True)


def anonimize_dicom_file(input_path, output_path):
    ds = pydicom.dcmread(input_path)
    # Aqui, você pode acessar os metadados do DICOM (por exemplo, ds.PatientName)
    # e modificar ou remover informações sensíveis.
    ds.PatientName = "Paciente Anônimo"
    # Outras ações de anonimização, se necessário...

    ds.save_as(output_path)



@app.route('/anonimize', methods=['POST'])
def anonimize_dicom():
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo fornecido"})

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Nome de arquivo vazio"})

    input_path = 'temp_input.dcm'
    output_path = 'temp_output.dcm'
    file.save(input_path)

    anonimize_dicom_file(input_path, output_path)

    # Envie o arquivo anonimizado como resposta
    return send_file(output_path, as_attachment=True)


    # Envie o arquivo anonimizado como resposta
    return send_file(output_path)

if __name__ == '__main__':
    app.run(debug=True)




