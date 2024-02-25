from setuptools import find_packages,setup

setup(
	name = 'pharmaQnAChatbot',
	version = '0.0.1',
	author = 'mohamed sabith',
	author_email = 'mohamedsabith2@gmail.com',
	install_requires = ["langchain-google-genai","langchain","streamlit","python-dotenv"],
	packages = find_packages()
)