from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='customer_segmentation_clustering',
    packages=find_packages(),
    version='0.1.0',
    description='Segmentation of customers into multiple clusters using fuzzy algorithm',
    long_description=readme,
    author='Spoorthi Chinivar',
    author_email='chinivarspoorthi@gmail.com'
    license=license,
    url='https://github.com/Spoorthi281997/Customer_Segmentation_Clustering'
)
