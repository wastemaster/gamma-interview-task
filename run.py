import json
from tempfile import NamedTemporaryFile
import gdown
import pandas as pd
import argparse


url = 'https://drive.google.com/file/d/1zLdEcpzCp357s3Rse112Lch9EMUWzMLE/view'
AVAILABLE_FIELDS = ['date', 'campaign', 'clicks', 'spend', 'medium', 'source']

parser = argparse.ArgumentParser(
    description="Interview task: CSV downloader",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

available_fields_printable = ','.join(AVAILABLE_FIELDS)
parser.add_argument('-f',
                    '--fields',
                    help=f'Comma-delimited names of field '
                         f'(fields are: {available_fields_printable})',
                    required=True,
                    type=str)
args = parser.parse_args()
target_fields = [item.strip() for item in args.fields.split(',')]

for item in target_fields:
    if item not in AVAILABLE_FIELDS:
        print(AVAILABLE_FIELDS)
        print(item)
        exit(f"Provided field name {item} "
             f"is not among the available "
             f"field names {available_fields_printable}")


with NamedTemporaryFile(suffix=".json", delete=False) as temp_file:
    gdown.download(url, temp_file.name, quiet=True, fuzzy=True)

    df = pd.read_csv(temp_file.name)
    filtered = df.filter(items=target_fields, axis=1)
    data = {"data": filtered.to_dict(orient='records')}

    print(json.dumps(data))
