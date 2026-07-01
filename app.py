from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/matrix", methods=["POST"])
def matrix():

    result = None
    error = None

    # Matrix sizes
    rows1 = int(request.form["rows1"])
    cols1 = int(request.form["cols1"])
    rows2 = int(request.form["rows2"])
    cols2 = int(request.form["cols2"])

    operation = request.form.get("operation")

    # First visit from index.html
    if operation is None:
        return render_template(
            "matrix.html",
            rows1=rows1,
            cols1=cols1,
            rows2=rows2,
            cols2=cols2,
        )

    # Read Matrix A
    matrix1 = []

    for i in range(rows1):
        row = []

        for j in range(cols1):
            row.append(float(request.form[f"m1_{i}_{j}"]))

        matrix1.append(row)

    # Read Matrix B
    matrix2 = []

    for i in range(rows2):
        row = []

        for j in range(cols2):
            row.append(float(request.form[f"m2_{i}_{j}"]))

        matrix2.append(row)

    A = np.array(matrix1)
    B = np.array(matrix2)

    try:

        if operation == "add":
            result = A + B

        elif operation == "subtract":
            result = A - B

        elif operation == "multiply":
            result = A @ B

        elif operation == "transpose1":
            result = A.T

        elif operation == "transpose2":
            result = B.T

        elif operation == "det1":
            result = np.linalg.det(A)

        elif operation == "det2":
            result = np.linalg.det(B)

    except Exception as e:
        error = str(e)

    return render_template(
        "matrix.html",
        rows1=rows1,
        cols1=cols1,
        rows2=rows2,
        cols2=cols2,
        matrix1=matrix1,
        matrix2=matrix2,
        result=result,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True)