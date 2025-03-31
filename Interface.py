import argparse

# Initialize argument parser
parser = argparse.ArgumentParser()

# Use `add_argument` with `action="store_true"` for boolean flags
parser.add_argument("-m", "--method", help="Call Euler method. Default method is implicit", choices=["I", "E", "i", "e"], default = "I")
parser.add_argument("dT", type=int, help="Number of steps")
parser.add_argument("IG", type=int, help="Initial guess")
parser.add_argument("FT", type=int, help="Final time")

# Parse arguments
args = parser.parse_args()

# Check which flag was used
if args.method.upper() == "E":
    print("Explicit", args.dT, args.IG, args.FT)
else:
    print("Implicit", args.dT, args.IG, args.FT)
