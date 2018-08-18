print("This message appears every time even if other python file import me.")

# You can avoid the running of code in case of import from other files as following.
if __name__ == "__main__":
    print("This message appears when \"module_something\" run himself only.")
