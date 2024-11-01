from src import create_app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=6043, host="127.0.0.1")
