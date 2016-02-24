from setuptools import setup

setup(
        name = "nonce",
        packages = ["nonce"],
        package_data = {"nonce":["data/*.gibi"]},
        version = "0.0.2",
        description = "CLI for gibi",
        url = "http://github.com/dustractor/nonce",
        author = "Shams Kitz",
        author_email = "dustractor@gmail.com",
        install_requires = [ "gibi" ],
        entry_points = { "console_scripts": [ "nonce = nonce.__main__:main" ] },
        keywords = "nonsense markhov gibberish gibi",
        license = "Free for education and entertainment purposes only.",
        classifiers = [
            "Development Status :: 3 - Alpha",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: End Users/Desktop",
            "License :: Free For Educational Use",
            "Programming Language :: Python :: 3",
            "Programming Language :: Unix Shell",
            "Topic :: Database",
            "Topic :: Utilities" ])
