import sys
import yaml
def main():
    print("got here")
    yaml_name_before = sys.argv[1]
    yaml_name_after = ""
    if len(sys.argv) > 2:
      yaml_name_after = sys.argv[2]
      print(yaml_name_after)
    print(yaml_name_before)
    


if __name__ == "__main__":
    main()


