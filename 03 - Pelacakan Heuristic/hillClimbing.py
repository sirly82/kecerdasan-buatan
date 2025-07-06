import random
from ai_pkg import Graph, Node, Problem, argmax_random_tie

city_map = Graph(
    {
        'Oradea': {'Oradea': 0, 'Sibiu': 24, 'Arad': 59, 'Zerind': 38},
        'Sibiu': {'Oradea': 24, 'Sibiu': 0, 'Arad': 51, 'Zerind': 56},
        'Arad': {'Oradea': 59, 'Sibiu': 51, 'Arad': 0, 'Zerind': 47},
        'Zerind': {'Oradea': 38, 'Sibiu': 56, 'Arad': 47, 'Zerind': 0}
    },
    directed=False
)


distances = {}

class TSPProblem(Problem):
    def generate_neighbour(self, state):
        neighbour_state = state[:]
        print(neighbour_state)
        left = random.randint(0, len(neighbour_state) - 1)
        right = random.randint(0, len(neighbour_state) - 1)
        if left > right:
            left, right = right, left
        neighbour_state[left:right+1] = list(reversed(neighbour_state[left:right+1]))
        print('left :', left)
        print('right :', right)
        print(neighbour_state)
        return neighbour_state

    def actions(self, state):
        return [self.generate_neighbour]

    def result(self, state, action):
        return action(state)

    def path_cost(self, state):
        cost = 0
        for i in range(len(state) - 1):
            current_city = state[i]
            next_city = state[i + 1]
            cost += distances[current_city][next_city]
        cost += distances[state[-1]][state[0]]  
        return cost

    def value(self, state):
        return -1 * self.path_cost(state)  

def hill_climbing(problem):
    def find_neighbors(state, number_of_neighbors=100):
        neighbors = []
        for _ in range(number_of_neighbors):
            new_state = problem.generate_neighbour(state)
            neighbors.append(Node(new_state))
        return neighbors

    current = Node(problem.initial)
    while True:
        neighbors = find_neighbors(current.state)
        if not neighbors:
            break
        neighbor = argmax_random_tie(neighbors, key=lambda node: problem.value(node.state))
        if problem.value(neighbor.state) <= problem.value(current.state):
            break
        current = neighbor
    return current.state

if __name__ == '__main__':
    all_cities = []
    cities_graph = city_map.graph_dict
    for city_1 in cities_graph.keys():
        distances[city_1] = {}
        if city_1 not in all_cities:
            all_cities.append(city_1)
        for city_2 in cities_graph.keys():
            if city_1 == city_2:
                distances[city_1][city_2] = 0
            elif cities_graph.get(city_1).get(city_2) is not None:
                distances[city_1][city_2] = cities_graph.get(city_1).get(city_2)
            else:
                distances[city_1][city_2] = float('inf')  

    random.shuffle(all_cities)  
    problem = TSPProblem(initial=all_cities.copy())

    best_path = hill_climbing(problem)
    print("Best path found:", best_path)
    print("Path cost:", problem.path_cost(best_path))