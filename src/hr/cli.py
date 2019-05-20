from argparse import Action, ArgumentParser

def create_parser():

    parser = ArgumentParser(description="""
    Tool used to display user information in CSV or JSON format
    """)

    parser.add_argument('--format', 
    help="Format of output, JSON or CSV",
    default='json', choices=['json', 'csv']
    )
    parser.add_argument('--path', help="Specify path to export file")

    return parser

