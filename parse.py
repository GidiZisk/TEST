import sys
import yaml
def main():
    print("got here")
    yaml_name_before = sys.argv[1]
    yaml_name_after = ""
    if len(sys.argv) > 2:
      yaml_name_after = sys.argv[2]
      with open(yaml_name_after, "r") as file:
          print(file.read())
    print(yaml_name_before)
    with open(yaml_name_before, "r") as file:
          print(file.read())
    


if __name__ == "__main__":
    main()


