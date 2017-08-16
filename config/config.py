"""
This file will contain the parsing the arguments it and its description
"""
import os
import yaml
import argparse
import utils.logger


def visualize_config(args):
    """
    Visualize the configuration on the terminal to check the state
    :param args:
    :return:
    """
    print("\nUsing this arguments check it\n")
    for key, value in sorted(vars(args).items()):
        if value is not None:
            print("{} -- {} --".format(key, value))
    print("\n\n")


def parse_config():
    """
    Parse Configuration of the run from YAML file
    :return args:
    """

    # Create a parser
    parser = argparse.ArgumentParser(description="Segmentation using tensorflow")
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    # parse the configuration file if given
    parser.add_argument('--load_config', default=None,
                        dest='config_path',
                        help='load config from a yaml file so specify it and put it in ./config/experiments_config/')
    args, unprocessed_args = parser.parse_known_args()
    config_path = args.config_path

    # Modules arguments
    parser.add_argument('mode', choices=('train_n_test', 'train', 'test', 'overfit'), default=None, help='Mode of operation')
    parser.add_argument('operator', default=None, help='Operator class (trainer of tester)')
    parser.add_argument('model', default=None, help='Model class to operate on')

    # Directories arguments
    parser.add_argument('--data_dir', default=None, help='The data folder')
    parser.add_argument('--exp_dir', default=None, help='The experiment folder')
    parser.add_argument('--out_dir', default=None, help='The output folder')

    # Data arguments
    parser.add_argument('--img_height', default=None, type=int, help='Image height of the data')
    parser.add_argument('--img_width', default=None, type=int, help='Image width of the data')
    parser.add_argument('--num_channels', default=None, type=int, help='Num of channels of the image of the data')
    parser.add_argument('--num_classes', default=None, type=int, help='Num of classes of the data')

    # Train arguments
    parser.add_argument('--num_epochs', default=2, type=int, help='number of epochs')
    parser.add_argument('--batch_size', default=32, type=int, help='batch size')
    parser.add_argument('--shuffle', action='store_true', help='Flag to shuffle the data while training')
    parser.add_argument('--save_every', default=1, type=int, help='save every n epochs')
    parser.add_argument('--test_every', default=1, type=int, help='test every n epochs')
    parser.add_argument('--max_to_keep', default=5, type=int, help='Max checkpoints to keep')

    # Test arguments

    # Models arguments
    parser.add_argument('--learning_rate', default=1e-5, type=float, help='learning rate')
    parser.add_argument('--weight_decay', default=5e-4, type=float, help='weight decay')
    parser.add_argument('--pretrained_path', default="", help='The path of pretrained weights')

    # Misc arguments
    parser.add_argument('--verbose', action='store_true', help='verbosity in the code')
    parser.add_argument('--yaml_name', help='Help to know which yaml you have selected')

    # Load the arguments from the configuration file
    yaml_path = os.path.realpath(os.getcwd()) + "/config/experiments_config/" + args.config_path
    if args.config_path:
        with open(yaml_path, 'r') as f:
            parser.set_defaults(**yaml.load(f))

    # parse the parameters
    args = parser.parse_args(unprocessed_args)
    args.config_path = config_path

    # visualize the configuration on the terminal
    visualize_config(args)

    return args
