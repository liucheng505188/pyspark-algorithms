#!/usr/bin/python
#-----------------------------------------------------
# Create a DataFrame from a CSV file With Header
# Input: CSV File With Header
#------------------------------------------------------
# Input Parameters:
#    a CSV file With Header
#-------------------------------------------------------
# @author Mahmoud Parsian
#-------------------------------------------------------
from __future__ import print_function 
import sys 
from pyspark.sql import SparkSession 
from pyspark.sql import Row

#=====================================
def debug_file(input_path):
    # Opening a file in python for reading is easy:
    f = open(input_path, 'r')

    # To get everything in the file, just use read()
    file_contents = f.read()
    
    #And to print the contents, just do:
    print ("file_contents = \n" + file_contents)

    # Don't forget to close the file when you're done.
    f.close()
#end-def
#=====================================
#

if __name__ == '__main__':

    #if len(sys.argv) != 2:  
    #    print("Usage: dataframe_creation_csv_with_header.py <csv-file>", file=sys.stderr)
    #    exit(-1)

    # create an instance of SparkSession
    spark = SparkSession\
        .builder\
        .appName("dataframe_creation_csv_with_header")\
        .getOrCreate()
    #
    print("spark=",  spark)

#
    # read name of input file
    input_path = sys.argv[1]
    print("input path : ", input_path)
    debug_file(input_path)
    

    #=====================================
    # Create a DataFrame from a given input file
    #=====================================

    # Spark enable us to read CSV files with a header.
    # Basically, a header is a CSV string of column names. 
    
    # The following example reads a CSV file with a 
    # header and create a new DataFrame and infers a 
    # schema from the content of columns:
    df = spark\
          .read\
          .format("csv")\
          .option("header","true")\
          .option("inferSchema", "true")\
          .load(input_path)
    #
    print("df = " , df.collect())
    #
    df.show()    
    #
    df.printSchema()
       
    # done!
    spark.stop()

