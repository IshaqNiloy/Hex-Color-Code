# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
class Regex():
    def __init__(self, string):
        self.string = string
    
    def verify_hex_code(self):
        if re.match('^[#]', string):
            pass
        else:
            hex_code_list = re.findall('[#][0-9a-f]{6}|[#][0-9a-f]{3}', string, re.I)
            for hex_code in hex_code_list:
                print(hex_code)

if __name__ == '__main__':
    test_case = int(input())

    for _ in range(test_case):
        string = input()
        my_object = Regex(string)
        my_object.verify_hex_code()
