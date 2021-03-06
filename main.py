from argparse import ArgumentParser
from drawer import Drawer

parser = ArgumentParser( description="Recreate given image with only lines" )
parser.add_argument( 'input' )
parser.add_argument( 'output' )
parser.add_argument( 'iterations' )

args = parser.parse_args()

drawer = Drawer.from_file( args.input )
drawer.draw( args.output, int( args.iterations ) )

