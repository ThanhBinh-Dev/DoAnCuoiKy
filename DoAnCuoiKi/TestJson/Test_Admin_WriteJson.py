from DoAnCuoiKi.Library.JsonFileFactory import JsonFileFactory
from DoAnCuoiKi.Model.Admin import Admin

list_admins = []
list_admins.append(Admin("admin1", "adm1", "0901122334"))
list_admins.append(Admin("admin2", "adm2", "0912233445"))
list_admins.append(Admin("admin3", "adm3", "0923344556"))
list_admins.append(Admin("admin4", "adm4", "0934455667"))

jff=JsonFileFactory()
filename= "../Dataset/Admin.json"
jff.write_data(list_admins,filename)