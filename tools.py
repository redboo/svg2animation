import os.path
from argparse import ArgumentParser


def svg2animation_shell(svg2animation):
    parser = ArgumentParser(
        description='This program converts svg picture to gif animation',
    )
    parser.add_argument('input_files', nargs='+')
    parser.add_argument('output_dir', nargs=1)
    args = parser.parse_args()
    for input_file_path in args.input_files:
        print('Processing:', input_file_path)
        file_name = os.path.basename(input_file_path)
        output_file_path = os.path.join(args.output_dir[0], f'{file_name}.gif')
        with open(input_file_path, 'rb') as input_file, open(output_file_path, 'wb') as output_file:
            svg2animation(input_file, output_file)
            print('Ready')

            print()
