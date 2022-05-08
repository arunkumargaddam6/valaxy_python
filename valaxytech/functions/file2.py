from logging import exception
import os
def main():
    req_path=input("Enter path to change working dir: ")
    print("the current working dir is: ",os.getcwd())
    try:
        os.chdir(req_path)
        print("now you new working dir is: ",os.getcwd())
    except FileNotFoundError:
        print("Given path is not a valid path. so can not change working dire")
    except NotADirectoryError:
        print("Given path is a file path. so cant change working dire")
    except PermissionError:
        print("sorry you dont have access for the given path. so cant change working dir")
    except exception as e:
        print(e)
    return None

if __name__=="__main__":
    main()