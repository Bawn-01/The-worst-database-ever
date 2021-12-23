class files:
    def new(file):
        open(file, "x")
    
    def edit(file):
        f = open(file, "a")
        inp = input()
        f.write(inp)
    
    def read(file):
        f = open(file, "r")
        print(f.read())
