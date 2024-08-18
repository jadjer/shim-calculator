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

from datetime import datetime


def _get_data_from_file(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()


def _save_data_to_file(file_path: str, data: str):
    with open(file_path, 'w') as f:
        f.write(data)


def get_source(file_path: str) -> str:
    return _get_data_from_file(file_path)


def save_source(file_path: str, data: str):
    _save_data_to_file(file_path, data)


def get_catalog(file_path: str) -> str:
    return _get_data_from_file(file_path)


def get_file_name(manufacturer, vehicle_name, cylinders, valves) -> str:
    if vehicle_name is None:
        vehicle_name = f"{cylinders}cylinders-{valves}valves"

    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    file_name = f"{manufacturer}-{vehicle_name}-{timestamp}.json"
    file_path = "data/"

    source_file = file_path + file_name

    return source_file
