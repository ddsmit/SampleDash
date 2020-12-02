import sys
sys.path.append(r'..')

import pathlib
import plotly.graph_objects as go

from Fast_Dash.components.visualizations.scatter import Scatter

def get_used_columns(df, datum):
    df = df.copy(deep=True)
    df = df.loc[df['DATUM_ID'] == datum,]
    df = df.filter(['VAL_INT','VAL_DEC','VAL_BOOL']).dropna(axis=1)
    column = list(df.columns)[0]
    return df[column].values

class TimeSeriesScatter(Scatter):
    def _post_process_data(self, **kwargs):
        pass

    def _build_plot_data(self, **kwargs):

        units = kwargs['units']
        traces = []
        for unit in units:
            df = self._data.loc[self._data['MACHINE_PERFORMED_PART_SEQUENCE'] == unit].copy(deep=True)
            x = get_used_columns(df, 'time')
            traces += [
                go.Scatter(
                    x=x,
                    y=get_used_columns(df, datum),
                    name=f'{unit}-{datum}'
                )
                for datum in set(df['DATUM_ID'])
                if datum != 'ECUTime'
            ]
        self._go_data = go.Figure(traces)._data