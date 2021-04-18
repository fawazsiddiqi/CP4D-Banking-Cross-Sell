# CP4D-Banking-Demo-Up-Cross-sell
This is a CP4D demo asset that focuses on Up/Cross sells in the Banking industry focusing on targeting customer for the right products. In other words it predicts which customers are more likely to buy a specific product or invest in a specific plan.

This data set that we are using contain many demographic fields (as relationship status, age, number of kids...) as well financial information (credit score, income, assets...). Using these multiple fields we build a prediction model with SPSS Modeler and visualize the insights to show which groups of customers are more likely to buy or show an interest in a specific bank product. </br>

In our use case example , the bank products/plans are : Increase net worth, Philanthropy, Capital Acquisition, Education Planning, Retirement Planing and Estate Planning.</br>

**Our goal is to taget the right customers to the right plans.**</br>

Click [Here](https://dataplatform.cloud.ibm.com/dashboards/43070085-9f20-4cd5-82c7-63308aaadd4f/view/503dd93b10e31f9560b3e6e407cd2a527c337754b4bb8002d28c7b490c667097a93c45c2c8794c5ade150432a5ba46599f
) to see a **Demo** of the results.

# Technolgies Used
- **Watson Studio** (CP4D)</br>
- **SPSS Modeler**: to build our prediction Model</br>
- **Cognos Dashboard**: To visualize our prediction output and show the insights</br>

# Architecture Flow
<img width="576" alt="Screen Shot 2020-12-16 at 5 02 17 PM" src="https://media.github.ibm.com/user/273026/files/7b4f5700-3fc0-11eb-9244-74d12e6c7bde">

1- Dataset is uploaded to Watson Studio to use it in SPSS Modeler for our predicton model (Here the data is already cleaned with Data refinery). </br>
2- **SPSS Modeler** targets the field *Pursuit* that contains the values of the bank products/plans.</br>
3- **SPSS Modeler** generates a new file with the prediction results that is used in **Cognos Dashboard** to visualize the insights.</br>

# SPSS Modeler

## Flow
![spss-flow](https://media.github.ibm.com/user/273026/files/ec404000-3fbb-11eb-93be-da40490acb3b)

- In this flow we are using our cleaned data set and it's partitioned( 20% used for testing and 80% for building the model).</br>
- Our target field as discussed above is *Pursuit* that contains the values of the bank products/plans.</br>
- This flow generates an output file that has the predicition results.</br>

## Prediction Model
Our prediction model consists of a combination of 5 different algorithms:
- Random Trees </br>
- XGBoost Tree </br>
- XGBoost Linear </br>
- Logistic Regression </br>
- CHAID </br>
<img width="654" alt="Screen Shot 2020-12-07 at 12 44 01 AM" src="https://media.github.ibm.com/user/273026/files/98822680-3fbc-11eb-9d82-06b493747335">

## All Data Fields
<img width="848" alt="Screen Shot 2020-12-16 at 4 56 33 PM" src="https://media.github.ibm.com/user/273026/files/eb111200-3fbf-11eb-8f89-13e77b02c47f">

# Data Visualization - Cognos Dashboard
<img width="1437" alt="Screen Shot 2020-12-16 at 4 46 15 PM" src="https://media.github.ibm.com/user/273026/files/1d6e3f80-3fbf-11eb-8879-13d7168b339f">
<img width="1424" alt="Screen Shot 2020-12-16 at 4 46 39 PM" src="https://media.github.ibm.com/user/273026/files/265f1100-3fbf-11eb-83bd-7fa6818f190a">

# Implementation Steps
1- Sign in to your [IBM Cloud Account](https://cloud.ibm.com/login). <br>
2- Create a **Watson Studio** service. <br>
3- Create a **Project** in **Watson Studio**. <br><br>

If you're having any issues with doing these steps go [Here](https://developer.ibm.com/tutorials/watson-studio-data-visualization-preparation-transformation/).

## SPSS Modeler Flow
1- Import the data file *merge_customer_summary_arabic.csv* to **Watson Studio** <br><br>
<img width="1440" alt="1" src="https://media.github.ibm.com/user/273026/files/0d601680-7c24-11eb-9a5e-5a608c629076">

2- Click on Add to Project and choose Modeler Flow <br><br>
<img width="1176" alt="2" src="https://media.github.ibm.com/user/273026/files/58c8f380-7c29-11eb-831c-2bce683c06d9">

3- Choose **From File** and import the flow *SPSS Product Market Targeting.str* that you can download from this repo. <br><br>
<img width="1440" alt="3" src="https://media.github.ibm.com/user/273026/files/af363200-7c29-11eb-98fa-3d6bfb993c95">

4- This is how the flow looks. The first node in this modeler represents our data source (the data file *merge_customer_summary_arabic.csv*). As you can see when you expand it we can select our data asset and configure the file (delimeters, characters...)<br><br>
<img width="1440" alt="4" src="https://media.github.ibm.com/user/273026/files/1f44b800-7c2a-11eb-8f93-891ed66c91ff">

5- The **Type** node is a field operation node that repesents our metadata. It shows us our data with their properties and detect their types automatically. In this node we choose our target field (the field that we want to predict in our model). In this case we want to predict **Pursuit** which is the product that the customer is interested in. <br><br>
<img width="1440" alt="5" src="https://media.github.ibm.com/user/273026/files/27622d80-7ce6-11eb-88ca-ab044cf8827b">

6- The **Partition** node is used to split our data into training and testing. To build a prediction model we need to have a data to build the model and another set of data ot test the model. Here we chose 80% our the data to train the model and the rest 20% for is used testing. <br><br>
<img width="1440" alt="6" src="https://media.github.ibm.com/user/273026/files/b96a3600-7ce6-11eb-852a-fcc9bfbd150c">

7- The next node is the Auto Classifier. It shows the name **PURSUIT** because this is our taget field that we want to predict. This node generate our prediction model with its top performant algorithms (the model is the node colored in gold).<br><br>
<img width="1440" alt="7" src="https://media.github.ibm.com/user/273026/files/5200b600-7ce7-11eb-8c15-2c5087c8f18c">

8- Once the model is generated you can click on it and check its metrics to get a better understanding of it. You can see the list of algorithms that were used to create the model and check their metrics<br><br>
<img width="1440" alt="Screen Shot 2021-02-24 at 3 31 36 PM" src="https://media.github.ibm.com/user/273026/files/f2f46e80-7cf1-11eb-9bc6-50b88431fd44">

9- You can click on a specific algorithm if you want to get some more information and insights about it. For example here we are checking the random trees algorithms<br><br>
<img width="1440" alt="8" src="https://media.github.ibm.com/user/273026/files/d18e8500-7ce7-11eb-820b-9b3fc6f49a55">

10- The **Matrix** node help us to understand the relationships between the different fields that we have in the data set after the model is generated.<br><br>
<img width="1440" alt="9" src="https://media.github.ibm.com/user/273026/files/63968d80-7ce8-11eb-83d7-3159bba6e419">

11- These table nodes are used to show the data. For example once the model is generated and the modeler run the flow, we use a table node to see the results.<br><br>
<img width="804" alt="Screen Shot 2021-03-04 at 12 51 19 PM" src="https://media.github.ibm.com/user/273026/files/f08f1600-7ceb-11eb-84f2-1813197a014d">

12- In the result table we will have 3 new added columns to the original data set: Partition,$XS-Pursuit (our target that we arew predicting) and $XSC-Pursuit (The conficence score of the predicition).<br>
The Partition column shows if the data row was used to train the model or to test it.<br><br>
<img width="1425" alt="Screen Shot 2021-02-24 at 3 36 48 PM" src="https://media.github.ibm.com/user/273026/files/0270b900-7cec-11eb-9ae7-f9e047bc59c6">

13- This last node is used to save and export the results if we want to after we run the model.<br><br>
<img width="1440" alt="10" src="https://media.github.ibm.com/user/273026/files/6f368400-7ce9-11eb-8c35-b65f895ebff9">

## Deploy Model 

1- First we need to save our model. You can choose the result table node or the export file node and click on save branch as model. <br><br>

<img width="1440" alt="11" src="https://media.github.ibm.com/user/273026/files/0cdf8280-7ced-11eb-96b6-2b8c76644f0c">
2- Now in your project dashboard, your saved model will be available under **Models**. We need to promote it in a deployment space. <br><br>

<img width="1440" alt="12" src="https://media.github.ibm.com/user/273026/files/38626d00-7ced-11eb-8267-947032a8f166">
3- Choose your target space and promote it, but if you don't have a space you first need to create one (*check step 4 below*). <br><br>

<img width="1440" alt="13" src="https://media.github.ibm.com/user/273026/files/bd4d8680-7ced-11eb-90f8-0d5d902725ae">
4- Here you can create your space, it needs an object storage service and a machine learning service (you can create these 2 instantially and assign them).<br><br>

<img width="1424" alt="14" src="https://media.github.ibm.com/user/273026/files/f4239c80-7ced-11eb-9460-af8fb1e2f124">
5- Once your model is promoted , go to your deployment space that you just created (you can find it by clicking on the hamburger menu icon on the top right corners). Once you are there you'll see your asset model promoted.<br><br>
<img width="1149" alt="15" src="https://media.github.ibm.com/user/273026/files/63998c00-7cee-11eb-8053-4381b358e0dc">

6- Click on it and now are are ready to deploy the model. Click on **Create Deployment**.<br><br>
<img width="1440" alt="16" src="https://media.github.ibm.com/user/273026/files/a65b6400-7cee-11eb-87a1-74534769bf12">

7- Choose **Online** and give your deployment a name. <br><br>
<img width="1363" alt="17" src="https://media.github.ibm.com/user/273026/files/d73b9900-7cee-11eb-9ea2-fdd3bd24cb2a">

8- Your model will start getting deployed. Once it's done you will see a green icon next to it. <br><br>
<img width="1440" alt="18" src="https://media.github.ibm.com/user/273026/files/0fdb7280-7cef-11eb-83ac-cb2fb2c2e259">

9- Once it's ready just click on it and you will see a **Test** tab. Here you will be able to test your deployed model.<br<br>
<img width="1440" alt="19" src="https://media.github.ibm.com/user/273026/files/503af080-7cef-11eb-9767-d552ca467818">

## Data Visualization using Cognos Dashboard Embedded
In your project dashboard, click on **Add to Project** and choose dashbaord. You will need to have a cognos service (you can create one instantially and assign it). Once you assign your cognos, you will be able to start making any visualization that you want. <br><br>

### Create the dashboard: 

1- Click Add to project + and then select Dashboard to create a new dashboard. <br<br>
<img width="1440" alt="20" src="https://media.github.ibm.com/user/266145/files/fc469780-8dd4-11eb-9846-693937362c26">

2- Follow these steps in the New Dashboard page: <br><br>
a. Enter a Name for the dashboard (for example, ‘Banking-Demo-Up-Cross-sell’.) <br><br>
b. Provide a Description for the dashboard (optional). <br><br>
c. For Cognos Dashboard Embedded Service, select the dashboard service that you created previously. <br><br>
<img width="1440" alt="21" src="https://media.github.ibm.com/user/266145/files/619a8880-8dd5-11eb-99c1-61388e62bdf1">
d. Click Create. <br><br>

3- On the next page, select the default tabbed layout and template. <br><br>
<img width="1440" alt="22" src="https://media.github.ibm.com/user/266145/files/87c02880-8dd5-11eb-8721-8a2ec13738b2">
4- Click OK to create an empty freeform dashboard with a single Tab. <br><br>

### To add a data connection:
a. Click the Add a source button (the + icon) in the upper-left part of the page: <br><br>
<img width="1440" alt="23" src="https://media.github.ibm.com/user/266145/files/ab836e80-8dd5-11eb-9add-a2512244622f">
b. Click Select to select ```predicted_output.csv``` which is generated by the SPSS Modeler Flow and clickselect after choosing the data source <br><br>
<img width="1791" alt="Screen Shot 2021-03-30 at 12 27 10" src="https://media.github.ibm.com/user/266300/files/9dc24600-9153-11eb-8eb1-c9a88bbc80d5">
c. Back in the dashboard, select the newly imported data source. <br><br>
<img width="449" alt="Screen Shot 2021-03-30 at 12 32 45" src="https://media.github.ibm.com/user/266300/files/0ad5db80-9154-11eb-8a12-bec6f0d4c51b">

d. Expand the customer summary data source by clicking the drop down button to show the columns. <br><br>
<img width="452" alt="Screen Shot 2021-03-30 at 12 34 28" src="https://media.github.ibm.com/user/266300/files/4a042c80-9154-11eb-853e-22dcce903d6c">

e. To add a particular column to the dashboard just drag and drop the columns onto the canvas, in our case we add the annual income and age range <br><br>
<img width="1104" alt="Screen Shot 2021-03-30 at 12 39 05" src="https://media.github.ibm.com/user/266300/files/7456e980-9156-11eb-9b14-11ea1dd21a45">
<img width="1189" alt="Screen Shot 2021-03-30 at 12 39 16" src="https://media.github.ibm.com/user/266300/files/74ef8000-9156-11eb-9916-c9e86ea35486">
<img width="1137" alt="Screen Shot 2021-03-30 at 12 39 31" src="https://media.github.ibm.com/user/266300/files/30afb000-9155-11eb-8e3f-7d043dc576f5">

Creating the dashboard would be subjective, in our case we have creatred it for the Annual Income by Age Range, we have also attached a canvas in this repository which will allow you to import the dashboard onto Cognos Dashboard Embedded which would really define its capability, moreover, you are more than welcome to try out new things with the data set.
