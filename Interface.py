import argparse

# Initialize argument parser
parser = argparse.ArgumentParser()

# Use `add_argument` with `action="store_true"` for boolean flags
parser.add_argument("-m", "--method", help="Call Euler methot", choices=["I", "E"])
#parser.add_argument("-I", "--implicit", help="Call Euler implicit method", action="store_true")
parser.add_argument("dT", type=int, help="Number of steps")
parser.add_argument("IG", type=int, help="Initial guess")
parser.add_argument("FT", type=int, help="Final time")

# Parse arguments
args = parser.parse_args()

# Check which flag was used
if args.method == "E":
    print("Explicit", args.dT, args.IG, args.FT)
elif args.method == "I":
    print("Implicit", args.dT, args.IG, args.FT)
else:
    print("No method specified. Use -E for Explicit or -I for Implicit.")
