from app import create_app

print("se ejecuta index")

flask_app = create_app()

if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", debug=True)