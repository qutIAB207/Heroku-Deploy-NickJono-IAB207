from projectfile.website import create_app


def start_app():
    if (__name__ == '__main__'):
        napp = create_app()
        napp.run(debug=True)
