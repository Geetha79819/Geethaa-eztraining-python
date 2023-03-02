class graph(object):
    def __init__(self,size):
        self.adjMatrix=[]
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
            self.size=size
    def add_edge(self,v1,v2):
        if v1==v2:
             print("same vertex %d and d% (v1,v2)")
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
    def remove_edge(self,v1,v2):
        if self.adjMatrix[v1][v2]==0:
            print("no edge between %d and %d"%(v1,v2))
            return
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0

    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:}'.format(val))
                    

def main():
    g=graph(5)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,2)
    g.add_edge(2,0)
    g.add_edge(2,3)

    g.print_matrix()
if __name__== '__main__':
   main()
    
                    
