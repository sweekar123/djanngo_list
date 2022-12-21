import mysql.connector as connector
import json
from db_manipulation import DbManipulator
import requests

class ProvinceDataPost:
	def __init__(self):
		self.con = connector.connect(host='localhost',port='3306',user='root',password='Sweepr@123',database='covid',auth_plugin='mysql_native_password')
		query = "create table if not exists province(provinceId int not null auto_increment,ProvinceName varchar(50),primary key(provinceId));"
		cur = self.con.cursor()
		cur.execute(query)
		print("province Created")

	def insert_province(self,province):
		query = "insert into province(ProvinceName) values('{}')".format(province)
		cur = self.con.cursor()
		cur.execute(query)
		self.con.commit()
		print("Province added")



class DistrictDataPost:
	def __init__(self):
		self.con = connector.connect(host='localhost',port='3306',user='root',password='Sweepr@123',database='covid',auth_plugin='mysql_native_password')
		query = 'create table if not exists district(districtId int unique,DistrictName varchar(100),provinceId int,CONSTRAINT fk_provinceId FOREIGN KEY(provinceId) REFERENCES province(provinceId))'
		cur = self.con.cursor()
		cur.execute(query)
		self.con.commit()
		print("Created")

	def insert_district(self,id,district,province):
		query = "insert into district(districtId,DistrictName,provinceId) values({},'{}',{})".format(
			id,district,province)
		print(query)
		cur = self.con.cursor()
		cur.execute(query)
		self.con.commit()
		print("district saved to db")

class MunicipalDataPost:
	def __init__(self):
		self.conn = connector.connect(host='localhost',port='3306',user='root',password='Sweepr@123',database='covid',auth_plugin='mysql_native_password')
		query = "create table if not exists municipality(municipalId int unique,MunicipalName varchar(200),districtId int NOT NULL,CONSTRAINT fk_districtId FOREIGN KEY(districtId) REFERENCES district(districtId))"
		cur = self.conn.cursor()
		cur.execute(query)
		self.conn.commit()	
		print("Municipality Created")

	def insert_municipality(self,id,municipal,district):
		query = "insert into municipality(municipalId,MunicipalName,districtId) values({},'{}',{})".format(id,municipal,district)
		cur = self.conn.cursor()
		cur.execute(query)
		self.conn.commit()
		print("Municipality Created")	


class Infected:
    def __init__(self):
        self.con = connector.connect(host='localhost',port='3306',user='root',password='Sweepr@123',database='covid',auth_plugin='mysql_native_password')
        print(self.con)
        query = "create table if not exists infected(infected_Id INT NOT NULL AUTO_INCREMENT,provinceId int,districtID int NOT NULL,municipalId int NOT NULL,gender varchar(10),ward int,PRIMARY KEY(infected_Id),CONSTRAINT fk_infected_provinceId FOREIGN KEY(provinceId) REFERENCES province(provinceId),CONSTRAINT fk_infected_districtId FOREIGN KEY(districtId) REFERENCES district(districtId),CONSTRAINT fk_municipal_municipalId FOREIGN KEY(municipalId) REFERENCES municipality(municipalId))"
        cur = self.con.cursor()
        print(cur)
        cur.execute(query)
        self.con.commit()
        print("Created")

    def insert_infected(self,province,district,municipal,gender,ward):
        query = "insert into infected(provinceId,districtId,municipalId,gender,ward) values({},{},{},'{}',{})".format(province,district,municipal,gender,ward)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Infected data Created")	



province = ["Province 1","Madesh","Bagmati","Gandaki","Lumbini","Karnali","Sudhur Paschim"]
p1 = ProvinceDataPost()
for item in province:
	p1.insert_province(item)
	print("{} is added to database".format(item))

district = DistrictDataPost()
response = requests.get("https://data.askbhunte.com/api/v1/districts")
print(response.text)
district_json_data = json.loads(response.text)
for district_data in district_json_data: 
	district.insert_district(district_data.get('id'),district_data.get('code'),district_data.get('province'))
	print("District with id : ",str(district_data.get('id')))

municipal = MunicipalDataPost()
municipal_json_data = json.loads(requests.get("https://data.askbhunte.com/api/v1/municipals").text)
for municipal_data in municipal_json_data:
	municipal.insert_municipality(municipal_data.get('id'),municipal_data.get('title'),municipal_data.get('district'))
	print("Municipality added in database")


infected = Infected()
infected_json_data = json.loads(requests.get("https://data.askbhunte.com/api/v1/covid").text)
for infected_data in infected_json_data:
    infected.insert_infected(infected_data.get('province'),infected_data.get('district'),infected_data.get('municipality'),infected_data.get('gender'),infected_data.get('ward'))
    print("infected added in database")



db1 = DbManipulator()
db1.create_and_insert_new_municipalities_tables()
db1.create_and_insert_new_infected_tables()
print("\n Fetching from API is now completed lets move ahead.")