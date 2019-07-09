from init import *
from main_window import MainWindow

def main():

    # Get arguments
    args = get_arguments()
    print (args ['local'], args['ncam'])
    root = Tk()
    gui = MainWindow(root, args ['local'], args['ncam'])
    root.mainloop()


def get_arguments():
    # Create parser
    ap = argparse.ArgumentParser()
    ap.add_argument('-l', '--local', required=False, action='store_true',
                    help='Use local webcam')
    ap.add_argument('-n', '--ncam', required=False, type = int,
                    help='Maximum number of cameras')
    args = vars(ap.parse_args())

    if args['local'] and args ['ncam'] not in [None, 1]  :
        ap.error("For local usage only one camera is allowed.")

    # Set default local camera to 1 and non local to 5
    if args['local'] and args ['ncam'] is None:
        args ['ncam'] = 1
    elif args ['ncam'] is None:
        args ['ncam'] = 5

    return args

                
if __name__ == "__main__":
    main()

            
            
            