#  Copyright 2024 Pavel Suprunov
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from loguru import logger
from argparse import ArgumentParser

from core.file_manager import get_file_name, save_source
from core.models import Engine
from core.functions.create_data import create_data


def main():
    parser = ArgumentParser(description="Source file generator")
    parser.add_argument("-m", "--manufacturer", type=str, required=True, help="Manufacturer name")
    parser.add_argument("-n", "--name", type=str, required=False, help="Vehicle name")
    parser.add_argument("-c", "--cylinders", type=int, required=True, help="Number of cylinders")
    parser.add_argument("-v", "--valves", type=int, required=True, help="Number of valves per cylinder")
    parser.add_argument("-i", "--intake", type=float, required=True, help="Normal clearance for intake")
    parser.add_argument("-e", "--exhaust", type=float, required=True, help="Normal clearance for exhaust")
    parser.add_argument("-id", "--intake_dev", type=float, required=True, help="Deviation for intake")
    parser.add_argument("-ed", "--exhaust_dev", type=float, required=True, help="Deviation for exhaust")
    parser.add_argument("-o", "--output", type=str, required=False, help="Output file name")

    args = parser.parse_args()

    if not args.output:
        args.output = get_file_name(args.manufacturer, args.name, args.cylinders, args.valves)

    logger.info(f"Manufacturer: {args.manufacturer}")
    logger.info(f"Cylinders: {args.cylinders}")
    logger.info(f"Valves: {args.valves}")
    logger.info(f"Intake: {args.intake} +/-{args.intake_dev}")
    logger.info(f"Exhaust: {args.exhaust} +/-{args.exhaust_dev}")

    engine: Engine = create_data(args.manufacturer, args.cylinders, args.valves, args.intake, args.intake_dev, args.exhaust, args.exhaust_dev)

    engine_data: str = engine.model_dump_json(indent=2)
    save_source(args.output, engine_data)

    logger.warning(f"Engine data saved as {args.output}. Complete it manually or use complete_data.py script.")


if __name__ == "__main__":
    main()
