# Python

## pip installation

  * Download `get-pip.py` to a folder on your computer. Open a command prompt window and navigate to the folder containing `get-pip.py`. Then run `python get-pip.py`. This will install pip.
  
  In Windows Command Window,
  
  `cd C:\...\Python36` change directory to where get-pip.py is
  
  `python get-pip.py`  install pip
  
  * verify a successful installation by opening a command prompt window and navigating to your Python installation's script directory (default is `C:\Python36\Scripts`). Type `pip frezze` from this location to launch the Python interpreter.
  
  `pip frezze` displays the version number of all modules installed in your Python non-standard library.
  
  * Pip not installed
  
  `python -m ensurepip --default-pip`
 
  * Set enviroment varibales for pip/python
  
    - Search environment variables in windows:
    
    `Edit environment variables for your account`
    
    - Add/Modify Path:
    
    Add `PYTHON_HOME` in new variable and set variable value to `C:\..\Pyhton36`
    
    Edit variable value in `Path`: `;%PYTHON_HOME%;%PYTHON_HOME%\Scripts\`
    
  * Package Installation via pip
        
    - Common Packages: **numpy**, **scipy**, **matplotlib**, **ipython**, **jupyter**, **pandas**, **sympy**, **nose**
    
    _cmd_
    
    `python -m pip install --user xxxx`
    
    
    
## Python Notes

  * Documentation Strings
  
    * The first line should always be a short, concise summary of the object's purpose. Should not explicitly state the object's name or type. This line should begin with a capital letter and end with a period
    * More than one line in documentation string. The second line should be blank, visually separating the summary from the rest of the description. The following lines should be one or more paragraphs describing the object's calling conventions, its side effects, etc.
    * The first non-blank line after the first line of the string detemines the amount of indentation for the entire documentation string.
  
    
    
    
