import argparse
import logging

from tabulate import tabulate

from utils import filtering, aggregate, read_file

LOG_FORMAT = "%(asctime)s %(levelname)s\n%(pathname)s:%(lineno)d\n%(message)s\n"
LOG_DEFAULT_LEVEL = logging.INFO
LOG_DATE_FORMAT = "%Y-%m-%d %H-%M-%S"
logging.basicConfig(format=LOG_FORMAT, datefmt=LOG_DATE_FORMAT, level=LOG_DEFAULT_LEVEL)

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser()

parser.add_argument('--file')
parser.add_argument('--aggregate')
parser.add_argument('--where')

args = parser.parse_args()

allow_operators = [
    '>', '<', '='
]


def processing_file(args):
    try:
        if args.file:
            filepath = args.file
            table = read_file(filepath=filepath)
            columns = table.pop(0)

        logger.info(f'{tabulate(table, headers=columns, tablefmt="pretty")}')
        if args.where:
            where = args.where
            for op in allow_operators:
                if op in where:
                    field, value = where.split(op) if op in where else None
                    break
            table = filtering(table, columns=columns, field=field, operator=op, value=value)

        if args.aggregate:
            aggregate_params = args.aggregate
            field, operation = aggregate_params.split('=')
            table = aggregate(table=table, columns=columns, field=field, operation=operation)
            columns = table.pop(0)

        logger.info(f'{tabulate(table, headers=columns, tablefmt="pretty")}')
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    processing_file(args)
