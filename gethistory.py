#run browserhistory.py as a script
print("iam called")
import browserhistory as bh
dict_obj = bh.get_browserhistory()
bh.write_browserhistory_csv()


