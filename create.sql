-- create database houses;
-- use houses;
CREATE TABLE sz_house(
  id int(11) NOT NULL AUTO_INCREMENT,
  create_time datetime DEFAULT now(),
  houselink varchar(255),
  title varchar(255),
  price int(11),
  price_per_square int(11),
  community_name varchar(255),
  area varchar(255),
  linknumber bigint(11),
  housing_type varchar(255),
  construction_area float,
  inside_area int(11),
  house_orientation varchar(255),
  renovation_condition varchar(255),
  equipped_with_elevator bool,
  floor_area varchar(255),
  total_floor int(11),
  unit_structure varchar(255),
  building_structure varchar(255),
  staircase_ratio varchar(255),
  room_spare_parts varchar(255),
  owner_ship varchar(255),
  usage_of_houses varchar(255),
  transaction_ownership varchar(255),
  housing_society_code varchar(255),
  mortgage_information varchar(255),
  housing_years varchar(255),
  last_transaction date,
  listing_time date,
  PRIMARY KEY (id)
);
-- 创建只有读和写响应表权限的用户
CREATE user houser identified BY 'houser';
-- 授予相应的读和写权限
GRANT SELECT ON houses.* to houser;
GRANT INSERT ON houses.* to houser;

-- 创建显示主要数据视图
DROP VIEW debug_view;
CREATE VIEW debug_view  AS SELECT area AS `行政区`, price AS `总价`,price_per_square AS `每平价格`,construction_area AS `建筑面积`,inside_area AS `套内面积`,total_floor AS `总楼层`,equipped_with_elevator AS `电梯`,floor_area AS `楼层区域`,housing_society_code AS `房协编码`,transaction_ownership AS `交易权属`,mortgage_information AS `有无抵押`,create_time AS `创建时间`,houselink AS `链接` FROM sz_house;
