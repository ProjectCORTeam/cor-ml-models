from setuptools import find_packages, setup  # type: ignore

# Library dependencies
INSTALL_REQUIRES = [

    "numpy==1.21.1",
    "psutil==5.8.0",
    "scikit-learn==1.0",
    "textacy==0.11.0",
    "joblib==1.0.1",
    "pandas==1.2.3",
    "nltk==3.6.7",
    "pickle-mixin"

]

#  Testing dependencies
TEST_REQUIRES = [
    "pytest",
    "black",
    "pre-commit",
    "flake8",
    "mypy",
    "pytest-cov",
    "pytest-mock",
]

setup(
    name="categorization",
    version="0.1.0",
    description="Ticket Categorization",
    author="COR Data Team",
    author_email="",
    packages=find_packages(),
    python_requires=">=3.7",
    setup_requires=["wheel"],
    install_requires=INSTALL_REQUIRES,
    extras_require={"test": TEST_REQUIRES},
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
)
