import sys
import yaml
def main():
    print("got here")
    yaml_name_before = sys.argv[1]
    yaml_name_after = ""
    if len(sys.argv) > 2:
      yaml_name_after = sys.argv[2]
    with open(yaml_name_before, "r") as file:
          bla= file.read()

    with open(f"123.{yaml_name_before}", "w") as file:
          file.write(bla)
          print(bla)
    


if __name__ == "__main__":
    main()


