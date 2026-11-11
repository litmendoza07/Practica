from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

estado = {
    "pila": [],
    "cola": [],
    "lista": [],
    "arbol": [],
    "grafo": {"vertices": [], "aristas": []},
}


def nuevo_estado():
    return {
        "pila": [],
        "cola": [],
        "lista": [],
        "arbol": [],
        "grafo": {"vertices": [], "aristas": []},
    }


@app.get("/")
def inicio():
    return render_template("index.html")


@app.get("/api/estado")
def api_estado():
    return jsonify({"estado": estado})


@app.post("/api/operacion")
def operacion():
    datos = request.get_json(silent=True) or {}
    tipo = datos.get("tipo")
    accion = datos.get("accion")
    valor = datos.get("valor")
    otro = datos.get("otro")

    if tipo not in estado:
        return jsonify({"error": "Estructura no válida"}), 400

    if accion not in ["agregar", "extraer", "reiniciar"]:
        return jsonify({"error": "Acción no válida"}), 400

    if tipo == "pila":
        if accion == "reiniciar":
            estado[tipo] = []
            return jsonify({"mensaje": "Pila reiniciada", "estado": estado})
        if accion == "agregar":
            estado[tipo].append(valor)
            return jsonify({"mensaje": "Valor agregado", "estado": estado})
        if accion == "extraer":
            if not estado[tipo]:
                return jsonify({"error": "La pila está vacía"}), 400
            valor_extraido = estado[tipo].pop()
            return jsonify({"mensaje": "Valor extraído", "valor": valor_extraido, "estado": estado})

    if tipo == "cola":
        if accion == "reiniciar":
            estado[tipo] = []
            return jsonify({"mensaje": "Cola reiniciada", "estado": estado})
        if accion == "agregar":
            estado[tipo].append(valor)
            return jsonify({"mensaje": "Valor agregado", "estado": estado})
        if accion == "extraer":
            if not estado[tipo]:
                return jsonify({"error": "La cola está vacía"}), 400
            valor_extraido = estado[tipo].pop(0)
            return jsonify({"mensaje": "Valor extraído", "valor": valor_extraido, "estado": estado})

    if tipo == "lista":
        if accion == "reiniciar":
            estado[tipo] = []
            return jsonify({"mensaje": "Lista reiniciada", "estado": estado})
        if accion == "agregar":
            estado[tipo].append(valor)
            return jsonify({"mensaje": "Valor agregado", "estado": estado})
        if accion == "extraer":
            if valor not in estado[tipo]:
                return jsonify({"error": "No encontrado"}), 404
            estado[tipo].remove(valor)
            return jsonify({"mensaje": "Valor eliminado", "estado": estado})

    if tipo == "arbol":
        if accion == "reiniciar":
            estado[tipo] = []
            return jsonify({"mensaje": "Árbol reiniciado", "estado": estado})
        if accion == "agregar":
            if not estado[tipo]:
                estado[tipo].append({"nombre": valor, "padre": None})
                return jsonify({"mensaje": "Nodo agregado", "estado": estado})
            if any(n.get("nombre") == valor for n in estado[tipo]):
                return jsonify({"error": "Nodo duplicado"}), 400
            if otro is None:
                return jsonify({"error": "El padre debe existir"}), 400
            if not any(n.get("nombre") == otro for n in estado[tipo]):
                return jsonify({"error": "No existe el padre"}), 400
            estado[tipo].append({"nombre": valor, "padre": otro})
            return jsonify({"mensaje": "Nodo agregado", "estado": estado})
        if accion == "extraer":
            for nodo in estado[tipo]:
                if nodo["nombre"] == valor:
                    estado[tipo].remove(nodo)
                    return jsonify({"mensaje": "Nodo extraído", "estado": estado})
            return jsonify({"error": "Nodo no encontrado"}), 404

    if tipo == "grafo":
        if accion == "reiniciar":
            estado[tipo] = {"vertices": [], "aristas": []}
            return jsonify({"mensaje": "Grafo reiniciado", "estado": estado})
        if accion == "agregar":
            if valor not in estado[tipo]["vertices"]:
                estado[tipo]["vertices"].append(valor)
                return jsonify({"mensaje": "Vértice agregado", "estado": estado})
            return jsonify({"error": "Vértice duplicado"}), 400
        if accion == "conectar":
            if valor not in estado[tipo]["vertices"] or otro not in estado[tipo]["vertices"]:
                return jsonify({"error": "Primero crea ambos vértices"}), 400
            if valor == otro:
                return jsonify({"error": "Una arista no se puede conectar consigo misma"}), 400
            pareja = sorted([valor, otro])
            if pareja not in estado[tipo]["aristas"]:
                estado[tipo]["aristas"].append(pareja)
                return jsonify({"mensaje": "Arista conectada", "estado": estado})
            return jsonify({"error": "La arista ya existe"}), 400
        if accion == "extraer":
            if valor in estado[tipo]["vertices"]:
                estado[tipo]["vertices"].remove(valor)
                estado[tipo]["aristas"] = [
                    arista for arista in estado[tipo]["aristas"] if valor not in arista
                ]
                return jsonify({"mensaje": "Vértice eliminado", "estado": estado})
            return jsonify({"error": "Vértice no encontrado"}), 404

    return jsonify({"error": "Acción no válida"}), 400


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)