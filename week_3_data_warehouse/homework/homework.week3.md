## Week 3 Homework
<b><u>Important Note:</b></u> <p>You can load the data however you would like, but keep the files in .GZ Format. 
If you are using orchestration such as Airflow or Prefect do not load the data into Big Query using the orchestrator.</br> 
Stop with loading the files into a bucket. </br></br>
<u>NOTE:</u> You can use the CSV option for the GZ files when creating an External Table</br>

### Response:
The code to upload data fhv from website to gcs can be found here: https://github.com/waleedayoub/data-engineering-zoomcamp/blob/main/week_3_data_warehouse/homework/web_to_gcs_hw.py

<b>SETUP:</b></br>
Create an external table using the fhv 2019 data. </br>
Create a table in BQ using the fhv 2019 data (do not partition or cluster this table). </br>
Data can be found here: https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/fhv </p>

### Response:
```sql
# external table
CREATE OR REPLACE EXTERNAL TABLE `trips_data_all.fhv_tripdata`
OPTIONS (
  format = 'CSV',
  uris = ['gs://dtc_data_lake_possible-lotus-375803/data/fhv/fhv_tripdata_2019-*.csv.gz']
);

# bq table

```


## Question 1:
What is the count for fhv vehicle records for year 2019?
- 65,623,481
- 43,244,696 <-
- 22,978,333
- 13,942,414

### Response:
```sql
SELECT count(*) from 'trips_data_all.fhv_tripdata'
```

## Question 2:
Write a query to count the distinct number of affiliated_base_number for the entire dataset on both the tables.</br> 
What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

- 25.2 MB for the External Table and 100.87MB for the BQ Table
- 225.82 MB for the External Table and 47.60MB for the BQ Table
- 0 MB for the External Table and 0MB for the BQ Table
- 0 MB for the External Table and 317.94MB for the BQ Table <-

### Response:
- 0 for external and 317.94MB for the BQ


## Question 3:
How many records have both a blank (null) PUlocationID and DOlocationID in the entire dataset?
- 717,748 <-
- 1,215,687
- 5
- 20,332

### Response:
```sql
select count(*)
from `trips_data_all.fhv_nonpartitioned_tripdata`
where PUlocationID is NULL
and DOlocationID is NULL;
```

## Question 4:
What is the best strategy to optimize the table if query always filter by pickup_datetime and order by affiliated_base_number?
- Cluster on pickup_datetime Cluster on affiliated_base_number
- Partition by pickup_datetime Cluster on affiliated_base_number <-
- Partition by pickup_datetime Partition by affiliated_base_number
- Partition by affiliated_base_number Cluster on pickup_datetime

### Response:
If your queries always filter by the pickup_datetime column and order by the affiliated_base_number column, the best optimization strategy would be Option 2: Partition by pickup_datetime and Cluster on affiliated_base_number.

Partitioning the table by pickup_datetime will allow you to efficiently retrieve only the data for the desired date range, rather than scanning the entire table. And clustering the data by affiliation_base_number will ensure that rows with the same affiliation_base_number are stored together on disk, reducing the number of blocks that need to be read when executing queries filtered by this column and ordered by pickup_datetime.

## Question 5:
Implement the optimized solution you chose for question 4. Write a query to retrieve the distinct affiliated_base_number between pickup_datetime 2019/03/01 and 2019/03/31 (inclusive).</br> 
Use the BQ table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 4 and note the estimated bytes processed. What are these values? Choose the answer which most closely matches.
- 12.82 MB for non-partitioned table and 647.87 MB for the partitioned table
- 647.87 MB for non-partitioned table and 23.06 MB for the partitioned table <-
- 582.63 MB for non-partitioned table and 0 MB for the partitioned table
- 646.25 MB for non-partitioned table and 646.25 MB for the partitioned table

### Response:
```sql
CREATE OR REPLACE TABLE `trips_data_all.fhv_partitioned_tripdata`
PARTITION BY DATE(pickup_datetime)
CLUSTER BY Affiliated_base_number AS (
  SELECT * FROM `trips_data_all.fhv_tripdata`
);

/* non partitioned */
select count(distinct Affiliated_base_number) as unique_affiliated
from trips_data_all.fhv_nonpartitioned_tripdata
where pickup_datetime between '2019-03-01' and '2019-03-31';

/* partitioned */
select count(distinct Affiliated_base_number) as unique_affiliated
from trips_data_all.fhv_partitioned_tripdata
where pickup_datetime between '2019-03-01' and '2019-03-31';

```


## Question 6: 
Where is the data stored in the External Table you created?

- Big Query
- GCP Bucket <-
- Container Registry
- Big Table

### Response:
- External tables are stored in GCS buckets which I guess most closely resembles GCP bucket in the above answer

## Question 7:
It is best practice in Big Query to always cluster your data:
- True
- False <-

### Response:
Whether or not to cluster your data in BigQuery depends on the specific needs of your queries and the characteristics of your data. Here are some factors to consider:

1. Query patterns: Clustering is most beneficial for queries that filter on the clustering column and return a large number of rows.
2. Unique values: Clustering is less effective when the clustering column has a high number of unique values.
3. Data size: Clustering can be more useful when working with large data sets, as it can reduce the amount of data that needs to be scanned.

## (Not required) Question 8:
A better format to store these files may be parquet. Create a data pipeline to download the gzip files and convert them into parquet. Upload the files to your GCP Bucket and create an External and BQ Table. 


Note: Column types for all files used in an External Table must have the same datatype. While an External Table may be created and shown in the side panel in Big Query, this will need to be validated by running a count query on the External Table to check if any errors occur. 
 
## Submitting the solutions

* Form for submitting: https://forms.gle/rLdvQW2igsAT73HTA
* You can submit your homework multiple times. In this case, only the last submission will be used. 

Deadline: 13 February (Monday), 22:00 CET


## Solution

We will publish the solution here
