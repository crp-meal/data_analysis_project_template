from {{cookiecutter.package_name}} import __version__ as _version
from {{cookiecutter.package_name}}.config.config import config
from {{cookiecutter.package_name}}.config.logging import ProcessLogger


def main():
    ProcessLogger.processLogger.info(f" =============== Starting process with version: {_version} ===============")

    return 0


if __name__ == "__main__":
    main()
    ProcessLogger.processLogger.info(f" ========================== PROCESS END ========================== ")
