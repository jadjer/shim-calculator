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

from core.models import Engine, EngineType, Cylinder, Valve, ValveType, Shim


def create_data(manufacturer, cylinders, valves, intake, intake_dev, exhaust, exhaust_dev) -> Engine:
    engine_type: EngineType = EngineType(cylinders)
    engine = Engine(manufacturer=manufacturer, engine_type=engine_type)

    for cylinder_number in range(1, cylinders + 1):
        cylinder: Cylinder = Cylinder(id=cylinder_number)

        for valve_number in range(1, valves + 1):
            valve_type: ValveType = ValveType.EXHAUST if valve_number % 2 == 0 else ValveType.INTAKE
            clearance = exhaust if valve_type == ValveType.EXHAUST else intake
            tolerance = exhaust_dev if valve_type == ValveType.EXHAUST else intake_dev

            shim: Shim = Shim(shim_set="unknown", shim_num="unknown", shim_thickness=0.0)
            valve: Valve = Valve(id=valve_number, valve_type=valve_type, clearance=clearance, tolerance=tolerance, measurement=0, shim=shim)

            cylinder.add_valve(valve)

        engine.add_cylinder(cylinder)

    return engine
