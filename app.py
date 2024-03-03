from flask import Flask



app = Flask(__name__)

# Read data from a file (e.g., "data.txt")
def read_data_from_file():
    with open("data.txt", "r") as file:
        return file.read()

@app.route("/")
def display_data():
    data = read_data_from_file()
    return f"<html><body><pre>{data}</pre></body></html>"

if __name__ == "__main__":
    app.run(debug=True)

