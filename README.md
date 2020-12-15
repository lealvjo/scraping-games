# scraping_game
Application Programming Interface (API) - web scraping on playstationstore promotions and returns a new json object for testing

#Importing the project and creat virtual environment project Pycharm

    import the project into git: https://github.com/lealvjo/web_scraping.git
    
    - [x] Open the project in pycharm
    - [x] Navigate to file and settings
    - [x] Navigate to python interpreter and click on the gear
    - [x] Select add and new environment
    
#Enabling virtual environment
    
    A virtual environment is a Python environment, so the Python interpreter, libraries and scripts 
    installed in it are isolated from those installed in other virtual environments.
     
    - [x] Open a terminal in pycharm in your root folder
    - [x] And type: cd venv\Scripts\
    - [x] And type: activate
    
    **After this will appear a (venv) before your project, it means that the virtual environment has been enabled**
        Ex: (venv) C:\Users\{user}\PycharmProjects\web_scraping\

#Installing external packages

    Text file, containing a list of items / packages to be installed during pip install.

    - [x] Open a terminal at the root where the requirements.txt file is located
    - [x] Type: pip install -r requirements.txt
    
    To check what has been installed
    
    - [x] Type: pip list
    
    ***The application is at the root /app

#Running IDE (Pycharm)

    - [x] It's going to ate or main method app/main.py
    - [x] Choose start or debug

    In this option the application rises in your virtualized environment

#Endpoints virtual environment and local environment

    - [x] /game
    - [x] /game/<int:id>
    - [x] /game/page/<int:page>

    Select all games raise all games

        - [x] using the get method
        
        url
            http://localhost:5000/game

    raise only one games

        - [x] using the get method
        
        url
            http://localhost:5000/game/<int:id>

    lift all sets from a specific page

        - [x] using the get method
        
        url
            http://localhost:5000/game/page/<int:page>

    submit a new game

        - [x] using the post method

        body ex = {
            "page_indx": 11,
            "name": "Jcyberpunk 2077",
            "price": "R$ 200,00",
            "game_link": "http://teste",
            "game_pht": "http://teste"
        }

        url
            http://localhost/5000/game

    delete a specific game

        - [x] using the delete method

        url
            http://localhost/5000/game/<int:id>

    change the price of a specific game
        
        - [x] using the put method

        body ex = {
                    "price": "R$ 00,00"
                }

        url
            http://localhost/5000/game/<int:id>

    schema:
        {
        "title": "Person",
        "type": "object",
        "required": [ "page_indx", "name", "price", "game_link", "game_pht"],
        "properties": {
            "id": {
                "type": "integer"
            },
            "page_indx": {
                "type": "integer"
            },
            "name": {
                "type": "string"
            },
            "price": {
                "type": "string"
            },
            "game_link": {
                "type": "string"
            },
            "game_pht": {
                "type": "string"
            }
          }
        }
        

#To generate a new installable package setup.py

    Setup.py is a python file, which usually informs you that the module / package you are about to install has been packaged and distributed with Distutils, 
    which is the standard for distributing Python modules. This allows you to easily install Python packages.
    
    - [x] Open a terminal at the root where the
    - [x] type: python setup.py bdist_wheel
    
    *** You can install it in the virtual environment or on any other machine, even yours locally.
    
    - [x] type: pip install --upgrade --force-reinstall dist/web_scraping-{version}-py3-none-any.whl
    

#To run the project installed

    If installed in any environment to run by calling entry_points.
    
    - [x] In the terminal type: {ps_store} and press enter
    
    Running on http://localhost/:5000/
    

