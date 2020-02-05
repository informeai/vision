import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="visionPDF", # Nome do Pacote
    version="1.0.1",
    author="Wellington Gadelha",
    author_email="contato.informeai@gmail.com",
    description="Modulo que ler,traduz e escreve arquivos PDF.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/informeai/vision",
    packages=setuptools.find_packages(),
    install_requires=['PyPDF2','reportlab','karkipytranslator'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
