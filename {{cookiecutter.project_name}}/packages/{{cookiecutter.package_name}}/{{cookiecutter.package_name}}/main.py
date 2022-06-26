from {{cookiecutter.package_name}} import __version__ as _version
from {{cookiecutter.package_name}}.config.config import config


def main():
    print(_version)
    print(config.PACKAGE_ROOT)

    return 0


if __name__ == "__main__":
    main()
