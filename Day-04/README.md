# Day 4 · Functions & Modules

Today we will learn how to organize our code so we don't have to copy-paste the same lines over and over.

## What You Will Learn

-   **Functions:** Blocks of code that do one specific thing (like "calculate total" or "send email").
-   **Modules:** Files containing python code that you can import into other scripts.
-   **Packages:** Folders containing multiple modules.

## Instructions

1.  **Read:** The section below explains the difference between Functions, Modules, and Packages.
2.  **Run Example:** See how we use functions to clean up code.
    ```bash
    cd examples
    # First, create a dummy file to read
    echo "web-server\ndatabase\ncache" > services.txt
    python3 function_refactor.py
    ```
3.  **Experiment:** Try adding a new function to the script that prints "Done!" at the end.

## Checklist

-   [ ] I can write a simple function (`def my_function():`).
-   [ ] I understand how to `import` code from another file.

---

# Python Functions, Modules and Packages

## 1. Functions
A function is a reusable block of code.
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

## 2. Modules
A module is just a Python file (e.g., `my_module.py`). You can use it in another file:
```python
import my_module
```

## 3. Packages
A package is a folder with a special file named `__init__.py`. It helps organize many modules together.