import time


# TM Simulator Class
class TM:
    def __init__(self, filename):
        self.dict = {}
        self.start = "N"
        self.accept = "N"
        self.read_rules(filename)
        self.state = self.start
        self.head = 0

    def run(self, input_str, steps=False, head=0):
        t = time.time()
        self.head = head
        self.state = self.start

        input_lst = list(input_str)
        while not self.accepted():
            if steps:
                print("".join(input_lst))
                for _ in range(self.head):
                    print(" ", end="")
                print("^")
                print("state: {0}".format(self.state))
            rule = self.dict[(self.state, input_lst[self.head])]
            if steps:
                print(str(rule) + "\n")
            input_lst[self.head] = rule[1]
            self.head += 1 if rule[2] == "R" else -1
            self.state = rule[0]
        print(str(time.time() - t))
        return "".join(input_lst)
        # print("".join(input_lst))

    def read_rules(self, filename):
        try:
            with open(filename) as infile:
                lines = infile.readlines()
                state_info = lines[0].rstrip("\n").split(",")
                self.start = state_info[0]
                self.accept = state_info[1:]
                for line in lines[1:]:
                    rule = line.rstrip("\n").split(",")
                    self.dict[tuple(rule[0:2])] = tuple(rule[2:])
            return True
        except:
            return False

    def accepted(self):
        if isinstance(self.accept, list):
            accept = False
            for state in self.accept:
                if self.state == state:
                    accept = True
            return accept
        else:
            return self.state == self.accept
