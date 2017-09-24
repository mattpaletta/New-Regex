class RegexParser:
    regex = ""
    indices = []
    graph = []

    def __init__(self, regex):
        self.regex = regex
        self.graph = []

    def compile(self):
        # Use Matrix grid for storing the graph
        #  Check for the empty string, then it's just an empty string.
        if self.regex == "":
            self.graph = [[]]
            return

        self.indices = list(self.regex)  # put each character in a slot
        #self.graph = [[None] * len(self.indices)] # Create a fake start node.

        # create the space for the graph.
        for _ in range(len(self.indices)):
            self.graph.append([None] * len(self.indices))

        #self.graph = [[None] * len(self.indices)]  # Create a fake end node.

        # Start at 0, end at len(self.graph)

        """
        (source:row) -> (dest:column)
              T A O P
            T 0 1 1 0
            A 0 0 1 1
            O 0 1 0 1
            P 0 0 0 0
        """

        shouldDistribute = False
        currentDistribution = ""

        for char in self.indices:
            if char in ["[", "]", "{", "}", "(", ")"]:
                shouldDistribute = True
            else:
                if shouldDistribute == True:
                    pass





    def match(self):
        return False


    def generateN(self, num):
        return ""


if __name__ == "__main__":
    regex = "T[ao]p"
    inputs = ["Top", "Tap"]