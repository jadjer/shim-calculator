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

from core.file_manager import save_source, get_source
from core.models import Engine
from core.functions.complete_data import complete_valve_data, complete_shim_data


def main():
    parser = ArgumentParser(description="Source file complete")
    parser.add_argument("-f", "--source_file", type=str, required=True, help="Source file")
    parser.add_argument("-v", "--valve", action='store_true', help="Complete for valves")
    parser.add_argument("-s", "--shim", action='store_true', help="Complete for shims")

    args = parser.parse_args()

    engine_data: str = get_source(args.source_file)

    try:
        engine: Engine = Engine.model_validate_json(engine_data)

        logger.info(f"Manufacturer: {engine.manufacturer}")

        if args.valve:
            complete_valve_data(engine)

        engine_data = engine.model_dump_json(indent=2)
        save_source(args.source_file, engine_data)

        if args.shim:
            complete_shim_data(engine)

        engine_data = engine.model_dump_json(indent=2)
        save_source(args.source_file, engine_data)

    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    main()
