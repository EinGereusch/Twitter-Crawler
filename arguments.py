import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-user", type=str,
                    help="Name of the user's timeline")
parser.add_argument("-destination-directory", type=str,
                    help="Destination directory")

