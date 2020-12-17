import sys
import getopt
import pandas as pd
from uplift_tree import build_uplift_tree

def main(argv):
    """Main aplication method"""

    treatment = None
    outcome = None
    file_name = None

    if not argv:
        #run with actionRules
        print('Please provide input arguments')
    else:
        # Catch parameters by console
        try:
            argv = sys.argv[1:]
            opts, args = getopt.getopt(argv, "f:t:y:")
            for opt, arg in opts:
                if opt in ['-t']:
                    treatment = arg
                elif opt in ['-y']:
                    outcome = arg
                elif opt in ['-f']:
                    file_name = arg

            print('name of treatment column: {}'.format(treatment))
            print('name of outcome column: {}'.format(outcome))
            print('name of file: {}'.format(file_name))

        except getopt.GetoptError:
            print('Invalid arguments')
            sys.exit(2)
    #execution
    data = pd.read_csv(file_name)
    build_uplift_tree(data, treatment, outcome)

if __name__ == "__main__":
    main(sys.argv[1:])