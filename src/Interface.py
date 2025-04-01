import argparse
import FunctionV3 as Function

# Initialize argument parser
parser = argparse.ArgumentParser()

# Add all arguments as options for input
# -- means it is a optional input, but since they are used we need default options
# Type specifies the type of the input (int, float, string, etc.)
# Help is what is displayed if using the help command
# Choices are possible inputs, throws error if input differs

parser.add_argument("-m", "--method", help="Call Euler method. Default method is implicit", choices=["I", "E", "i", "e", "si", "SI"], default = "I")
parser.add_argument("dT", type=float, help="Timestep")
parser.add_argument("-IG1", "--initial_guess1", type=float, help="First initial gues", default = 0)
parser.add_argument("-IG2", "--initial_guess2", type=float, help="Second initial gues", default = 0)
parser.add_argument("FT", type=int, help="Final time")

# Parse arguments
args = parser.parse_args()

# Check which flag was used
if args.method.upper() == "E":
    print("Explicit method is used")
    Function.explicit_euler(args.initial_guess1, args.initial_guess2, int(args.FT / args.dT), args.dT)
elif args.method.upper() == "SI":
    print("Semi-implicit method is used")
    Function.semi_implicit_euler(args.initial_guess1, args.initial_guess2, int(args.FT / args.dT), args.dT)    
else:
    print("Implicit method is used")
    Function.implicit_euler(args.initial_guess1, args.initial_guess2, int(args.FT / args.dT), args.dT)