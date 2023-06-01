from flask import Flask, request, jsonify, render_template, abort
from flask import Blueprint
from labrinth import Labyrinth
app = Flask(__name__)
labs = {
    1: Labyrinth("labyrinth.txt"),
    2: Labyrinth("labyrinth2.txt"),
    3: Labyrinth("labyrinth3.txt"),
    4: Labyrinth("labyrinth4.txt"),
    5: Labyrinth("labyrinth5.txt"),
}
api_lb = Blueprint('labyrinth', __name__, url_prefix='/labyrinth')


@api_lb.route('/solve', methods=['POST'])
def labyrinth():
    data = request.get_json()
    filename = data['filename']
    lab = Labyrinth(filename)
    lab.solve()
    return jsonify(lab._solution)


@api_lb.route('/solve/<lab_id>', methods=['GET'])
def labyrinth_get(lab_id):
    try:
        lab = labs[int(lab_id)]
    except KeyError:
        return jsonify({"message": "Lab not found"}), 404
    lab.solve()
    return jsonify(lab._solution)


app.register_blueprint(api_lb)


@app.route('/visualise/<lab_id>', methods=['GET'])
def visualise_html(lab_id):
    try:
        lab = labs[int(lab_id)]
    except KeyError:
        abort(404)
    lab.solve()
    visualized = lab.show(show_solution=True)
    matrice_visualized = visualized.split('\n')
    for i in range(len(matrice_visualized)):
        matrice_visualized[i] = ' '.join(matrice_visualized[i])

    return render_template('visualise.html', lab=matrice_visualized, path=lab._solution)


@app.route('/lab/<lab_id>', methods=['GET'])
def lab_html(lab_id):
    try:
        lab = labs[int(lab_id)]
    except KeyError:
        abort(404)
    lab.solve()
    visualized = lab.show()
    matrice_visualized = visualized.split('\n')
    for i in range(len(matrice_visualized)):
        matrice_visualized[i] = ' '.join(matrice_visualized[i])

    return render_template('visualise.html', lab=matrice_visualized, path=lab._solution)


if __name__ == '__main__':
    app.run(debug=True)
