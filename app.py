import sys
sys.path.append(r'..')

import dash
import dash_html_components as html
import functools

from Fast_Dash.data.sql import SqlDataSource

from pane import TimeSeriesPane
from engine import sqlite

app = dash.Dash(__name__)

data_source = SqlDataSource(
    sql_folder_path=r'',
    sql_file_name='sample.sql',
    engine=sqlite,
    cache=functools.lru_cache,
)

pane = TimeSeriesPane(
    drop_down_source=data_source.query.ids,
    visualization_source=data_source.query.get_ids,
)

app.layout = html.Div(
    pane.get_layout()
)

for cb in pane:
    app.callback(cb.outputs,cb.inputs, cb.states)(cb.func)

if __name__ == '__main__':
    app.run_server(debug=True)