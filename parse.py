import sys
import yaml
def main():
    yaml_name_before = sys.argv[1]
    yaml_name_after = sys.argv[2]
    print(yaml_name_before)
    print(yaml_name_after)

    if yaml_name_before:
        with open(yaml_name_before, "r") as file:
              bla= file.read()

        with open(f"123.{yaml_name_before}", "w") as file:
              file.write(bla)

    if yaml_name_after:
        with open(yaml_name_after, "r") as file:
              bla= file.read()

        with open(f"456.{yaml_name_after}", "w") as file:
              file.write(bla)
    


if __name__ == "__main__":
    main()


