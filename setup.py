from setuptools import setup
from setuptools import find_packages

setup(
    name = 'runMathQuiz',
    version = '0.1.0',  
    description = 'A simple math quiz package with random integer generation, operator selection, and expression calculation',
    author = 'Oscar Rivera',  
    author_email = 'xy14gyco@fauad.fau.de',
    url='https://github.com/yourusername/math_quiz',
    packages=find_packages(exclude=('tests', 'docs')),  # Finds and packages modules in the project directory
    install_requires=["numpy", "pandas"],
    python_requires='>=3.6',  # Specify the minimum Python version
    keywords='math quiz game random integer operators',
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.__main__:main',  # If applicable; this makes a CLI command available
        ],
    },
)
