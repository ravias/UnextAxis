%fs help

%fs ls /FileStore/tables

%fs mkdirs /FileStore/tables/mydir

%fs cp /FileStore/tables/SparkRDD/war_and_peace.txt /FileStore/tables/mydir/war_and_peace

%fs ls /FileStore/tables/mydir

%fs mv /FileStore/tables/mydir/war_and_peace /FileStore/tables/mydir/war_and_peace.txt

%fs ls /FileStore/tables/mydir

%fs rm /FileStore/tables/mydir/war_and_peace.txt

%fs rm -r /FileStore/tables/mydir/

%fs ls dbfs:/FileStore/tables/

dbutils.fs.help()

dbutils.fs.ls("/FileStore/tables")

display(dbutils.fs.ls("/FileStore/tables"))

dbutils.fs.mkdirs("/FileStore/tables/mydir", recurse=True)

display(dbutils.fs.ls("/FileStore/tables"))

dbutils.fs.cp("/FileStore/tables/SparkRDD/war_and_peace.txt",  "/FileStore/tables/mydir/war_and_peace")

display(dbutils.fs.ls("/FileStore/tables/mydir"))

dbutils.fs.mv("/FileStore/tables/mydir/war_and_peace",  "/FileStore/tables/mydir/war_and_peace.txt")

display(dbutils.fs.ls("/FileStore/tables/mydir"))

dbutils.fs.rm("/FileStore/tables/mydir/war_and_peace.txt")

dbutils.fs.rm("/FileStore/tables/mydir/", recurse=True)

display(dbutils.fs.ls("/FileStore/tables"))