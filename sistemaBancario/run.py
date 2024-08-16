from flet import app
from sistemaBancario.main.handle_process import start


if __name__ == '__main__':
    app(target=start, assets_dir="assets")
