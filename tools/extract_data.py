"""Aggregate data/rms_crime_incidents.csv into the small JSON that powers docs/index.html.

Run from the repository root (the raw CSV is stored via Git LFS):
    python tools/extract_data.py

Mirrors the notebook's filtering (incidents from 2016-08-01 onward) and produces
per-year breakdowns for the dashboard's year filter. Output: tools/crime_agg.json.
"""
import json
import pandas as pd

COLS = ['incident_occurred_at', 'offense_category', 'police_precinct',
        'neighborhood', 'latitude', 'longitude']
df = pd.read_csv('data/rms_crime_incidents.csv', usecols=COLS)
df['incident_occurred_at'] = (
    pd.to_datetime(df['incident_occurred_at'], errors='coerce', utc=True)
    .dt.tz_convert('America/Detroit'))  # source timestamps are UTC; hours must read local
df = df[df['incident_occurred_at'].notna()]
df = df[df['incident_occurred_at'] >= pd.Timestamp('2016-08-01', tz='America/Detroit')]

t = df['incident_occurred_at']
df['year'] = t.dt.year
df['month'] = t.dt.to_period('M').astype(str)
df['dow'] = t.dt.dayofweek
df['hour'] = t.dt.hour

years = sorted(df['year'].unique().tolist())

def per_year(frame, key, top=None):
    """{year: {value: count}} plus 'all'."""
    out = {}
    keys = None
    if top:
        keys = frame[key].value_counts().head(top).index.tolist()
    for label, sub in [('all', frame)] + [(str(y), frame[frame['year'] == y]) for y in years]:
        vc = sub[key].value_counts()
        if keys is not None:
            vc = vc.reindex(keys).fillna(0).astype(int)
        out[label] = {str(k): int(v) for k, v in vc.items()}
    return out

def dow_hour(frame):
    out = {}
    for label, sub in [('all', frame)] + [(str(y), frame[frame['year'] == y]) for y in years]:
        m = sub.groupby(['dow', 'hour']).size()
        grid = [[int(m.get((d, h), 0)) for h in range(24)] for d in range(7)]
        out[label] = grid
    return out

monthly = df.groupby('month').size()
# keep zero-padded ids matching data/detroit_precincts.geojson names; drop junk (0, HP, 0W, 00)
precinct = df[df['police_precinct'].astype(str).str.fullmatch(r'0[2-9]|1[0-2]')].copy()

data = {
    'meta': {
        'total': int(len(df)),
        'start': str(t.min().date()),
        'end': str(t.max().date()),
        'precincts': int(precinct['police_precinct'].nunique()),
        'neighborhoods': int(df['neighborhood'].nunique()),
        'categories': int(df['offense_category'].nunique()),
        'years': years,
    },
    'monthly': {'labels': monthly.index.tolist(),
                'counts': [int(v) for v in monthly.values]},
    'yearly': {str(k): int(v) for k, v in df.groupby('year').size().items()},
    'category': per_year(df, 'offense_category', top=12),
    'precinct': per_year(precinct, 'police_precinct'),
    'neighborhood_top': per_year(df, 'neighborhood', top=10),
    'dow_hour': dow_hour(df),
}

with open('tools/crime_agg.json', 'w') as f:
    json.dump(data, f)

assert data['meta']['total'] == sum(data['yearly'].values()), 'yearly counts must sum to total'
print('total:', data['meta']['total'], '| years:', years)
