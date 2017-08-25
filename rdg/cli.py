import argparse
import sys
import json
import jinja2.exceptions
import os.path
from . import jinja, type, version
from .random_record import RandomRecord
from .vocabulary import Vocabulary


def __main() -> None:
    args = __parse_args()

    vocabulary = Vocabulary(json.load(args["vocabulary"]))

    jinja_environment = jinja.environment()

    rr = RandomRecord(
        jinja_environment,
        vocabulary
    )

    if args["list"] is True:
        __list_vars(rr)
        exit(0)

    if args["version"] is True:
        print(version)
        exit(0)

    template = jinja_environment.from_string(args["template"].read())
    for item in rr.generate(args["count"], args["delay"]):
        print(template.render(item))


def main() -> None:
    try:
        __main()
    except jinja2.exceptions.TemplateError as error:
        print("There was a problem with your template: {}".format(error.message))
        exit(1)
    except KeyboardInterrupt:
        exit(0)


def __list_vars(rr: RandomRecord) -> None:
    print("\n".join(sorted(rr.keys())))


def __parse_args() -> type.args:
    parser = argparse.ArgumentParser(
        prog='rdg',
        description='''
            rdg reads a jinja2 template from STDIN or from a file, renders it with random values from the
            builtin us_top1000 vocabulary or from a custom file and writes the result to STDOUT
        '''
    )

    parser.add_argument("--version",
                        action="store_true",
                        help="Print the version and exit"
                        )

    parser.add_argument("-c", "--count",
                        metavar="COUNT",
                        type=int,
                        default=sys.maxsize,
                        help="Number of datasets to generate, defaults to 0 (unlimited)"
                        )

    parser.add_argument("-d", "--delay",
                        metavar="SECONDS",
                        type=float,
                        default=0,
                        help="Wait SECONDS between dataset generation, defaults to 0 (no waiting)"
                        )

    parser.add_argument("-l", "--list",
                        action="store_true",
                        help="List the available variables and exit"
                        )

    parser.add_argument("-t", "--template",
                        metavar="FILENAME",
                        type=argparse.FileType('r'),
                        help="Path to the template file. If omitted the template is read from STDIN",
                        default=sys.stdin
                        )

    parser.add_argument("-v", "--vocabulary",
                        metavar="FILENAME",
                        type=argparse.FileType('r'),
                        help="Path to the vocabulary file. Defaults to us_top1000.json",
                        default=open(os.path.dirname(os.path.realpath(__file__)) + '/vocabulary/us_top1000.json', 'r')
                        )

    return vars(parser.parse_args())
