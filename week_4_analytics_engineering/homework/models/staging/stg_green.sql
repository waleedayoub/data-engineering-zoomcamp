{{ config(materialized='view' )}}

select * from {{ source('staging','greentripdata' )}}
limit 200

