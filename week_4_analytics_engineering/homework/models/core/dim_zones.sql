{{ config(materialized='table') }}

select locationid,
    borough,
    zone,
    replace(service_zone, 'Boro', 'FHV') as service_zone
from {{ ref('taxi_zones') }}