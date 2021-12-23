class grab:
    def grabFile(file, type):
        f = open(file, type)
    
class join:
    def join(file, File):
        f = open(file, "r")
        l = open(File, "r")
        nf = open(file + File, "x")
        a = print(f.read())
        b = print(l.read())
        nf.write(a + " " + b)
        
