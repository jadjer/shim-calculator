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

from core.models import Engine, ValveType


def complete_valve_data(engine: Engine):
    print("=========== Complete valve data ===========")

    for cylinder in engine.cylinders:
        for valve in cylinder.valves:
            print(f"Complete valve data for cylinder {cylinder.id} valve {valve.id}")

            while True:
                valve_type = input(f"Enter valve type (in/ex): ")

                if valve_type == "in" :
                    valve.valve_type = ValveType.INTAKE
                    break

                if valve_type == "ex":
                    valve.valve_type = ValveType.EXHAUST
                    break

            measurement = input(f"Enter measurement: ")
            if measurement:
                valve.measurement = float(measurement)


def complete_shim_data(engine: Engine):
    print("=========== Complete shim data ===========")

    for cylinder in engine.cylinders:
        for valve in cylinder.valves:
            print(f"Complete shim data for cylinder {cylinder.id} valve {valve.id}")

            shim_set = input(f"Enter shim set: ")
            if shim_set:
                valve.shim.shim_set = shim_set

            shim_num = input(f"Enter shim number: ")
            if shim_num:
                valve.shim.shim_num = shim_num

            shim_thickness = input(f"Enter shim thickness: ")
            if shim_thickness:
                valve.shim.shim_thickness = float(shim_thickness)
