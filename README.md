# Data-Pipeline-Using-Automation-Tool-Make

In this repo, I demonstrate how an automation platform like Make or Zappier can be used to build a data pipeline.

## Data Pipeline for CDC.gov Dataset using Make.com


<img width="1281" alt="Make Workflow Screenshot" src="https://github.com/user-attachments/assets/d5858404-6aaf-474a-9fb1-8a1fdb18c599">


This project demonstrates an automated data pipeline built using Make.com to fetch, clean, transform, and load data from the CDC.gov Public Health Emergency Response Data Catalog ([link](https://dev.socrata.com/foundry/data.cdc.gov/fhky-rtsk)).

### Project Overview

This pipeline showcases the capabilities of Make.com to orchestrate data processing tasks. It utilizes various modules to:

* **Fetch data:** An HTTP module retrieves data from the CDC.gov API with authentication.
* **Clean and Transform data:** An AWS Lambda function cleanses and transforms the retrieved data.
* **Parse and Convert JSON:** A JSON module parses the processed JSON data returned by the Lambda function and converts it into an array.
* **Iterate and Insert:** A flow control module iterates through each data row and inserts it into an Amazon Redshift data warehouse using a Redshift module.
* **Data Quality Check:** Another Redshift module performs basic null checks on the loaded data.

### Architecture Diagram

[Image of Pipeline Architecture Diagram Here]![CDC HEALTH VACCINE DATA PIPELINE](https://github.com/user-attachments/assets/198b9c8d-0114-44e7-aff1-b796174b9b53)

### Make Workflow Diagram

<img width="1360" alt="Screenshot 2024-10-16 at 16 03 46" src="https://github.com/user-attachments/assets/57268552-e024-464f-bcea-bc52f2cfdfa4">

### Scenarios

This data pipeline can be used in various scenarios where data needs to be automatically fetched, processed, and stored in a data warehouse. Here are some potential applications:

* **Public health data analysis:** The pipeline can be adapted to fetch and analyze other relevant datasets from the CDC.gov API, aiding public health professionals in monitoring and understanding disease trends.
* **Real-time data monitoring:** The pipeline can be configured to run on a schedule, ensuring the Redshift data warehouse is kept up-to-date with the latest information.
* **Data integration pipelines:** This example can serve as a building block for more complex data integration pipelines involving multiple data sources and transformations.

### Technologies Used

* Make.com: A visual automation platform used to orchestrate the data pipeline.
  * HTTP Module: Makes HTTP requests to fetch and push data.
  * JSON Module: Parses and manipulates JSON data.
  * Array Aggregator Module: Converts JSON data into an array.
  * Flow Control/Iterator Module: Iterates through data elements.
* Amazon Web Services
  * AWS Lambda: Serverless function for data cleaning and transformation.
  * Amazon Redshift: A data warehouse that serves as data store for transformation and analytics.

### Getting Started

**Prerequisites:**

* A Make.com account
* An AWS account with a configured Lambda function
* Access credentials for the CDC.gov API

**Instructions/What's in this repo:**

This repository doesn't necessarily provide step by step instructions. Instead, it just acts as a guide to demonstrate what's possible using an automation platform which should be more cost effective than a full fledged no-code data platform like Talend or Estuary.

1. This repository contains architecture diagrams to serve as a guide.
2. Configure the Make.com workflow with your specific credentials and settings.
3. Customize the Lambda function logic for data cleaning and transformation as needed. The code I used is in the `code` folder.
4. Schedule the workflow on Make.com to run, eg every 1 hour. You can also use system variables to calculate things like offset and limit for the API calls.
5. Deploy the Make.com workflow and start automating your data pipeline.

### Additional Notes

* This example provides a basic framework for building a data pipeline using Make.com.
* You can extend it to incorporate more complex data processing logic and data quality checks.
* Refer to the Make.com documentation for details on specific modules and their functionalities.

This project serves as a starting point for building automated data pipelines using Make.com. Feel free to modify and adapt it to your specific data processing needs.
