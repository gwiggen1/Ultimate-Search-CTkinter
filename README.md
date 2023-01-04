# Ultimate-Search CTkinter
## Description
Creates a GUI Search Bar that links to multiple search engines and inputs user's search.

Uses Search Engines Google, Bing, and DuckDuckGO
## Requirements
Uses libraries Selenium, tkinter, CTkinter

Must have chrome webdriver installed
## GUI
![UltimateSearch](https://user-images.githubusercontent.com/121186555/209994760-3c66262b-e417-4e84-9869-73418ff79fd7.PNG)


## Packaging

When trying to package a CTkinter GUI Program as an executable I recommend using auto-py-to-exe (a bit more user friendly than pyinstaller)

To Install auto-py-to-exe:

```
pip install auto-py-to-exe
```

Open auto-py-to-exe:


```
python -m auto_py_to_exe
```


This should open auto-py-to-exe. Once inside you must use One Directory (`--onedir`[^1]) and Add Folder CTkinter in Additional Files (`--add-data`[^1])

Here is some additional help/explanation from the devs:

[CTK Packaging Help](https://github.com/TomSchimansky/CustomTkinter/wiki/Packaging)


[^1]: If using CTkinter library you will not be able to do One File. You must also add CTkinter to the package. Else you will get an error.
