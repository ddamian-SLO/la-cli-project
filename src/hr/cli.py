import argparse

def create_parser():

    parser = argparse.ArgumentParser(description="""
    Tool used to display user information in CSV or JSON format
    """)

    parser.add_argument('--format', 
    help="Format of output, [json or csv]",
    default='json', choices=['json', 'csv'],
    type=str.lower
    )
    parser.add_argument('--path', help="Specify path to export file")

    return parser

def main():
    import sys
    from hr import users, export
    from hr import users as u 
    
    args = create_parser().parse_args()
    users = u.get_users()
    
    if args.path:
        output_file = open(args.path, 'w', newline='')
    else: 
        output_file = sys.stdout

    if args.format == 'csv':
        export.format_csv(users, output_file)
    else:
        export.format_json(users, output_file)