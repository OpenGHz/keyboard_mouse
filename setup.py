from setuptools import setup, find_packages

setup(
    name="keyboard_mouse",
    version="1.0.0",
    packages=find_packages(),
    package_dir={"": "."},
    install_requires=[
        "python-xlib",
    ],
    author="OpenGHz",
    author_email="ghz23@mails.tsinghua.edu.cn",
    description="Tools to read the inputs of your keyboard and mouse.",
    url="https://github.com/OpenGHz/keyboard_mouse.git",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
