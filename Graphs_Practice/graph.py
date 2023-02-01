'''
Graph datastructure is another recursive datastructure that is bidirectional.
Lets take the example,Vijayawada connected to Chennai and Trichy, Chennai connected to Trichy and Singapore, and Trichy connected to Singapore by flights.
The total no.of paths from Vijayawada to Singapore are:
Vijayawada->Chennai->Singapore
Vijayawada->Trichy->Singapore
Vijayawada->Chennai->Trichy->Singapore
Clearly if we can find the paths from Chennai and Trichy to Singapore we can just prefix Vijayawada. So, its recursion from ending to starting stop.

Since, recursion has a base case which here will be if start and end are same or if start is not present in the routes(dictionary)

Any print statements in __init__ function will be executed as soon as object of its corresponding class is instantiated
Routes/edges are tuples with start,destinations nodes.
'''

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        # print(self.graph_dict)
    
    def get_paths(self, start, end, path = []):
        '''
        Let's consider the example at the beginning of this .py file. To find all paths from Vijayawada to Singapore find all subpaths to Singapore and prefix Vijayawada.
        i.e, Chennai->Singapore, Trichy->Singapore,Chennai->Trichy->Singapore
        This is a recursive case and so we need to start with the base case where start == destination
        Another base case is to take care of destination when its considered as a starting route to return empty list. 
        '''
        # If the start and end destinations are the same then return a list with only the name of the destination/start
        path = path + [start] ## square brackets around start is mandatory as it concatenation of str with a list is not possible 
        # print(path)
        if start == end:
            return [path]

        # If the start location is not present in the routes dictionary(network/graph given), return empty list i.e Singapore is destination in example but doesn't have any other place as its starting point in my example
        if start not in self.graph_dict:
            return []
        
        # Track a list of all paths
        paths = []
        # For each destination of start node, check if the destination works as an intermediate node to the end node
        # Recursive case, to find paths from Vijayawada to Singapore, check the values in graph_dictionary created with all the edges for the key value start point.
        #i.e Vijayawada, it has values lets say Chennai, Trichy that are also keys with destination Singapore. 

        for node in self.graph_dict[start]: #For each node(which points to values in dictionary with key as starting point)
            if node not in path: # If the node lets say Trichy is not added then add a new path  
                new_paths = self.get_paths(node, end, path)
                # print(path)
                # print(paths)
                for p in new_paths:
                    paths.append(p)

        return paths
    
    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path





if __name__ == '__main__':

    routes = [
            # ("Mumbai", "Paris"),
            # ("Mumbai", "Dubai"),
            # ("Paris", "Dubai"),
            # ("Paris", "New York"),
            # ("Dubai", "New York"),
            # ("New York", "Toronto"),
            ("Vijayawada","Trichy"),
            ("Vijayawada","Chennai"),
            ("Chennai","Trichy"),
            ("Chennai","Singapore"),
            ("Trichy","Singapore")
        ]
    
    route_graph = Graph(routes)

    start = "Vijayawada"
    end = "Singapore"

    print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))

    # start = "Dubai"
    # end = "New York"

    # print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
    # print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))