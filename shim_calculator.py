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

import argparse

from loguru import logger

from core.file_manager import get_source
from core.models import Engine
from core.functions.calculate_shims import calculate_shims


def main():
    parser = argparse.ArgumentParser(description="Shim generator")
    parser.add_argument("-f", "--source_file", type=str, required=True, help="Source file")

    args = parser.parse_args()

    engine_data: str = get_source(args.source_file)

    try:
        engine: Engine = Engine.model_validate_json(engine_data)

        logger.info(f"Manufacturer: {engine.manufacturer}")

        calculate_shims(engine, "")

    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    main()
