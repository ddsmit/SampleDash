import sys
sys.path.append(r'..')

import dash_html_components as html
import dash_core_components as dcc

from plot import TimeSeriesScatter

from Fast_Dash.components.pane import Pane
from Fast_Dash.callbacks.callback import CallbackDefinition
from Fast_Dash.components.controls.drop_down import DropDown




class TimeSeriesPane(Pane):
    def __init__(self, visualization_source, drop_down_source, **kwargs):
        self._layout = None
        self._visualization_source = visualization_source
        self._drop_down_source = drop_down_source
        self._build_visualizations(**kwargs)
        self._build_controls(**kwargs)
        self._build_layout()
        self._build_callbacks()

    def _build_visualizations(self, **kwargs):
        self._units = tuple(set(self._drop_down_source()['MACHINE_PERFORMED_PART_SEQUENCE']))
        self._scatter = TimeSeriesScatter(
            data_source=self._visualization_source,
            units=self._units[:1],
            unit_list_query_string=', '.join([str(unit) for unit in self._units][:1]),
        )

    def _build_controls(self, **kwargs):
        self._unit_drop_down = DropDown(
            values=self._units

        )

    def _build_layout(self):
        self._layout = html.Div(
            [
                self._scatter.dash_component,
                self._unit_drop_down.dash_component,
            ]
        )

    def _build_callbacks(self):
        def unit_pick(data):

            if isinstance(data, tuple):
                data = data
            elif isinstance(data, (set, list)):
                data = tuple(data)
            else:
                data = tuple([data])

            return [
                self._scatter.update_component(
                    units=data,
                    unit_list_query_string=', '.join([str(d) for d in data]),
                )
            ]

        self._callbacks = [
            CallbackDefinition(
                inputs=[
                    self._unit_drop_down.get_input(),
                ],
                outputs=[
                    self._scatter.get_output(),
                ],
                func=unit_pick,
            )
        ]


