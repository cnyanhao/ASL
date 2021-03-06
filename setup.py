from setuptools import setup, find_packages


setup(
    name="dalib", # Replace with your own username
    description="A Library for Deep Domain Adaptation",
    packages=find_packages(),
    install_requires=[
        'torch>=1.4.0',
        'torchvision>=0.5.0',
        'numpy',
        'qpsolvers>=1.4.0'
    ],
)
