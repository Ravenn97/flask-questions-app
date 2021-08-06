from setuptools import setup, find_packages

setup (
    name = 'flaskapp',
    version='0.1.0',
    description='Flask Questions app',
    url='https://github.com/shaneboulden/flask-questions-app',
    author='Shane Boulden',
    author_email='sboulden@redhat.com',
    keywords='flask containers openshift',
    include_package_data=True,
    packages=find_packages()
)
