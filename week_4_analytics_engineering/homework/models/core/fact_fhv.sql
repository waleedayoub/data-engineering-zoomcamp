{{ config(materialized='table') }}

with stg_fhv as (
    select * from {{ ref('stg_fhv') }}
),

dim_zones as (
    select * from {{ ref('dim_zones') }}
    where borough != 'Unknown'
)

select 
    stg_fhv.dispatching_base_num,
    stg_fhv.affiliated_base_num,
    
    -- timestamps
    stg_fhv.pickup_datetime,
    stg_fhv.dropoff_datetime,
    
    -- trip info
    stg_fhv.SR_flag,
    pickup_zone.borough as pickup_borough,
    pickup_zone.zone as pickup_zone,
    dropoff_zone.borough as dropoff_borough, 
    dropoff_zone.zone as dropoff_zone
    
from stg_fhv
inner join dim_zones as pickup_zone
on stg_fhv.pickup_locationid = pickup_zone.locationid
inner join dim_zones as dropoff_zone
on stg_fhv.dropoff_locationid = dropoff_zone.locationid
