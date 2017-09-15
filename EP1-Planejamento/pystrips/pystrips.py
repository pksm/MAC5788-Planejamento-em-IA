import argparse
import time

from parserIA   import Parser
from planner    import ProgressionPlanning

def parse():
    usage = 'python3 pystrips.py {show, ground, solve} <DOMAIN> <INSTANCE> [OPTIONS]'
    description = 'PyStrips is a classical planner based on HSP for PDDL/STRIPS language.'
    help_commands = '''
    show PDDL files, ground all actions or solve domain/problem instance.
    '''.strip()
    parser = argparse.ArgumentParser(usage=usage, description=description)
    parser.add_argument('command', choices=['show', 'ground', 'solve'], help=help_commands)
    parser.add_argument('domain',  type=str, help='path to PDDL domain file')
    parser.add_argument('problem', type=str, help='path to PDDL problem file')
    parser.add_argument('-s', '--search', choices=['depth', 'breadth'],
                        default='depth', type=str, help='Search Type (default=depth)')
    #parser.add_argument('-w', '--weight', type=float, default=1.0, help='heuristics weight (default=1.0)')
    parser.add_argument('-v', '--verbose', action='store_true')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse()

    uptime = {}

    start_time = time.time()
    domain  = Parser.parse(args.domain)
    problem = Parser.parse(args.problem)
    end_time = time.time()
    uptime['parsing'] = end_time - start_time

    if args.command == 'show':
        print(domain)
        print(problem)
    elif args.command == 'ground':
        print(domain)
        print(problem)
        all_actions = problem.ground_all_actions(domain)
        for action in all_actions:
            print(action)
    elif args.command == 'solve':
        start_time = time.time()
        planner = ProgressionPlanning(domain, problem)
        end_time = time.time()
        uptime['grounding'] = end_time - start_time

        h = 0
        if args.search == 'depth':
            h = 0
        elif args.search == 'breadth':
            h = 1

        start_time = time.time()
        solution, explored, visited = planner.solve(h) # IMPORTANTE
        end_time = time.time()
        uptime['planning'] = end_time - start_time

        # print statistics
        print('>> solution length =', len(solution))
        print('>> time: parsing = {0:.4f}, grounding = {1:.4f}, planning = {2:.4f}'.format(
            uptime['parsing'], uptime['grounding'], uptime['planning']))
        print('>> nodes explored =', explored)
        print('>> nodes visited  =', visited)
        print('>> ramification factor = {0:.4f}'.format(visited / explored))
        print()

        if args.verbose:
            print('>> Initial state:')
            print(', '.join(sorted(problem.init)))
            print()
            print('>> Solution:')
            print('\n'.join(map(repr, solution)))
            print()
            print('>> Goal state:')
            print(', '.join(sorted(problem.goal)))
