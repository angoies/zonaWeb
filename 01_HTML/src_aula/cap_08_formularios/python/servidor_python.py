from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def procesar_formulario():

    if request.method == 'POST':
        # Procesar datos enviados por POST (ej: desde un formulario)
        print("\n--- PETICIÓN POST RECIBIDA ---")
        for key, value in request.form.items():
            print(f"Campo [{key}] = {value}")
        print("-" * 31 + "\n")
        return "Datos POST recibidos correctamente."
    
    else:
        # Procesar datos enviados por GET (ej: parámetros en la URL)
        print("\n--- PETICIÓN GET RECIBIDA ---")
        for key, value in request.args.items():
            print(f"Parámetro [{key}] = {value}")
        print("-" * 30 + "\n")
        return "Datos GET recibidos correctamente."

if __name__ == '__main__':
    app.run(host='0.00.0', port=5000, debug=True)