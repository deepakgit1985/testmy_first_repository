### **Framework Documentation**

The main objectives in functional automation testing of the env are: 
1. To ensure that the implementation is working correctly as expected — no bugs!
2. To ensure that the implementation is working as specified according to the requirements specification.
3. To prevent regressions between code merges and releases.

## Usage

### Installation

```python

python 3.6 or above

```
## Install requirements
Install additional requirements from requirements.text.

```python

pytest
allure-pytest
Selenium

```
## How to execute testcase

For executing the testcase we have to use below command.
```python
pytest testcases\testcasename
```

## Framework Structure

## Packages : 
We have separate packages for test, utility and testdata, All tests related classes come under Tests Package.

## Utility Class
Utility class stores and handles the functions (The Code which is repetitive in Nature Such as accessing excels, getuniquename, statuscode etc..) Which can be commonly used across the framework. The reason behind creating a utility class is to achieve reusability .

## Test Data 
All the historical test data will be kept in excel sheet(furnish.xlsx), we pass test data and handle data driven testing. We use python libraries to handle excel sheets.

## Pytest 
This will be used for Assertions,Grouping and Parallel execution.

## Version Control Tool 
we use 1 as a repository to store our tests scripts.

## Jenkins
By using Jenkins CI (Continuous Integration) Tool, We execute test cases on daily and for Nightly execution based on the schedule.Test Result will be sent to the peers using Jenkins.

## Allure Reports 
For the reporting purpose, we are using allure reports. it generates beautiful reports. we use the allure reports for maintaining logs and to include the screenshots of failed test cases in the allure Report. 

**How to generate Allure reports on local:**

1. Download allure command line. https://drive.google.com/file/d/1wbRK98UVkcxK7TsGGJhXnYD70BnWCy4c/view?usp=sharing
2. Unzip it and save it to any place on your system.
3. Go to environmental variable and set the allure path. eg :(C:\allure-2.13.5\bin)
4. Install allure-pytest in project using pip command.
5. Run testsuite with below command.
pytest -v -s --alluredir="./reports" testsuite.py

