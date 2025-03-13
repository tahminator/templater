# Templater

## Description

Templater is a basic program that does string-replacement around brackets,
similar to how f-strings work in Python. While many tools like this already exist,
I found it helpful that it was a simple Python script (with 0 dependencies)
I also like having all these templates in one folder to be reused anywhere.

## Installation

Steps to install and set up the project:

```sh
# Clone the repository
git clone https://github.com/tahminator/templater.git
cd templater

# No dependencies required, just make sure you have Python installed.
python3 run.py
```

## Usage

NOTE: You can always check `templates/example` for how it should work.

How to setup templates:

1. You must name a folder inside of the `templates/` directory:

  ```txt
  templates/
  │── linkedin/
  │   └── template.txt
  ```

2. Inside of the folder, you just have to create a `template.txt` folder with the actual template text.

  ```txt
  Hello {name},

  My name is {myName} and I am currently a {major} major at {college}. Thank you!

  Best,
  {myName}
  ```

3. Just run `python3 run.py` and you should be able to select the folder now!
